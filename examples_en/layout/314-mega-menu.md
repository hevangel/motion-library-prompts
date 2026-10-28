# 314 · Mega Menu — 大型下拉選單

When you hover over a navigation bar item, a large multi-column menu expands below it, and each column slides in in sequence

- Component: Layout · Pages (`layout`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction
- Style / keywords: Mega Menu Dropdown Navigation Bar Multi-column mega menu Dropdown Navigation Header Layout Page
- Tag: CSS transition
- Example text: "Brand Design Web Development Motion Video Social Media Case Studies Design Guide" (stage background: dark)
- Added: 2026-10-21

**AI prompt (English copy format):**

```text
"Mega Menu (大型下拉選單)" motion effect: A website navigation bar: when the mouse moves over "Products", a large, wide menu panel expands below it (sliding down from slightly higher up and fading in); inside, the panel is divided into three columns: two columns are link lists with small icons, and one column is a featured image card; the three columns slide up and in in sequence (about 0.06 seconds apart); when the mouse leaves the navigation area, the panel collapses. (CSS: by default the panel has opacity 0, translateY(−8px), pointer-events:none, restored when the parent has :hover or .open; each column is given a transition-delay to create the sequential appearance)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx314">`, preview text "Brand Design Web Development Motion Video Social Media Case Studies Design Guide". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Mega Menu".

### JavaScript — `FX[314]` from `site/fx.js`

```js
314(s,x,card){const f=lyPage(s,true);const ws=words(x);const nav=el('div','pg-mn');nav.innerHTML='<span class="pg-mi">產品 ▾</span><span>方案</span><span>關於</span>';const pn=el('div','pg-mp');pn.innerHTML=[0,1,2].map(c=>'<div class="pg-mc"><small>'+['服務','資源','精選'][c]+'</small>'+(c<2?[0,1,2].map(r=>'<p><i></i><b></b></p>').join(''):'<div class="pg-mf">'+mdImg(1)+'</div>')+'</div>').join('');pn.querySelectorAll('p b').forEach((b,i)=>b.textContent=ws[i%ws.length]);f.querySelector('.ly-bar').append(nav);f.append(pn);
  const mi=nav.querySelector('.pg-mi');let real=0;const open=o=>f.classList.toggle('pg-open',o);mi.addEventListener('pointerenter',()=>{real=Date.now();open(true)});f.addEventListener('pointerleave',()=>open(false));pn.addEventListener('pointerenter',()=>real=Date.now());
  card._timers.push(setInterval(()=>{if(Date.now()-real>5000)open(!f.classList.contains('pg-open'))},1800))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx314` rules from `site/fx.css`

_No dedicated `.fx314` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #314
