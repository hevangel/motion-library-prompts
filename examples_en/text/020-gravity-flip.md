# 020 · Gravity Flip — 重力反轉

Gravity reverses and it bounces upward

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Transitions
- Style / keywords: Letter-by-Letter Motion
- Tag: Surprise · SF
- Example text: "Gravity Flip" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Gravity Flip (重力反轉)" motion effect: Each character first accelerates as it “falls” upward to the top and flips upside down, pauses, then drops back into place and flips upright, with a small bounce on landing, the characters staggered in sequence from each other. About 3 seconds per cycle.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx20">`, preview text "Gravity Flip". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Gravity Flip".

### JavaScript — `FX[20]` from `site/fx.js`

```js
20(s,x){s.append(split(x))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx20` rules from `site/fx.css`

```css
.fx20 .c{animation:grv 3s calc(var(--i)*.09s) infinite}
.fx20 .c:nth-child(even){color:var(--a)}
@keyframes grv{0%,10%{transform:none;animation-timing-function:cubic-bezier(.5,0,1,.5)}33%{transform:translateY(-80%) rotate(180deg);animation-timing-function:ease-out}40%{transform:translateY(-65%) rotate(180deg);animation-timing-function:ease-in}46%,58%{transform:translateY(-80%) rotate(180deg);animation-timing-function:cubic-bezier(.5,0,1,.5)}80%{transform:translateY(0) rotate(360deg);animation-timing-function:ease-out}87%{transform:translateY(-14%) rotate(360deg)}93%,100%{transform:rotate(360deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #20
