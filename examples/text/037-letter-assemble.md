# 037 · 文字聚集 — Letter Assemble

散落的文字聚集

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、Logo・品牌
- 風格／關鍵字 Style: 衝擊登場
- 標籤 Tag: 標題・導入
- 範例文字 Example text: 「あつまる」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「文字聚集（Letter Assemble）」動態效果：文字的每個字從畫面四處、帶著旋轉與模糊放大飛進來，逐一聚集到正確位置並變清晰，停留後再散開。約 3.2 秒一輪，標題導入感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx37">`, preview text 「あつまる」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「文字聚集」.

### JavaScript — `FX[37]` from `site/fx.js`

```js
37(s,x){const t=split(x);t.querySelectorAll('.c').forEach(c=>{c.style.setProperty('--dx',rnd(-35,35)+'cqw');c.style.setProperty('--dy',rnd(-22,22)+'cqw');c.style.setProperty('--r',rnd(-180,180)+'deg')});s.append(t)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx37` rules from `site/fx.css`

```css
.fx37 .c{animation:asm 3.2s calc(var(--i)*.12s) infinite cubic-bezier(.2,.9,.3,1.1)}
.fx37 .c:nth-child(odd){color:var(--a)}
@keyframes asm{0%{transform:translate(var(--dx),var(--dy)) rotate(var(--r)) scale(1.6);opacity:0;filter:blur(6px)}12%{opacity:.6}50%,82%{transform:none;opacity:1;filter:none}100%{transform:translate(var(--dx),var(--dy)) rotate(var(--r)) scale(1.6);opacity:0;filter:blur(6px)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #37
