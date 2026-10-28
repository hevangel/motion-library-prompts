# 310 · 照片堆展開 — Stack to Grid

一疊散亂的照片，點一下平滑排成整齊的網格，再點收回成一疊

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 切換
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、標題・Hero
- 風格／關鍵字 Style: 照片 堆疊 展開 網格 相簿 整理 Photo Pile Stack To Grid Spread Flip 卡片 群組
- 標籤 Tag: Flip
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「照片堆展開（Stack to Grid）」動態效果：一疊散亂的照片（每張帶寬邊框、隨機歪斜不同角度、疊在中央）：點擊後，照片一張接一張（間隔約 0.04 秒）平滑地飛到整齊的 3 × 2 網格位置並轉正；再點一次則從網格飛回成散亂的一疊。約 0.7 秒、緩入緩出。（GSAP Flip：Flip.getState(照片) → 切換容器的 class（從絕對定位堆疊改成 grid 排列、rotate 歸零）→ Flip.from(state, {absolute:true, stagger:.04})）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx310">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「照片堆展開」.

### JavaScript — `FX[310]` from `site/fx.js`

```js
310(s,x,card){const w=el('div','cg-sg2');const cs=[0,1,2,3,4,5].map(i=>{const c=el('div','cg-ph');c.innerHTML=mdImg(i);c.style.setProperty('--r',((i*37)%25-12)+'deg');w.append(c);return c});const lb=el('div','cg-lb','點一下展開');s.append(w,lb);let open=false,real=0;
  const tog=()=>{const st=Flip.getState(cs);open=!open;w.classList.toggle('open',open);lb.textContent=open?'點一下收起':'點一下展開';Flip.from(st,{duration:.7,ease:'power3.inOut',stagger:.04,absolute:true})};
  w.onclick=()=>{real=Date.now();tog()};card._timers.push(setInterval(()=>{if(Date.now()-real>5000)tog()},2400))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx310` rules from `site/fx.css`

_No dedicated `.fx310` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #310
