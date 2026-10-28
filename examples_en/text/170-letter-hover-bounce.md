# 170 · Letter Hover Bounce — 逐字跳動

When you glide over text, each letter you touch bounces once on its own

- Component: Text (`text`)
- Timing: Hover · Click
- Tech: CSS
- Uses: Headline · Hero, Emphasis
- Style / keywords: text character-by-character bouncing bounce playful letter bounce hover playful hover hover mouse-enter hover-over interaction
- Tag: CSS keyframes
- Example text: "HOVER ME Try It" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Letter Hover Bounce (逐字跳動)" motion effect: Title text is split into individual characters. Whichever character the cursor glides over, that character bounces up once and briefly turns into an accent color (about 0.5 seconds, elastic), and a fast horizontal sweep of the cursor forms a wave in succession; each character's animation is independent, and it returns to its original position when finished. (How to: wrap each character in an inline-block span, on pointerenter remove and re-add the animation class to replay it, remove it on animationend; keyframes at 30% translateY(-35%) scale(1.12))
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx170">`, preview text "HOVER ME Try It". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Letter Hover Bounce".

### JavaScript — `FX[170]` from `site/fx.js`

```js
170(s,x,card){x=x.replace(/ /g,'\u00a0');const t=split(x,Math.min(11,70/chars(x).length));t.classList.add('lw');s.append(t);const cs=[...t.querySelectorAll('.c')];
  const jump=c=>{c.classList.remove('j');void c.offsetWidth;c.classList.add('j')};cs.forEach(c=>{c.addEventListener('pointerenter',()=>jump(c));c.addEventListener('animationend',()=>c.classList.remove('j'))});
  let real=false;t.addEventListener('pointerenter',()=>real=true);t.addEventListener('pointerleave',()=>real=false);card._timers.push(setInterval(()=>{if(!real)cs.forEach((c,i)=>setTimeout(()=>jump(c),i*60))},2200))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx170` rules from `site/fx.css`

_No dedicated `.fx170` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #170
