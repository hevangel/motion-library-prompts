# 019 · Text Flag — 文字旗幟

Text flutters like a flag

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Emphasis
- Style / keywords: Letter-by-Letter Motion
- Tag: Powerful · Cheering
- Example text: "Fluttering Flag" (stage background: cream)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Text Flag (文字旗幟)" motion effect: There is a flagpole at the left side of the text; each character flips in 3D and tilts in sequence, forming a wave like a flag fluttering in the wind. About 1.3 seconds per wave, with a powerful cheering feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx19">`, preview text "Fluttering Flag". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Text Flag".

### JavaScript — `FX[19]` from `site/fx.js`

```js
19(s,x){const w=el('div','w');w.append(el('div','pole'),split(x));s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx19` rules from `site/fx.css`

```css
.fx19 .w{display:flex;align-items:center;gap:2cqw}
.fx19 .pole{width:1cqw;height:34cqw;background:#333;border-radius:2px;align-self:center}
.fx19 .c{animation:flag 1.3s calc(var(--i)*-.17s) ease-in-out infinite;transform-origin:0 50%}
.fx19 .c:nth-child(even){color:var(--a)}
@keyframes flag{0%,100%{transform:rotateY(0) skewY(0) translateY(0)}50%{transform:rotateY(38deg) skewY(-9deg) translateY(-7%)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #19
