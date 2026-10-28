# 056 · 文字走廊 — Text Corridor

地板牆壁都是字，一路往前

- 元件 Component: 背景・氛圍 (`bg`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 背景裝飾、標題・Hero
- 風格／關鍵字 Style: 3D 空間旋轉
- 標籤 Tag: 沉浸・MV
- 範例文字 Example text: 「前進」（預覽底色：acc）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「文字走廊（Text Corridor）」動態效果：3D 透視的走廊，地板、天花板、左右牆面全部鋪滿重複文字，文字往觀者方向持續流動，中心消失點處有暗色漸層。約 6 秒一輪，沉浸往前感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx56">`, preview text 「前進」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「文字走廊」.

### JavaScript — `FX[56]` from `site/fx.js`

```js
56(s,x){const u=rep(x+'　',14);const rows=Array(28).fill(`<div style="white-space:nowrap;font-weight:900;font-size:6cqw;line-height:1.3">${u}</div>`).join('');
  const P=(tf,w,h,anim)=>`<div style="position:absolute;left:50%;top:50%;width:${w}cqw;height:${h}cqw;margin:${-h/2}cqw 0 0 ${-w/2}cqw;transform:${tf};overflow:hidden;background:var(--a);color:#111"><div style="animation:${anim}">${rows}${rows}</div></div>`;
  s.insertAdjacentHTML('beforeend',`<div style="position:absolute;inset:0;perspective:30cqw;transform-style:preserve-3d">
  ${P('translateY(13cqw) translateZ(-138cqw) rotateX(90deg)',52,300,'mqv 6s linear infinite reverse')}
  ${P('translateY(-13cqw) translateZ(-138cqw) rotateX(-90deg)',52,300,'mqv 6s linear infinite reverse')}
  ${P('translateX(-26cqw) translateZ(-138cqw) rotateY(90deg)',300,26,'mq 6s linear infinite')}
  ${P('translateX(26cqw) translateZ(-138cqw) rotateY(-90deg)',300,26,'mq 6s linear infinite reverse')}
  </div><div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 50%,#111 0 4%,#1116 12%,transparent 30%)"></div>`)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx56` rules from `site/fx.css`

```css
.fx51 svg,.fx56 svg{width:100%;height:100%}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #56
