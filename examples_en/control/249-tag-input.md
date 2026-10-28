# 249 · Tag Input — 標籤輸入

Type text and press Enter to turn it into a popping tag; press × or Backspace and the tag shrinks away

- Component: Form · Controls (`control`)
- Timing: Entrance, Exit
- Tech: CSS
- Uses: UI Interaction, App Interface
- Style / keywords: Tag tag chip Input Keywords Interests Tag Input Chips Token Field Form Control
- Tag: JS + CSS
- Example text: "Design Motion Frontend Illustration Branding" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Tag Input (標籤輸入)" motion effect: Tag input field: after the user types text and presses Enter (or a comma), the text becomes a capsule tag, enlarging from 0 with a bounce to appear in front of the input cursor; each tag has a × button on its right side, and when clicked — or when Backspace is pressed in an empty input — the last tag shrinks and fades out and the content behind it smoothly moves up to fill the gap; when the whole field is focused, its border lights up. (JS: keydown handles Enter / comma / Backspace, new elements are inserted before the input; CSS keyframes: entrance scale 0→1 using cubic-bezier(.3,1.6,.5,1), exit scale→0 using a negative margin-right to collapse, and the element is removed after animationend)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx249">`, preview text "Design Motion Frontend Illustration Branding". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Tag Input".

### JavaScript — `FX[249]` from `site/fx.js`

```js
249(s,x,card){const w=el('div','fm-tg');w.innerHTML='<div class="fm-tb"><input aria-label="新增標籤" placeholder="輸入後按 Enter"></div>';const tb=w.querySelector('.fm-tb'),inp=tb.querySelector('input');s.append(w);let real=0;
  const add=t=>{t=t.trim();if(!t)return;const c=el('span','fm-chip');c.innerHTML='<b></b><button type="button" aria-label="移除">×</button>';c.querySelector('b').textContent=t;c.querySelector('button').onclick=()=>{real=Date.now();del(c)};tb.insertBefore(c,inp)};
  const del=c=>{c.classList.add('out');c.addEventListener('animationend',()=>c.remove(),{once:true})};
  inp.addEventListener('keydown',e=>{real=Date.now();if((e.key==='Enter'||e.key===',')&&inp.value.trim()){e.preventDefault();add(inp.value);inp.value=''}else if(e.key==='Backspace'&&!inp.value){const cs=tb.querySelectorAll('.fm-chip:not(.out)');if(cs.length)del(cs[cs.length-1])}});
  const ws=words(x);ws.slice(0,2).forEach(add);let k=2;card._timers.push(setInterval(()=>{if(Date.now()-real<6000||document.activeElement===inp)return;const cs=tb.querySelectorAll('.fm-chip:not(.out)');if(cs.length>=3)del(cs[0]);else add(ws[k++%ws.length])},1300))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx249` rules from `site/fx.css`

_No dedicated `.fx249` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #249
