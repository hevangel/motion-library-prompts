# 105 · 3D 傾斜視差圖片 — Tilt Parallax Image

hover 時圖片跟著游標 3D 傾斜，景物分層視差、反光與說明滑出

- 元件 Component: 圖片・媒體 (`media`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、強調重點
- 風格／關鍵字 Style: 圖片 照片 hover 懸停 3D 傾斜 視差 反光 Tilt Parallax Glare Image Hover Card
- 標籤 Tag: quickTo・3D
- 範例文字 Example text: 「山嵐 夕照」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「3D 傾斜視差圖片（Tilt Parallax Image）」動態效果：一張圖片卡片，滑鼠在圖片上移動時，整張圖以游標位置為方向做 3D 傾斜（最多約 ±10 度）並微微放大；圖片內的遠景、中景、近景分層往反方向位移，形成視差景深；一道柔和的反光跟著游標移動；同時底部的說明文字（小標＋標題）從下方滑上來。滑鼠離開時全部平滑回正、說明收回。（GSAP：gsap.quickTo 控制 rotationX / rotationY / scale，父層設 perspective；各圖層用 quickTo 依不同係數位移；反光用 radial-gradient 搭配 CSS 變數 --gx、--gy 定位；說明用 transform 過場）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx105">`, preview text 「山嵐 夕照」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「3D 傾斜視差圖片」.

### JavaScript — `FX[105]` from `site/fx.js`

```js
105(s,x){const l=layer(s);l.style.perspective='700px';const id='tg'+Math.random().toString(36).slice(2);const f=el('div','tilt');
  f.innerHTML=`<svg viewBox="0 0 160 120" preserveAspectRatio="xMidYMid slice"><defs><linearGradient id="${id}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffb36b"/><stop offset="1" stop-color="#ff6b8b"/></linearGradient></defs><rect x="-20" y="-20" width="200" height="160" fill="url(#${id})"/><g class="l1"><circle cx="108" cy="42" r="15" fill="#fff3d6"/></g><g class="l2"><path d="M-30,92 L28,48 L60,72 L96,36 L140,80 L190,56 L190,140 L-30,140Z" fill="#8a3f6e"/></g><g class="l3"><path d="M-30,110 L18,82 L54,102 L92,78 L132,104 L190,84 L190,140 L-30,140Z" fill="#3b1f45"/></g></svg><div class="glare"></div><div class="cap"><small>PHOTO</small><b></b></div>`;
  f.querySelector('.cap b').textContent=x;l.append(f);
  const q=(e,k,d=.5)=>gsap.quickTo(e,k,{duration:d,ease:'power3.out'});const rx=q(f,'rotationX'),ry=q(f,'rotationY'),sc=q(f,'scale');
  const ls=[...f.querySelectorAll('.l1,.l2,.l3')].map((g,i)=>[q(g,'x',.6),q(g,'y',.6),[4,8,13][i]]);
  pointer(l,(px,py)=>{const nx=(px-f.offsetLeft)/f.offsetWidth,ny=(py-f.offsetTop)/f.offsetHeight,inside=nx>=0&&nx<=1&&ny>=0&&ny<=1;f.classList.toggle('on',inside);
    const dx=inside?nx-.5:0,dy=inside?ny-.5:0;rx(-dy*18);ry(dx*22);sc(inside?1.05:1);ls.forEach(([a,b,k])=>{a(-dx*k);b(-dy*k*.6)});f.style.setProperty('--gx',nx*100+'%');f.style.setProperty('--gy',ny*100+'%')},
    [[.5,.5],[.36,.34],[.64,.38],[.6,.66],[.38,.64],[.08,.2],[.92,.85]])}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx105` rules from `site/fx.css`

_No dedicated `.fx105` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #105
