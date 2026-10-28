# 296 · Blur In Letters — 逐字模糊浮現

Each character in turn becomes clear and settles into place from a blurred, slightly larger state

- Component: Text (`text`)
- Timing: Entrance
- Tech: GSAP
- Uses: Headline · Hero
- Style / keywords: Blur Emergence Letter by Letter Soft Entrance Blur In Letters Soft Reveal Stagger Text Heading Animated Text
- Tag: SplitText
- Example text: "Slowly Emerging" (stage background: dark)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Blur In Letters (逐字模糊浮現)" motion effect: Each character of a heading in turn changes from a "blurred, transparent, slightly larger, slightly lower" state to become clear and settle into position, with about 0.07 seconds between each character, giving an overall soft, refined feel; after lingering for a while, they blur out in sequence and replay. (GSAP + SplitText: fromTo on the characters {opacity:0, filter:"blur(10px)", y:".25em", scale:1.15} → {opacity:1, filter:"blur(0px)", y:0, scale:1}, ease power2.out, stagger 0.07)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx296">`, preview text "Slowly Emerging". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Blur In Letters".

### JavaScript — `FX[296]` from `site/fx.js`

```js
296(s,x){const t=T(x);s.append(t);const sp=SplitText.create(t,{type:'chars'});gsap.timeline({repeat:-1,repeatDelay:.4}).fromTo(sp.chars,{opacity:0,filter:'blur(10px)',y:'.25em',scale:1.15},{opacity:1,filter:'blur(0px)',y:0,scale:1,duration:.9,ease:'power2.out',stagger:.07}).to(sp.chars,{opacity:0,filter:'blur(10px)',duration:.6,stagger:.03,ease:'power1.in'},'+=1.6')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx296` rules from `site/fx.css`

_No dedicated `.fx296` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #296
