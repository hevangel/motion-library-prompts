# 242 · 勾選框打勾 — Animated Checkbox

勾選時方框彈一下、勾勾像用筆畫出來，項目文字加上刪除線

- 元件 Component: 表單・控制項 (`control`)
- 時機 Timing: 切換
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 勾選框 核取方塊 打勾 待辦 清單 todo Checkbox Check Animation Todo List 表單 控制項
- 標籤 Tag: stroke-dashoffset
- 範例文字 Example text: 「買咖啡豆 回覆信件 整理桌面」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「勾選框打勾（Animated Checkbox）」動態效果：一組待辦清單的勾選框：點擊勾選時，方框先縮小再彈大一點（約 0.4 秒），底色填滿；裡面的勾勾從左下到右上像用筆畫出來；右側的項目文字變淡並加上一條刪除線。取消勾選時反向回復。（CSS：隱藏原生 checkbox，自訂方框與 SVG 勾勾；勾勾 path 用 stroke-dasharray 與 stroke-dashoffset 從全長變 0；:checked + 樣式切換，方框用 scale 的 keyframes 彈跳；保留 :focus-visible 外框給鍵盤使用者）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx242">`, preview text 「買咖啡豆 回覆信件 整理桌面」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「勾選框打勾」.

### JavaScript — `FX[242]` from `site/fx.js`

```js
242(s,x,card){const ws=words(x);const w=el('div','fm-ck');ws.slice(0,3).forEach((t,i)=>{const l=el('label');l.innerHTML='<input type="checkbox"><i><svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7"/></svg></i><span></span>';l.querySelector('span').textContent=t;if(i===0)l.querySelector('input').checked=true;w.append(l)});s.append(w);
  const ins=[...w.querySelectorAll('input')];let real=0,k=0;w.addEventListener('pointerdown',()=>real=Date.now());card._timers.push(setInterval(()=>{if(Date.now()-real<5000)return;const i=ins[k++%ins.length];i.checked=!i.checked},1100))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx242` rules from `site/fx.css`

_No dedicated `.fx242` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #242
