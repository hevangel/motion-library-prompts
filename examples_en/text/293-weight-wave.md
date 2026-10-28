# 293 · Weight Wave — 字重波浪

Each character's weight changes in turn, like a wave sweeping from left to right

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Headline · Hero, Emphasis
- Style / keywords: Font Weight Thickness Variable Font Wave Breathing Variable Font Weight Wave Breathing Text Heading Animated Text
- Tag: variable font
- Example text: "WEIGHT" (stage background: dark)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Weight Wave (字重波浪)" motion effect: Each character of a heading alternates in font weight between the thinnest and the boldest, with adjacent characters delayed in sequence, so it looks like a wave of thickness continuously sweeping from left to right; at its boldest, a character also turns into the accent color. (CSS: use a font that supports variable font weight, split each character into its own element, share one keyframes that varies font-weight between 100 ↔ 900, with animation-delay increasing by index)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx293">`, preview text "WEIGHT". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Weight Wave".

### JavaScript — `FX[293]` from `site/fx.js`

```js
293(s,x){const t=T(x,Math.min(15,64/chars(x).length));t.classList.add('tx-ww');s.append(t);const sp=SplitText.create(t,{type:'chars'});sp.chars.forEach((c,i)=>c.style.animationDelay=(i*.09-3)+'s')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx293` rules from `site/fx.css`

_No dedicated `.fx293` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #293
