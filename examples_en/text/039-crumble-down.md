# 039 · Crumble Down — 崩落

Text crumbles and falls

- Component: Text (`text`)
- Timing: Exit
- Tech: CSS
- Uses: Transitions
- Style / keywords: Dissipating Exit
- Tag: Ending · Twist
- Example text: "Crumble" (stage background: cream)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Crumble Down (崩落)" motion effect: Each character first tilts slightly, then falls downward in sequence as if crumbling, accelerating under gravity, rotating and fading out, then drops back from above into its original place to reassemble. About 3.4 seconds per cycle, with an ending feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx39">`, preview text "Crumble". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Crumble Down".

### JavaScript — `FX[39]` from `site/fx.js`

```js
39(s,x){const t=split(x);t.querySelectorAll('.c').forEach(c=>{c.style.setProperty('--r0',rnd(-12,12)+'deg');c.style.setProperty('--r',rnd(-90,90)+'deg')});s.append(t)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx39` rules from `site/fx.css`

```css
.fx39 .c{animation:crm 3.4s calc(var(--i)*.16s) infinite}
.fx39 .c:nth-child(even){color:#c08a00}
@keyframes crm{0%,22%{transform:none;opacity:1}27%{transform:rotate(var(--r0))}30%{transform:rotate(var(--r0));animation-timing-function:cubic-bezier(.5,0,1,.5)}62%{transform:translateY(170%) rotate(var(--r));opacity:0}80%{transform:translateY(-50%);opacity:0;animation-timing-function:ease-out}92%,100%{transform:none;opacity:1}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #39
