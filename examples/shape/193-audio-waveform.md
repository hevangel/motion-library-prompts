# 193 · 音訊波形 — Audio Waveform

一排長條像音訊波形一樣隨機跳動

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 循環待機
- 技術 Tech: GSAP
- 情境 Uses: 數字資訊、介面互動、App 介面
- 風格／關鍵字 Style: 音訊 波形 音樂 播放器 等化器 Podcast Audio Waveform Equalizer Visualizer SVG 圖形
- 標籤 Tag: SVG bars
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「音訊波形（Audio Waveform）」動態效果：音訊播放器中的波形：一排細長圓角長條以中線為基準上下伸縮，每根長條高度隨機、速度略有不同且持續變化，像正在播放的聲音；左側圓形播放按鈕、右側顯示時間。（GSAP：對所有 rect tween scaleY:"random(.12,1)"、duration:"random(.22,.5)"，repeat:-1、yoyo:true、repeatRefresh:true 讓每次重複都重新取亂數，transformOrigin 置中）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx193">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「音訊波形」.

### JavaScript — `FX[193]` from `site/fx.js`

```js
193(s){const n=34,w=el('div','wvf');w.innerHTML='<i class="pl">▶</i><svg viewBox="0 0 '+(n*6)+' 40" preserveAspectRatio="none">'+[...Array(n)].map((_,i)=>`<rect x="${i*6+1}" y="2" width="3.4" height="36" rx="1.7"/>`).join('')+'</svg><small>0:42</small>';s.append(w);
  gsap.to(w.querySelectorAll('rect'),{scaleY:'random(.12,1)',transformOrigin:'50% 50%',duration:'random(.22,.5)',ease:'sine.inOut',repeat:-1,yoyo:true,repeatRefresh:true,stagger:{each:.02,from:'random'}})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx193` rules from `site/fx.css`

_No dedicated `.fx193` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #193
