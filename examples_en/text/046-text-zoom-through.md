# 046 · Text Zoom Through — 穿越放大

Dives into the letters, connects to the next word

- Component: Text (`text`)
- Timing: Switch
- Tech: CSS
- Uses: Transitions
- Style / keywords: Text Switching
- Tag: Transition·Sense of Speed
- Example text: "Into the Words Next" (stage background: cream)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Text Zoom Through (穿越放大)" motion effect: A word scales up from small to normal size, then accelerates and enlarges until it fills the frame and fades out, like the camera diving into the letters; the next word then appears from far away to follow. About 1.2 seconds per word.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx46">`, preview text "Into the Words Next". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Text Zoom Through".

### JavaScript — `FX[46]` from `site/fx.js`

```js
46(s,x,card){const ws=words(x);let i=0;const show=()=>{const e=el('div','zt');e.textContent=ws[i%ws.length];if(i%2)e.style.color='var(--a)';s.append(e);setTimeout(()=>e.remove(),1500);i++};show();card._timers.push(setInterval(show,1150))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx46` rules from `site/fx.css`

```css
.fx46 .zt{position:absolute;font-weight:900;font-size:15cqw;color:#111;animation:zt 1.5s both cubic-bezier(.6,0,.9,.5)}
@keyframes zt{0%{transform:scale(.2);opacity:0}22%{transform:scale(1);opacity:1;animation-timing-function:linear}60%{transform:scale(1.15);opacity:1;animation-timing-function:cubic-bezier(.7,0,1,.6)}100%{transform:scale(16);opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #46
