# 114 · 骨架載入 — Skeleton Shimmer

內容載入前顯示骨架，光澤掃過後淡入真正內容

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 循環待機、進場
- 技術 Tech: CSS
- 情境 Uses: 介面互動、數字資訊
- 風格／關鍵字 Style: 骨架 載入 讀取 佔位 Skeleton Loading Shimmer Placeholder Loader
- 標籤 Tag: Skeleton
- 範例文字 Example text: 「一起來設計動態吧」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「骨架載入（Skeleton Shimmer）」動態效果：資料載入中時，卡片先顯示低對比的骨架：圓形頭像、兩條長短不一的文字條、一塊大圖區，骨架上有一道柔和的亮光由左往右持續掃過；載入完成後骨架淡出，真正的頭像、標題、時間與圖片淡入並微微往上滑到定位。（CSS：骨架元素用 linear-gradient 亮帶 + background-size:300% 並以 keyframes 移動 background-position；載入完成時切換 class，骨架 opacity 0、內容 opacity 1 + translateY 過場）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx114">`, preview text 「一起來設計動態吧」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「骨架載入」.

### JavaScript — `FX[114]` from `site/fx.js`

```js
114(s,x,card){const c=el('div','skc');c.innerHTML='<div class="sk"><i class="av"></i><i class="l1"></i><i class="l2"></i><i class="im"></i></div><div class="rl"><i class="av"></i><b></b><span>剛剛 · 3 分鐘閱讀</span><i class="im"></i></div>';c.querySelector('.rl b').textContent=x;s.append(c);card._timers.push(setInterval(()=>c.classList.toggle('ld'),2200))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx114` rules from `site/fx.css`

_No dedicated `.fx114` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #114
