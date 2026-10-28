# 024 · 文字扇 — Text Fan

同一字像扇子般展開

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: CSS
- 情境 Uses: Logo・品牌、標題・Hero
- 風格／關鍵字 Style: 3D 空間旋轉
- 標籤 Tag: 和風・登場
- 範例文字 Example text: 「扇」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「文字扇（Text Fan）」動態效果：同一個字複製 7 份疊在一起，以字下方為軸心像扇子一樣展開成扇形，停留後再收合。中央那份不透明，其餘半透明。約 3 秒一輪，和風登場感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx24">`, preview text 「扇」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「文字扇」.

### JavaScript — `FX[24]` from `site/fx.js`

```js
24(s,x){const w=el('div','w');const ch=chars(x)[0];for(let i=0;i<7;i++){const sp=el('span');sp.textContent=ch;sp.style.setProperty('--a2',(i-3)*24+'deg');sp.style.opacity=i===3?1:.45+Math.abs(3-i)*-.08+.25;if(i!==3)sp.style.color='var(--a)';sp.style.zIndex=i===3?2:1;w.append(sp)}s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx24` rules from `site/fx.css`

```css
.fx24 .w{position:relative;width:1px;height:1px}
.fx24 .w span{position:absolute;left:0;top:0;font-weight:900;font-size:17cqw;line-height:1;transform-origin:50% 140%;translate:-50% -60%;animation:fan 3s ease-in-out infinite;color:#fff}
@keyframes fan{0%,12%{transform:rotate(0)}45%,80%{transform:rotate(var(--a2))}100%{transform:rotate(0)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #24
