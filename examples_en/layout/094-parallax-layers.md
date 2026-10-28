# 094 · Parallax Layers — 視差圖層

Far, middle and near layers move at different speeds

- Component: Layout · Pages (`layout`)
- Timing: Scroll-triggered
- Tech: GSAP
- Uses: Scroll Effects, Background Decoration
- Style / keywords: 
- Tag: ScrollTrigger scrub
- Example text: "Parallax" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Parallax Layers (視差圖層)" motion effect: When scrolling, large background text in the far layer, dots in the middle layer and the title in the near layer move up and down at different speeds — the near layer fastest, the far layer slowest — creating depth-of-field parallax. (GSAP: one timeline bound to a ScrollTrigger with scrub, the three layers each set to a different yPercent range)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx94">`, preview text "Parallax". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Parallax Layers".

### JavaScript — `FX[94]` from `site/fx.js`

```js
94(s,x){const{sc,wrap,view}=scrollBox(s);view.classList.add('pv');view.innerHTML='<div class="l1">遠景</div><div class="l2"></div><div class="l3"></div>';view.querySelector('.l3').textContent=x;const l2=view.querySelector('.l2');
  [[12,20,9],[78,15,14],[60,62,6],[22,70,12],[88,72,8]].forEach(([l,t,z])=>{const i=el('i');i.style.cssText=`left:${l}%;top:${t}%;width:${z}cqw;height:${z}cqw;opacity:.85`;l2.append(i)});
  gsap.timeline({scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:.5}}).fromTo(view.querySelector('.l1'),{yPercent:15},{yPercent:-15,ease:'none'},0).fromTo(l2,{yPercent:45},{yPercent:-45,ease:'none'},0).fromTo(view.querySelector('.l3'),{yPercent:260},{yPercent:-260,ease:'none'},0);autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx94` rules from `site/fx.css`

_No dedicated `.fx94` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #94
