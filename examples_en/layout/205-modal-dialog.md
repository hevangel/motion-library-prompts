# 205 · Modal Dialog — 彈出視窗

The background blurs and darkens, and a window pops out elastically from a slightly smaller, lower position

- Component: Layout · Pages (`layout`)
- Timing: Entrance, Exit
- Tech: CSS
- Uses: UI Interaction, App Interface
- Style / keywords: popup dialog window confirm modal dialog popup background blur Overlay layout page web structure
- Tag: CSS transition
- Example text: "Ready to submit?" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Modal Dialog (彈出視窗)" motion effect: After a button is clicked, the background gets a translucent mask and a slight blur (fading in over about 0.35 seconds), and a dialog floats elastically to the exact center from 90% size and a position slightly below center, with a slight overshoot; the content includes a title, a description, and Cancel / Confirm buttons; clicking the mask or either button fades the dialog out and shrinks it back, and the mask fades out. (CSS: toggle an open class; mask opacity + backdrop-filter:blur; dialog transform:translate(-50%,-40%) scale(.9) to translate(-50%,-50%) scale(1), transition cubic-bezier(.3,1.4,.5,1); remember to handle focus and closing with the Esc key)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx205">`, preview text "Ready to submit?". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Modal Dialog".

### JavaScript — `FX[205]` from `site/fx.js`

```js
205(s,x,card){const f=lyPage(s);f.insertAdjacentHTML('beforeend','<div class="ly-pg"><b>商品頁</b><i class="ly-bl"></i><i class="ly-bl s"></i><button class="ly-ob">開啟視窗</button></div><div class="ly-bd"></div><div class="ly-md"><b></b><i class="ly-bl"></i><i class="ly-bl s"></i><div class="ly-mb"><span>取消</span><span class="p">確定</span></div></div>');f.querySelector('.ly-md b').textContent=x;
  let real=0;const ob=f.querySelector('.ly-ob');const tog=()=>f.classList.toggle('ly-open');ob.onclick=()=>{real=Date.now();tog()};f.querySelector('.ly-bd').onclick=()=>{real=Date.now();f.classList.remove('ly-open')};f.querySelectorAll('.ly-mb span').forEach(e=>e.onclick=()=>{real=Date.now();f.classList.remove('ly-open')});
  card._timers.push(setInterval(()=>{if(Date.now()-real>4000){if(!f.classList.contains('ly-open')){ob.classList.add('pr');setTimeout(()=>ob.classList.remove('pr'),160)}tog()}},1800))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx205` rules from `site/fx.css`

_No dedicated `.fx205` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #205
