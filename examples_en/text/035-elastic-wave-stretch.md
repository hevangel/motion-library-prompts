# 035 · Elastic Wave Stretch — 彈性拉伸

Text stretches vertically into a wave

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Headline · Hero
- Style / keywords: Letter-by-Letter Motion
- Tag: Pop · Music
- Example text: "Stretchy Wave" (stage background: cream)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Elastic Wave Stretch (彈性拉伸)" motion effect: With its base at the bottom, each character stretches vertically in sequence to about 1.7x and then shrinks back, while narrowing horizontally at the same time, forming an elastic wave; the last character uses an accent color. About 1.3 seconds per wave, with a pop-music feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx35">`, preview text "Stretchy Wave". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Elastic Wave Stretch".

### JavaScript — `FX[35]` from `site/fx.js`

```js
35(s,x){s.append(split(x))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx35` rules from `site/fx.css`

```css
.fx35 .c{transform-origin:50% 100%;animation:str 1.3s calc(var(--i)*-.16s) ease-in-out infinite}
.fx35 .c:last-child{color:#c08a00}
@keyframes str{0%,100%{transform:scale(1.05,.85)}50%{transform:scale(.85,1.75)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #35
