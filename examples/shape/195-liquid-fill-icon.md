# 195 · 液體填充圖示 — Liquid Fill Icon

圖示內的液面帶著波浪慢慢上升，百分比同步增加

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 循環待機
- 技術 Tech: GSAP
- 情境 Uses: 數字資訊、介面互動、App 介面
- 風格／關鍵字 Style: 液體 填充 波浪 進度 百分比 載入 Liquid Fill Wave Progress Loading Icon SVG 圖形
- 標籤 Tag: SVG clipPath
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「液體填充圖示（Liquid Fill Icon）」動態效果：一個愛心形狀的圖示，內部的液體帶著兩層互相交錯流動的波浪，液面從底部慢慢上升到填滿，中央的百分比數字從 0% 同步增加到 100%；液面以外保留圖示外框。可用於上傳進度、目標達成率。（SVG：用 clipPath 把波浪限制在圖示形狀內；波浪 path 寬度為兩個波長，CSS translateX 無縫循環；液面高度用 GSAP 控制外層 g 的 y，數字同步 tween）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx195">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「液體填充圖示」.

### JavaScript — `FX[195]` from `site/fx.js`

```js
195(s){const id='lq'+Math.random().toString(36).slice(2),H='M50,88 C20,68 6,50 6,32 C6,18 17,8 30,8 C40,8 47,14 50,22 C53,14 60,8 70,8 C83,8 94,18 94,32 C94,50 80,68 50,88 Z',W='M0,10 C12.5,0 37.5,0 50,10 C62.5,20 87.5,20 100,10 C112.5,0 137.5,0 150,10 C162.5,20 187.5,20 200,10 L200,120 L0,120 Z';
  const w=el('div','lqw');w.innerHTML=`<svg viewBox="0 0 100 100"><defs><clipPath id="${id}"><path d="${H}"/></clipPath></defs><g clip-path="url(#${id})"><g class="lv"><path class="w1" d="${W}"/><path class="w2" d="${W}"/></g></g><path class="ol" d="${H}"/></svg><b>0%</b>`;s.append(w);const b=w.querySelector('b'),o={v:0};
  gsap.timeline({repeat:-1,repeatDelay:.5}).fromTo(w.querySelector('.lv'),{y:92},{y:12,duration:3,ease:'power1.inOut'},0).fromTo(o,{v:0},{v:100,duration:3,ease:'power1.inOut',onUpdate:()=>b.textContent=Math.round(o.v)+'%'},0).to({},{duration:.8})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx195` rules from `site/fx.css`

_No dedicated `.fx195` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #195
