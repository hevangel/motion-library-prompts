# 217 · Infinite Card Wall — 無限捲動卡片牆

Two rows of cards move infinitely in opposite directions, and pause when the mouse moves over them

- Component: Cards · Groups (`card`)
- Timing: Loop · Idle, Hover · Click
- Tech: CSS
- Uses: Background Decoration, Numbers & Data
- Style / keywords: Marquee Card Wall Testimonials Clients Logo Wall Infinite Infinite Marquee Testimonials Logo Wall Cards Group
- Tag: CSS marquee
- Example text: "Designer Engineer Marketer Founder" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Infinite Card Wall (無限捲動卡片牆)" motion effect: Two rows of testimonial or client cards move horizontally in an infinite loop, the top row to the left and the bottom row to the right, at a slow, steady speed; when the mouse moves over the card wall both rows pause for easy reading, and continue when it moves away. Suitable for client testimonials and partner logo walls. (CSS: each row's content is duplicated twice on the same track, and keyframes translateX(0 to -50%) linear infinite achieves a seamless loop; the reverse row uses animation-direction:reverse; on :hover, animation-play-state:paused)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx217">`, preview text "Designer Engineer Marketer Founder". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Infinite Card Wall".

### JavaScript — `FX[217]` from `site/fx.js`

```js
217(s,x){const ws=words(x);const w=el('div','kd-wall');for(let r=0;r<2;r++){const row=el('div','kd-row'+(r?' kd-rv':''));const tr=el('div','kd-tr');const mk=()=>ws.map((v,i)=>{const c=el('div','kd-wc');c.innerHTML='<i></i><span><b></b><em></em><em class="s"></em></span>';c.querySelector('i').style.background=GC[(i+r*2)%5];c.querySelector('b').textContent=v;return c});[...mk(),...mk()].forEach(c=>tr.append(c));row.append(tr);w.append(row)}s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx217` rules from `site/fx.css`

_No dedicated `.fx217` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #217
