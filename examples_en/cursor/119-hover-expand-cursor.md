# 119 · Hover Expand Cursor — 懸停放大游標

A small dot cursor expands into a circle with text in it when moved over a work

- Component: Cursor (`cursor`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction
- Style / keywords: Cursor Custom Cursor Enlarge Hover VIEW View Custom Cursor Hover Expand Portfolio
- Tag: Custom cursor
- Example text: "VIEW" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Hover Expand Cursor (懸停放大游標)" motion effect: Hide the system cursor and use a small dot that follows the mouse instead (with a slight lag); when the cursor moves over a work thumbnail, the small dot smoothly expands into a circle about 3× larger, with prompt text such as "VIEW" appearing in the center of the circle, and the work itself shrinks slightly in response; when leaving the work, it shrinks back to a small dot and the text fades out. The expansion takes about 0.35 seconds, ease-out. (How it works: the container is set to cursor:none; the custom cursor uses position:fixed + transform to follow mousemove; when hovering a target, add a class so the inner circle goes scale(0.16→1) and the text opacity 0→1; this effect should be disabled on touch devices)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx119">`, preview text "VIEW". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Hover Expand Cursor".

### JavaScript — `FX[119]` from `site/fx.js`

```js
119(s,x,card){const l=el('div','abs gl cz');const row=el('div','czr');const ts=[0,1,2].map(i=>{const t=el('div','czt');t.style.background=`linear-gradient(135deg,${GC[i]},${GC[i+1]})`;row.append(t);return t});
  const c=el('div','cx');const cb=el('div','cb');const lb=el('span');lb.textContent=x;cb.append(lb);c.append(cb);l.append(row,c);s.append(l);
  vpointer(l,card,(px,py)=>{c.style.transform=`translate(${px}px,${py}px)`;let on=false;ts.forEach(t=>{const h=px>=t.offsetLeft&&px<=t.offsetLeft+t.offsetWidth&&py>=t.offsetTop&&py<=t.offsetTop+t.offsetHeight;t.classList.toggle('hv',h);on=on||h});c.classList.toggle('big',on)})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx119` rules from `site/fx.css`

_No dedicated `.fx119` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #119
