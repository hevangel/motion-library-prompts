# 268 · 縮圖列相簿 — Thumbnail Gallery

點下方縮圖，大圖從側邊推入換張並微微縮回，指示條滑到目前縮圖

- 元件 Component: 圖片・媒體 (`media`)
- 時機 Timing: 切換、循環待機
- 技術 Tech: GSAP
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 相簿 縮圖 大圖 商品圖 輪播 Gallery Thumbnails Slider Product Images Carousel 圖片 媒體
- 標籤 Tag: GSAP
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「縮圖列相簿（Thumbnail Gallery）」動態效果：商品相簿：上方一張大圖，下方一排縮圖；點擊某張縮圖時，新的大圖從對應方向（往後點從右、往前點從左）推入，舊圖往反方向稍微移出，新圖內部同時從 1.25 倍緩緩縮回原尺寸，增加景深感；縮圖列中目前那張變得完全不透明，其他半透明，下方一條指示條滑動並對齊目前縮圖；也可以自動輪播。（GSAP：新圖 fromTo xPercent ±100 → 0，舊圖 to xPercent ∓30，power3.inOut 0.6 秒；指示條用 CSS transform 與 width 過渡）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx268">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「縮圖列相簿」.

### JavaScript — `FX[268]` from `site/fx.js`

```js
268(s,x,card){const w=el('div','md-gl');w.innerHTML='<div class="md-gm"></div><div class="md-gs"><i class="md-gi"></i></div>';const gm=w.querySelector('.md-gm'),gs=w.querySelector('.md-gs'),gi=w.querySelector('.md-gi');
  const big=[0,1,2,3].map(i=>{const d=el('div','md-gb');d.innerHTML=mdImg(i);gm.append(d);return d});const th=[0,1,2,3].map(i=>{const b=el('button','md-gt');b.setAttribute('aria-label','第 '+(i+1)+' 張');b.innerHTML=mdImg(i);b.onclick=()=>{real=Date.now();go(i)};gs.append(b);return b});s.append(w);let cur=-1,real=0;
  const go=i=>{if(i===cur)return;const dir=i>cur?1:-1;big.forEach((d,j)=>{d.style.zIndex=j===i?2:j===cur?1:0});if(cur>=0)gsap.to(big[cur],{xPercent:-30*dir,duration:.6,ease:'power3.inOut'});gsap.fromTo(big[i],{xPercent:100*dir,scale:1},{xPercent:0,duration:.6,ease:'power3.inOut'});gsap.fromTo(big[i].firstChild,{scale:1.25},{scale:1,duration:.9,ease:'power2.out'});
    cur=i;th.forEach((b,j)=>b.classList.toggle('on',j===i));gi.style.transform=`translateX(${th[i].offsetLeft}px)`;gi.style.width=th[i].offsetWidth+'px'};requestAnimationFrame(()=>{go(0)});
  card._timers.push(setInterval(()=>{if(Date.now()-real>5000)go((cur+1)%4)},2000))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx268` rules from `site/fx.css`

_No dedicated `.fx268` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #268
