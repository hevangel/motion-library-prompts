# 071 · Text Mask Pattern — 圖案遮罩

Text becomes a window, stripes flow through inside

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Headline · Hero
- Style / keywords: Textured Fill
- Tag: Playful·Festival
- Example text: "Festival" (stage background: cream)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Text Mask Pattern (圖案遮罩)" motion effect: The text is like a window, filled inside with diagonal stripes alternating in two colors, the stripes continuously flowing sideways. Bold typeface, flowing through one stripe cycle in about 1 second, with a playful festival feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx71">`, preview text "Festival". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Text Mask Pattern".

### JavaScript — `FX[71]` from `site/fx.js`

```js
71(s,x){s.append(T(x,22))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx71` rules from `site/fx.css`

```css
.fx71 .t{background:repeating-linear-gradient(45deg,var(--a) 0 1.2cqw,#222 1.2cqw 2.4cqw);background-size:3.394cqw 3.394cqw;-webkit-background-clip:text;background-clip:text;color:transparent;animation:mp 1s linear infinite}
@keyframes mp{to{background-position:3.394cqw 0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #71
