# 015 · Gradient Flow — 漸層流動

A gradient flows through the text

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Headline · Hero, Logo · Brand
- Style / keywords: Textured Fill
- Tag: Title · Trendy
- Example text: "Flowing Colors" (stage background: cream)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Gradient Flow (漸層流動)" motion effect: The text is filled with a multi-color gradient that keeps flowing from left to right inside the letters. Large bold type, about 3 seconds per flow cycle, with a fashionable headline feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx15">`, preview text "Flowing Colors". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Gradient Flow".

### JavaScript — `FX[15]` from `site/fx.js`

```js
15(s,x){s.append(T(x))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx15` rules from `site/fx.css`

```css
.fx15 .t{background:linear-gradient(90deg,#c22,#ff6b4a,#ffcf3c,#ff6b4a,#7a1a1a,#c22);background-size:300% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:gf 3s linear infinite}
@keyframes gf{to{background-position:300% 0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #15
