# 245 · 滑桿數值氣泡 — Range Slider Bubble

拖曳滑桿時上方彈出數值氣泡，跟著把手移動，放開時縮回

- 元件 Component: 表單・控制項 (`control`)
- 時機 Timing: 拖曳手勢
- 技術 Tech: CSS
- 情境 Uses: 介面互動、數字資訊
- 風格／關鍵字 Style: 滑桿 拉桿 數值 氣泡 範圍 音量 Range Slider Tooltip Bubble Value Input 表單 控制項
- 標籤 Tag: input range
- 範例文字 Example text: 「音量」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「滑桿數值氣泡（Range Slider Bubble）」動態效果：範圍滑桿：已拖過的軌道部分填滿；按住或拖曳把手時，把手微微放大，正上方彈出一個帶小三角的數值氣泡，氣泡跟著把手水平移動並即時顯示數字；放開時氣泡縮小淡出。（CSS：自訂 input[type=range] 的軌道與 ::-webkit-slider-thumb；軌道填滿用背景 linear-gradient 搭配 CSS 變數百分比；氣泡為絕對定位的 output，left = 把手寬度 / 2 + (軌道寬 − 把手寬) × 百分比，以 scale 與 opacity 做彈出）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx245">`, preview text 「音量」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「滑桿數值氣泡」.

### JavaScript — `FX[245]` from `site/fx.js`

```js
245(s,x,card){const w=el('div','fm-rg');w.innerHTML='<label></label><div class="fm-rt"><input type="range" min="0" max="100" value="40"><output></output></div>';w.querySelector('label').textContent=x;s.append(w);const r=w.querySelector('input'),o=w.querySelector('output');
  const upd=()=>{const v=+r.value;w.style.setProperty('--p',v);o.textContent=v};r.addEventListener('input',upd);upd();let real=0;['pointerdown','focus'].forEach(e=>r.addEventListener(e,()=>{real=Date.now();w.classList.add('drag')}));['pointerup','blur'].forEach(e=>r.addEventListener(e,()=>w.classList.remove('drag')));
  let t=0;card._kill.push(()=>{});ticks.set(card,tm=>{if(Date.now()-real<5000)return;r.value=Math.round(50+42*Math.sin(tm*.9));upd();w.classList.toggle('drag',Math.cos(tm*.9)>-.3)})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx245` rules from `site/fx.css`

_No dedicated `.fx245` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #245
