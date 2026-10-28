# 118 · 通知堆疊 — Toast Stack

通知從右下角依序彈入堆疊，幾秒後滑出消失

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 進場、退場
- 技術 Tech: CSS
- 情境 Uses: 介面互動、數字資訊
- 風格／關鍵字 Style: 通知 提示 訊息 吐司 彈出 Toast Notification Snackbar Alert Stack
- 標籤 Tag: Toast
- 範例文字 Example text: 「已儲存變更」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「通知堆疊（Toast Stack）」動態效果：操作完成時，畫面右下角彈出一則通知（左邊打勾圓形圖示、中間訊息、右邊「剛剛」時間），從下方帶一點縮放彈性地進場；新通知會疊在下面，舊的往上推；最多同時顯示 3 則，每則約 3.4 秒後往右滑出淡掉，其餘通知平滑補位。（CSS + JS：通知外層用 display:grid + grid-template-rows 1fr→0fr 做高度收合，讓補位平滑；進場用 keyframes translateY + scale；離場加 .out class 後再移除元素）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx118">`, preview text 「已儲存變更」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「通知堆疊」.

### JavaScript — `FX[118]` from `site/fx.js`

```js
118(s,x,card){const box=el('div','tst');s.append(box);const msgs=[x,'上傳完成','有 3 則新留言','已加入收藏'];let k=0;
  const push=()=>{const t=el('div','ti');t.innerHTML='<div><div class="tb"><i>✓</i><b></b><small>剛剛</small></div></div>';t.querySelector('b').textContent=msgs[k++%msgs.length];box.append(t);
    const live=[...box.querySelectorAll('.ti:not(.out)')];if(live.length>3)live[0].classList.add('out');setTimeout(()=>t.classList.add('out'),3400);setTimeout(()=>t.remove(),4000)};
  push();card._timers.push(setInterval(push,1100))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx118` rules from `site/fx.css`

_No dedicated `.fx118` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #118
