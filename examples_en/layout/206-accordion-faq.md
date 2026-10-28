# 206 · Accordion FAQ — 手風琴問答

When a question is clicked, its answer area smoothly expands, the plus turns into an X, and the other questions collapse at the same time

- Component: Layout · Pages (`layout`)
- Timing: Hover · Click, Switch
- Tech: CSS
- Uses: UI Interaction, Numbers & Data
- Style / keywords: Accordion FAQ Expand Collapse Fold Accordion Collapse Expand Details Layout Page Web Structure
- Tag: grid-template-rows
- Example text: "How do I order? How is shipping calculated? Can I return items?" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Accordion FAQ (手風琴問答)" motion effect: A FAQ list, with a plus icon on the right of each question; when one question is opened, the height of its answer area smoothly expands from 0 to the content height (not an instant jump), the plus rotates 135 degrees to become an X at the same time, and any other expanded questions collapse in sync, so only one is open at a time. About 0.45 seconds, ease-in-out. (CSS: the answer wrapper uses display:grid with a transition on grid-template-rows: 0fr to 1fr, and the inner layer has overflow:hidden; the plus is made of two lines and rotated; details/summary with JS can also be used)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx206">`, preview text "How do I order? How is shipping calculated? Can I return items?". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Accordion FAQ".

### JavaScript — `FX[206]` from `site/fx.js`

```js
206(s,x,card){const ws=words(x);const w=el('div','ly-acc');const its=ws.slice(0,3).map(v=>{const it=el('div','ly-ai');it.innerHTML='<button><span></span><i></i></button><div class="ly-ab"><div><em></em><em class="s"></em></div></div>';it.querySelector('span').textContent=v;w.append(it);return it});s.append(w);let real=0,k=0;
  const open=i=>its.forEach((it,j)=>it.classList.toggle('on',j===i&&!it.classList.contains('on')));its.forEach((it,i)=>it.querySelector('button').onclick=()=>{real=Date.now();open(i)});
  card._timers.push(setInterval(()=>{if(Date.now()-real>4000)open(k++%3)},1600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx206` rules from `site/fx.css`

_No dedicated `.fx206` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #206
