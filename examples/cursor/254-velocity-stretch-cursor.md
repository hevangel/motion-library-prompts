# 254 · 速度拉伸游標 — Velocity Stretch Cursor

圓形游標依移動速度沿著方向拉長，停下來時恢復圓形

- 元件 Component: 游標 (`cursor`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、標題・Hero
- 風格／關鍵字 Style: 速度 拉伸 拉長 彈性 方向 Velocity Stretch Squash Cursor Elastic 游標 滑鼠
- 標籤 Tag: JS rAF
- 範例文字 Example text: 「Stretch」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「速度拉伸游標（Velocity Stretch Cursor）」動態效果：一顆圓形游標以平滑延遲跟隨滑鼠，每幀計算移動速度：移動越快，圓形越沿著移動方向被拉長、垂直方向變扁，像有彈性的果凍；滑鼠停下時慢慢恢復成正圓。（JS requestAnimationFrame：位置 lerp 追上目標；速度 = 這幀位移長度，角度 = atan2(dy,dx)；transform = translate → rotate(角度) → scale(1 + 速度係數, 1 − 速度係數 × 0.45)，速度係數本身也 lerp 避免抖動）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx254">`, preview text 「Stretch」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「速度拉伸游標」.

### JavaScript — `FX[254]` from `site/fx.js`

```js
254(s,x,card){const l=el('div','abs gl cr-vs');l.append(T(x,Math.min(13,56/chars(x).length)));const c=el('i','cr-vc');l.append(c);s.append(l);let px0=0,py0=0,tx=0,ty=0,cx=0,cy=0,sc=0,ang=0;
  vpointer(l,card,(px,py)=>{tx=px;ty=py});const prev=ticks.get(card);
  ticks.set(card,t=>{prev&&prev(t);const nx=cx+(tx-cx)*.22,ny=cy+(ty-cy)*.22,vx=nx-cx,vy=ny-cy,v=Math.hypot(vx,vy);cx=nx;cy=ny;sc+=(Math.min(v/14,1)-sc)*.25;if(v>.4)ang=Math.atan2(vy,vx)*180/Math.PI;
    c.style.transform=`translate(${cx}px,${cy}px) translate(-50%,-50%) rotate(${ang}deg) scale(${1+sc*1.3},${1-sc*.45})`})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx254` rules from `site/fx.css`

_No dedicated `.fx254` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #254
