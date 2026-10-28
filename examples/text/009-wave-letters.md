# 009 · 波浪文字 — Wave Letters

文字像波浪上下起伏

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero
- 風格／關鍵字 Style: 逐字律動
- 標籤 Tag: 歡樂・夏日
- 範例文字 Example text: 「うねる波」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「波浪文字（Wave Letters）」動態效果：每個字依序上下起伏並輕微左右擺動，形成連續流動的波浪，字與字可用兩種色調交錯。約 1.4 秒一個波，輕鬆歡樂的夏日感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx9">`, preview text 「うねる波」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「波浪文字」.

### JavaScript — `FX[9]` from `site/fx.js`

```js
9(s,x){s.append(split(x))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx9` rules from `site/fx.css`

```css
.fx9 .c{animation:wv 1.4s calc(var(--i)*-.18s) ease-in-out infinite}
.fx9 .c:nth-child(even){color:var(--a)}
@keyframes wv{0%,100%{transform:translateY(14%) rotate(-4deg)}50%{transform:translateY(-14%) rotate(4deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #9
