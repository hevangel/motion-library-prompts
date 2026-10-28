# 224 · 散景光點 — Bokeh Lights

大小不一的柔焦光點緩緩上飄、淡入淡出

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 背景裝飾、標題・Hero
- 風格／關鍵字 Style: 散景 光點 柔焦 泡泡 漂浮 上飄 夢幻 Bokeh Lights Bubbles Floating Blur 背景 氛圍
- 標籤 Tag: CSS blur
- 範例文字 Example text: 「Bokeh」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「散景光點（Bokeh Lights）」動態效果：背景飄著十多個大小不一、帶柔焦模糊的圓形光點，每個從下方以不同速度（約 7–14 秒）緩緩上飄，途中輕微左右偏移，出現時淡入、接近頂端時淡出，透明度各不相同，營造夢幻、溫暖的氛圍；標題在中間保持清楚。（CSS：每顆光點用 CSS 變數設定大小、水平位置、時長、負的 animation-delay 與偏移量，filter:blur，keyframes 控制 translate 與 opacity）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx224">`, preview text 「Bokeh」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「散景光點」.

### JavaScript — `FX[224]` from `site/fx.js`

```js
224(s,x){const w=el('div','abs bga-bk');for(let i=0;i<16;i++){const b=el('i');const z=rnd(5,16);b.style.cssText=`--z:${z}cqw;left:${rnd(-5,95)}%;--d:${rnd(7,14).toFixed(1)}s;--dl:${-rnd(0,14).toFixed(1)}s;--o:${rnd(.25,.7).toFixed(2)};--dx:${rnd(-8,8).toFixed(1)}cqw;background:${i%3?'var(--a)':GC[i%5]}`;w.append(b)}s.append(w,T(x,Math.min(12,56/chars(x).length)))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx224` rules from `site/fx.css`

```css
.fx222 .t,.fx224 .t,.fx227 .t,.fx231 .t{color:#fff;z-index:1;text-shadow:0 .4cqw 2cqw #0006}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #224
