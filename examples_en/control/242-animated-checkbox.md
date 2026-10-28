# 242 · Animated Checkbox — 勾選框打勾

When checked, the box gives a bounce, the checkmark is drawn as if with a pen, and the item text gets a strikethrough

- Component: Form · Controls (`control`)
- Timing: Switch
- Tech: CSS
- Uses: UI Interaction, App Interface
- Style / keywords: Checkbox Checkbox Check To-Do List todo Checkbox Check Animation Todo List Form Control
- Tag: stroke-dashoffset
- Example text: "Buy Coffee Beans Reply to Emails Tidy Desk" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Animated Checkbox (勾選框打勾)" motion effect: A checkbox for a to-do list: when clicked to check it, the box first shrinks and then bounces slightly larger (about 0.4 seconds), and its background fills; the checkmark inside is drawn from bottom-left to top-right as if with a pen; the item text on the right fades and gains a strikethrough line. When unchecked, it reverses back. (CSS: hide the native checkbox and customize the box and an SVG checkmark; the checkmark path uses stroke-dasharray and stroke-dashoffset going from full length to 0; :checked plus style switching; the box bounces with a scale keyframes; keep a :focus-visible outline for keyboard users)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx242">`, preview text "Buy Coffee Beans Reply to Emails Tidy Desk". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Animated Checkbox".

### JavaScript — `FX[242]` from `site/fx.js`

```js
242(s,x,card){const ws=words(x);const w=el('div','fm-ck');ws.slice(0,3).forEach((t,i)=>{const l=el('label');l.innerHTML='<input type="checkbox"><i><svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7"/></svg></i><span></span>';l.querySelector('span').textContent=t;if(i===0)l.querySelector('input').checked=true;w.append(l)});s.append(w);
  const ins=[...w.querySelectorAll('input')];let real=0,k=0;w.addEventListener('pointerdown',()=>real=Date.now());card._timers.push(setInterval(()=>{if(Date.now()-real<5000)return;const i=ins[k++%ins.length];i.checked=!i.checked},1100))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx242` rules from `site/fx.css`

_No dedicated `.fx242` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #242
