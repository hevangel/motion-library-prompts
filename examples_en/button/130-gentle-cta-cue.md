# 130 · Gentle CTA Cue — 行動按鈕提示

After the content appears, a halo gently spreads around the button, drawing the eye to it

- Component: Button (`button`)
- Timing: Entrance
- Tech: GSAP
- Uses: Emphasis, UI Interaction
- Style / keywords: CTA Call to Action Button Cue Halo Diffusion Attention Gentle Soft Light Guidance Flow Gaze Reading Order Low-key Subtle Gentle Soft Entrance Visual Flow Hierarchy
- Tag: CTA cue
- Example text: "Free Trial" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Gentle CTA Cue (行動按鈕提示)" motion effect: A content section (heading, two lines of body copy, and a button) first fades in and rises gently in sequence; about 0.3 seconds after everything has appeared, a translucent halo softly spreads out from around the call-to-action button and fades away, twice in a row, while the button lifts slightly by 3px and returns to place, as if gently reminding 'the next step is here,' then stays still without flashing continuously. (GSAP: first a staggered fade-in, then tween the CSS variable --ring 0→1 to control the spread and opacity of the ::after box-shadow, repeat:1; the whole sequence plays only once)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx130">`, preview text "Free Trial". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Gentle CTA Cue".

### JavaScript — `FX[130]` from `site/fx.js`

```js
130(s,x){const w=el('div','gs');w.innerHTML='<b>準備好開始了嗎？</b><i class="ln"></i><i class="ln s"></i><span class="bt ctaa"></span>';const bt=w.querySelector('.bt');bt.textContent=x;s.append(w);const it=[...w.children];
  gsap.timeline({repeat:-1,repeatDelay:.3}).fromTo(it,{opacity:0,y:14},{opacity:1,y:0,duration:.8,ease:'power2.out',stagger:.12})
    .fromTo(bt,{'--ring':0},{'--ring':1,duration:1.3,ease:'power2.out',repeat:1},'+=.3').fromTo(bt,{y:0},{y:-3,duration:.5,ease:'power2.out',yoyo:true,repeat:1},'<').to(it,{opacity:0,duration:.5},'+=1.2')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx130` rules from `site/fx.css`

_No dedicated `.fx130` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #130
