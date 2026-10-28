# 146 · 按鈕載入成功 — Loading Button

按下後按鈕縮成圓形轉圈，完成時打勾再恢復

- 元件 Component: 按鈕 (`button`)
- 時機 Timing: 懸停・點擊、切換
- 技術 Tech: GSAP
- 情境 Uses: App 介面、介面互動
- 風格／關鍵字 Style: 按鈕 載入 送出 轉圈 成功 打勾 狀態 Loading Button Submit Spinner Success Morph App 手機 行動裝置 微互動 Mobile App Micro-interaction
- 標籤 Tag: Loading state
- 範例文字 Example text: 「送出訂單」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「按鈕載入成功（Loading Button）」動態效果：點擊「送出」按鈕時，按鈕先輕輕按下（縮到 95%），文字淡出，按鈕寬度收縮成一個圓形（約 0.4 秒），圓形中出現旋轉的載入圈；完成後載入圈消失，換成一個被畫出來的打勾，按鈕輕彈一下；停留約 0.8 秒後再展開回原本寬度、文字淡入。防止重複點擊，也讓使用者清楚知道狀態。（GSAP：timeline 依序 tween width、spinner rotation、DrawSVG 打勾；寬度用固定單位做 fromTo）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx146">`, preview text 「送出訂單」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「按鈕載入成功」.

### JavaScript — `FX[146]` from `site/fx.js`

```js
146(s,x){const b=el('button','lb2');b.innerHTML='<span class="t2"></span><i class="spn"></i><svg class="ck" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7"/></svg>';b.querySelector('.t2').textContent=x;s.append(b);const q=c=>b.querySelector(c);
  gsap.timeline({repeat:-1,repeatDelay:.8}).set(b,{width:'30cqw'},0).set(q('.spn'),{opacity:0},0).set(q('.ck path'),{drawSVG:'0%'},0)
    .to(b,{scale:.95,duration:.1},.3).to(b,{scale:1,duration:.15}).to(q('.t2'),{opacity:0,duration:.15},'<').fromTo(b,{width:'30cqw'},{width:'8cqw',duration:.4,ease:'power3.inOut'},'<')
    .to(q('.spn'),{opacity:1,duration:.15}).fromTo(q('.spn'),{rotation:0},{rotation:720,duration:1.2,ease:'none'},'<').to(q('.spn'),{opacity:0,duration:.15})
    .to(q('.ck path'),{drawSVG:'100%',duration:.35,ease:'power2.out'}).fromTo(b,{scale:1},{scale:1.08,duration:.15,yoyo:true,repeat:1},'<')
    .to(q('.ck path'),{drawSVG:'100% 100%',duration:.25},'+=.8').fromTo(b,{width:'8cqw'},{width:'30cqw',duration:.4,ease:'power3.inOut'}).to(q('.t2'),{opacity:1,duration:.2})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx146` rules from `site/fx.css`

_No dedicated `.fx146` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #146
