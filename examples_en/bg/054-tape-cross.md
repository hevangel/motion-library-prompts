# 054 · Tape Cross — 封鎖膠帶

Taped text crossed into an X

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Emphasis, Background Decoration
- Style / keywords: Flowing Background
- Tag: Warning·Street
- Example text: "No Entry" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Tape Cross (封鎖膠帶)" motion effect: Two caution tapes with thick borders cross into an X shape, the repeated text on the tapes sliding in opposite directions, with shadows. About 6–8 seconds per cycle, with a warning, cordoned-off feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx54">`, preview text "No Entry". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Tape Cross".

### JavaScript — `FX[54]` from `site/fx.js`

```js
54(s,x){const st='background:repeating-linear-gradient(90deg,#ffd400 0 100%);color:#111;border-block:.6cqw solid #111';const a=mqRow(rep(x+'・',8),6.5,8,false,st);a.className+=' band';a.style.top='36%';a.style.transform='rotate(-15deg)';const b=mqRow(rep(x+'・',8),6.5,6,true,st);b.className+=' band';b.style.top='38%';b.style.transform='rotate(13deg)';s.append(b,a)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx54` rules from `site/fx.css`

_No dedicated `.fx54` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #54
