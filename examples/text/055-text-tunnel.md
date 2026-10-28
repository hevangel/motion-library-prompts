# 055 · 文字隧道 — Text Tunnel

從文字中間穿過去

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 轉場切換、標題・Hero
- 風格／關鍵字 Style: 3D 空間旋轉
- 標籤 Tag: 開場・科幻
- 範例文字 Example text: 「穿越」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「文字隧道（Text Tunnel）」動態效果：同一個詞的多層複本從中心極小處持續放大，越來越大直到衝出畫面並淡出，一層接一層，像穿過文字隧道，相鄰層用兩種色調交錯。約 3.6 秒一層。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx55">`, preview text 「穿越」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「文字隧道」.

### JavaScript — `FX[55]` from `site/fx.js`

```js
55(s,x){for(let i=0;i<7;i++){const l=el('div','tl');l.innerHTML=`<span>${x}</span>`;l.style.animationDelay=(-i*3.6/7)+'s';s.append(l)}}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx55` rules from `site/fx.css`

```css
.fx55 .tl,.fx58 .tl{position:absolute;left:50%;top:50%;width:0;height:0;display:grid;place-items:center;animation:tun 3.6s linear infinite}
.fx55 .tl span{font-weight:900;font-size:11cqw;white-space:nowrap;color:#fff}
.fx55 .tl:nth-child(even) span{color:var(--a)}
@keyframes tun{0%{transform:scale(.04);opacity:0}25%{opacity:1}100%{transform:scale(9);opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #55
