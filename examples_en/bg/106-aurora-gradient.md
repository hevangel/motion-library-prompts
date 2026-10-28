# 106 · Aurora Gradient — 流動光暈漸層

Several blurred glows drift and blend slowly, flowing like an aurora

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Background Decoration, Headline · Hero
- Style / keywords: Background Aurora Gradient Glow Aurora Mesh Gradient Blob Glow Hero Background
- Tag: CSS blur
- Example text: "Aurora" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Aurora Gradient (流動光暈漸層)" motion effect: In a Hero section background, place 3–4 large circular glows that overlap and blend into each other after heavy blurring, each slowly drifting, scaling up and down and swaying back and forth at a different speed (about 9–16 seconds), forming a gradient that keeps flowing like an aurora; the foreground title stays clear and readable. (CSS: each glow is a large circle + filter:blur + mix-blend-mode:screen, each set to a different animation-duration and a negative animation-delay, with animation-direction:alternate)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx106">`, preview text "Aurora". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Aurora Gradient".

### JavaScript — `FX[106]` from `site/fx.js`

```js
106(s,x){const a=el('div','aur');for(let i=0;i<4;i++)a.append(el('i'));s.append(a,T(x,Math.min(14,60/chars(x).length)))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx106` rules from `site/fx.css`

```css
.fx106 .t{color:#fff;mix-blend-mode:overlay;z-index:1}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #106
