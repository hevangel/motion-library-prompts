# 051 · 緞帶 — Text Ribbon

文字沿著波浪線流動

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 背景裝飾
- 風格／關鍵字 Style: 流動背景
- 標籤 Tag: 裝飾・配樂感
- 範例文字 Example text: 「跟著節奏走」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「緞帶（Text Ribbon）」動態效果：一條寬的半透明波浪緞帶橫過畫面，文字沿著波浪曲線持續流動前進。約 2.4 秒流過一段，有配樂律動的裝飾感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx51">`, preview text 「跟著節奏走」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「緞帶」.

### JavaScript — `FX[51]` from `site/fx.js`

```js
51(s,x){const id='rb'+Math.random().toString(36).slice(2);const unit=x+'・';const L=chars(unit).length*18;const P='M-30,130 C40,40 110,40 160,95 S270,150 350,55';
  s.insertAdjacentHTML('beforeend',`<svg viewBox="0 0 320 180"><path id="${id}" d="${P}" fill="none" stroke="#ffffff12" stroke-width="34"/><text font-size="18" font-weight="900" fill="#fff" dy="6"><textPath href="#${id}" startOffset="0">${rep(unit,9)}<animate attributeName="startOffset" from="${-L}" to="0" dur="2.4s" repeatCount="indefinite"/></textPath></text></svg>`)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx51` rules from `site/fx.css`

```css
.fx51 svg,.fx56 svg{width:100%;height:100%}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #51
