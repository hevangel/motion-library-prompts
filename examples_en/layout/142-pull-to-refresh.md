# 142 · Pull to Refresh — 下拉重新整理

Pull a list down, a spinning icon appears, and on release it loads and springs back

- Component: Layout · Pages (`layout`)
- Timing: Drag Gesture
- Tech: GSAP
- Uses: App Interface, UI Interaction
- Style / keywords: Pull Down Refresh Reload List Gesture Pull Refresh Spinner Gesture App Mobile Mobile Device Micro-interaction Mobile App Micro-interaction
- Tag: Pull to refresh
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Pull to Refresh (下拉重新整理)" motion effect: When you pull down at the top of a mobile list page, the list follows the finger downward (the further you pull, the greater the resistance), and a circular loading icon is revealed above; the icon's rotation angle increases with the pull distance. On release, the icon keeps spinning to indicate loading; when loading finishes, the list smoothly springs back to the top, and the newest item is briefly highlighted before fading back. (GSAP: get the pull distance from the gesture using Draggable or Observer and multiply it by a damping coefficient; on release, a timeline: spinner rotation → list y back to 0 (power3.out) → the new item's background fades out)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx142">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Pull to Refresh".

### JavaScript — `FX[142]` from `site/fx.js`

```js
142(s){const ph=phone(s);const sp=el('i','ptr');const fg=el('i','tap');const list=el('div','pl');for(let i=0;i<7;i++)list.append(mrow(i));ph.append(sp,list,fg);const H=()=>ph.offsetHeight;
  gsap.timeline({repeat:-1,repeatDelay:.6}).set([sp,fg],{opacity:0},0).set(fg,{y:()=>H()*.3},0).to(fg,{opacity:.7,duration:.2},.2)
    .to([list,fg],{y:i=>i?H()*.48:H()*.17,duration:.7,ease:'power2.out'},.3).fromTo(sp,{opacity:0,rotation:0},{opacity:1,rotation:240,duration:.7,ease:'power2.out'},.3).to(fg,{opacity:0,duration:.2})
    .to(sp,{rotation:'+=720',duration:1.2,ease:'none'}).to(list,{y:0,duration:.5,ease:'power3.out'}).to(sp,{opacity:0,duration:.2},'<').fromTo(list.firstChild,{backgroundColor:'rgba(255,255,255,.12)'},{backgroundColor:'rgba(255,255,255,0)',duration:1})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx142` rules from `site/fx.css`

_No dedicated `.fx142` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #142
