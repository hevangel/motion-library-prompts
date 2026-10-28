# 048 · Huge Text Scroll — 巨字滑過

Huge text crosses the screen, one fast and one slow

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Background Decoration
- Style / keywords: Flowing Background
- Tag: Background·Distant View
- Example text: "Night in Taipei" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Huge Text Scroll (巨字滑過)" motion effect: Text at an oversized scale (larger than the frame) continuously drifts slowly from right to left across the frame, while a thin strip at the bottom carries small text sliding faster in the opposite direction. The large text takes about 9 seconds per cycle, giving a distant background feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx48">`, preview text "Night in Taipei". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Huge Text Scroll".

### JavaScript — `FX[48]` from `site/fx.js`

```js
48(s,x){s.append(mqRow(rep(x+'・',3),34,9,false,'font-weight:900;line-height:1;color:#fff'));const sm=mqRow(rep(x+'・',10),4,5,true);sm.className+=' small';s.append(sm)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx48` rules from `site/fx.css`

```css
.fx48 .big{font-weight:900;font-size:34cqw;line-height:1;color:#fff}
.fx48 .small{position:absolute;bottom:3cqw;left:0;font-weight:900;font-size:4cqw;background:var(--a);color:#111;padding:.3cqw 0}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #48
