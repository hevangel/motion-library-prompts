# 028 · Rotating Words — 圓環換字

Switches words inside a ring

- Component: Text (`text`)
- Timing: Switch
- Tech: CSS
- Uses: Numbers & Data, Logo · Brand
- Style / keywords: Text Switching
- Tag: Time · Seasons
- Example text: "春夏秋冬" (stage background: dark, fixed text)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Rotating Words (圓環換字)" motion effect: The character inside the rounded square at the center switches in sequence (e.g., Spring → Summer → Autumn → Winter), each switch with an up-and-down flipping motion, while a ring of text around it keeps rotating slowly. One switch about every 1.3 seconds.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx28">`, preview text "春夏秋冬". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Rotating Words".

### JavaScript — `FX[28]` from `site/fx.js`

```js
28(s,x,card){s.append(ringOf('はる・なつ・あき・ふゆ・','17','3.6','cw'));const c=el('div','center');s.append(c);const cs=chars(x);let i=0;const show=()=>{c.textContent=cs[i];c.classList.remove('flip');void c.offsetWidth;c.classList.add('flip');i=(i+1)%cs.length};show();card._timers.push(setInterval(show,1300))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx28` rules from `site/fx.css`

```css
.fx28 .center{position:relative;font-weight:900;font-size:13cqw;background:#fff;color:#111;padding:0 1.5cqw;border-radius:2cqw;line-height:1.2;z-index:2}
.fx28 .center.flip{animation:flp .5s}
@keyframes flp{0%{transform:rotateX(90deg)}100%{transform:none}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #28
