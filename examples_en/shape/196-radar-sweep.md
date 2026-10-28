# 196 · Radar Sweep — 雷達掃描

A scanning fan sector keeps circling, and dots light up where it sweeps past

- Component: Shapes · SVG (`shape`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Numbers & Data, Background Decoration
- Style / keywords: radar scan search positioning tech map Radar Scan Sweep Ping Search Tech SVG graphic
- Tag: SVG radar
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Radar Sweep (雷達掃描)" motion effect: A radar screen: several concentric circles and crosshairs, and a translucent fan-shaped scanning sector rotates continuously clockwise (about 3 seconds per revolution). Where the scan line passes, dots light up and briefly grow larger, then gradually fade out, lighting up again when the next revolution sweeps past. Suitable for searching, positioning, and tech-style dashboards. (SVG + CSS: the fan-shaped path is placed in a g and rotated around the center; each dot's animation-delay is calculated from its angle as the time the scan line arrives)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx196">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Radar Sweep".

### JavaScript — `FX[196]` from `site/fx.js`

```js
196(s){const B=[[40,.55],[115,.75],[200,.4],[290,.8],[335,.3]];s.insertAdjacentHTML('beforeend',`<svg class="rdr" viewBox="-50 -50 100 100"><circle r="44"/><circle r="30"/><circle r="16"/><path d="M-44,0H44M0,-44V44"/><g class="sw"><path d="M0,0 L0,-44 A44,44 0 0,1 31.1,-31.1 Z"/><path class="ed" d="M0,0 L31.1,-31.1"/><animateTransform attributeName="transform" type="rotate" from="0 0 0" to="360 0 0" dur="3s" repeatCount="indefinite"/></g>${B.map(([a,r])=>{const rad=(a-90)*Math.PI/180;return `<circle class="bp" cx="${(Math.cos(rad)*r*44).toFixed(1)}" cy="${(Math.sin(rad)*r*44).toFixed(1)}" r="2.2" style="animation-delay:${(((a-45+360)%360)/360*3).toFixed(2)}s"/>`}).join('')}</svg>`)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx196` rules from `site/fx.css`

_No dedicated `.fx196` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #196
