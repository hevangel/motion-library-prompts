# 269 · Slice Transition — 切片轉場

An image is cut into vertical strips that slide away in sequence, one up and one down, revealing the next image

- Component: Images · Media (`media`)
- Timing: Switch, Loop · Idle
- Tech: GSAP
- Uses: Transitions, Headline · Hero
- Style / keywords: Slice Vertical Strips Transition Image Change Blinds Slice Strips Image Transition Slideshow Venetian Image Media
- Tag: GSAP stagger
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Slice Transition (切片轉場)" motion effect: An image carousel transition: the current image is cut into 6 equal-width vertical strips, and when changing to the next image, these strips in sequence (each spaced about 0.06 seconds apart) slide out of the screen alternating one up and one down, revealing the next image underneath, while the next image simultaneously shrinks slowly back from 1.15 times to the original size. (Implementation: each vertical strip is an overflow: hidden container, with the same image inside shifted left by “strip width × index” so that assembled they form a complete image; GSAP applies yPercent ±110 to all strips, stagger 0.06, power3.in)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx269">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Slice Transition".

### JavaScript — `FX[269]` from `site/fx.js`

```js
269(s,x,card){const N=6;const w=el('div','md-sl');const mk=p=>{const l=el('div','md-sll');for(let i=0;i<N;i++){const sl=el('div','md-slc');sl.innerHTML=mdImg(p);sl.style.setProperty('--i',i);sl.style.setProperty('--n',N);l.append(sl)}return l};let p=0;let top=mk(0);w.append(top);s.append(w);let busy=false;
  const next=()=>{if(busy)return;busy=true;p=(p+1)%4;const nw=mk(p);w.prepend(nw);gsap.to(top.children,{yPercent:i=>i%2?110:-110,duration:.7,ease:'power3.in',stagger:.06,onComplete:()=>{top.remove();top=nw;busy=false}});gsap.from(nw.children,{scale:1.15,duration:1.2,ease:'power2.out'})};
  w.onclick=next;card._timers.push(setInterval(next,2600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx269` rules from `site/fx.css`

_No dedicated `.fx269` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #269
