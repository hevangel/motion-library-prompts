# 074 · Highlight Text — 螢光筆

A highlighter sweeps across behind the text

- Component: Text (`text`)
- Timing: Entrance
- Tech: CSS
- Uses: Emphasis
- Style / keywords: Textured Fill
- Tag: Emphasis·Commentary
- Example text: "Power of Words" (stage background: acc)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Highlight Text (螢光筆)" motion effect: For text on a card, a highlighter line sweeps from left to right behind the lower half of the letters, lingers, then fades out. The sweep takes about 1 second, the whole cycle about 3 seconds, with an emphasis-and-commentary feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx74">`, preview text "Power of Words". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Highlight Text".

### JavaScript — `FX[74]` from `site/fx.js`

```js
74(s,x){const p=el('div','panel');p.append(T(x,Math.min(9,64/chars(x).length)));s.append(p)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx74` rules from `site/fx.css`

```css
.fx74 .panel{background:#fff;padding:3cqw 4cqw;border-radius:1cqw}
.fx74 .t{color:#111;position:relative;z-index:1}
.fx74 .t::before{content:"";position:absolute;left:-1%;bottom:4%;height:42%;width:0;background:var(--l);z-index:-1;animation:hlt 3s infinite cubic-bezier(.6,0,.3,1)}
@keyframes hlt{0%,10%{width:0}45%,85%{width:102%}100%{width:102%;opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #74
