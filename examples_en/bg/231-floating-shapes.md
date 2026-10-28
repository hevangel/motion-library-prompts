# 231 · Floating Shapes — 漂浮幾何

Geometric shapes such as circles, squares, triangles and rings randomly float and rotate slowly in the background

- Component: Background · Ambience (`bg`)
- Timing: Loop · Idle, Entrance
- Tech: GSAP
- Uses: Background Decoration, Headline · Hero
- Style / keywords: Floating Geometric Shapes Random Decoration Background Floating Shapes Geometric Random Decoration Background Atmosphere
- Tag: repeatRefresh
- Example text: "Shapes" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Floating Shapes (漂浮幾何)" motion effect: More than ten simple geometric shapes are scattered in the background: solid circles, rounded squares, triangles, hollow rings and crosses, of different sizes; on entrance each appears in sequence with an elastic scale-up, after which each shape continuously drifts slowly in a random direction and rotates, choosing a new random target on each round trip, looking natural and non-repetitive; the title sits in the middle. (GSAP: for each shape, gsap.to on x / y / rotation uses "random(-40,40)" strings, with duration random(3,6), ease sine.inOut, repeat:-1, yoyo:true, repeatRefresh:true; entrance with gsap.from scale:0 paired with back.out)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx231">`, preview text "Shapes". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Floating Shapes".

### JavaScript — `FX[231]` from `site/fx.js`

```js
231(s,x){const w=el('div','abs bga-fs');const K=['c','q','t','ring','c','q','t','ring','c','plus','q','plus'];const es=K.map((k,i)=>{const e=el('i','bga-'+k);e.style.cssText=`left:${rnd(4,90)}%;top:${rnd(6,82)}%;--z:${rnd(3,7)}cqw;color:${i%3?'var(--a)':GC[i%5]}`;w.append(e);return e});s.append(w,T(x,Math.min(12,56/chars(x).length)));
  es.forEach(e=>{gsap.to(e,{x:'random(-40,40)',y:'random(-30,30)',rotation:'random(-120,120)',duration:'random(3,6)',ease:'sine.inOut',repeat:-1,yoyo:true,repeatRefresh:true});gsap.from(e,{scale:0,opacity:0,duration:.8,ease:'back.out(2)',delay:rnd(0,.8)})})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx231` rules from `site/fx.css`

```css
.fx222 .t,.fx224 .t,.fx227 .t,.fx231 .t{color:#fff;z-index:1;text-shadow:0 .4cqw 2cqw #0006}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #231
