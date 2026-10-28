# 251 · File Drop Upload — 拖放上傳

When a file is dragged into the area, the border lights up and the icon floats up; after dropping, a file row appears and a checkmark pops in once the progress bar finishes

- Component: Form · Controls (`control`)
- Timing: Drag Gesture, Switch
- Tech: GSAP
- Uses: UI Interaction, App Interface
- Style / keywords: Upload File Drag-and-Drop Dragging Progress Bar Drag Drop File Upload Dropzone Progress Form Control
- Tag: GSAP timeline
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"File Drop Upload (拖放上傳)" motion effect: File drag-and-drop upload area: in the middle of a dashed border there is an upload icon and “Drag files here”; when a file is dragged over the area, the border becomes solid, the background lights up faintly, and the icon floats upward; after dropping, the area bounces lightly, a file information row (file name + progress bar) pops in from below at the bottom, the progress bar fills in about 1.3 seconds, a checkmark icon pops in on the right, and after staying for one second the file row moves up and fades out. Clicking the area also lets you select files. (JS: dragenter/dragover add a class, drop reads the file name; GSAP timeline chains the bounce, the file row entrance, the progress bar scaleX 0→1, and the checkmark with back.out)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx251">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "File Drop Upload".

### JavaScript — `FX[251]` from `site/fx.js`

```js
251(s,x,card){const w=el('div','fm-up');w.innerHTML='<input type="file" aria-label="選擇檔案"><svg class="fm-ui" viewBox="0 0 24 24"><path d="M12 16V4M7 9l5-5 5 5M4 16v3a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-3"/></svg><b>拖曳檔案到這裡</b><div class="fm-file"><span></span><div class="fm-pg"><i></i></div><svg class="fm-ok" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7"/></svg></div>';s.append(w);
  const file=w.querySelector('.fm-file'),nm=file.querySelector('span'),bar=file.querySelector('.fm-pg i'),ok=file.querySelector('.fm-ok');let busy=false,real=0,tl;
  const run=(name,force)=>{if(busy&&!force)return;if(tl)tl.kill();gsap.set(ok,{scale:0});busy=true;nm.textContent=name;tl=gsap.timeline({onComplete:()=>busy=false});
    tl.to(w,{scale:1.03,duration:.2}).to(w,{scale:1,duration:.3,ease:'back.out(3)'}).fromTo(file,{y:'60%',opacity:0},{y:0,opacity:1,duration:.4,ease:'back.out(1.6)'},'<').fromTo(bar,{scaleX:0},{scaleX:1,duration:1.3,ease:'power1.inOut'}).fromTo(ok,{scale:0},{scale:1,duration:.4,ease:'back.out(3)'}).to(file,{opacity:0,y:'-40%',duration:.3,delay:1}).set(ok,{scale:0})};
  const inp=w.querySelector('input');inp.onchange=()=>{real=Date.now();if(inp.files[0])run(inp.files[0].name,1);inp.value=''};
  ['dragenter','dragover'].forEach(e=>w.addEventListener(e,ev=>{ev.preventDefault();w.classList.add('over')}));['dragleave','drop'].forEach(e=>w.addEventListener(e,()=>w.classList.remove('over')));w.addEventListener('drop',ev=>{ev.preventDefault();real=Date.now();const f=ev.dataTransfer.files[0];if(f)run(f.name,1)});
  let k=0;card._timers.push(setInterval(()=>{if(Date.now()-real<6000||busy)return;w.classList.add('over');setTimeout(()=>{w.classList.remove('over');run(['design.fig','motion.mp4','cover.png'][k++%3])},500)},3800))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx251` rules from `site/fx.css`

_No dedicated `.fx251` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #251
