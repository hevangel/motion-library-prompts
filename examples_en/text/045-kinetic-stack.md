# 045 · Kinetic Stack — 動態堆疊

Words fly in one by one and stack up

- Component: Text (`text`)
- Timing: Entrance
- Tech: CSS
- Uses: Headline · Hero
- Style / keywords: Impact Entrance
- Tag: MV·Lyrics
- Example text: "Through the Night Let's Go" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Kinetic Stack (動態堆疊)" motion effect: Three lines of words fly in with rotation from the left, right, and below respectively, stacking in sequence into a centered layout, each line at a different font size with the middle line in an accent color; after lingering, they fade out together. About 3.4 seconds per cycle, with an MV lyric feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx45">`, preview text "Through the Night Let's Go". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Kinetic Stack".

### JavaScript — `FX[45]` from `site/fx.js`

```js
45(s,x){const w=el('div','w');const ws=words(x);const dirs=[['-60cqw','0','-20deg'],['60cqw','0','15deg'],['0','40cqw','0deg'],['0','-40cqw','8deg']];ws.forEach((t,i)=>{const d=el('div');d.textContent=t;d.style.setProperty('--i',i);d.style.fontSize=(i===ws.length-1?9:i===1?13:8)+'cqw';const [fx,fy,fr]=dirs[i%4];d.style.setProperty('--fx',fx);d.style.setProperty('--fy',fy);d.style.setProperty('--fr',fr);w.append(d)});s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx45` rules from `site/fx.css`

```css
.fx45 .w{display:flex;flex-direction:column;align-items:center;gap:.6cqw}
.fx45 .w div{font-weight:900;line-height:1.1;color:#fff;animation:ks 3.4s calc(var(--i)*.35s) infinite both cubic-bezier(.2,.9,.3,1.15)}
.fx45 .w div:nth-child(2){color:var(--a)}
@keyframes ks{0%{opacity:0;transform:translate(var(--fx),var(--fy)) rotate(var(--fr)) scale(1.4)}13%{opacity:1;transform:none}82%{opacity:1;transform:none}96%,100%{opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #45
