# 111 · Like Burst — 愛心按讚爆開

Clicking the heart makes it bounce and scale up, spraying small dots and a ring of light around it

- Component: Button (`button`)
- Timing: Hover · Click, Entrance
- Tech: CSS
- Uses: UI Interaction
- Style / keywords: Button Like Favorite Heart Click Feedback Micro-interaction Like Heart Burst Micro-interaction Twitter
- Tag: CSS keyframes
- Example text: "Like" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Like Burst (愛心按讚爆開)" motion effect: When the "Like" button is clicked, the hollow heart instantly fills and bounces up from small to large, while 8 small dots spray outward from around the heart and a ring of light expands and disappears, and the number beside it goes +1; clicking again cancels it, the heart returns to hollow and the number goes −1. The whole thing takes about 0.5 seconds, with an elastic feedback feel. (CSS: toggling the .on class; the heart uses a scale bounce keyframes, the small dots use rotate(var(--r)) translateY to fly outward while shrinking and fading, the ring uses scale + opacity; before replaying, remove the class first and trigger a reflow)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx111">`, preview text "Like". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Like Burst".

### JavaScript — `FX[111]` from `site/fx.js`

```js
111(s,x,card){const b=el('button','like');b.innerHTML='<span class="hw"><i class="ring"></i>'+[...Array(8)].map((_,i)=>`<i class="p" style="--r:${i*45}deg"></i>`).join('')+'<svg viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg></span><span class="lt"></span><span class="ct">128</span>';
  b.querySelector('.lt').textContent=x;s.append(b);const ct=b.querySelector('.ct');let real=false;
  const tog=()=>{const on=!b.classList.contains('on');b.classList.remove('on');void b.offsetWidth;b.classList.toggle('on',on);ct.textContent=on?129:128};
  b.onclick=tog;b.addEventListener('pointerenter',()=>real=true);b.addEventListener('pointerleave',()=>real=false);card._timers.push(setInterval(()=>{if(!real)tog()},1600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx111` rules from `site/fx.css`

_No dedicated `.fx111` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #111
