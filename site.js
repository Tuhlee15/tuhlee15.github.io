/* Tully Njoroge · site interactions. Plain JS, no dependencies. */
(function(){
'use strict';
const reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const $$=(s,r=document)=>[...r.querySelectorAll(s)];

/* nav state */
const nav=document.querySelector('.nav');
const onScroll=()=>{if(nav)nav.classList.toggle('solid',window.scrollY>40)};
window.addEventListener('scroll',onScroll,{passive:true});onScroll();

/* split headlines into words for the rise-in */
$$('.split').forEach(el=>{
  const walk=n=>{[...n.childNodes].forEach(c=>{
    if(c.nodeType===3){const frag=document.createDocumentFragment();c.textContent.split(/(\s+)/).forEach(w=>{if(!w)return;if(/^\s+$/.test(w)){frag.appendChild(document.createTextNode(w));return}const o=document.createElement('span');o.className='w';const i=document.createElement('span');i.textContent=w;o.appendChild(i);frag.appendChild(o)});c.replaceWith(frag)}
    else if(c.nodeType===1&&!c.classList.contains('w'))walk(c)})};
  walk(el);
  $$('.w>span',el).forEach((s,i)=>s.style.transitionDelay=(i*0.06)+'s');
});

/* count-up numbers */
function countUp(el){
  const end=parseFloat(el.dataset.count),dec=+(el.dataset.dec||0),pre=el.dataset.pre||'',suf=el.dataset.suf||'';
  const fmt=v=>pre+v.toLocaleString('en-US',{minimumFractionDigits:dec,maximumFractionDigits:dec})+suf;
  if(reduce){el.textContent=fmt(end);return}
  const t0=performance.now(),dur=1400;
  const step=t=>{const k=Math.min(1,(t-t0)/dur),e=1-Math.pow(1-k,3);el.textContent=fmt(end*e);if(k<1)requestAnimationFrame(step)};
  requestAnimationFrame(step);
}

/* reveal on scroll */
const io=('IntersectionObserver' in window)?new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');$$('[data-count]',e.target).forEach(n=>{if(!n._done){n._done=1;countUp(n)}});io.unobserve(e.target)}})},{rootMargin:'0px 0px -8% 0px',threshold:0.08}):null;
$$('.rv,.split,[data-count-wrap]').forEach(el=>{if(io)io.observe(el);else el.classList.add('in')});
setTimeout(()=>$$('.rv,.split').forEach(el=>{const r=el.getBoundingClientRect();if(r.top<innerHeight)el.classList.add('in')}),60);

/* spotlight on project panels */
$$('.proj').forEach(p=>p.addEventListener('pointermove',e=>{const r=p.getBoundingClientRect();p.style.setProperty('--mx',(e.clientX-r.left)+'px');p.style.setProperty('--my',(e.clientY-r.top)+'px')}));

/* ---------- hero flight field ---------- */
const NODES=[['LOU',38.13,-85.80,1],['PAH',37.08,-88.67,0],['OWB',37.74,-87.15,0],['MDV',37.32,-87.49,0],['MUR',36.61,-88.32,0],['BWG',36.99,-86.46,0],['ETN',37.70,-85.88,0],['EVV',37.97,-87.53,0],['SDF',38.17,-85.74,0]];
function field(cv,opts={}){
  const c=cv.getContext('2d');let W,H,D,nodes=[],arcs=[],craft=[],mx=.5,my=.5,t0=performance.now();
  const read=opts.readout;
  function layout(){
    const r=cv.getBoundingClientRect();D=Math.min(2,devicePixelRatio||1);W=r.width;H=r.height;cv.width=W*D;cv.height=H*D;
    const narrow=W<760;const x0=narrow?.06:.46,x1=narrow?.94:.97,y0=narrow?.12:.13,y1=narrow?.50:.56;
    nodes=NODES.map(([id,la,lo,hub])=>({id,hub,la,lo,x:(x0+(lo+89.3)/4.0*(x1-x0))*W,y:(y0+(38.5-la)/2.1*(y1-y0))*H}));
    const hub=nodes[0];arcs=nodes.filter(n=>!n.hub&&n.id!=='SDF').map(n=>{const mxp=(hub.x+n.x)/2,myp=(hub.y+n.y)/2;const dx=n.x-hub.x,dy=n.y-hub.y;const L=Math.hypot(dx,dy);const bend=L*0.18;return{a:hub,b:n,cx:mxp-dy/L*bend,cy:myp+dx/L*bend,L}});
    if(!craft.length)craft=arcs.map((a,i)=>({arc:i,t:Math.random(),v:(0.018+Math.random()*0.02)*(i%2?1:-1)}));
  }
  const q=(a,t)=>{const u=1-t;return{x:u*u*a.a.x+2*u*t*a.cx+t*t*a.b.x,y:u*u*a.a.y+2*u*t*a.cy+t*t*a.b.y}};
  function frame(now){
    const s=(now-t0)/1000;c.setTransform(D,0,0,D,0,0);c.clearRect(0,0,W,H);
    const ox=(mx-.5)*14,oy=(my-.5)*10;
    // dot grid
    c.fillStyle='rgba(238,241,246,0.07)';const g=30;for(let x=((ox%g)+g)%g;x<W;x+=g)for(let y=((oy%g)+g)%g;y<H;y+=g)c.fillRect(x,y,1.2,1.2);
    c.save();c.translate(-ox*0.6,-oy*0.6);
    const hub=nodes[0];
    // range rings
    for(let k=0;k<3;k++){const ph=((s*0.22+k/3)%1);c.beginPath();c.arc(hub.x,hub.y,40+ph*Math.max(W,H)*0.55,0,7);c.strokeStyle=`rgba(91,140,255,${0.22*(1-ph)})`;c.lineWidth=1;c.stroke()}
    for(const r of [120,240,360]){c.beginPath();c.arc(hub.x,hub.y,r*(W/1400+.4),0,7);c.strokeStyle='rgba(238,241,246,0.05)';c.setLineDash([2,6]);c.stroke();c.setLineDash([])}
    // arcs
    for(const a of arcs){c.beginPath();c.moveTo(a.a.x,a.a.y);c.quadraticCurveTo(a.cx,a.cy,a.b.x,a.b.y);c.strokeStyle='rgba(169,194,255,0.16)';c.lineWidth=1;c.stroke()}
    // craft
    craft.forEach((k,i)=>{if(!reduce){k.t+=k.v*0.016;if(k.t>1)k.t-=1;if(k.t<0)k.t+=1}const a=arcs[k.arc];
      for(let j=18;j>=0;j--){const tt=k.t-j*0.006*Math.sign(k.v);if(tt<0||tt>1)continue;const p=q(a,tt);c.fillStyle=`rgba(169,194,255,${0.5*(1-j/18)})`;c.fillRect(p.x-1,p.y-1,2,2)}
      const p=q(a,k.t);c.beginPath();c.arc(p.x,p.y,3.2,0,7);c.fillStyle=i===0?'#ffffff':'#a9c2ff';c.fill();c.beginPath();c.arc(p.x,p.y,9,0,7);c.strokeStyle=i===0?'rgba(255,255,255,0.45)':'rgba(169,194,255,0.25)';c.stroke();
      if(i===0){k.pos=p;c.font='11px "IBM Plex Mono", monospace';c.fillStyle='rgba(238,241,246,0.85)';c.fillText('HX-201',p.x+13,p.y-8)}});
    // nodes
    c.font='11px "IBM Plex Mono", monospace';
    for(const n of nodes){if(n.id==='SDF')continue;if(n.hub){c.strokeStyle='#eef1f6';c.lineWidth=1.5;c.strokeRect(n.x-6,n.y-6,12,12);c.fillStyle='#eef1f6';c.fillRect(n.x-2,n.y-2,4,4)}else{c.fillStyle='rgba(238,241,246,0.75)';c.fillRect(n.x-2.5,n.y-2.5,5,5)}c.fillStyle='rgba(238,241,246,0.5)';c.fillText(n.id,n.x+10,n.y+4)}
    c.restore();
    if(read&&craft[0].pos&&(!read._t||now-read._t>250)){read._t=now;const p=craft[0].pos,hubN=nodes[0];
      // invert projection for a readout
      const narrow=W<760;const x0=narrow?.06:.46,x1=narrow?.94:.97,y0=narrow?.12:.13,y1=narrow?.50:.56;const lo=(p.x/W-x0)/(x1-x0)*4.0-89.3,la=38.5-(p.y/H-y0)/(y1-y0)*2.1;
      const d=new Date();const tt=d.toLocaleTimeString('en-US',{hour12:false,timeZone:'America/New_York'});
      read.innerHTML=`<span>TRACK</span><b>HX-201 · LOU → ${NODES[craft[0].arc+1]?NODES[craft[0].arc+1][0]:'PAH'}</b><span>POS</span><b>${la.toFixed(3)}°N ${Math.abs(lo).toFixed(3)}°W</b><span>GS</span><b>${(108+Math.sin(now/900)*3).toFixed(0)} KT</b><span>LOUISVILLE</span><b>${tt} ET</b>`}
    if(!reduce||!frame._once){frame._once=1;requestAnimationFrame(frame)}
  }
  layout();addEventListener('resize',layout);
  addEventListener('pointermove',e=>{mx=e.clientX/innerWidth;my=e.clientY/innerHeight},{passive:true});
  requestAnimationFrame(frame);
}
$$('canvas[data-field]').forEach(cv=>field(cv,{readout:document.getElementById(cv.dataset.readout)}));


/* data window: metro dot field */
$$('canvas[data-dots]').forEach(cv=>{const c=cv.getContext('2d');let W,H,D,pts=[],hubs=[];
  const lay=()=>{const r=cv.getBoundingClientRect();D=Math.min(2,devicePixelRatio||1);W=r.width;H=r.height;cv.width=W*D;cv.height=H*D;pts=[];for(let x=14;x<W;x+=16)for(let y=14;y<H;y+=16){const n=Math.sin(x*0.021)+Math.cos(y*0.027)+Math.sin((x+y)*0.011);if(n>-0.2)pts.push({x,y,a:0.08+Math.max(0,n)*0.12})}
    hubs=[[.22,.36],[.38,.62],[.55,.3],[.7,.55],[.84,.4],[.3,.82]].map(([a,b],i)=>({x:a*W,y:b*H,s:i<2?1:0}))};
  const f=t=>{c.setTransform(D,0,0,D,0,0);c.clearRect(0,0,W,H);for(const p of pts){c.fillStyle=`rgba(79,209,197,${p.a})`;c.fillRect(p.x-1,p.y-1,2.2,2.2)}
    c.strokeStyle='rgba(79,209,197,0.28)';c.lineWidth=1;c.beginPath();hubs.forEach((h,i)=>{if(i)c.lineTo(h.x,h.y);else c.moveTo(h.x,h.y)});c.stroke();
    hubs.forEach((h,i)=>{const ph=reduce?0.5:((t/1000*0.5+i*0.17)%1);c.beginPath();c.arc(h.x,h.y,4+ph*18,0,7);c.strokeStyle=`rgba(79,209,197,${0.5*(1-ph)})`;c.stroke();c.beginPath();c.arc(h.x,h.y,h.s?5:3.5,0,7);c.fillStyle=h.s?'#4fd1c5':'rgba(238,241,246,0.8)';c.fill()});
    if(!reduce)requestAnimationFrame(f)};
  lay();addEventListener('resize',lay);requestAnimationFrame(f)});

/* ---------- charts (finance page) ---------- */
const tip=document.createElement('div');tip.className='tip';document.body.appendChild(tip);
const showTip=(e,html)=>{tip.innerHTML=html;tip.style.opacity=1;const x=Math.min(innerWidth-tip.offsetWidth-12,e.clientX+14),y=Math.min(innerHeight-tip.offsetHeight-12,e.clientY+14);tip.style.left=x+'px';tip.style.top=y+'px'};
const hideTip=()=>tip.style.opacity=0;
const NS='http://www.w3.org/2000/svg';
const el=(n,a={},txt)=>{const e=document.createElementNS(NS,n);for(const k in a)e.setAttribute(k,a[k]);if(txt!=null)e.textContent=txt;return e};
const COL={pos:'#5b8cff',neg:'#c47a22',neu:'#4a5160',ink:'#eef1f6',muted:'#8d95a6',grid:'rgba(238,241,246,0.10)',surf:'#0b0e14'};

function diverging(host){
  const data=JSON.parse(host.dataset.rows),hl=host.dataset.highlight,unit=host.dataset.unit||'%',neutral=+(host.dataset.neutral||1);
  const draw=()=>{
    host.innerHTML='';const W=Math.max(320,host.clientWidth),row=30,top=8,bot=26,H=top+bot+row*data.length;
    const lab=W<480?118:170,pad=46;const max=Math.max(...data.map(d=>Math.abs(d.v)))*1.05;const x0=lab+pad+(W-lab-pad*2)/2;const sc=(W-lab-pad*2)/2/max;
    const svg=el('svg',{viewBox:`0 0 ${W} ${H}`,role:'img','aria-label':host.dataset.label});
    // grid
    [-1,-.5,0,.5,1].forEach(f=>{const v=Math.round(max*f/5)*5;const x=x0+v*sc;svg.appendChild(el('line',{x1:x,x2:x,y1:top,y2:H-bot,stroke:v===0?'rgba(238,241,246,0.35)':COL.grid,'stroke-width':1}));svg.appendChild(el('text',{x,y:H-8,'text-anchor':'middle','font-size':11,fill:COL.muted,'font-family':'IBM Plex Mono, ui-monospace, monospace'},(v>0?'+':'')+v+unit))});
    data.forEach((d,i)=>{const y=top+i*row+row/2;const isH=d.k===hl;const col=Math.abs(d.v)<=neutral?COL.neu:(d.v>0?COL.pos:COL.neg);
      svg.appendChild(el('text',{x:lab,y:y+4,'text-anchor':'end','font-size':13,fill:isH?COL.ink:COL.muted,'font-weight':isH?700:400,'font-family':'Archivo, Arial, sans-serif'},d.k));
      const w=Math.max(2,Math.abs(d.v)*sc),x=d.v>=0?x0:x0-w,h=14;
      const r=Math.min(4,w/2);const p=d.v>=0?`M${x},${y-h/2}h${w-r}a${r},${r} 0 0 1 ${r},${r}v${h-2*r}a${r},${r} 0 0 1 -${r},${r}h-${w-r}z`:`M${x+w},${y-h/2}h-${w-r}a${r},${r} 0 0 0 -${r},${r}v${h-2*r}a${r},${r} 0 0 0 ${r},${r}h${w-r}z`;
      const bar=el('path',{d:p,fill:col,opacity:isH||!hl?1:0.75});svg.appendChild(bar);
      svg.appendChild(el('text',{x:d.v>=0?x0+w+6:x0-w-6,y:y+4,'text-anchor':d.v>=0?'start':'end','font-size':12,fill:isH?COL.ink:COL.muted,'font-family':'IBM Plex Mono, ui-monospace, monospace','font-weight':isH?600:400},(d.v>0?'+':'')+d.v+unit));
      const hit=el('rect',{x:0,y:y-row/2,width:W,height:row,fill:'transparent'});
      hit.addEventListener('pointermove',e=>{showTip(e,`<b>${d.k}</b><br>${d.tip}`);bar.setAttribute('opacity',1)});hit.addEventListener('pointerleave',()=>{hideTip();bar.setAttribute('opacity',isH||!hl?1:0.75)});svg.appendChild(hit)});
    host.appendChild(svg);
  };
  draw();let rt;addEventListener('resize',()=>{clearTimeout(rt);rt=setTimeout(draw,120)});
}
function football(host){
  const rows=JSON.parse(host.dataset.rows);
  const draw=()=>{
    host.innerHTML='';const W=Math.max(320,host.clientWidth),row=78,top=10,bot=30,H=top+bot+row*rows.length,lab=W<480?64:96,pr=24;
    const lo=80,hi=180,sc=(W-lab-pr)/(hi-lo),X=v=>lab+(v-lo)*sc;
    const svg=el('svg',{viewBox:`0 0 ${W} ${H}`,role:'img','aria-label':host.dataset.label});
    for(let v=lo;v<=hi;v+=20){svg.appendChild(el('line',{x1:X(v),x2:X(v),y1:top,y2:H-bot,stroke:COL.grid}));svg.appendChild(el('text',{x:X(v),y:H-10,'text-anchor':'middle','font-size':11,fill:COL.muted,'font-family':'IBM Plex Mono, ui-monospace, monospace'},'$'+v))}
    rows.forEach((d,i)=>{const y=top+i*row+row/2;
      svg.appendChild(el('text',{x:0,y:y+5,'font-size':15,fill:COL.ink,'font-weight':700,'font-family':'Archivo, Arial, sans-serif'},d.k));
      const g=el('g');
      g.appendChild(el('rect',{x:X(d.lo),y:y-8,width:X(d.hi)-X(d.lo),height:16,rx:4,fill:COL.pos}));
      g.appendChild(el('line',{x1:X(d.price),x2:X(d.price),y1:y-20,y2:y+20,stroke:COL.neg,'stroke-width':2.5}));
      g.appendChild(el('circle',{cx:X(d.base),cy:y,r:6.5,fill:COL.ink,stroke:COL.surf,'stroke-width':2}));
      g.appendChild(el('text',{x:X(d.base),y:y-16,'text-anchor':'middle','font-size':12,fill:COL.ink,'font-family':'IBM Plex Mono, ui-monospace, monospace','font-weight':600},'$'+d.base.toFixed(2)));
      g.appendChild(el('text',{x:X(d.price),y:y+33,'text-anchor':'middle','font-size':11.5,fill:COL.muted,'font-family':'IBM Plex Mono, ui-monospace, monospace'},'$'+d.price.toFixed(2)));
      svg.appendChild(g);
      const hit=el('rect',{x:0,y:y-row/2,width:W,height:row,fill:'transparent'});
      hit.addEventListener('pointermove',e=>showTip(e,`<b>${d.name}</b><br><span class="k">Base-case value</span> $${d.base.toFixed(2)}<br><span class="k">Sensitivity range</span> $${d.lo}–$${d.hi}<br><span class="k">Price, 3 Mar 2026</span> $${d.price.toFixed(2)}<br><span class="k">Implied upside</span> ${d.up}`));hit.addEventListener('pointerleave',hideTip);svg.appendChild(hit)});
    host.appendChild(svg);
  };
  draw();let rt;addEventListener('resize',()=>{clearTimeout(rt);rt=setTimeout(draw,120)});
}
$$('[data-chart="diverging"]').forEach(diverging);
$$('[data-chart="football"]').forEach(football);
})();
