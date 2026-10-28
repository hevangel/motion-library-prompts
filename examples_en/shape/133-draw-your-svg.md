# 133 · Draw Your SVG — 上傳 SVG 描繪

Upload your own line SVG and watch it drawn stroke by stroke, as if by a pen

- Component: Shapes · SVG (`shape`)
- Timing: Entrance
- Tech: GSAP
- Uses: Logo · Brand, Emphasis
- Style / keywords: SVG Upload Custom Line Stroke Hand-drawn Stroke Logo Illustration Line Drawing Stroke Draw Upload Custom
- Tag: DrawSVG·Upload
- Example text: "" (stage background: cream, fixed text)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Draw Your SVG (上傳 SVG 描繪)" motion effect: Turn the line SVG I provide (pasted after these instructions) into a 'drawn with a pen' entrance: each path is traced one after another in its original drawing order, with each stroke's drawing time allocated by length (longer lines draw longer, shorter ones quicker), the strokes slightly overlapping as they connect, about 3 seconds overall, ease-in-out; after finishing, it can hold then fade out and replay, or play only once. All shapes are changed to stroke only, no fill, with round line caps and joins. (GSAP: DrawSVGPlugin; for each path / line / polyline / circle, fromTo drawSVG "0%"→"100%" in sequence, with duration calculated in proportion to getTotalLength(); pure CSS can also do this with stroke-dasharray + stroke-dashoffset)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx133">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Draw Your SVG".

### JavaScript — `FX[133]` from `site/fx.js`

```js
133(s,x,card){const w=el('div','abs gl cdraw');const box=el('div','cdbox');const ui=el('div','cdui');ui.innerHTML='<label class="cdbtn">上傳 SVG<input type="file" accept=".svg,image/svg+xml" hidden></label><button class="cdbtn" type="button">重播</button><span class="cdmsg"></span>';w.append(box,ui);s.append(w);
  const msg=ui.querySelector('.cdmsg');let tl;card._kill.push(()=>tl&&tl.kill());
  const play=()=>{tl&&tl.kill();gsap.set(box,{opacity:1});const ps=[...box.querySelectorAll('path,line,polyline,polygon,circle,ellipse,rect')];const L=ps.map(p=>{try{return p.getTotalLength()||1}catch(e){return 1}}),sum=L.reduce((a,b)=>a+b,0);
    tl=gsap.timeline({repeat:-1,repeatDelay:.6});tl.set(box,{opacity:1},0);let t=0;ps.forEach((p,i)=>{const d=Math.max(.2,L[i]/sum*3.2);tl.fromTo(p,{drawSVG:'0%'},{drawSVG:'100%',duration:d,ease:'power1.inOut'},t);t+=d*.85});tl.to(box,{opacity:0,duration:.5},'+=1.4')};
  const load=(txt,quiet)=>{const sv=cleanSVG(txt);if(!sv){msg.textContent='找不到可描繪的線條';return false}box.innerHTML='';box.append(sv);if(!quiet)msg.textContent='';play();return true};
  ui.querySelector('input').addEventListener('change',e=>{const f=e.target.files[0];if(!f)return;f.text().then(t=>{if(load(t))card._svgTxt=t});e.target.value=''});
  ui.querySelector('button').onclick=play;
  w.addEventListener('dragover',e=>{e.preventDefault();w.classList.add('drag')});w.addEventListener('dragleave',()=>w.classList.remove('drag'));
  w.addEventListener('drop',e=>{e.preventDefault();w.classList.remove('drag');const f=e.dataTransfer.files[0];if(f)f.text().then(t=>{if(load(t))card._svgTxt=t})});
  load(card._svgTxt||PLANT,true)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx133` rules from `site/fx.css`

_No dedicated `.fx133` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #133
