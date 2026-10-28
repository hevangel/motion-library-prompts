# 002 · Laser Cut — 雷射切斷

A laser slices the text in two

- Component: Text (`text`)
- Timing: Exit
- Tech: CSS
- Uses: Transitions, Headline · Hero
- Style / keywords: Dissipating Exit
- Tag: SF · Severed
- Example text: "Sliced" (stage background: acc)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Laser Cut (雷射切斷)" motion effect: A glowing laser line cuts rapidly from left to right across the middle of the text; after it passes, the top half of the text shifts up-left and the bottom half shifts down-right, tilting slightly, pauses for a moment, then comes back together. About 2.6 seconds per cycle, with a crisp sci-fi feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx2">`, preview text "Sliced". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Laser Cut".

### JavaScript — `FX[2]` from `site/fx.js`

```js
2(s,x){const w=el('div','w');const a=T(x);a.classList.add('top');const b=T(x);b.classList.add('bot');w.append(a,b,el('div','laser'));s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx2` rules from `site/fx.css`

```css
.fx2 .w{position:relative}
.fx2 .top{clip-path:inset(0 0 50% 0);animation:lzT 2.6s infinite}
.fx2 .bot{position:absolute;left:0;top:0;clip-path:inset(50% 0 0 0);animation:lzB 2.6s infinite}
.fx2 .laser{position:absolute;left:-6%;top:50%;height:3px;margin-top:-1.5px;background:#fff;box-shadow:0 0 6px #f22,0 0 16px #f22,0 0 30px #f44;animation:lzL 2.6s infinite;z-index:3}
@keyframes lzB{0%,38%{transform:none}48%,85%{transform:translate(5%,10%) rotate(2deg)}100%{transform:none}}
@keyframes lzL{0%{width:0;opacity:1}35%{width:112%;opacity:1}45%,100%{width:112%;opacity:0}}
@keyframes lzT{0%,38%{transform:none}48%,85%{transform:translate(-5%,-10%) rotate(-3deg)}100%{transform:none}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #2
