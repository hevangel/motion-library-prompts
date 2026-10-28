# 193 · Audio Waveform — 音訊波形

A row of bars jumps randomly like an audio waveform

- Component: Shapes · SVG (`shape`)
- Timing: Loop · Idle
- Tech: GSAP
- Uses: Numbers & Data, UI Interaction, App Interface
- Style / keywords: audio waveform music player equalizer Podcast Audio Waveform Equalizer Visualizer SVG graphic
- Tag: SVG bars
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Audio Waveform (音訊波形)" motion effect: A waveform in an audio player: a row of thin, rounded bars stretches up and down with the center line as a baseline, each bar's height is random, their speeds differ slightly and they keep changing, like sound being played; there is a circular play button on the left, and the time is shown on the right. (GSAP: tween all rects with scaleY:"random(.12,1)", duration:"random(.22,.5)", repeat:-1, yoyo:true, repeatRefresh:true so each repeat picks new random numbers, transformOrigin centered)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx193">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Audio Waveform".

### JavaScript — `FX[193]` from `site/fx.js`

```js
193(s){const n=34,w=el('div','wvf');w.innerHTML='<i class="pl">▶</i><svg viewBox="0 0 '+(n*6)+' 40" preserveAspectRatio="none">'+[...Array(n)].map((_,i)=>`<rect x="${i*6+1}" y="2" width="3.4" height="36" rx="1.7"/>`).join('')+'</svg><small>0:42</small>';s.append(w);
  gsap.to(w.querySelectorAll('rect'),{scaleY:'random(.12,1)',transformOrigin:'50% 50%',duration:'random(.22,.5)',ease:'sine.inOut',repeat:-1,yoyo:true,repeatRefresh:true,stagger:{each:.02,from:'random'}})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx193` rules from `site/fx.css`

_No dedicated `.fx193` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #193
