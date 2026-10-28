# 050 · Diagonal Text Bands — 斜線帶

Diagonal bands, text running in reverse

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Background Decoration, Transitions
- Style / keywords: Flowing Background
- Tag: Transition·Playful
- Example text: "Before Dawn" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Diagonal Text Bands (斜線帶)" motion effect: Two diagonal text bands cross through the frame, distinguished by different background colors, the repeated text on the bands continuously sliding in opposite directions, the bands casting shadows. About 7–9 seconds per cycle, with a playful transition feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx50">`, preview text "Before Dawn". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Diagonal Text Bands".

### JavaScript — `FX[50]` from `site/fx.js`

```js
50(s,x){const a=mqRow(rep(x+'・',8),7,9,false,'background:var(--a);color:#111');a.className+=' band';a.style.top='22%';a.style.transform='rotate(-9deg)';const b=mqRow(rep(x+'・',8),7,7,true,'background:#fff;color:#111');b.className+=' band';b.style.top='56%';b.style.transform='rotate(6deg)';s.append(a,b)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx50` rules from `site/fx.css`

_No dedicated `.fx50` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #50
