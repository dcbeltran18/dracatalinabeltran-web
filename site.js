/* Medición del sitio orgánico: una fila por visita en VISITAS y una en CLICS al tocar WhatsApp.
   Mismo registro que valoracion.dracatalinabeltran.com, con origen "(web: página)".
   No usa la etiqueta de Google Ads: las visitas orgánicas no cuentan como conversiones de anuncios. */
(()=>{
const SHEET='https://script.google.com/macros/s/AKfycbwSk8zhfTzRJgFQuA7WReGAeDxd-9RH94Ba1KKbLUvnV-81_7YqCcBwd7ky6qYoc43XrA/exec';
let on=/(^|\.)dracatalinabeltran\.com$/.test(location.hostname);
const q=new URLSearchParams(location.search);
try{const y=q.get('yo');if(y==='1')localStorage.setItem('dcb_interno','1');if(y==='0')localStorage.removeItem('dcb_interno');if(localStorage.getItem('dcb_interno')==='1')on=false;}catch(e){}
const ss=(k,v)=>{try{if(v!==undefined)sessionStorage.setItem(k,v);return sessionStorage.getItem(k)}catch(e){return v??null}};
let ref=ss('ref');if(!ref){const a='23456789ABCDEFGHJKMNPQRSTVWXYZ';ref='DS-'+Array.from({length:4},()=>a[Math.floor(Math.random()*a.length)]).join('');ss('ref',ref);}
const lang=document.documentElement.lang||'es';
const slug=(location.pathname.replace(/\/$/,'').split('/').pop())||'inicio';
const click={gclid:q.get('gclid')||ss('gclid')||'',gbraid:q.get('gbraid')||'',wbraid:q.get('wbraid')||'',camp:q.get('utm_campaign')||''};if(click.gclid)ss('gclid',click.gclid);
let rh='';try{rh=document.referrer?new URL(document.referrer).hostname.replace(/^www\./,''):''}catch(e){}
const src=()=>{if(click.gclid||click.gbraid||click.wbraid)return'Google Ads';const u=q.get('utm_source');if(u)return u;
  if(!rh||rh===location.hostname.replace(/^www\./,''))return ss('src')||'Directo';
  if(/(^|\.)google\./.test(rh))return'Google orgánico';if(/bing\.com$/.test(rh))return'Bing orgánico';
  if(/chatgpt\.com$|openai\.com$/.test(rh))return'ChatGPT';if(/perplexity\.ai$/.test(rh))return'Perplexity';return rh;};
const s0=src();ss('src',s0);
const origen=s0+' (web: '+slug+')';
/* Código de referencia en cada mensaje de WhatsApp, igual que en la página de valoración */
document.querySelectorAll('a[href^="https://wa.me/"]').forEach(a=>{try{const u=new URL(a.href);const t=(u.searchParams.get('text')||'')+' (ref. '+ref.replace(/^DS-/,'')+')';a.href=u.origin+u.pathname+'?text='+encodeURIComponent(t);}catch(e){}
  a.addEventListener('click',()=>{if(!on)return;try{navigator.sendBeacon(SHEET,JSON.stringify({ref,lang,boton:'web-'+slug,tz:(Intl.DateTimeFormat().resolvedOptions().timeZone||''),...click}))}catch(e){}});});
if(!on)return;
let nv=1;try{if(!sessionStorage.getItem('dcb_s')){sessionStorage.setItem('dcb_s','1');localStorage.setItem('dcb_vis',String(+(localStorage.getItem('dcb_vis')||0)+1));}nv=+(localStorage.getItem('dcb_vis')||1);}catch(e){}
const base={t:'v',ref,origen,disp:/Mobi|Android|iPhone|iPad/i.test(navigator.userAgent)?'Celular':'Computador',tz:(Intl.DateTimeFormat().resolvedOptions().timeZone||''),lang};
const send=o=>{try{navigator.sendBeacon(SHEET,JSON.stringify({...base,...o}))}catch(e){}};
send({ev:'load',kw:'',mt:'',nueva:nv<=1?'Nueva':'Repetida ('+nv+'a)'});
const t0=Date.now();let max=0;
addEventListener('scroll',()=>{const h=document.documentElement;const p=Math.round((h.scrollTop+innerHeight)/h.scrollHeight*100);if(p>max)max=p;},{passive:true});
const carga=()=>{try{const n=performance.getEntriesByType('navigation')[0];const t=n&&(n.loadEventEnd||n.domContentLoadedEventEnd);return t?Math.round(t/100)/10:'';}catch(e){return ''}};
let sent=false;
document.addEventListener('visibilitychange',()=>{if(document.visibilityState==='hidden'&&!sent){sent=true;send({ev:'out',hasta:Math.min(max,100)+'%',seg:Math.round((Date.now()-t0)/1000),carga:carga(),videos:''});}});
})();
document.querySelectorAll('.cmp input').forEach(r=>r.addEventListener('input',()=>r.parentNode.style.setProperty('--pos',r.value+'%')));
