# 031 · ∞ 軌道 — Roller Path

文字沿 ∞ 軌道奔馳

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 背景裝飾
- 風格／關鍵字 Style: 流動背景
- 標籤 Tag: 疾走・歡樂
- 範例文字 Example text: 「ころがる」（預覽底色：cream）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「∞ 軌道（Roller Path）」動態效果：每個字沿著一條「∞」形的虛線軌道依序奔跑，字會隨行進方向轉向，像小車隊一樣首尾相接。約 4.5 秒繞一圈，歡樂疾走感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx31">`, preview text 「ころがる」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「∞ 軌道」.

### JavaScript — `FX[31]` from `site/fx.js`

```js
31(s,x){const P='M160,90 C200,30 280,30 280,90 C280,150 200,150 160,90 C120,30 40,30 40,90 C40,150 120,150 160,90 Z';const cs=chars(x);
  s.insertAdjacentHTML('beforeend',`<svg viewBox="0 0 320 180"><path d="${P}" fill="none" stroke="#111" stroke-opacity=".25" stroke-width="2" stroke-dasharray="2 6" stroke-linecap="round"/>${cs.map((c,i)=>`<text font-size="30" font-weight="900" text-anchor="middle" dy="10" fill="${i%2?'#111':'var(--a)'}">${c}<animateMotion dur="4.5s" repeatCount="indefinite" rotate="auto" begin="${-(cs.length-i)*0.22}s" path="${P}"/></text>`).join('')}</svg>`)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx31` rules from `site/fx.css`

```css
.fx31 svg{width:100%;height:100%}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #31
