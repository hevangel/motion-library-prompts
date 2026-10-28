# 001 · Lightning Strike — 閃電砸落

Slams down hard with a lightning flash

- Component: Text (`text`)
- Timing: Entrance
- Tech: CSS
- Uses: Headline · Hero, Emphasis
- Style / keywords: Impact Entrance
- Tag: Impact · Opening
- Example text: "Thunder" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Lightning Strike (閃電砸落)" motion effect: The screen first flashes brightly twice and a lightning bolt appears; the text slams down instantly from 2x size and shrinks back to its original size, trembling slightly on landing, then keeps a soft outer glow. The whole sequence lasts about 2.4 seconds, with a fast, explosive rhythm.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx1">`, preview text "Thunder". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Lightning Strike".

### JavaScript — `FX[1]` from `site/fx.js`

```js
1(s,x){s.append(el('div','flash'));s.insertAdjacentHTML('beforeend','<svg viewBox="0 0 160 90" preserveAspectRatio="none"><polyline points="95,0 82,30 92,32 74,60 84,62 70,90" fill="none" stroke="#fff" stroke-width="1.6"/></svg>');s.append(T(x))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx1` rules from `site/fx.css`

```css
.fx1 .t{animation:ls 2.4s infinite;color:#fff}
.fx1 .flash{position:absolute;inset:0;background:#fff;animation:fl 2.4s infinite;z-index:5;pointer-events:none}
.fx1 svg{position:absolute;inset:0;width:100%;height:100%;animation:fl 2.4s infinite;z-index:4}
@keyframes fl{0%,19%{opacity:0}20%{opacity:.85}23%{opacity:0}25%{opacity:.55}28%,100%{opacity:0}}
@keyframes ls{0%,18%{opacity:0;transform:scale(2.4)}22%{opacity:1;transform:scale(.9)}26%{transform:scale(1.06) translate(-4px,3px)}30%{transform:scale(1) translate(3px,-2px)}34%,85%{transform:none;opacity:1;text-shadow:0 0 10px var(--a),0 0 28px var(--a)}100%{opacity:0;transform:none}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #1
