# 023 · Weight Grow — 字重變粗

Thin text gradually grows bolder

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Emphasis
- Style / keywords: Textured Fill
- Tag: Emphasis · Change
- Example text: "Bolder" (stage background: cream)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Weight Grow (字重變粗)" motion effect: The text slowly changes from an extremely thin font weight to the heaviest font weight, pauses, then returns to thin again (a variable-weight font is required). About 3 seconds per cycle, emphasizing the sense of transformation.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx23">`, preview text "Bolder". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Weight Grow".

### JavaScript — `FX[23]` from `site/fx.js`

```js
23(s,x){s.append(T(x))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx23` rules from `site/fx.css`

```css
.fx23 .t{font-weight:100;animation:wg 3s ease-in-out infinite}
@keyframes wg{0%,12%{font-weight:100}55%,82%{font-weight:900}100%{font-weight:100}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #23
