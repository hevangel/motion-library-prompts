# 017 · Water Reflection — 水面倒影

A reflection swaying on the water's surface

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Headline · Hero
- Style / keywords: Textured Fill
- Tag: Nightscape · Calm
- Example text: "Water" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Water Reflection (水面倒影)" motion effect: Below the text is a thin horizontal line; beneath the line is an upside-down reflection that is semi-transparent and fades out as it goes down, continually tilting and swaying side to side like ripples on water, while the text above also floats slightly. A calm night-scene feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx17">`, preview text "Water". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Water Reflection".

### JavaScript — `FX[17]` from `site/fx.js`

```js
17(s,x){const w=el('div','w');const a=T(x,18);const r=T(x,18);r.classList.add('ref');w.append(a,el('div','line'),r);s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx17` rules from `site/fx.css`

```css
.fx17 .w{display:flex;flex-direction:column;align-items:center}
.fx17 .t{color:#fff;animation:bob 3s ease-in-out infinite}
.fx17 .line{width:70cqw;height:1px;background:linear-gradient(90deg,transparent,#fff8,transparent)}
.fx17 .ref{transform:scaleY(-1);opacity:.45;color:var(--a);-webkit-mask:linear-gradient(transparent 20%,#000);mask:linear-gradient(transparent 20%,#000);animation:rip 2.2s ease-in-out infinite;filter:blur(.6px)}
@keyframes bob{0%,100%{transform:none}50%{transform:translateY(-3%)}}
@keyframes rip{0%,100%{transform:scaleY(-1) skewX(0)}25%{transform:scaleY(-.92) skewX(7deg) translateX(1%)}75%{transform:scaleY(-1.04) skewX(-7deg) translateX(-1%)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #17
