# 047 · Text Squeeze — 擠壓彈跳

Squashes flat like rubber, then swaps the word

- Component: Text (`text`)
- Timing: Switch
- Tech: CSS
- Uses: Emphasis, Transitions
- Style / keywords: Per-Character Motion
- Tag: Elastic·Switching
- Example text: "Rebound Elastic" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Text Squeeze (擠壓彈跳)" motion effect: The text squashes flat into a line like rubber, then springs up tall and rebounds into place; after pausing, it squashes flat again, swapping to the next word at its flattest point. About 1.5 seconds per cycle, an elastic switch.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx47">`, preview text "Rebound Elastic". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Text Squeeze".

### JavaScript — `FX[47]` from `site/fx.js`

```js
47(s,x){const ws=words(x);let i=0;const e=el('div','sq');e.textContent=ws[0];e.addEventListener('animationiteration',()=>{i++;e.textContent=ws[i%ws.length];e.style.color=i%2?'var(--a)':'#fff'});s.append(e)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx47` rules from `site/fx.css`

```css
.fx47 .sq{font-weight:900;font-size:17cqw;color:#fff;transform-origin:50% 90%;animation:sq 1.5s infinite}
@keyframes sq{0%{transform:scale(1.45,.12)}18%{transform:scale(.82,1.28)}32%{transform:scale(1.1,.9)}44%,80%{transform:none}100%{transform:scale(1.45,.12)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #47
