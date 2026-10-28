# 102 · Rolling Text Button — 文字翻滾按鈕

On hover the letters roll up one by one, the button inverts, and the arrow turns

- Component: Button (`button`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction, Emphasis
- Style / keywords: Button hover Hover Rolling Text Roll Text Button Hover Stagger CTA
- Tag: CSS hover
- Example text: "View Works" (stage background: cream)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Rolling Text Button (文字翻滾按鈕)" motion effect: A pill-shaped button, with text on the left and a circular arrow on the right. When the mouse moves over it, each letter of the button text rolls upward in sequence (each letter delayed by about 0.035 seconds), with an identical copy of the text filling in from below; at the same time, the button's background and text colors swap to the accent scheme, the circle on the right also inverts its colors, and the arrow rotates to point up-right at 45 degrees; when the mouse leaves, everything rolls back in reverse. The whole thing takes about 0.55 seconds, with ease-in-out (cubic-bezier(.7,0,.2,1)). (CSS: each letter wrapped in a span, ::after{content:attr(data-t);top:100%} creates the second copy of the text, the outer layer has overflow:hidden, on :hover translateY(-100%), and transition-delay uses calc(var(--i)*.035s) to stagger the letters)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx102">`, preview text "View Works". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Rolling Text Button".

### JavaScript — `FX[102]` from `site/fx.js`

```js
102(s,x,card){const b=el('button','rbtn');b.setAttribute('aria-label',x);const lab=el('span','rl');b.style.fontSize=Math.min(5,40/chars(x).length)+'cqw';
  chars(x).forEach((ch,i)=>{const c=el('span','rc');c.style.setProperty('--i',i);c.textContent=c.dataset.t=ch===' '?'\u00a0':ch;lab.append(c)});
  const ar=el('i','ra');ar.textContent='→';b.append(lab,ar);s.append(b);
  // 沒人操作時自動示範 hover；滑鼠移上去就交給真正的 :hover
  let real=false;b.addEventListener('pointerenter',()=>{real=true;b.classList.remove('hv')});b.addEventListener('pointerleave',()=>real=false);
  card._timers.push(setInterval(()=>{if(!real)b.classList.toggle('hv')},1500))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx102` rules from `site/fx.css`

_No dedicated `.fx102` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #102
