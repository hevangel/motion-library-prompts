# 074 · 螢光筆 — Highlight Text

螢光筆從字後面劃過

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: CSS
- 情境 Uses: 強調重點
- 風格／關鍵字 Style: 質感填色
- 標籤 Tag: 強調・解說
- 範例文字 Example text: 「一句話的力量」（預覽底色：acc）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「螢光筆（Highlight Text）」動態效果：卡片上的文字，一條螢光筆線由左往右從字的下半部後方劃過，停留後淡出。劃過約 1 秒，整輪約 3 秒，強調解說感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx74">`, preview text 「一句話的力量」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「螢光筆」.

### JavaScript — `FX[74]` from `site/fx.js`

```js
74(s,x){const p=el('div','panel');p.append(T(x,Math.min(9,64/chars(x).length)));s.append(p)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx74` rules from `site/fx.css`

```css
.fx74 .panel{background:#fff;padding:3cqw 4cqw;border-radius:1cqw}
.fx74 .t{color:#111;position:relative;z-index:1}
.fx74 .t::before{content:"";position:absolute;left:-1%;bottom:4%;height:42%;width:0;background:var(--l);z-index:-1;animation:hlt 3s infinite cubic-bezier(.6,0,.3,1)}
@keyframes hlt{0%,10%{width:0}45%,85%{width:102%}100%{width:102%;opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #74
