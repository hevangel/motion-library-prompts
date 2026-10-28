# 133 · 上傳 SVG 描繪 — Draw Your SVG

上傳自己的線條 SVG，看它像用筆一筆一筆畫出來

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: Logo・品牌、強調重點
- 風格／關鍵字 Style: SVG 上傳 自訂 線條 描邊 手繪 筆畫 Logo 插畫 Line Drawing Stroke Draw Upload Custom
- 標籤 Tag: DrawSVG・上傳
- 範例文字 Example text: 「」（預覽底色：cream，固定文字）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「上傳 SVG 描繪（Draw Your SVG）」動態效果：把我提供的線條 SVG（貼在這段說明後面）做成「像用筆畫出來」的進場：每條路徑依照原本的繪製順序一筆接一筆描出來，每筆的描繪時間依長度分配（長的線畫久一點、短的快一點），筆畫之間稍微重疊銜接，整體約 3 秒、緩入緩出；畫完停留後可淡出重播，或只播放一次。所有圖形改為只描邊、不填色，線端與轉角使用圓角。（GSAP：DrawSVGPlugin，對每個 path / line / polyline / circle 依序 fromTo drawSVG "0%"→"100%"，duration 依 getTotalLength() 比例計算；純 CSS 也可用 stroke-dasharray + stroke-dashoffset 做到）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx133">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「上傳 SVG 描繪」.

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
