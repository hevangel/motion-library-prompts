# 187 · Scrapbook — 剪貼簿

Photos, tape, stickers and a title are pasted on one by one at slight angles

- Component: Cards · Groups (`card`)
- Timing: Entrance
- Tech: CSS
- Uses: Headline · Hero, Emphasis
- Style / keywords: scrapbook collage journal photo sticker tape Scrapbook Collage Sticker Photo Journal Canva style Canva Scrapbook scrapbook presentation social post animation
- Tag: CSS keyframes
- Example text: "My Summer" (stage background: cream)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Scrapbook (剪貼簿)" motion effect: A layout like a journal collage: two Polaroid photos, a strip of washi tape, a round sticker and a hand-lettered-style title are 'pasted' on one by one in sequence — each element drops quickly from a slightly larger, somewhat higher position, with its own small tilt angle, and bounces slightly when it lands (about 0.5 seconds, at intervals of about 0.28 seconds), then after a pause they all fade out together. Warm, handmade feel. (CSS: each element sets its own rotation angle and delay with CSS variables, keyframes translateY(-30%) scale(1.25) to scale(.95) to 1, keeping rotate(var(--r)))
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx187">`, preview text "My Summer". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Scrapbook".

### JavaScript — `FX[187]` from `site/fx.js`

```js
187(s,x){const w=el('div','scb');w.innerHTML=`<div class="pc ph1" style="--r:-7deg;--d:0s">${scene('#9fd3ff','#ffe1b0','#4f7a6a','#264a3f','#fff6d8')}</div><div class="pc ph2" style="--r:6deg;--d:.28s">${scene('#ffd9c2','#c9b6ff','#7b6ca8','#3f3566','#fff6e6')}</div><i class="pc tape" style="--r:-14deg;--d:.56s"></i><i class="pc stk" style="--r:8deg;--d:.76s">★</i><b class="pc ttl" style="--r:-3deg;--d:.96s"></b>`;w.querySelector('.ttl').textContent=x;s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx187` rules from `site/fx.css`

_No dedicated `.fx187` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #187
