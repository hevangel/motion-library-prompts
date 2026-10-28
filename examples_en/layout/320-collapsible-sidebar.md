# 320 · Collapsible Sidebar — 側欄收合

Click to collapse an admin sidebar to just icons, the text fades out, and the main content area widens in sync

- Component: Layout · Pages (`layout`)
- Timing: Switch
- Tech: CSS
- Uses: UI Interaction, App Interface
- Style / keywords: Sidebar Collapse Expand Admin Dashboard Collapsible Sidebar Nav Dashboard Admin Layout Page
- Tag: CSS transition
- Example text: "Home Reports Messages Settings" (stage background: dark)
- Added: 2026-10-21

**AI prompt (English copy format):**

```text
"Collapsible Sidebar (側欄收合)" motion effect: The sidebar on the left of an admin interface: when you click the collapse button at the top of the sidebar, the sidebar's width smoothly narrows to fit only the icons (about 0.45 seconds), the text of each item simultaneously fades out to the left, and the main content area on the right widens in sync; click again to expand and the text fades back in; the currently active item has a faint accent background color. (CSS: the sidebar uses a width transition, cubic-bezier(.6,0,.2,1); item text transitions opacity and translateX, with white-space:nowrap + overflow:hidden to prevent wrapping; the main content uses flex:1 to fill automatically)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx320">`, preview text "Home Reports Messages Settings". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Collapsible Sidebar".

### JavaScript — `FX[320]` from `site/fx.js`

```js
320(s,x,card){const ws=words(x);const w=el('div','pg-sbw');w.innerHTML='<aside class="pg-side"><button class="pg-tg" aria-label="收合側欄">«</button>'+['⌂','▦','✉','⚙'].map((ic,i)=>`<a class="${i?'':'on'}"><i>${ic}</i><span></span></a>`).join('')+'</aside><main class="pg-main"><b>儀表板</b><div class="pg-cards"><i></i><i></i><i></i></div><i class="ly-bl"></i><i class="ly-bl s"></i></main>';w.querySelectorAll('.pg-side span').forEach((sp,i)=>sp.textContent=ws[i%ws.length]);s.append(w);
  let real=0;const tg=w.querySelector('.pg-tg');const tog=()=>{const c=w.classList.toggle('mini');tg.textContent=c?'»':'«';tg.setAttribute('aria-label',c?'展開側欄':'收合側欄')};tg.onclick=()=>{real=Date.now();tog()};card._timers.push(setInterval(()=>{if(Date.now()-real>5000)tog()},2000))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx320` rules from `site/fx.css`

_No dedicated `.fx320` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #320
