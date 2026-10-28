# 191 · Ken Burns — 緩慢推鏡

An image continuously zooms in slowly and pans slightly, like a documentary push-in

- Component: Images · Media (`media`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Headline · Hero, Background Decoration
- Style / keywords: push-in slow zoom pan photo documentary Ken Burns Slow Zoom Pan Photo Canva style Canva Photo Zoom photo zoom presentation social post animation
- Tag: CSS keyframes
- Example text: "Coastline" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Ken Burns (緩慢推鏡)" motion effect: A photo zooms in very slowly inside a fixed frame (over about 9 seconds, to 1.22x) while panning slightly to one side at the same time, then slowly retreats back, cycling back and forth, like a documentary push-in on a still photo, giving a static image a sense of life; the title on the image stays still. (CSS: outer frame overflow:hidden, inner image keyframes scale(1) to scale(1.22) translate(-4%, 2%), ease-in-out, alternate infinite, transform-origin set near the subject)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx191">`, preview text "Coastline". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Ken Burns".

### JavaScript — `FX[191]` from `site/fx.js`

```js
191(s,x){const w=el('div','kbw');w.innerHTML=scene('#ffb36b','#ff6b8b','#8a3f6e','#3b1f45','#fff3d6');const t=T(x,Math.min(6,36/chars(x).length));t.classList.add('kbt');w.append(t);s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx191` rules from `site/fx.css`

_No dedicated `.fx191` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #191
