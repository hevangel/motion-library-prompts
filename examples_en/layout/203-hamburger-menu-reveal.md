# 203 · Hamburger Menu Reveal — 漢堡選單展開

Three lines transform into an X, and a fullscreen menu expands in a circle from the button

- Component: Layout · Pages (`layout`)
- Timing: Hover · Click, Switch
- Tech: CSS
- Uses: UI Interaction, App Interface
- Style / keywords: hamburger menu menu fullscreen navigation mobile X Hamburger Menu Overlay Fullscreen Nav Toggle layout page web structure
- Tag: clip-path
- Example text: "Home Work Services Contact" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Hamburger Menu Reveal (漢堡選單展開)" motion effect: When the hamburger menu button at the top-right is clicked, the three lines transform into an X (the top and bottom lines rotate ±45 degrees and move to the middle, the middle line shortens and fades out), while the fullscreen menu expands with a circular mask centered on the button's position, and the menu items slide in from below and fade in, top to bottom in sequence (about 0.07 seconds apart); clicking again collapses it in reverse. About 0.6 seconds, ease in and out. (CSS: toggle an open class; menu layer clip-path:circle(0% at the button position) to circle(150%); the lines transition top and rotate; the items' transition-delay increases by index)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx203">`, preview text "Home Work Services Contact". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Hamburger Menu Reveal".

### JavaScript — `FX[203]` from `site/fx.js`

```js
203(s,x,card){const f=lyPage(s,true);const bt=el('button','ly-hb');bt.setAttribute('aria-label','選單');bt.innerHTML='<i></i><i></i><i></i>';const ov=el('nav','ly-ov');words(x).slice(0,4).forEach((v,i)=>{const a=el('span');a.textContent=v;a.style.setProperty('--i',i);ov.append(a)});f.append(ov,bt);
  let real=0;const tog=()=>f.classList.toggle('ly-open');bt.onclick=()=>{real=Date.now();tog()};card._timers.push(setInterval(()=>{if(Date.now()-real>4000)tog()},2200))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx203` rules from `site/fx.css`

_No dedicated `.fx203` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #203
