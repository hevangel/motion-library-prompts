# 247 · Expanding Search — 展開搜尋框

Usually only a round magnifier button; clicking it expands it to the left into a search box

- Component: Form · Controls (`control`)
- Timing: Switch
- Tech: CSS
- Uses: UI Interaction, App Interface
- Style / keywords: Search Magnifier Expand Collapse Navigation Bar Expanding Search Bar Icon Input Header Form Control
- Tag: CSS transition
- Example text: "Search works..." (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Expanding Search (展開搜尋框)" motion effect: Search in a navigation bar: usually just a round magnifier button; when clicked, the button smoothly expands to the left into a long search box (about 0.5 seconds), the text inside the input fades in only after the expansion is halfway, the magnifier rotates 90 degrees and a ring border lights up around it; when the input loses focus and has no content, it retracts back into a round button. (CSS: the container has overflow:hidden, width transitions from the round button's width to the expanded width with cubic-bezier(.6,0,.2,1); the input opacity is paired with a transition-delay; JS toggles the class and focuses the input)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx247">`, preview text "Search works...". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Expanding Search".

### JavaScript — `FX[247]` from `site/fx.js`

```js
247(s,x,card){const w=el('div','fm-sr');w.innerHTML='<input type="search" aria-label="搜尋"><button type="button" aria-label="搜尋"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/></svg></button>';const inp=w.querySelector('input');inp.placeholder=x;s.append(w);
  w.querySelector('button').onclick=()=>{real=Date.now();if(w.classList.contains('open')&&!inp.value){w.classList.remove('open');inp.blur()}else{w.classList.add('open');inp.focus()}};inp.addEventListener('blur',()=>{if(!inp.value)w.classList.remove('open')});let real=0;
  card._timers.push(setInterval(()=>{if(Date.now()-real<6000||document.activeElement===inp)return;w.classList.toggle('open')},1800))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx247` rules from `site/fx.css`

_No dedicated `.fx247` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #247
