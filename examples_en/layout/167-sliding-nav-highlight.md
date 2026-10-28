# 167 · Sliding Nav Highlight — 選單滑塊跟隨

When you hover over a menu item, a background pill slider follows to that item

- Component: Layout · Pages (`layout`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, App Interface
- Style / keywords: menu navigation slider pill highlight follow nav pill hover indicator tabs hover hover mouse-enter hover-over interaction
- Tag: CSS + JS
- Example text: "Home Work Services Articles Contact" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Sliding Nav Highlight (選單滑塊跟隨)" motion effect: A pill-shaped navigation bar. When the mouse moves over an item, a pill background slider smoothly slides over from its original position and changes width to fit that item, and the text simultaneously switches to a color that contrasts with the slider; when the mouse leaves the whole menu, the slider returns to the item for the current page. About 0.4 seconds, with a slight overshoot. (How to: on pointerenter, read the item's offsetLeft and offsetWidth, set the slider's translateX and width, transition cubic-bezier(.2,.9,.3,1.1))
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx167">`, preview text "Home Work Services Articles Contact". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Sliding Nav Highlight".

### JavaScript — `FX[167]` from `site/fx.js`

```js
167(s,x,card){const n=el('nav','npw');const pill=el('i','npl');n.append(pill);const its=words(x).slice(0,5).map(v=>{const a=el('span','npi');a.textContent=v;n.append(a);return a});s.append(n);let real=false,k=0;
  const go=i=>{const a=its[i];pill.style.width=a.offsetWidth+'px';pill.style.transform=`translateX(${a.offsetLeft}px)`;its.forEach(o=>o.classList.toggle('on',o===a))};
  its.forEach((a,i)=>a.addEventListener('pointerenter',()=>{real=true;go(i)}));n.addEventListener('pointerleave',()=>{real=false;go(0)});requestAnimationFrame(()=>go(0));card._timers.push(setInterval(()=>{if(!real)go(++k%its.length)},1000))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx167` rules from `site/fx.css`

_No dedicated `.fx167` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #167
