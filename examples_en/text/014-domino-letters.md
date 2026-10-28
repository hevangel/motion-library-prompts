# 014 · Domino Letters — 骨牌倒下

Text topples like dominoes

- Component: Text (`text`)
- Timing: Exit
- Tech: CSS
- Uses: Emphasis
- Style / keywords: Dissipating Exit
- Tag: Humor · Chain Reaction
- Example text: "Dominoes" (stage background: acc)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Domino Letters (骨牌倒下)" motion effect: Each character pivots on its bottom-right corner and topples to the right in sequence by about 72 degrees, falling in a chain like dominoes, then all stand back up together after a pause. There is a floor line beneath the text. About 3.2 seconds per cycle.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx14">`, preview text "Dominoes". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Domino Letters".

### JavaScript — `FX[14]` from `site/fx.js`

```js
14(s,x){s.append(split(x),el('div','floor'))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx14` rules from `site/fx.css`

```css
.fx14 .c{transform-origin:100% 100%;animation:dom 3.2s calc(var(--i)*.13s) infinite cubic-bezier(.5,0,.8,.6)}
.fx14 .c:nth-child(3n+2){color:#fff6ea}
.fx14 .floor{position:absolute;left:8%;right:8%;bottom:26%;height:2px;background:#0005}
@keyframes dom{0%,8%{transform:none}24%,74%{transform:rotate(72deg)}86%,100%{transform:none}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #14
