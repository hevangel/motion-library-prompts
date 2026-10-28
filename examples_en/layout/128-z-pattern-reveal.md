# 128 · Z-pattern Reveal — Z 字閱讀動線

A homepage layout appears in sequence following a Z-pattern reading order

- Component: Layout · Pages (`layout`)
- Timing: Entrance
- Tech: GSAP
- Uses: Headline · Hero
- Style / keywords: Homepage Hero Layout Z Shape F Shape Reading Pattern Logo Navigation Image Action Button Gentle Soft Light Guidance Flow Gaze Reading Order Low-key Subtle Gentle Soft Entrance Visual Flow Hierarchy
- Tag: Z-pattern
- Example text: "Let the flow happen naturally" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Z-pattern Reveal (Z 字閱讀動線)" motion effect: When a homepage hero enters, the elements fade in and rise in sequence following a Z-pattern reading path: logo at top left → navigation menu at top right → main heading and body copy on the left → hero image on the right → call-to-action button at bottom left → secondary link at bottom right. Each element is spaced about 0.4 seconds apart, rising gently from about 12px below, with an even rhythm and no exaggerated displacement, so the user's gaze moves in the designed order. (The thin lines in the preview only illustrate the Z path and are not needed on a real site. GSAP: arrange the elements in an array in reading order, fromTo y:12 / opacity:0, stagger 0.42, ease power2.out)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx128">`, preview text "Let the flow happen naturally". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Z-pattern Reveal".

### JavaScript — `FX[128]` from `site/fx.js`

```js
128(s,x){const w=el('div','abs zp');w.innerHTML='<svg viewBox="0 0 100 56" preserveAspectRatio="none"><path d="M10,7 L90,7 L12,47 L90,47"/></svg><i class="lg"></i><div class="nv"><i></i><i></i><i></i></div><b class="hd2"></b><i class="ph"></i><i class="im2"></i><span class="cta">開始</span><i class="lk"></i>';
  w.querySelector('.hd2').textContent=x;s.append(w);const q=c=>w.querySelector(c),path=q('path');
  gsap.timeline({repeat:-1,repeatDelay:.3}).set(w,{opacity:1},0).set(path,{opacity:1},0).fromTo(path,{drawSVG:'0%'},{drawSVG:'100%',duration:3,ease:'power1.inOut'},0)
    .fromTo(['.lg','.nv','.hd2','.ph','.im2','.cta','.lk'].map(q),{opacity:0,y:12},{opacity:1,y:0,duration:.8,ease:'power2.out',stagger:.42},.1)
    .to(path,{opacity:0,duration:.6},'-=.2').to(w,{opacity:0,duration:.5},'+=1.4')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx128` rules from `site/fx.css`

_No dedicated `.fx128` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #128
