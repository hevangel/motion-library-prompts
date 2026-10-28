# 185 · 翻滾 — Tumble

每個字從縮小狀態旋轉翻滾著登場

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、強調重點
- 風格／關鍵字 Style: 翻滾 旋轉 登場 逐字 俏皮 Tumble Spin Rotate In Canva 風格 Canva Tumble 翻滾 簡報 社群貼文 動畫
- 標籤 Tag: CSS keyframes
- 範例文字 Example text: 「翻滾登場」（預覽底色：acc）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「翻滾（Tumble）」動態效果：每個字從約 0.2 倍大、逆時針旋轉 200 度的狀態，一邊轉正一邊放大登場，最後略微過衝（轉過頭 10 度、放大到 1.08）再回正，字與字之間依序延遲約 0.08 秒，俏皮有活力。（CSS：每個字 inline-block，keyframes rotate(-200deg) scale(.2) → rotate(10deg) scale(1.08) → none，animation-delay 依索引遞增）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx185">`, preview text 「翻滾登場」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「翻滾」.

### JavaScript — `FX[185]` from `site/fx.js`

```js
185(s,x){s.append(split(x.replace(/ /g,' '),Math.min(14,64/chars(x).length)))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx185` rules from `site/fx.css`

```css
.fx185 .c{animation:tumble 3.6s cubic-bezier(.2,.8,.3,1.1) infinite;animation-delay:calc(var(--i) * .08s)}
@keyframes tumble{0%{transform:rotate(-200deg) scale(.2);opacity:0}24%{transform:rotate(10deg) scale(1.08);opacity:1}32%,80%{transform:none;opacity:1}92%,100%{transform:none;opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #185
