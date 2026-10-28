# 016 · 圓環文字 — Circle Text

文字圓環反向旋轉

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: Logo・品牌、背景裝飾
- 風格／關鍵字 Style: 3D 空間旋轉
- 標籤 Tag: Logo・催眠
- 範例文字 Example text: 「CIRCLE TEXT ✦ 」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「圓環文字（Circle Text）」動態效果：兩圈環狀排列的文字，外圈順時針慢轉、內圈逆時針較快轉，內外圈用不同色調區分。外圈約 9 秒、內圈約 6 秒一圈，催眠 Logo 感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx16">`, preview text 「CIRCLE TEXT ✦ 」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「圓環文字」.

### JavaScript — `FX[16]` from `site/fx.js`

```js
16(s,x){s.append(ringOf(x.repeat(Math.max(1,Math.round(28/chars(x).length))),18,4,'cw'),ringOf(x.repeat(Math.max(1,Math.round(18/chars(x).length))),11,3.4,'ccw'))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx16` rules from `site/fx.css`

```css
.fx16 .ring2.ccw span{color:var(--a)}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #16
