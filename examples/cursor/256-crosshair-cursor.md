# 256 · 十字準星座標 — Crosshair Cursor

橫豎兩條細線跟著游標，旁邊即時顯示座標數字

- 元件 Component: 游標 (`cursor`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: CSS
- 情境 Uses: 介面互動、數字資訊、標題・Hero
- 風格／關鍵字 Style: 十字 準星 座標 瞄準 科技 藍圖 Crosshair Coordinates Cursor Blueprint Tech 游標 滑鼠
- 標籤 Tag: JS + CSS
- 範例文字 Example text: 「Precision」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「十字準星座標（Crosshair Cursor）」動態效果：帶淡淡格線的背景上，一條橫線與一條直線跨滿整個區塊、交會在游標位置，交點有一個小圓圈；游標右下方有一個小標籤，用等寬字體即時顯示目前的 X、Y 座標數字（換算成 1920 × 1080），靠近邊緣時標籤自動往內收，不會超出畫面。適合科技、設計工具或作品集首頁。（JS：mousemove 時用 transform 移動兩條線與標籤，座標 = 游標位置 / 容器寬高 × 1920、1080，padStart 補零）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx256">`, preview text 「Precision」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「十字準星座標」.

### JavaScript — `FX[256]` from `site/fx.js`

```js
256(s,x,card){const l=el('div','abs cr-xh');l.innerHTML='<i class="h"></i><i class="v"></i><b></b><em></em>';const t=T(x,Math.min(12,52/chars(x).length));l.append(t);s.append(l);const [h,v]=l.querySelectorAll('i'),rd=l.querySelector('b'),dot=l.querySelector('em');
  vpointer(l,card,(px,py)=>{const W=l.offsetWidth,H=l.offsetHeight;h.style.transform=`translateY(${py}px)`;v.style.transform=`translateX(${px}px)`;dot.style.transform=`translate(${px}px,${py}px)`;rd.textContent=`X ${String(Math.round(px/W*1920)).padStart(4,'0')}  Y ${String(Math.round(py/H*1080)).padStart(4,'0')}`;rd.style.transform=`translate(${Math.min(px+10,W-rd.offsetWidth-6)}px,${Math.min(py+10,H-rd.offsetHeight-6)}px)`})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx256` rules from `site/fx.css`

_No dedicated `.fx256` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #256
