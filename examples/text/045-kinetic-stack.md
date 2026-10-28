# 045 · 動態堆疊 — Kinetic Stack

詞一個個飛進來疊起來

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero
- 風格／關鍵字 Style: 衝擊登場
- 標籤 Tag: MV・歌詞
- 範例文字 Example text: 「穿過 黑夜 現在就走」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「動態堆疊（Kinetic Stack）」動態效果：三行詞彙分別從左、右、下方旋轉飛入，依序疊成一組置中排版，每行字級不同、中間那行用強調色，停留後一起淡出。約 3.4 秒一輪，MV 歌詞感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx45">`, preview text 「穿過 黑夜 現在就走」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「動態堆疊」.

### JavaScript — `FX[45]` from `site/fx.js`

```js
45(s,x){const w=el('div','w');const ws=words(x);const dirs=[['-60cqw','0','-20deg'],['60cqw','0','15deg'],['0','40cqw','0deg'],['0','-40cqw','8deg']];ws.forEach((t,i)=>{const d=el('div');d.textContent=t;d.style.setProperty('--i',i);d.style.fontSize=(i===ws.length-1?9:i===1?13:8)+'cqw';const [fx,fy,fr]=dirs[i%4];d.style.setProperty('--fx',fx);d.style.setProperty('--fy',fy);d.style.setProperty('--fr',fr);w.append(d)});s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx45` rules from `site/fx.css`

```css
.fx45 .w{display:flex;flex-direction:column;align-items:center;gap:.6cqw}
.fx45 .w div{font-weight:900;line-height:1.1;color:#fff;animation:ks 3.4s calc(var(--i)*.35s) infinite both cubic-bezier(.2,.9,.3,1.15)}
.fx45 .w div:nth-child(2){color:var(--a)}
@keyframes ks{0%{opacity:0;transform:translate(var(--fx),var(--fy)) rotate(var(--fr)) scale(1.4)}13%{opacity:1;transform:none}82%{opacity:1;transform:none}96%,100%{opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #45
