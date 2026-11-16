"""Escribe los metadatos de autoría (IPTC en XMP) dentro de las fotos del sitio, sin volver a comprimirlas.

Google lee estos campos (creador, crédito, aviso de copyright y página de derechos) y los puede
mostrar en Google Imágenes. Se llama desde build.py; si una foto ya tiene el bloque correcto, no la toca.
"""
import glob, os, struct
from PIL import Image

CREATOR = "Dra. Catalina Beltrán"
RIGHTS = "© 2026 Dra. Catalina Beltrán. Todos los derechos reservados."
STATEMENT = "https://dracatalinabeltran.com/"

XMP = f"""<?xpacket begin="﻿" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/"><rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
<rdf:Description rdf:about="" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/" xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/">
<dc:creator><rdf:Seq><rdf:li>{CREATOR}</rdf:li></rdf:Seq></dc:creator>
<dc:rights><rdf:Alt><rdf:li xml:lang="x-default">{RIGHTS}</rdf:li></rdf:Alt></dc:rights>
<photoshop:Credit>{CREATOR}</photoshop:Credit>
<xmpRights:WebStatement>{STATEMENT}</xmpRights:WebStatement>
</rdf:Description></rdf:RDF></x:xmpmeta>
<?xpacket end="w"?>""".encode("utf-8")

def _chunks(data):
    i = 12
    while i + 8 <= len(data):
        fourcc, size = data[i:i + 4], struct.unpack("<I", data[i + 4:i + 8])[0]
        yield fourcc, data[i + 8:i + 8 + size]
        i += 8 + size + (size & 1)

def _chunk(fourcc, payload):
    return fourcc + struct.pack("<I", len(payload)) + payload + (b"\0" if len(payload) & 1 else b"")

def webp(path):
    data = open(path, "rb").read()
    if data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        return False
    chunks = list(_chunks(data))
    if any(f == b"XMP " and p == XMP for f, p in chunks):
        return False
    chunks = [(f, p) for f, p in chunks if f != b"XMP "]
    if chunks[0][0] == b"VP8X":
        vp8x = bytearray(chunks[0][1])
        vp8x[0] |= 0x04
        chunks[0] = (b"VP8X", bytes(vp8x))
    else:
        with Image.open(path) as im:
            w, h, alpha = im.width, im.height, im.mode in ("RGBA", "LA")
        flags = 0x04 | (0x10 if alpha else 0)
        vp8x = bytes([flags, 0, 0, 0]) + (w - 1).to_bytes(3, "little") + (h - 1).to_bytes(3, "little")
        chunks.insert(0, (b"VP8X", vp8x))
    body = b"WEBP" + b"".join(_chunk(f, p) for f, p in chunks) + _chunk(b"XMP ", XMP)
    open(path, "wb").write(b"RIFF" + struct.pack("<I", len(body)) + body)
    return True

def jpeg(path):
    data = open(path, "rb").read()
    if data[:2] != b"\xff\xd8":
        return False
    head = b"http://ns.adobe.com/xap/1.0/\0"
    seg = b"\xff\xe1" + struct.pack(">H", len(head) + len(XMP) + 2) + head + XMP
    if seg in data:
        return False
    # quita un XMP anterior si lo hay
    i, out = 2, bytearray(b"\xff\xd8")
    while i < len(data) and data[i] == 0xFF and data[i + 1] not in (0xDA, 0xD9):
        n = struct.unpack(">H", data[i + 2:i + 4])[0]
        s = data[i:i + 2 + n]
        if not (data[i + 1] == 0xE1 and s[4:4 + len(head)] == head):
            out += s
        i += 2 + n
    # el XMP va después de JFIF (APP0) si existe
    if out[2:4] == b"\xff\xe0":
        n = struct.unpack(">H", out[4:6])[0]
        out = out[:4 + n] + seg + out[4 + n:]
    else:
        out = out[:2] + seg + out[2:]
    open(path, "wb").write(bytes(out) + data[i:])
    return True

def run(root):
    n = 0
    for f in sorted(glob.glob(os.path.join(root, "img", "*")) + glob.glob(os.path.join(root, "video", "*.webp"))):
        if f.endswith(".webp"):
            n += webp(f)
        elif f.endswith((".jpg", ".jpeg")):
            n += jpeg(f)
    return n
