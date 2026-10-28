# 185 · Tumble — 翻滾

Each character makes its entrance tumbling and rotating from a shrunken state

- Component: Text (`text`)
- Timing: Entrance
- Tech: CSS
- Uses: Headline · Hero, Emphasis
- Style / keywords: tumble rotate entrance character-by-character playful Tumble Spin Rotate In Canva style Canva Tumble tumble presentation social post animation
- Tag: CSS keyframes
- Example text: "Tumbling In" (stage background: acc)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Tumble (翻滾)" motion effect: Each character enters tumbling: starting from about 0.2x size and rotated 200 degrees counterclockwise, it straightens while scaling up to make its entrance, finally overshooting slightly (rotating 10 degrees too far, scaling to 1.08) before settling upright, with a sequential delay of about 0.08 seconds between characters — playful and full of energy. (CSS: each character is inline-block, keyframes rotate(-200deg) scale(.2) to rotate(10deg) scale(1.08) to none, animation-delay increasing by index)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx185">`, preview text "Tumbling In". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Tumble".

### JavaScript — `FX[185]` from `site/fx.js`

```js
185(s,x){s.append(split(x.replace(/ /g,' '),Math.min(14,64/chars(x).length)))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx185` rules from `site/fx.css`

```css
.fx185 .c{animation:tumble 3.6s cubic-bezier(.2,.8,.3,1.1) infinite;animation-delay:calc(var(--i) * .08s)}
@keyframes tumble{0%{transform:rotate(-200deg) scale(.2);opacity:0}24%{transform:rotate(10deg) scale(1.08);opacity:1}32%,80%{transform:none;opacity:1}92%,100%{transform:none;opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #185
