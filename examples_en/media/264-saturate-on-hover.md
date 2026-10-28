# 264 · Saturate on Hover — 低飽和喚醒

Images are normally low-saturation and slightly dark, and on hover regain vividness and enlarge slightly

- Component: Images · Media (`media`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction
- Style / keywords: Grayscale Desaturate Saturation Awaken Filter Portfolio Team Photos Grayscale Saturate Filter Hover Team Image Media
- Tag: CSS filter
- Example text: "Spring Summer Autumn" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Saturate on Hover (低飽和喚醒)" motion effect: A row of team or work photos, normally presented in low saturation and slightly dark so the whole row looks quiet and unified; when the mouse hovers over one, that photo regains its full saturation and brightness within about 0.6 seconds and enlarges slightly within the frame to 1.05 times, and the name label at the bottom floats up. (CSS: img defaults to filter: grayscale(.9) brightness(.8), on :hover filter: none and scale(1.05), with filter and transform transitioning together)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx264">`, preview text "Spring Summer Autumn". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Saturate on Hover".

### JavaScript — `FX[264]` from `site/fx.js`

```js
264(s,x,card){const ws=words(x);const w=el('div','md-sg');const fs=[0,1,3].map((p,i)=>{const f=el('figure','md-st');f.innerHTML=mdImg(p)+'<figcaption></figcaption>';f.querySelector('figcaption').textContent=ws[i%ws.length];w.append(f);return f});s.append(w);autoHover(w,fs,card,1300)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx264` rules from `site/fx.css`

_No dedicated `.fx264` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #264
