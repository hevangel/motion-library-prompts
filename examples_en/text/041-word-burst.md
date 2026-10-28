# 041 · Word Burst — 文字爆開

A word pops out with a thump

- Component: Text (`text`)
- Timing: Entrance
- Tech: CSS
- Uses: Emphasis
- Style / keywords: Impact Entrance Canva Style Canva Pop Pop Out
- Tag: Emphasis · Highlight
- Example text: "Impact" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Word Burst (文字爆開)" motion effect: The text rapidly pops out from 0, enlarges to 1.25x, then returns to its original size, while a ring of short lines radiates outward from the center, flying apart and disappearing. About 1.8 seconds per cycle, emphasizing the highlight.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx41">`, preview text "Impact". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Word Burst".

### JavaScript — `FX[41]` from `site/fx.js`

```js
41(s,x){const r=el('div','rays');for(let i=0;i<14;i++){const e=el('i');e.style.setProperty('--r',i*360/14+'deg');r.append(e)}s.append(r,T(x,Math.min(20,74/chars(x).length)))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx41` rules from `site/fx.css`

```css
.fx41 .t{color:var(--a);animation:burst 1.8s infinite cubic-bezier(.2,1.6,.4,1)}
.fx41 .rays{position:absolute;left:50%;top:50%}
.fx41 .rays i{position:absolute;left:-.4cqw;top:0;width:.8cqw;height:6cqw;background:var(--a);transform-origin:50% 0;opacity:0;animation:ray 1.8s infinite}
@keyframes burst{0%{transform:scale(0);opacity:0}25%{transform:scale(1.25);opacity:1}35%,85%{transform:scale(1);opacity:1}100%{transform:scale(1);opacity:0}}
@keyframes ray{0%,12%{opacity:0;transform:rotate(var(--r)) translateY(9cqw) scaleY(.2)}24%{opacity:1;transform:rotate(var(--r)) translateY(14cqw) scaleY(1)}45%,100%{opacity:0;transform:rotate(var(--r)) translateY(24cqw) scaleY(.3)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #41
