# 204 · Push Side Drawer — 側邊抽屜推移

When the menu opens, the whole content page shrinks and pushes to the right, revealing the menu underneath

- Component: Layout · Pages (`layout`)
- Timing: Hover · Click, Switch
- Tech: CSS
- Uses: UI Interaction, App Interface
- Style / keywords: side menu drawer push shrink off-canvas mobile Side Drawer Push Menu Off Canvas Scale layout page web structure
- Tag: CSS transform
- Example text: "Home Work Services Contact" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Push Side Drawer (側邊抽屜推移)" motion effect: When the hamburger icon is clicked, the current content page is pushed to the right as a whole and shrinks to about 86%, with rounded corners and a shadow added, pushed open like a card, revealing the menu hidden underneath, and the menu items slide in from the left and fade in, in sequence; clicking again slides the content page back to cover the menu. About 0.55 seconds, ease in and out. (CSS: content layer transform:translateX(38%) scale(.86), transform-origin at the middle of the left side, border-radius transitions along with it; the menu items are staggered with transition-delay)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx204">`, preview text "Home Work Services Contact". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Push Side Drawer".

### JavaScript — `FX[204]` from `site/fx.js`

```js
204(s,x,card){const w=el('div','ly-dw');w.innerHTML='<nav class="ly-dr"><b>MENU</b></nav><div class="ly-ct"><div class="ly-cb"><i class="ly-hm"></i></div><b></b><i class="ly-bl"></i><i class="ly-bl s"></i><div class="ly-gr"><i></i><i></i></div></div>';const dr=w.querySelector('.ly-dr');words(x).slice(0,4).forEach(v=>{const a=el('span');a.textContent=v;dr.append(a)});
  w.querySelector('.ly-ct b').textContent='首頁';w.querySelectorAll('.ly-gr i').forEach((e,i)=>e.style.background=GC[i+1]);s.append(w);let real=0;w.querySelector('.ly-hm').onclick=()=>{real=Date.now();w.classList.toggle('ly-open')};
  card._timers.push(setInterval(()=>{if(Date.now()-real>4000)w.classList.toggle('ly-open')},2000))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx204` rules from `site/fx.css`

_No dedicated `.fx204` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #204
