# 037 · Letter Assemble — 文字聚集

Scattered text gathers together

- Component: Text (`text`)
- Timing: Entrance
- Tech: CSS
- Uses: Headline · Hero, Logo · Brand
- Style / keywords: Impact Entrance
- Tag: Headline · Intro
- Example text: "Gather" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Letter Assemble (文字聚集)" motion effect: Each character of the text flies in from all over the screen with rotation, blur and enlargement, gathering one by one into its correct position and sharpening into focus, pauses, then scatters apart again. About 3.2 seconds per cycle, with a title-intro feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx37">`, preview text "Gather". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Letter Assemble".

### JavaScript — `FX[37]` from `site/fx.js`

```js
37(s,x){const t=split(x);t.querySelectorAll('.c').forEach(c=>{c.style.setProperty('--dx',rnd(-35,35)+'cqw');c.style.setProperty('--dy',rnd(-22,22)+'cqw');c.style.setProperty('--r',rnd(-180,180)+'deg')});s.append(t)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx37` rules from `site/fx.css`

```css
.fx37 .c{animation:asm 3.2s calc(var(--i)*.12s) infinite cubic-bezier(.2,.9,.3,1.1)}
.fx37 .c:nth-child(odd){color:var(--a)}
@keyframes asm{0%{transform:translate(var(--dx),var(--dy)) rotate(var(--r)) scale(1.6);opacity:0;filter:blur(6px)}12%{opacity:.6}50%,82%{transform:none;opacity:1;filter:none}100%{transform:translate(var(--dx),var(--dy)) rotate(var(--r)) scale(1.6);opacity:0;filter:blur(6px)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #37
