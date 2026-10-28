# 318 · Speed Dial FAB — 浮動按鈕展開選單

When the "+" button in the bottom-right corner is clicked it turns into a "×", and several small action buttons and labels pop out above it in sequence

- Component: Layout · Pages (`layout`)
- Timing: Switch
- Tech: CSS
- Uses: UI Interaction, App Interface
- Style / keywords: Floating Button FAB Expand Quick Actions Speed Dial Floating Action Button Menu Layout Page
- Tag: CSS transition
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-21

**AI prompt (English copy format):**

```text
"Speed Dial FAB (浮動按鈕展開選單)" motion effect: A circular floating action button (+) in the bottom-right corner of the screen: when clicked, the button rotates 135 degrees into a ×, a translucent overlay covers the background, and three small circular action buttons pop out above it from bottom to top in sequence, each with a text label on its left (for example New note, Take a photo, Share a link), appearing by enlarging with a bounce-back from a smaller, slightly lower position; click again or click the overlay to retract them in the reverse order. (CSS: when .open, the main button uses rotate(135deg); each action item is given a --i, transitions transform: translateY + scale, with transition-delay computed by index, in the reverse order when collapsing)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx318">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Speed Dial FAB".

### JavaScript — `FX[318]` from `site/fx.js`

```js
318(s,x,card){const f=lyPage(s);f.insertAdjacentHTML('beforeend','<div class="pg-pc"><b>文件</b><i class="ly-bl"></i><i class="ly-bl s"></i><i class="ly-bl"></i></div><div class="pg-bd"></div>');const dial=el('div','pg-dl');const A=[['✎','新增筆記'],['📷','拍照'],['🔗','分享連結']];dial.innerHTML=A.map(([i,l],k)=>`<div class="pg-da" style="--i:${k}"><span></span><button aria-label="${l}">${i}</button></div>`).join('')+'<button class="pg-fab" aria-label="更多">+</button>';dial.querySelectorAll('.pg-da span').forEach((sp,k)=>sp.textContent=A[k][1]);f.append(dial);
  let real=0;const tog=o=>f.classList.toggle('pg-dopen',o);dial.querySelector('.pg-fab').onclick=()=>{real=Date.now();tog(!f.classList.contains('pg-dopen'))};f.querySelector('.pg-bd').onclick=()=>{real=Date.now();tog(false)};
  card._timers.push(setInterval(()=>{if(Date.now()-real>5000)tog(!f.classList.contains('pg-dopen'))},1700))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx318` rules from `site/fx.css`

_No dedicated `.fx318` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #318
