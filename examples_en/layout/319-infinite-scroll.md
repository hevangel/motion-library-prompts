# 319 · Infinite Scroll — 無限捲動載入

When you scroll to the bottom, a spinning "loading more" appears, and new content then floats up one item after another

- Component: Layout · Pages (`layout`)
- Timing: Scroll-triggered
- Tech: GSAP
- Uses: UI Interaction, App Interface, Scroll Effects
- Style / keywords: Infinite Scroll Load More Pagination Feed Wall Infinite Scroll Load More Feed Pagination Layout Page
- Tag: GSAP
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-21

**AI prompt (English copy format):**

```text
"Infinite Scroll (無限捲動載入)" motion effect: Infinite scrolling on a social feed wall or article list: when the user scrolls to the bottom of the list, a spinning loading indicator and "Loading more…" appear at the bottom; after about a second, a new batch of cards is appended after the list, fading in and floating up from below in sequence (about 0.12 seconds apart), and the user can keep scrolling down. (Implementation: use IntersectionObserver to watch a sentinel element at the bottom of the list; when it enters the viewport, show the loading indicator and request the next page; after the new cards are inserted, use GSAP from y:24, opacity:0, with stagger for the entrance)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx319">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Infinite Scroll".

### JavaScript — `FX[319]` from `site/fx.js`

```js
319(s,x){const sc=el('div','scr pg-is');const list=el('div','pg-il2');const sp=el('div','pg-ld','<i></i><span>載入更多…</span>');sc.append(list,sp);s.append(sc);let n=0;
  const add=k=>{const items=[];for(let i=0;i<k;i++){const c=el('div','pg-it');c.innerHTML=mdImg(n++)+'<b>貼文 #'+n+'</b>';list.append(c);items.push(c)}return items};add(4);let loading=false;
  const step=()=>{const max=sc.scrollHeight-sc.clientHeight;gsap.to(sc,{scrollTop:max,duration:1.4,ease:'power1.inOut',onComplete:()=>{sp.classList.add('on');gsap.delayedCall(.9,()=>{sp.classList.remove('on');const it=add(2);gsap.from(it,{y:24,opacity:0,duration:.5,stagger:.12,ease:'power3.out'});if(n>=12){gsap.delayedCall(1.2,()=>{gsap.to(sc,{scrollTop:0,duration:.6,onComplete:()=>{list.innerHTML='';n=0;add(4);gsap.delayedCall(.6,step)}})})}else gsap.delayedCall(.9,step)})}})};
  gsap.delayedCall(.6,step)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx319` rules from `site/fx.css`

_No dedicated `.fx319` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #319
