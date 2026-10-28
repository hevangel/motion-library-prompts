# 224 · Bokeh Lights — 散景光點

Soft-focus light spots of different sizes slowly float upward, fading in and out

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Background Decoration, Headline · Hero
- Style / keywords: Bokeh Light Spots Soft Focus Bubbles Floating Rise Dreamy Bokeh Lights Bubbles Floating Blur Background Atmosphere
- Tag: CSS blur
- Example text: "Bokeh" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Bokeh Lights (散景光點)" motion effect: In the background float more than ten circular light spots of different sizes with a soft-focus blur; each slowly floats upward from below at a different speed (about 7-14 seconds), drifting slightly left and right along the way, fading in as it appears and fading out near the top, each with different opacity, creating a dreamy, warm atmosphere; the title in the center stays clear. (CSS: each light spot uses CSS variables to set its size, horizontal position, duration, negative animation-delay and offset, with filter:blur, and keyframes control translate and opacity)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx224">`, preview text "Bokeh". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Bokeh Lights".

### JavaScript — `FX[224]` from `site/fx.js`

```js
224(s,x){const w=el('div','abs bga-bk');for(let i=0;i<16;i++){const b=el('i');const z=rnd(5,16);b.style.cssText=`--z:${z}cqw;left:${rnd(-5,95)}%;--d:${rnd(7,14).toFixed(1)}s;--dl:${-rnd(0,14).toFixed(1)}s;--o:${rnd(.25,.7).toFixed(2)};--dx:${rnd(-8,8).toFixed(1)}cqw;background:${i%3?'var(--a)':GC[i%5]}`;w.append(b)}s.append(w,T(x,Math.min(12,56/chars(x).length)))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx224` rules from `site/fx.css`

```css
.fx222 .t,.fx224 .t,.fx227 .t,.fx231 .t{color:#fff;z-index:1;text-shadow:0 .4cqw 2cqw #0006}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #224
