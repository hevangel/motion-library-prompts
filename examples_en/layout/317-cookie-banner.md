# 317 · Cookie Banner — Cookie 同意橫幅

A cookie consent card pops up at the bottom, the cookie icon wiggles; after pressing a button it shrinks back and slides away

- Component: Layout · Pages (`layout`)
- Timing: Entrance, Exit
- Tech: GSAP
- Uses: UI Interaction
- Style / keywords: Cookie Consent Banner Privacy GDPR Notice Consent Banner Privacy Notice Layout Page
- Tag: GSAP
- Example text: "This site uses cookies" (stage background: dark)
- Added: 2026-10-21

**AI prompt (English copy format):**

```text
"Cookie Banner (Cookie 同意橫幅)" motion effect: A cookie consent card at the bottom of the website: when entering the page, the card slides up from below with a bounce-back, and the cookie icon on the left elastically straightens and enlarges from a small, tilted state; inside the card there is a heading, a brief description and two buttons (Essential only / Accept all); when either button is pressed, the button presses down lightly, and the card then slides down and out and fades away. (GSAP: the card fromTo yPercent 140 → 0, ease back.out(1.4); the icon rotation −40 → 0, scale .4 → 1, ease elastic.out; on close, yPercent → 140, power3.in)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx317">`, preview text "This site uses cookies". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Cookie Banner".

### JavaScript — `FX[317]` from `site/fx.js`

```js
317(s,x,card){const f=lyPage(s);f.insertAdjacentHTML('beforeend','<div class="pg-pc"><b>首頁</b><i class="ly-bl"></i><i class="ly-bl s"></i><i class="ly-bl"></i></div><div class="pg-ck"><span class="pg-cki">🍪</span><p><b></b><br><small>我們使用 Cookie 改善瀏覽體驗。</small></p><div><button class="no">只用必要</button><button class="ok">全部接受</button></div></div>');f.querySelector('.pg-ck b').textContent=x;const ck=f.querySelector('.pg-ck');let real=0;
  const show=()=>{gsap.fromTo(ck,{yPercent:140,opacity:0},{yPercent:0,opacity:1,duration:.6,ease:'back.out(1.4)'});gsap.fromTo(ck.querySelector('.pg-cki'),{rotation:-40,scale:.4},{rotation:0,scale:1,duration:.7,ease:'elastic.out(1,.5)',delay:.25})};
  const hide=b=>{gsap.timeline().to(b,{scale:.92,duration:.08}).to(b,{scale:1,duration:.15}).to(ck,{yPercent:140,opacity:0,duration:.4,ease:'power3.in'})};
  ck.querySelectorAll('button').forEach(b=>b.onclick=()=>{real=Date.now();hide(b);setTimeout(show,1800)});show();card._timers.push(setInterval(()=>{if(Date.now()-real<5000)return;hide(ck.querySelector('.ok'));setTimeout(show,1400)},3600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx317` rules from `site/fx.css`

_No dedicated `.fx317` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #317
