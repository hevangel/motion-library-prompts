# 043 · Text Stamp — 印章

Stamped on one by one like a seal

- Component: Text (`text`)
- Timing: Entrance
- Tech: CSS
- Uses: Emphasis
- Style / keywords: Impact Entrance Canva Style Canva Stomp Smash
- Tag: Announcement·Decision
- Example text: "Approved" (stage background: cream)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Text Stamp (印章)" motion effect: Two stamped texts with thick borders slam down diagonally with a bang from 2.4x size, settling after shrinking back slightly, the stamp faces with a slightly distressed texture, the two stamps coming down in sequence. About 2.8 seconds per cycle.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx43">`, preview text "Approved". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Text Stamp".

### JavaScript — `FX[43]` from `site/fx.js`

```js
43(s,x){[[x,'-9deg','18%','24%','0s'],['核准','7deg','55%','46%','.55s']].forEach(([w,r,l,t,d])=>{const e=el('div','st');e.textContent=w;e.style.cssText+=`;left:${l};top:${t};--r:${r};--d:${d}`;s.append(e)})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx43` rules from `site/fx.css`

```css
.fx43 .st{position:absolute;font-weight:900;color:var(--a);border:.7cqw solid var(--a);border-radius:1.4cqw;padding:.4cqw 2.4cqw;font-size:8cqw;animation:stamp 2.8s var(--d) infinite both;-webkit-mask:repeating-radial-gradient(circle at 30% 40%,#000 0 3px,#000c 3px 4px)}
@keyframes stamp{0%{opacity:0;transform:rotate(var(--r)) scale(2.4)}9%{opacity:1;transform:rotate(var(--r)) scale(.93)}13%,82%{opacity:1;transform:rotate(var(--r)) scale(1)}95%,100%{opacity:0;transform:rotate(var(--r))}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #43
