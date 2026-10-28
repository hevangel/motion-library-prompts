# 073 · Liquid Fill — 液體填滿

Hollow text is slowly filled with liquid

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Emphasis
- Style / keywords: Textured Fill
- Tag: Fresh·MV
- Example text: "Full" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Liquid Fill (液體填滿)" motion effect: At first there is only outlined hollow text; liquid slowly fills the letters from bottom to top; after filling and lingering, it empties and starts over. About 3.4 seconds per cycle, with a fresh MV feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx73">`, preview text "Full". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Liquid Fill".

### JavaScript — `FX[73]` from `site/fx.js`

```js
73(s,x){s.append(T(x,chars(x).length<2?30:undefined))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx73` rules from `site/fx.css`

```css
.fx73 .t{-webkit-text-stroke:.35cqw var(--a);color:transparent;background:linear-gradient(to top,var(--a) var(--lv),transparent calc(var(--lv) + .1%));-webkit-background-clip:text;background-clip:text;animation:lq 3.4s ease-in-out infinite}
@keyframes lq{0%,6%{--lv:0%}70%,90%{--lv:100%}100%{--lv:0%}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #73
