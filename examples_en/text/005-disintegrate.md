# 005 · Disintegrate — 粒子消散

Text dissolves into particles

- Component: Text (`text`)
- Timing: Exit
- Tech: CSS
- Uses: Transitions
- Style / keywords: Dissipating Exit
- Tag: Annihilation · Drama
- Example text: "Vanish" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Disintegrate (粒子消散)" motion effect: From left to right, each character blurs in turn, drifts up and to the right, and fades out, while many small square particles appear around it and float away; after disappearing, the text re-emerges. About 3 seconds per cycle, dramatic.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx5">`, preview text "Vanish". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Disintegrate".

### JavaScript — `FX[5]` from `site/fx.js`

```js
5(s,x){const w=el('div');w.style.position='relative';const t=split(x,18);w.append(t);for(let i=0;i<46;i++){const p=el('i','p');p.style.left=rnd(5,95)+'%';p.style.top=rnd(10,90)+'%';p.style.setProperty('--dx',rnd(5,40)+'cqw');p.style.setProperty('--dy',rnd(-25,5)+'cqw');p.style.animationDelay=(parseFloat(p.style.left)/100*.5)+'s';w.append(p)}s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx5` rules from `site/fx.css`

```css
.fx5 .c{animation:dis 3s calc(var(--i)*.25s) infinite}
.fx5 .c:nth-child(1){color:var(--a)}
.fx5 .p{position:absolute;width:1.2cqw;height:1.2cqw;background:var(--a);opacity:0;animation:prt 3s infinite}
@keyframes dis{0%,25%{opacity:1;filter:none;transform:none}60%{opacity:0;filter:blur(6px);transform:translate(12%,-25%) scale(1.25)}85%{opacity:0;transform:none;filter:blur(6px)}100%{opacity:1;filter:none}}
@keyframes prt{0%,25%{opacity:0;transform:none}35%{opacity:1}70%{opacity:0;transform:translate(var(--dx),var(--dy))}100%{opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #5
