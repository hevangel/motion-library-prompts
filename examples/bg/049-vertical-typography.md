# 049 · 直書逆走 — Vertical Typography

直排文字往反方向流

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 背景裝飾
- 風格／關鍵字 Style: 流動背景
- 標籤 Tag: 東方・靜與動
- 範例文字 Example text: 「寂靜」（預覽底色：acc）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「直書逆走（Vertical Typography）」動態效果：多欄直排文字，粗欄與細欄交錯，相鄰欄位一欄往上、一欄往下反方向流動，明體字。大欄慢（約 11 秒）、小欄快（約 6 秒），東方靜與動。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx49">`, preview text 「寂靜」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「直書逆走」.

### JavaScript — `FX[49]` from `site/fx.js`

```js
49(s,x){const c=el('div','cols');for(let i=0;i<6;i++){const e=el('div','col'+(i%2?' rev':''));const w=i%2?'疾走':x;e.innerHTML=chars(rep(w+'　',8)).join('<br>');e.style.fontSize=(i%2?5:9)+'cqw';e.style.setProperty('--dur',(i%2?6:11)+'s');c.append(e)}s.append(c)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx49` rules from `site/fx.css`

```css
.fx49 .cols{position:absolute;inset:0;display:flex;justify-content:space-around;overflow:hidden}
.fx49 .col{align-self:flex-start;text-align:center;font-family:"Noto Serif JP",serif;font-weight:900;color:#111;line-height:1;white-space:nowrap;animation:mqv var(--dur) linear infinite}
.fx49 .col.rev{animation-direction:reverse}
@keyframes mqv{to{transform:translateY(-50%)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #49
