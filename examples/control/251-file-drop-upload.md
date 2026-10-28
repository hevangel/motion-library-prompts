# 251 · 拖放上傳 — File Drop Upload

檔案拖進區塊時框線亮起、圖示上浮；放下後出現檔案列，進度條跑完打勾

- 元件 Component: 表單・控制項 (`control`)
- 時機 Timing: 拖曳手勢、切換
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 上傳 檔案 拖放 拖曳 進度條 Drag Drop File Upload Dropzone Progress 表單 控制項
- 標籤 Tag: GSAP timeline
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「拖放上傳（File Drop Upload）」動態效果：檔案拖放上傳區：虛線框中間有上傳圖示與「拖曳檔案到這裡」；檔案被拖進區塊上方時，框線變實、底色淡淡亮起、圖示往上浮；放下後區塊輕彈一下，底部從下方彈出一列檔案資訊（檔名 + 進度條），進度條約 1.3 秒跑滿，右側打勾圖示彈出，停留一秒後檔案列上移淡出。點擊區塊也可以選檔案。（JS：dragenter/dragover 加 class，drop 讀取檔名；GSAP timeline 串接彈跳、檔案列進場、進度條 scaleX 0→1、打勾 back.out）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx251">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「拖放上傳」.

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
