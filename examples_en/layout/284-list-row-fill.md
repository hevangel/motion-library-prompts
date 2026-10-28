# 284 · List Row Fill — 清單列滑入填滿

When hovering over a list row, the background color brushes in from the left, the text makes way to the right, and an arrow slides out

- Component: Layout · Pages (`layout`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction
- Style / keywords: List Rows Service Items Menu Background Fill Arrow List Row Hover Fill Sweep Arrow Services Menu hover Hovering Hover Over
- Tag: CSS hover
- Example text: "Brand Identity Website Design Motion Graphics Packaging Design" (stage background: dark)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"List Row Fill (清單列滑入填滿)" motion effect: A list of service items, each row with a number, an item name, and an arrow on the right, with thin divider lines between rows: when the mouse hovers over a row, a solid background color brushes in from the left to fill the whole row, the item name moves a little to the right to make way, the arrow on the right slides in from the left and appears, and the text color inverts to stay readable; when moving away the background color retracts to the right. About 0.5 seconds. (CSS: inside each row an absolutely positioned background layer transform: scaleX(0), on hover scaleX(1) with transform-origin from left; on leave transform-origin changes to right, forming “in from the left, out to the right”)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx284">`, preview text "Brand Identity Website Design Motion Graphics Packaging Design". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "List Row Fill".

### JavaScript — `FX[284]` from `site/fx.js`

```js
284(s,x,card){const ws=words(x).slice(0,4);const w=el('ul','ho-rw');const its=ws.map((t,i)=>{const li=el('li');li.innerHTML='<i></i><em>0'+(i+1)+'</em><b></b><svg viewBox="0 0 24 24"><path d="M5 12h13M13 6l6 6-6 6"/></svg>';li.querySelector('b').textContent=t;w.append(li);return li});s.append(w);autoHover(w,its,card,1000)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx284` rules from `site/fx.css`

_No dedicated `.fx284` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #284
