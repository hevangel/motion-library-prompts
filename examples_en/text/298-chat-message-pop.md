# 298 · Chat Message Pop — 聊天訊息出現

The other person first shows the three "typing" dots, which then turn into a message, and then your reply pops out

- Component: Text (`text`)
- Timing: Entrance, Loop · Idle
- Tech: GSAP
- Uses: App Interface, UI Interaction
- Style / keywords: Chat Message Chat Box Bubble Typing Typing Indicator Customer Service Chat Bubble Typing Indicator Message Pop Text Heading Animated Text
- Tag: GSAP timeline
- Example text: "Yes! Feel free to ask 😊" (stage background: dark)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Chat Message Pop (聊天訊息出現)" motion effect: Simulate a chat interface: the other person's chat bubble first appears on the left, containing three dots bouncing up and down in sequence (typing…); after about 1.4 seconds the bubble turns into a message (for example "Are you there? I have a question~") and bounces lightly; then your reply bubble pops out on the right in the accent color (appearing by enlarging from the bottom-right corner); after lingering, they move up and fade out together, then start again. (GSAP timeline: bubbles scale 0 → 1, transform-origin set at the corner of the bubble's tail, ease back.out; the three dots use CSS keyframes with staggered animation-delay)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx298">`, preview text "Yes! Feel free to ask 😊". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Chat Message Pop".

### JavaScript — `FX[298]` from `site/fx.js`

```js
298(s,x){const w=el('div','tx-ch');w.innerHTML='<div class="tx-b them"></div><div class="tx-b me"></div>';const me=w.querySelector('.me'),ty=w.querySelector('.them');me.textContent=x;s.append(w);
  const reset=()=>{ty.classList.remove('msg');ty.innerHTML='<i></i><i></i><i></i>';gsap.set([ty,me],{y:0,opacity:1});gsap.set(me,{scale:0,opacity:0})};reset();
  gsap.timeline({repeat:-1,repeatDelay:.6}).call(reset).fromTo(ty,{scale:0},{scale:1,transformOrigin:'0% 100%',duration:.35,ease:'back.out(2)'})
    .call(()=>{ty.classList.add('msg');ty.textContent='在嗎？想問一下～'},null,'+=1.4').fromTo(ty,{scale:.85},{scale:1,duration:.3,ease:'back.out(3)'})
    .fromTo(me,{scale:0,opacity:0},{scale:1,opacity:1,transformOrigin:'100% 100%',duration:.4,ease:'back.out(2)',immediateRender:false},'+=.7')
    .to([ty,me],{opacity:0,y:-10,duration:.4,stagger:.08},'+=1.8')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx298` rules from `site/fx.css`

_No dedicated `.fx298` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #298
