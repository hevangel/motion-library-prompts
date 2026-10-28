# 008 · Number Slam — 倒數砸落

Countdown numbers slam down hard

- Component: Text (`text`)
- Timing: Entrance
- Tech: CSS
- Uses: Numbers & Data, Headline · Hero
- Style / keywords: Impact Entrance
- Tag: Opening · Countdown
- Example text: "3,2,1,GO!" (stage background: dark, fixed text)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Number Slam (倒數砸落)" motion effect: The countdown “3, 2, 1, GO!” appears in sequence; each number slams down forcefully from 3x size and rebounds to its original size, about 0.75 seconds per number, with GO! highlighted in an accent color. Bold black type, with a strong opening feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx8">`, preview text "3,2,1,GO!". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Number Slam".

### JavaScript — `FX[8]` from `site/fx.js`

```js
8(s,x,card){const seq=['3','2','1','GO!'];let i=0;const show=()=>{s.querySelector('.n')?.remove();const n=el('div','n'+(seq[i]==='GO!'?' go':''),seq[i]);s.append(n);i=(i+1)%seq.length};show();card._timers.push(setInterval(show,750))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx8` rules from `site/fx.css`

```css
.fx8 .n{font-weight:900;font-size:24cqw;line-height:1;animation:slam .7s both cubic-bezier(.2,1.4,.4,1)}
.fx8 .n.go{color:var(--a)}
@keyframes slam{0%{transform:scale(3);opacity:0}35%{transform:scale(.9);opacity:1}55%{transform:scale(1.05)}100%{transform:scale(1)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #8
