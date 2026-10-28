# 058 · 圓環隧道 — Ring Text Tunnel

一圈圈文字撲面而來

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 轉場切換、背景裝飾
- 風格／關鍵字 Style: 3D 空間旋轉
- 標籤 Tag: 開場・科幻
- 範例文字 Example text: 「TUNNEL・」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「圓環隧道（Ring Text Tunnel）」動態效果：多圈由文字組成的圓環，從中心極小處一圈圈放大朝觀者撲來並淡出，每圈本身也在旋轉、相鄰方向相反。約 4.2 秒一圈。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx58">`, preview text 「TUNNEL・」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「圓環隧道」.

### JavaScript — `FX[58]` from `site/fx.js`

```js
58(s,x){for(let i=0;i<6;i++){const l=el('div','tl');l.append(ringOf(rep(x,Math.max(1,Math.round(16/chars(x).length))),9,2.4,i%2?'cw':'ccw'));l.querySelector('.ring2').style.position='static';l.style.animationDelay=(-i*4.2/6)+'s';s.append(l)}}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx58` rules from `site/fx.css`

```css
.fx55 .tl,.fx58 .tl{position:absolute;left:50%;top:50%;width:0;height:0;display:grid;place-items:center;animation:tun 3.6s linear infinite}
.fx58 .tl{animation-duration:4.2s}
.fx58 .tl:nth-child(even) .ring2 span{color:var(--a)}
@keyframes tun{0%{transform:scale(.04);opacity:0}25%{opacity:1}100%{transform:scale(9);opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #58
