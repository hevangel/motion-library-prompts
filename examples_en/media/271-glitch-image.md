# 271 · Glitch Image — 故障錯位圖片

On hover, an image splits into two color layers offset left and right, flickering in segments like a bad signal

- Component: Images · Media (`media`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, Emphasis
- Style / keywords: Glitch glitch Offset Color Version Signal Cyberpunk Glitch Image RGB Split Distortion Cyberpunk Image Media
- Tag: CSS clip-path
- Example text: "SIGNAL" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Glitch Image (故障錯位圖片)" motion effect: When the mouse hovers over an image it triggers a glitch effect: the image overlays two copies in different color versions, stacked on the original with a “screen” blend mode, each offset left and right by a few percent, using clip-path to show only random horizontal bands, flickering and jumping rapidly; the original image itself also jitters slightly left and right; the title text in the middle shows two color edges offset left and right; when moving away it returns to normal. (CSS: the two copies use filter: sepia + saturate + hue-rotate to make different color versions, mix-blend-mode: screen; keyframes combined with steps() change transform and clip-path: inset(...))
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx271">`, preview text "SIGNAL". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Glitch Image".

### JavaScript — `FX[271]` from `site/fx.js`

```js
271(s,x,card){const f=el('div','md-gc');f.innerHTML=mdImg(2,'o')+mdImg(2,'c1')+mdImg(2,'c2')+'<b class="md-gx"></b>';f.querySelector('.md-gx').textContent=x;s.append(f);autoHover(f,[f],card,1700)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx271` rules from `site/fx.css`

_No dedicated `.fx271` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #271
