# 004 · Explode Out — 爆炸四散

Text explodes and flies in all directions

- Component: Text (`text`)
- Timing: Exit
- Tech: CSS
- Uses: Transitions, Emphasis
- Style / keywords: Dissipating Exit
- Tag: Impact · Chorus
- Example text: "Explode" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Explode Out (爆炸四散)" motion effect: The text first swells slightly to build up energy, then each character explodes randomly in a different direction, spinning, shrinking and fading out; after a pause, the characters fly back into place to form the text again, alternating between the primary color and an accent color. About 2.8 seconds per cycle, with a strong sense of impact.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx4">`, preview text "Explode". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Explode Out".

### JavaScript — `FX[4]` from `site/fx.js`

```js
4(s,x){const t=split(x);t.querySelectorAll('.c').forEach(c=>{c.style.setProperty('--dx',rnd(-40,40)+'cqw');c.style.setProperty('--dy',rnd(-30,30)+'cqw');c.style.setProperty('--r',rnd(-200,200)+'deg')});s.append(t)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx4` rules from `site/fx.css`

```css
.fx4 .c{animation:exp 2.8s calc(var(--i)*.03s) infinite cubic-bezier(.2,.7,.3,1)}
.fx4 .c:nth-child(even){color:var(--a)}
@keyframes exp{0%,22%{transform:none;opacity:1}26%{transform:scale(1.15)}50%,72%{transform:translate(var(--dx),var(--dy)) rotate(var(--r)) scale(.5);opacity:0}90%,100%{transform:none;opacity:1}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #4
