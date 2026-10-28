# 297 · Strike & Rewrite — 劃掉改寫

A word is struck through with one stroke, and a new word is written out above it in handwriting, one character at a time

- Component: Text (`text`)
- Timing: Switch
- Tech: GSAP
- Uses: Emphasis, Headline · Hero
- Style / keywords: Strike Through Strikethrough Rewrite Correction Handwriting Copy Strikethrough Rewrite Correction Copywriting Text Heading Animated Text
- Tag: GSAP timeline
- Example text: "Cheap Affordable" (stage background: dark)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Strike & Rewrite (劃掉改寫)" motion effect: A word originally in the copy (for example "cheap") is first struck through from left to right by a slightly slanted thick line, and the original word fades; then below it, a new word (for example "affordable") pops out one character at a time in a handwritten-style font in the accent color, as if someone is revising the copy by hand, to emphasize the better wording. (GSAP timeline: the strikethrough element scaleX 0 → 1, transform-origin:left; the original word's opacity drops to 0.4; the new word is split into characters with SplitText and pops out in sequence from below with back.out)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx297">`, preview text "Cheap Affordable". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Strike & Rewrite".

### JavaScript — `FX[297]` from `site/fx.js`

```js
297(s,x){const ws=words(x);const a=ws[0]||'便宜',bw=ws[1]||'實惠';const w=el('div','tx-rw');w.innerHTML='<span class="tx-o"><b></b><i class="tx-st"></i></span><span class="tx-n"></span>';w.querySelector('.tx-o b').textContent=a;const nw=w.querySelector('.tx-n');nw.textContent=bw;w.style.fontSize=Math.min(12,50/Math.max(chars(a).length,chars(bw).length))+'cqw';s.append(w);
  const sp=SplitText.create(nw,{type:'chars'});const st=w.querySelector('.tx-st'),ob=w.querySelector('.tx-o b');
  gsap.timeline({repeat:-1,repeatDelay:.6}).set([st,sp.chars,ob],{clearProps:'all'}).set(st,{scaleX:0}).set(sp.chars,{opacity:0,y:'.3em'}).to(st,{scaleX:1,duration:.45,ease:'power2.inOut'},.6).to(ob,{opacity:.4,duration:.3},'<.2').to(sp.chars,{opacity:1,y:0,duration:.25,stagger:.12,ease:'back.out(3)'}).to(w,{opacity:0,duration:.4},'+=1.6').set(w,{opacity:1})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx297` rules from `site/fx.css`

_No dedicated `.fx297` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #297
