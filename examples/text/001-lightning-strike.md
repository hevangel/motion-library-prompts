# 001 · 閃電砸落 — Lightning Strike

伴隨閃電閃光重重砸下

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、強調重點
- 風格／關鍵字 Style: 衝擊登場
- 標籤 Tag: 衝擊・開場
- 範例文字 Example text: 「雷鳴」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「閃電砸落（Lightning Strike）」動態效果：畫面先閃兩下強光並出現一道閃電線，文字從 2 倍大瞬間砸下縮回原尺寸，落地時輕微震動，之後保持柔和的外發光。整段約 2.4 秒，節奏急促有爆發力。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx1">`, preview text 「雷鳴」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「閃電砸落」.

### JavaScript — `FX[1]` from `site/fx.js`

```js
1(s,x){s.append(el('div','flash'));s.insertAdjacentHTML('beforeend','<svg viewBox="0 0 160 90" preserveAspectRatio="none"><polyline points="95,0 82,30 92,32 74,60 84,62 70,90" fill="none" stroke="#fff" stroke-width="1.6"/></svg>');s.append(T(x))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx1` rules from `site/fx.css`

```css
.fx1 .t{animation:ls 2.4s infinite;color:#fff}
.fx1 .flash{position:absolute;inset:0;background:#fff;animation:fl 2.4s infinite;z-index:5;pointer-events:none}
.fx1 svg{position:absolute;inset:0;width:100%;height:100%;animation:fl 2.4s infinite;z-index:4}
@keyframes fl{0%,19%{opacity:0}20%{opacity:.85}23%{opacity:0}25%{opacity:.55}28%,100%{opacity:0}}
@keyframes ls{0%,18%{opacity:0;transform:scale(2.4)}22%{opacity:1;transform:scale(.9)}26%{transform:scale(1.06) translate(-4px,3px)}30%{transform:scale(1) translate(3px,-2px)}34%,85%{transform:none;opacity:1;text-shadow:0 0 10px var(--a),0 0 28px var(--a)}100%{opacity:0;transform:none}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #1
