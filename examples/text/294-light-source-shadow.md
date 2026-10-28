# 294 · 光源投影字 — Light Source Shadow

游標像一盞燈，文字的長陰影永遠朝游標的反方向延伸

- 元件 Component: 文字 (`text`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、強調重點
- 風格／關鍵字 Style: 光源 投影 陰影 長陰影 立體 游標 Light Source Long Shadow Cursor 3D Text 文字 標題 動態文字
- 標籤 Tag: text-shadow
- 範例文字 Example text: 「SHADOW」（預覽底色：dark）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「光源投影字（Light Source Shadow）」動態效果：區塊中有一個大標題，游標位置是一顆發光的小光源：文字背後有一道由多層陰影組成的長陰影，陰影永遠朝「遠離游標」的方向延伸，越遠的層顏色越淡；游標移動時陰影方向即時跟著轉動，像光源在繞著文字移動。（JS：mousemove 計算游標相對於文字中心的方向向量，產生 18 層 text-shadow，每層偏移 = 方向 × 層數，顏色依層數逐漸變淡）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx294">`, preview text 「SHADOW」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「光源投影字」.

### JavaScript — `FX[294]` from `site/fx.js`

```js
294(s,x,card){const l=el('div','abs gl tx-ls');const t=T(x,Math.min(15,64/chars(x).length));const sun=el('i','tx-sun');l.append(t,sun);s.append(l);
  vpointer(l,card,(px,py)=>{const W=l.offsetWidth,H=l.offsetHeight,dx=(W/2-px)/W,dy=(H/2-py)/H,n=18,sh=[];for(let i=1;i<=n;i++)sh.push(`${(dx*i*1.4).toFixed(1)}px ${(dy*i*1.4).toFixed(1)}px 0 color-mix(in srgb,var(--a) ${Math.round(100-i/n*85)}%,#15161a)`);t.style.textShadow=sh.join(',');sun.style.transform=`translate(${px}px,${py}px)`})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx294` rules from `site/fx.css`

_No dedicated `.fx294` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #294
