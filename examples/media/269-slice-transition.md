# 269 · 切片轉場 — Slice Transition

圖片被切成直條，一條上一條下依序滑走，露出下一張

- 元件 Component: 圖片・媒體 (`media`)
- 時機 Timing: 切換、循環待機
- 技術 Tech: GSAP
- 情境 Uses: 轉場切換、標題・Hero
- 風格／關鍵字 Style: 切片 直條 轉場 換圖 百葉窗 Slice Strips Image Transition Slideshow Venetian 圖片 媒體
- 標籤 Tag: GSAP stagger
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「切片轉場（Slice Transition）」動態效果：圖片輪播的轉場：目前的圖片被切成 6 條等寬的直條，換下一張時，這些直條依序（每條間隔約 0.06 秒）一條往上、一條往下交錯滑出畫面，露出底下的下一張圖，下一張圖同時從 1.15 倍慢慢縮回原尺寸。（實作：每條直條是 overflow:hidden 的容器，裡面放同一張圖並往左位移「條寬 × 索引」使拼起來是完整一張；GSAP 對所有直條 yPercent ±110、stagger 0.06、power3.in）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx269">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「切片轉場」.

### JavaScript — `FX[269]` from `site/fx.js`

```js
269(s,x,card){const N=6;const w=el('div','md-sl');const mk=p=>{const l=el('div','md-sll');for(let i=0;i<N;i++){const sl=el('div','md-slc');sl.innerHTML=mdImg(p);sl.style.setProperty('--i',i);sl.style.setProperty('--n',N);l.append(sl)}return l};let p=0;let top=mk(0);w.append(top);s.append(w);let busy=false;
  const next=()=>{if(busy)return;busy=true;p=(p+1)%4;const nw=mk(p);w.prepend(nw);gsap.to(top.children,{yPercent:i=>i%2?110:-110,duration:.7,ease:'power3.in',stagger:.06,onComplete:()=>{top.remove();top=nw;busy=false}});gsap.from(nw.children,{scale:1.15,duration:1.2,ease:'power2.out'})};
  w.onclick=next;card._timers.push(setInterval(next,2600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx269` rules from `site/fx.css`

_No dedicated `.fx269` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #269
