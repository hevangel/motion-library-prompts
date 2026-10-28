# 160 · Section Theme Switch — 章節主題切換

When scrolled to different sections, the whole page's background and text scheme switch along with it

- Component: Background · Ambience (`bg`)
- Timing: Scroll-triggered, Switch
- Tech: GSAP
- Uses: Background Decoration, Scroll Effects, Transitions
- Style / keywords: Background Theme Switch Section Block Section Theme Background Change On Scroll Chapters Scroll Scroll scroll ScrollTrigger scrub Scroll-triggered
- Tag: ScrollTrigger toggle
- Example text: "Prologue Philosophy Work Contact" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Section Theme Switch (章節主題切換)" motion effect: The page is divided into several sections, each with its own background and text color theme; when a section scrolls to the middle line of the screen, the whole page's background and text smoothly transition over about 0.6 seconds to that section's theme, and scrolling back switches back to the previous one, so each chapter has a clear mood change. (GSAP: one ScrollTrigger per section, start "top 50%", end "bottom 50%", switching CSS variables or a class onToggle; CSS adds a transition to background / color)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx160">`, preview text "Prologue Philosophy Work Contact". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Section Theme Switch".

### JavaScript — `FX[160]` from `site/fx.js`

```js
160(s,x){const sc=el('div','scr nopad thm');const TH=[['#15161a','#fff'],['#f4f1e8','#111'],['#ff7a2f','#111'],['#7c5cff','#fff']];const ws=words(x);
  const secs=ws.slice(0,4).map((v,i)=>{const e=el('section','ths');e.innerHTML=`<small>CHAPTER 0${i+1}</small><b></b><i></i><i class="s"></i>`;e.querySelector('b').textContent=v;sc.append(e);return e});s.append(sc);
  const set=i=>{sc.style.background=TH[i][0];sc.style.color=TH[i][1]};set(0);secs.forEach((e,i)=>ScrollTrigger.create({trigger:e,scroller:sc,start:'top 50%',end:'bottom 50%',onToggle:t=>{if(t.isActive)set(i)}}));autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx160` rules from `site/fx.css`

_No dedicated `.fx160` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #160
