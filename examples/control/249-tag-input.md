# 249 · 標籤輸入 — Tag Input

輸入文字按 Enter 變成彈出的標籤，按 × 或倒退鍵時標籤縮小消失

- 元件 Component: 表單・控制項 (`control`)
- 時機 Timing: 進場、退場
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 標籤 tag chip 輸入 關鍵字 興趣 Tag Input Chips Token Field 表單 控制項
- 標籤 Tag: JS + CSS
- 範例文字 Example text: 「設計 動態 前端 插畫 品牌」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「標籤輸入（Tag Input）」動態效果：標籤輸入框：使用者輸入文字後按 Enter（或逗號），文字變成一顆膠囊標籤，從 0 帶回彈放大出現在輸入游標前方；每顆標籤右側有 × 按鈕，點擊或在空白輸入框按倒退鍵時，最後一顆標籤縮小淡出並讓後面的內容平滑補位；整個框聚焦時外框亮起。（JS：keydown 處理 Enter／逗號／Backspace，新增元素插在 input 前；CSS keyframes：進場 scale 0→1 用 cubic-bezier(.3,1.6,.5,1)，退場 scale→0 並用負的 margin-right 收合，animationend 後移除元素）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx249">`, preview text 「設計 動態 前端 插畫 品牌」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「標籤輸入」.

### JavaScript — `FX[249]` from `site/fx.js`

```js
249(s,x,card){const w=el('div','fm-tg');w.innerHTML='<div class="fm-tb"><input aria-label="新增標籤" placeholder="輸入後按 Enter"></div>';const tb=w.querySelector('.fm-tb'),inp=tb.querySelector('input');s.append(w);let real=0;
  const add=t=>{t=t.trim();if(!t)return;const c=el('span','fm-chip');c.innerHTML='<b></b><button type="button" aria-label="移除">×</button>';c.querySelector('b').textContent=t;c.querySelector('button').onclick=()=>{real=Date.now();del(c)};tb.insertBefore(c,inp)};
  const del=c=>{c.classList.add('out');c.addEventListener('animationend',()=>c.remove(),{once:true})};
  inp.addEventListener('keydown',e=>{real=Date.now();if((e.key==='Enter'||e.key===',')&&inp.value.trim()){e.preventDefault();add(inp.value);inp.value=''}else if(e.key==='Backspace'&&!inp.value){const cs=tb.querySelectorAll('.fm-chip:not(.out)');if(cs.length)del(cs[cs.length-1])}});
  const ws=words(x);ws.slice(0,2).forEach(add);let k=2;card._timers.push(setInterval(()=>{if(Date.now()-real<6000||document.activeElement===inp)return;const cs=tb.querySelectorAll('.fm-chip:not(.out)');if(cs.length>=3)del(cs[0]);else add(ws[k++%ws.length])},1300))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx249` rules from `site/fx.css`

_No dedicated `.fx249` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #249
