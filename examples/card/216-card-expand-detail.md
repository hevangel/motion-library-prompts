# 216 · 卡片展開詳情 — Card Expand Detail

點擊卡片時它平滑放大成詳情面板，其他卡片淡出

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 切換
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、轉場切換
- 風格／關鍵字 Style: 卡片 展開 詳情 放大 共享元素 shared element transition Expand Detail Flip 卡片 群組
- 標籤 Tag: Flip
- 範例文字 Example text: 「作品一 作品二 作品三 作品四」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「卡片展開詳情（Card Expand Detail）」動態效果：一排作品卡片，點擊其中一張時，它從原本的位置與大小平滑放大成填滿整個區塊的詳情面板（左側大圖、右側標題與說明），其他卡片同時淡出；詳情內的文字在放大完成前後依序淡入；再點一次則縮回原位、其他卡片淡回。約 0.6 秒、緩入緩出。（GSAP Flip：Flip.getState 記錄所有卡片 → 切換放大那張的 class（改成絕對定位填滿容器與新版面）→ Flip.from 補間，nested:true 讓內部元素一起變形）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx216">`, preview text 「作品一 作品二 作品三 作品四」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「卡片展開詳情」.

### JavaScript — `FX[216]` from `site/fx.js`

```js
216(s,x,card){const ws=words(x);const g=el('div','kd-xg');const cs=[...Array(4)].map((_,i)=>{const c=el('div','kd-xc');c.innerHTML='<i class="kd-xi"></i><b></b><div class="kd-xd"><em></em><em></em><em class="s"></em></div>';c.querySelector('.kd-xi').style.background=`linear-gradient(140deg,${GC[i%5]},${GC[(i+2)%5]})`;c.querySelector('b').textContent=ws[i%ws.length];g.append(c);return c});s.append(g);let open=null,real=0,k=0;
  const tog=c=>{const st=Flip.getState(cs);if(open){open.classList.remove('big');g.classList.remove('has');open=open===c?null:c}else open=c;if(open){open.classList.add('big');g.classList.add('has')}Flip.from(st,{duration:.6,ease:'power3.inOut',absolute:true,nested:true});if(open)gsap.fromTo(open.querySelectorAll('.kd-xd em'),{opacity:0,y:8},{opacity:1,y:0,stagger:.06,delay:.35,duration:.35})};
  cs.forEach(c=>c.onclick=()=>{real=Date.now();tog(c)});card._timers.push(setInterval(()=>{if(Date.now()-real<4000)return;tog(open?open:cs[k++%4])},1600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx216` rules from `site/fx.css`

_No dedicated `.fx216` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #216
