# 126 · Soft Line Fade — 逐行淡入

A paragraph becomes clear line by line from a slight blur, setting a reading rhythm

- Component: Text (`text`)
- Timing: Entrance
- Tech: GSAP
- Uses: Headline · Hero
- Style / keywords: Paragraph Body Line-by-Line Blur Copy Gentle Soft Light Guidance Flow Gaze Reading Order Low-key Subtle Gentle Soft Entrance Visual Flow Hierarchy Canva Style Canva Fade Clarify Fade In Clear
- Tag: Line fade
- Example text: "Good motion doesn't grab attention it gently guides your gaze to the next step" (stage background: cream)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Soft Line Fade (逐行淡入)" motion effect: When a multi-line passage enters, each line in turn slowly becomes clear and fades in from about 10px below, slightly blurred and transparent, with about 0.28 seconds between lines (slower than a typical stagger, close to reading speed), about 1.1 seconds per line, easing out smoothly. The overall feel is quiet and breathable, suited to a brand philosophy or quote section. (GSAP: one element per line or SplitText with type lines, fromTo y:10 / opacity:0 / filter:blur(4px) → clear, stagger 0.28, ease power2.out)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx126">`, preview text "Good motion doesn't grab attention it gently guides your gaze to the next step". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Soft Line Fade".

### JavaScript — `FX[126]` from `site/fx.js`

```js
126(s,x){const w=el('div','sl');words(x).forEach(v=>{const d=el('div');d.textContent=v;w.append(d)});s.append(w);const it=w.children;
  gsap.timeline({repeat:-1,repeatDelay:.3}).fromTo(it,{y:10,opacity:0,filter:'blur(4px)'},{y:0,opacity:1,filter:'blur(0px)',duration:1.1,ease:'power2.out',stagger:.28}).to(it,{opacity:0,duration:.6},'+=1.6')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx126` rules from `site/fx.css`

_No dedicated `.fx126` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #126
