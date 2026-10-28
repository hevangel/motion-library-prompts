# 210 · 左右分割捲動 — Split Screen Scroll

右側文字往下捲，左側固定的圖片跟著切換對應的段落

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 捲動效果、標題・Hero
- 風格／關鍵字 Style: 分割畫面 左右 雙欄 固定 圖片切換 說故事 Split Screen Sticky Image Scrollytelling 版面 頁面 網頁結構
- 標籤 Tag: Sticky・ScrollTrigger
- 範例文字 Example text: 「清晨 午後 夜晚」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「左右分割捲動（Split Screen Scroll）」動態效果：畫面分成左右兩欄：左欄是固定不動（sticky）的大圖區，右欄是一段段可以捲動的文字章節；每當右側某一章節捲到畫面中段時，左側圖片交叉淡入成對應章節的圖片，並從略為放大的狀態縮回原尺寸，形成圖文同步的說故事體驗。（CSS position:sticky + GSAP ScrollTrigger：每個章節 start "top 55%"、end "bottom 55%"，onToggle 切換左側對應圖片的 active class；圖片用 opacity 與 scale 的 transition）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx210">`, preview text 「清晨 午後 夜晚」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「左右分割捲動」.

### JavaScript — `FX[210]` from `site/fx.js`

```js
210(s,x){const ws=words(x).slice(0,3);const sc=el('div','scr nopad ly-sp');const P=[['#9fd3ff','#ffe1b0','#4f7a6a','#264a3f','#fff6d8'],['#ffd9c2','#c9b6ff','#7b6ca8','#3f3566','#fff6e6'],['#1b1f4a','#4a2a6b','#2c2a55','#14122e','#f4f1d0']];
  sc.innerHTML='<div class="ly-sl"><div class="ly-si"></div></div><div class="ly-sr"></div>';const si=sc.querySelector('.ly-si'),sr=sc.querySelector('.ly-sr');const ims=P.map((p,i)=>{const d=el('div','ly-im'+(i?'':' on'));d.innerHTML=scene(...p);si.append(d);return d});
  ws.forEach((v,i)=>{const sec=el('section');sec.innerHTML=`<small>0${i+1}</small><b></b><i class="ly-bl"></i><i class="ly-bl s"></i>`;sec.querySelector('b').textContent=v;sr.append(sec);ScrollTrigger.create({trigger:sec,scroller:sc,start:'top 55%',end:'bottom 55%',onToggle:t=>{if(t.isActive)ims.forEach((m,j)=>m.classList.toggle('on',j===i))}})});s.append(sc);autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx210` rules from `site/fx.css`

_No dedicated `.fx210` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #210
