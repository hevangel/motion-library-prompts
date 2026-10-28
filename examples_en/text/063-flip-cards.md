# 063 · Flip Cards — 翻卡

Cards flip over one by one to change the text

- Component: Text (`text`)
- Timing: Switch
- Tech: CSS
- Uses: Transitions
- Style / keywords: Text Switching
- Tag: Switching·Announcement
- Example text: "Sleepless Night" (stage background: acc)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Flip Cards (翻卡)" motion effect: Each character is a card that flips in sequence around the Y axis, front and back in contrasting color schemes; after flipping into another set of text it lingers, then flips back. About 3.4 seconds per cycle, with an announcement-switching feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx63">`, preview text "Sleepless Night". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Flip Cards".

### JavaScript — `FX[63]` from `site/fx.js`

```js
63(s,x){const w=el('div','w');const a=chars(x).slice(0,4);const b=x==='夜未眠'?[...'月光下']:[...a].reverse();a.forEach((c,i)=>{const d=el('div','cd');d.style.setProperty('--i',i);d.innerHTML=`<b>${c}</b><b>${b[i]}</b>`;w.append(d)});s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx63` rules from `site/fx.css`

```css
.fx63 .w{display:flex;gap:2cqw}
.fx63 .cd{width:16cqw;height:19cqw;position:relative;transform-style:preserve-3d;animation:fc 3.4s calc(var(--i)*.16s) infinite}
.fx63 .cd b{position:absolute;inset:0;display:grid;place-items:center;font-weight:900;font-size:12cqw;background:#fff;color:#111;border-radius:1.4cqw;backface-visibility:hidden;box-shadow:0 .6cqw 1.4cqw #0003}
.fx63 .cd b+b{transform:rotateY(180deg);background:#111;color:var(--a)}
@keyframes fc{0%,25%{transform:rotateY(0)}42%,75%{transform:rotateY(180deg)}92%,100%{transform:rotateY(360deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #63
