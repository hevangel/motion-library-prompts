# 294 · Light Source Shadow — 光源投影字

The cursor is like a lamp, and the text's long shadow always extends in the direction opposite the cursor

- Component: Text (`text`)
- Timing: Hover · Click
- Tech: CSS
- Uses: Headline · Hero, Emphasis
- Style / keywords: Light Source Projection Shadow Long Shadow 3D Cursor Light Source Long Shadow Cursor 3D Text Text Heading Animated Text
- Tag: text-shadow
- Example text: "SHADOW" (stage background: dark)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Light Source Shadow (光源投影字)" motion effect: There is a large heading in a section, and the cursor position is a small glowing light source: behind the text is a long shadow made of multiple shadow layers, and the shadow always extends in the direction "away from the cursor", with layers farther away becoming fainter in color; as the cursor moves, the shadow's direction turns in real time to follow, as if the light source is moving around the text. (JS: on mousemove, compute the direction vector of the cursor relative to the text's center, and generate 18 layers of text-shadow, each layer's offset = direction × layer number, with the color gradually fading by layer number)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx294">`, preview text "SHADOW". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Light Source Shadow".

### JavaScript — `FX[294]` from `site/fx.js`

```js
294(s,x,card){const l=el('div','abs gl tx-ls');const t=T(x,Math.min(15,64/chars(x).length));const sun=el('i','tx-sun');l.append(t,sun);s.append(l);
  vpointer(l,card,(px,py)=>{const W=l.offsetWidth,H=l.offsetHeight,dx=(W/2-px)/W,dy=(H/2-py)/H,n=18,sh=[];for(let i=1;i<=n;i++)sh.push(`${(dx*i*1.4).toFixed(1)}px ${(dy*i*1.4).toFixed(1)}px 0 color-mix(in srgb,var(--a) ${Math.round(100-i/n*85)}%,#15161a)`);t.style.textShadow=sh.join(',');sun.style.transform=`translate(${px}px,${py}px)`})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx294` rules from `site/fx.css`

_No dedicated `.fx294` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #294
