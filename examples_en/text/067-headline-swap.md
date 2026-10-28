# 067 · Headline Swap — 標題切換

News headlines swap one for another

- Component: Text (`text`)
- Timing: Switch
- Tech: CSS
- Uses: Numbers & Data, Transitions
- Style / keywords: Text Switching
- Tag: Breaking News·Commentary
- Example text: "Fully Free Live Tonight 3 Days Only" (stage background: acc)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Headline Swap (標題切換)" motion effect: A 'Breaking News' label stays fixed on the left, while news headlines in the frame on the right slide in from below as the old headline slides out upward, one replacing another. A new headline about every 1.6 seconds.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx67">`, preview text "Fully Free Live Tonight 3 Days Only". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Headline Swap".

### JavaScript — `FX[67]` from `site/fx.js`

```js
67(s,x,card){const w=el('div','w');w.innerHTML='<div class="lab">快訊</div>';const box=el('div','box');w.append(box);s.append(w);const ws=words(x);let i=0;const show=()=>{box.querySelector('.hl:not(.out)')?.classList.add('out');const h=el('div','hl');h.textContent=ws[i++%ws.length];box.append(h);setTimeout(()=>{box.querySelectorAll('.out').forEach(o=>o.remove())},500)};show();card._timers.push(setInterval(show,1600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx67` rules from `site/fx.css`

```css
.fx67 .w{display:flex;align-items:stretch;width:84%;height:22cqw}
.fx67 .lab{background:#fff;color:#111;font-weight:900;font-size:8cqw;display:grid;place-items:center;padding:0 3cqw}
.fx67 .box{flex:1;background:#2b2b2b;position:relative;overflow:hidden}
.fx67 .hl{position:absolute;inset:0;display:flex;align-items:center;padding-left:3cqw;font-weight:900;font-size:8.5cqw;color:var(--a);animation:hl .55s both cubic-bezier(.2,.9,.3,1)}
.fx67 .hl.out{animation:hlo .4s both}
@keyframes hl{from{transform:translateY(100%)}to{transform:none}}
@keyframes hlo{to{transform:translateY(-100%)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #67
