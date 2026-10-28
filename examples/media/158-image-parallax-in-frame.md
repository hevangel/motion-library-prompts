# 158 · 圖框內視差 — Image Parallax in Frame

圖片在框裡移動得比捲動慢，產生深度

- 元件 Component: 圖片・媒體 (`media`)
- 時機 Timing: 捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 捲動效果、標題・Hero
- 風格／關鍵字 Style: 圖片 視差 圖框 照片 景深 Image Parallax Frame Inner Parallax Gallery 捲動 滾動 scroll ScrollTrigger scrub 捲動觸發
- 標籤 Tag: ScrollTrigger scrub
- 範例文字 Example text: 「清晨 午後 夜晚」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「圖框內視差（Image Parallax in Frame）」動態效果：一列上下排列的圖片，每張圖片外框固定、裁切超出的部分，圖片本身比外框高一些；捲動時圖片在框內以較慢的速度反向位移（從上偏到下偏約 ±12%），看起來像窗外的風景，比整塊一起捲動更有深度；圖片下方有簡短說明。（GSAP：外框 overflow:hidden，內層圖高約 128%，每張圖一個 ScrollTrigger，start "top bottom"、end "bottom top"，scrub yPercent -12→12）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx158">`, preview text 「清晨 午後 夜晚」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「圖框內視差」.

### JavaScript — `FX[158]` from `site/fx.js`

```js
158(s,x){const sc=el('div','scr');const ws=words(x);const P=[['#9fd3ff','#ffe1b0','#4f7a6a','#264a3f','#fff6d8'],['#ffd9c2','#c9b6ff','#7b6ca8','#3f3566','#fff6e6'],['#1b1f4a','#4a2a6b','#2c2a55','#14122e','#f4f1d0']];
  sc.innerHTML='<div class="pxs"></div>';const box=sc.firstChild;P.forEach((c,i)=>{const fr=el('figure','pxf');fr.innerHTML=`<div class="pxi">${scene(...c)}</div><figcaption></figcaption>`;fr.querySelector('figcaption').textContent=ws[i%ws.length];box.append(fr)});s.append(sc);
  box.querySelectorAll('.pxf').forEach(fr=>gsap.fromTo(fr.querySelector('.pxi'),{yPercent:-12},{yPercent:12,ease:'none',scrollTrigger:{trigger:fr,scroller:sc,start:'top bottom',end:'bottom top',scrub:true}}));autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx158` rules from `site/fx.css`

_No dedicated `.fx158` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #158
