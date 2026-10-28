# 134 · 手寫簽名 — Signature Writing

一顆筆尖沿著簽名路徑書寫，最後補上一道底線

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: Logo・品牌、標題・Hero
- 風格／關鍵字 Style: 簽名 手寫 草寫 書寫 筆尖 Signature Handwriting Cursive Pen Write On
- 標籤 Tag: DrawSVG・MotionPath
- 範例文字 Example text: 「」（預覽底色：cream，固定文字）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「手寫簽名（Signature Writing）」動態效果：一個草寫簽名的線條路徑，從起筆處開始被慢慢寫出來，路徑最前端有一顆小圓點筆尖跟著移動，像真的有人在書寫（約 2.6 秒、緩入緩出）；簽名寫完後筆尖消失，下方再快速劃出一道微彎的底線收尾。適合作品集 Hero 或品牌簽名。（GSAP：DrawSVGPlugin 描繪簽名路徑，同時用 MotionPathPlugin 讓筆尖圓點沿同一條路徑移動，兩者時間與 ease 相同；簽名需是單筆的描邊路徑，不是外框字）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx134">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「手寫簽名」.

### JavaScript — `FX[134]` from `site/fx.js`

```js
134(s){const id='sg'+Math.random().toString(36).slice(2);s.insertAdjacentHTML('beforeend',`<svg class="sig" viewBox="0 0 160 90"><path id="${id}" d="M14,58 C22,30 30,18 34,22 C38,27 30,52 26,64 C34,44 44,36 48,42 C52,48 46,62 52,62 C58,62 60,44 66,42 C72,40 70,58 66,60 C62,62 62,48 70,46 C78,44 76,62 82,60 C88,58 90,40 96,40 C102,40 98,60 104,58 C110,56 112,42 118,42 C124,42 120,60 126,58 C132,56 136,36 142,30"/><path class="sw" d="M20,74 C60,66 110,66 146,72"/><circle class="nib" r="2.4"/></svg>`);
  const sv=s.querySelector('.sig'),p=sv.querySelector('#'+id),sw=sv.querySelector('.sw'),nib=sv.querySelector('.nib');
  gsap.timeline({repeat:-1,repeatDelay:.5}).set(sv,{opacity:1},0).fromTo(p,{drawSVG:'0%'},{drawSVG:'100%',duration:2.6,ease:'power1.inOut'},0).fromTo(nib,{opacity:1},{motionPath:{path:p,align:p,alignOrigin:[.5,.5]},duration:2.6,ease:'power1.inOut'},0)
    .fromTo(sw,{drawSVG:'0%'},{drawSVG:'100%',duration:.7,ease:'power2.out'}).to(nib,{opacity:0,duration:.2},'<').to(sv,{opacity:0,duration:.5},'+=1.4')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx134` rules from `site/fx.css`

_No dedicated `.fx134` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #134
