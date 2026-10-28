# 140 · 打勾完成 — Success Checkmark

先畫一個圓，再打勾並輕彈，最後浮出成功訊息

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、數字資訊
- 風格／關鍵字 Style: 成功 完成 打勾 勾選 確認 送出 付款 狀態 Success Check Done Confirm Tick
- 標籤 Tag: DrawSVG
- 範例文字 Example text: 「付款成功」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「打勾完成（Success Checkmark）」動態效果：送出或付款完成時的成功狀態：先描出一個圓（約 0.8 秒），接著在圓內快速劃出一個打勾（約 0.45 秒），打勾完成的瞬間整個圖示輕輕彈大 8% 再回來，同時下方的「付款成功」文字從下方 8px 淡入。乾淨、明確、讓人安心。（GSAP：DrawSVGPlugin 依序描繪 circle 與勾的 path；圖示 scale 1→1.08 yoyo；文字 fromTo y:8 / opacity:0）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx140">`, preview text 「付款成功」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「打勾完成」.

### JavaScript — `FX[140]` from `site/fx.js`

```js
140(s,x){const w=el('div','okw');w.innerHTML='<svg viewBox="0 0 52 52"><circle class="oc" cx="26" cy="26" r="23"/><path class="ok" d="M15 27l7 7 15-16"/></svg><b></b>';w.querySelector('b').textContent=x;s.append(w);const sv=w.querySelector('svg');
  gsap.timeline({repeat:-1,repeatDelay:.4}).set(w,{opacity:1},0).fromTo(w.querySelector('.oc'),{drawSVG:'0%'},{drawSVG:'100%',duration:.8,ease:'power2.inOut'}).fromTo(w.querySelector('.ok'),{drawSVG:'0%'},{drawSVG:'100%',duration:.45,ease:'power2.out'})
    .fromTo(sv,{scale:1},{scale:1.08,duration:.18,yoyo:true,repeat:1,ease:'power2.out'},'<.3').fromTo(w.querySelector('b'),{opacity:0,y:8},{opacity:1,y:0,duration:.5,ease:'power2.out'},'<').to(w,{opacity:0,duration:.5},'+=1.6')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx140` rules from `site/fx.css`

_No dedicated `.fx140` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #140
