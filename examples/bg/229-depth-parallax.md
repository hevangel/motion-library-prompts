# 229 · 景深視差圖層 — Depth Parallax

前中後三層圖形依距離不同幅度跟著游標反向移動，產生立體感

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、背景裝飾
- 風格／關鍵字 Style: 視差 景深 圖層 立體 滑鼠 游標 Mouse Parallax Depth Layers 3D Hero 背景 氛圍
- 標籤 Tag: JS parallax
- 範例文字 Example text: 「Depth」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「景深視差圖層（Depth Parallax）」動態效果：Hero 背景由三層裝飾圖形組成：遠層是模糊的大圓、中層是圓角方塊、前層是空心圓環，標題夾在中層與前層之間；游標在區塊內移動時，各層朝游標的反方向移動，越近的圖層移動幅度越大（例如遠層 15%、中層 45%、前層 100%），標題只微微移動，形成立體的景深感，移動帶有平滑的延遲跟隨。（JS：mousemove 計算游標相對於中心的比例 -0.5 ~ 0.5，每層 translate = -比例 × 該層係數，搭配 CSS transition 或 lerp 平滑）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx229">`, preview text 「Depth」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「景深視差圖層」.

### JavaScript — `FX[229]` from `site/fx.js`

```js
229(s,x,card){const w=el('div','abs bga-dp');const L=[[.15,7,'o'],[.45,5,'s'],[1,4,'r']].map(([k,n,cl],li)=>{const l=el('div','abs bga-dl');l._k=k;for(let i=0;i<n;i++){const e=el('i','bga-'+cl);e.style.cssText=`left:${(i+.5)/n*100+rnd(-8,8)}%;top:${rnd(10,85)}%;--z:${(li+1)*3+rnd(0,3)}cqw;background:${cl==='r'?'transparent':li===1?'var(--a)':GC[(i+li)%5]}`;l.append(e)}w.append(l);return l});
  const t=T(x,Math.min(12,56/chars(x).length));t.classList.add('bga-dt');w.insertBefore(t,L[2]);s.append(w);
  vpointer(w,card,(px,py)=>{const W=w.offsetWidth,H=w.offsetHeight,dx=px/W-.5,dy=py/H-.5;L.forEach(l=>l.style.transform=`translate(${-dx*l._k*14}cqw,${-dy*l._k*9}cqw)`);t.style.transform=`translate(${-dx*3}cqw,${-dy*2}cqw)`})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx229` rules from `site/fx.css`

_No dedicated `.fx229` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #229
