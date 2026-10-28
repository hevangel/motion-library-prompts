# 006 · Heartbeat Zoom — 心跳放大

Zooms with a heartbeat and spreads ripples

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Emphasis
- Style / keywords: Impact Entrance
- Tag: Moving · Drama
- Example text: "Throb" (stage background: acc)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Heartbeat Zoom (心跳放大)" motion effect: The text zooms in twice in a row like a heartbeat — “thump-thump” — then returns to its original size; with each beat, two circular ripples spread out from the center at the same time and fade away. About 1.3 seconds per beat.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx6">`, preview text "Throb". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Heartbeat Zoom".

### JavaScript — `FX[6]` from `site/fx.js`

```js
6(s,x){s.append(el('div','ring'),el('div','ring b'),T(x,18))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx6` rules from `site/fx.css`

```css
.fx6 .t{animation:beat 1.3s infinite}
.fx6 .ring{position:absolute;left:50%;top:50%;width:30cqw;height:30cqw;margin:-15cqw 0 0 -15cqw;border:2px solid #111;border-radius:50%;animation:rng 1.3s infinite ease-out;opacity:0}
.fx6 .ring.b{animation-delay:.18s}
@keyframes beat{0%{transform:scale(1)}12%{transform:scale(1.2)}24%{transform:scale(1)}36%{transform:scale(1.12)}60%,100%{transform:scale(1)}}
@keyframes rng{0%{transform:scale(.4);opacity:.7}100%{transform:scale(2.6);opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #6
