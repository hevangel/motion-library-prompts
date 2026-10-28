# 025 · Karaoke Ball — 卡拉OK小球

A small ball bounces, lighting up each character

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Emphasis
- Style / keywords: Letter-by-Letter Motion
- Tag: Song · Subtitles
- Example text: "Bouncing Ball" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Karaoke Ball (卡拉OK小球)" motion effect: A small glowing ball jumps to the right above the text, character by character; each time it lands on a character, that character lights up from dim with a glow, like karaoke subtitles. About 0.38 seconds per character; after jumping through the whole line, it starts again.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx25">`, preview text "Bouncing Ball". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Karaoke Ball".

### JavaScript — `FX[25]` from `site/fx.js`

```js
25(s,x,card){const w=el('div','w');const t=split(x);const ball=el('div','ball');w.append(t,ball);s.append(w);const cs=[...t.querySelectorAll('.c')];const per=.38,n=cs.length,cyc=n*per+1.2;
  ticks.set(card,tt=>{const ph=tt%cyc;const k=ph/per;const idx=Math.min(n-1,Math.floor(k));const fr=Math.min(1,k-idx);const c=cs[idx];if(!c)return;const cx=c.offsetLeft+c.offsetWidth/2;ball.style.left=cx+'px';ball.style.transform=`translateY(${-Math.sin(Math.PI*fr)*w.offsetHeight*.35}px)`;cs.forEach((e,i)=>e.classList.toggle('on',ph<n*per+1?i<=idx&&(i<idx||fr>.5):false))})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx25` rules from `site/fx.css`

```css
.fx25 .w{position:relative}
.fx25 .c{color:#555;transition:color .15s}
.fx25 .c.on{color:#fff;text-shadow:0 0 8px var(--a)}
.fx25 .ball{position:absolute;width:3cqw;height:3cqw;border-radius:50%;background:var(--a);top:-4cqw;margin-left:-1.5cqw;box-shadow:0 0 10px var(--a)}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #25
