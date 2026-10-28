# 034 · Jitter Settle — 顫抖穩定

Shakes, then gradually settles

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Emphasis
- Style / keywords: Letter-by-Letter Motion
- Tag: Scary · Tense
- Example text: "Trembling" (stage background: acc)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Jitter Settle (顫抖穩定)" motion effect: The text first shakes violently left, right, up and down and rotates; the shaking gradually gets smaller until it finally settles and stops, pauses for a while, then starts shaking again. About 2.4 seconds per cycle, with a startled, tense feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx34">`, preview text "Trembling". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Jitter Settle".

### JavaScript — `FX[34]` from `site/fx.js`

```js
34(s,x){s.append(split(x))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx34` rules from `site/fx.css`

```css
.fx34 .c{animation:jit 2.4s calc(var(--i)*.09s) infinite linear}
.fx34 .c:nth-child(even){color:#7a5500}
@keyframes jit{0%{transform:translate(9%,-7%) rotate(7deg)}4%{transform:translate(-9%,6%) rotate(-7deg)}8%{transform:translate(8%,5%) rotate(6deg)}12%{transform:translate(-7%,-6%) rotate(-5deg)}16%{transform:translate(6%,4%) rotate(4deg)}21%{transform:translate(-4%,-3%) rotate(-3deg)}26%{transform:translate(3%,2%) rotate(2deg)}32%{transform:translate(-2%,-1%) rotate(-1deg)}38%{transform:translate(1%,1%) rotate(.5deg)}44%,86%{transform:none}100%{transform:translate(9%,-7%) rotate(7deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #34
