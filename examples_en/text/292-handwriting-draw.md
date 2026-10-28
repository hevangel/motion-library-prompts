# 292 · Handwriting Draw — 手寫描繪

The strokes of the text are drawn one stroke at a time as if written with a pen, then fill in once finished

- Component: Text (`text`)
- Timing: Entrance, Loop · Idle
- Tech: GSAP
- Uses: Headline · Hero, Logo · Brand
- Style / keywords: Handwriting Signature Stroke Drawing Writing Handwriting Signature Stroke Draw Text SVG Text Heading Animated Text
- Tag: stroke-dashoffset
- Example text: "Thank you" (stage background: dark)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Handwriting Draw (手寫描繪)" motion effect: A piece of text (for example a signature or "Thank you") presented in a handwritten-style font: at first you see only blank space, then the outline strokes of the text are drawn along the letterforms one stroke at a time (about 2.4 seconds), as if someone is writing with a pen; after the strokes are drawn, the inside of the letters fades in to fill them. (SVG: set stroke and fill on the <text>; use a stroke-dasharray equal to or greater than the total path length, and tween stroke-dashoffset from the total length to 0; after drawing, fill-opacity 0 → 1. For greater precision, convert the text to a path and use DrawSVG)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx292">`, preview text "Thank you". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Handwriting Draw".

### JavaScript — `FX[292]` from `site/fx.js`

```js
292(s,x){const w=el('div','tx-hw');const fs=Math.min(30,130/chars(x).length);w.innerHTML=`<svg viewBox="0 0 200 70"><text x="100" y="50" text-anchor="middle" style="font-size:${fs*1.9}px"></text></svg>`;w.querySelector('text').textContent=x;s.append(w);
  const tx=w.querySelector('text');const L=600;gsap.timeline({repeat:-1,repeatDelay:.6}).set(tx,{strokeDasharray:L,strokeDashoffset:L,fillOpacity:0}).to(tx,{strokeDashoffset:0,duration:2.4,ease:'power1.inOut'}).to(tx,{fillOpacity:1,duration:.6},'-=.4').to(tx,{opacity:0,duration:.4},'+=1.4').set(tx,{opacity:1})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx292` rules from `site/fx.css`

_No dedicated `.fx292` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #292
