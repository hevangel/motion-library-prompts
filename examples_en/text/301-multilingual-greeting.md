# 301 · Multilingual Greeting — 多語問候切換

"Hello" in different languages takes turns appearing, blurring in and out, while the frame's width smoothly follows along

- Component: Text (`text`)
- Timing: Switch, Loop · Idle
- Tech: GSAP
- Uses: Headline · Hero
- Style / keywords: Multilingual Greeting Hello Hello Switching International Multilingual Greeting Hello Languages Rotate Text Heading Animated Text
- Tag: GSAP
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Multilingual Greeting (多語問候切換)" motion effect: At the Hero heading position, "hello" in different languages is shown in rotation (Hello, Ni Hao, Konnichiwa, Bonjour, Hola, Annyeonghaseyo, Ciao), switching about every 1.6 seconds: the old word blurs and fades out upward, and the new word blurs in from below and becomes clear; because each word has a different length, the width of the container wrapping the text smoothly scales to the new word's width, so the small dot following behind it also moves smoothly instead of jumping instantly. (GSAP: first measure the new word's width (with a hidden measuring element), tween the container's width to the new width with power3.inOut; fade the text out and in with opacity, filter:blur and y)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx301">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Multilingual Greeting".

### JavaScript — `FX[301]` from `site/fx.js`

```js
301(s,x){const G=['Hello','你好','こんにちは','Bonjour','Hola','안녕하세요','Ciao'];const w=el('div','tx-ml');w.innerHTML='<span class="tx-mw"><b></b></span><i class="tx-dot"></i>';const box=w.querySelector('.tx-mw'),b=box.querySelector('b');s.append(w);let k=0;
  const ms=el('span','tx-me');w.append(ms);const meas=t=>{ms.textContent=t;return ms.offsetWidth};
  const go=()=>{const t=G[k++%G.length];const wd=meas(t);gsap.timeline().to(b,{opacity:0,filter:'blur(8px)',y:'-.3em',duration:.3,ease:'power2.in'}).add(()=>{b.textContent=t}).to(box,{width:wd,duration:.45,ease:'power3.inOut'},'<').fromTo(b,{opacity:0,filter:'blur(8px)',y:'.3em'},{opacity:1,filter:'blur(0px)',y:0,duration:.4,ease:'power2.out'})};
  b.textContent=G[0];requestAnimationFrame(()=>{box.style.width=meas(G[0])+'px';k=1});gsap.timeline({repeat:-1}).add(go,1.4).add(()=>{},1.6)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx301` rules from `site/fx.css`

_No dedicated `.fx301` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #301
