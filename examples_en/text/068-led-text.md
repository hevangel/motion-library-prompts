# 068 · LED Text — LED 看板

Electronic text made of dots

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Numbers & Data, Background Decoration
- Style / keywords: Flowing Background
- Tag: Retro·Tech
- Example text: "Latest News •" (stage background: cream)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"LED Text (LED 看板)" motion effect: Text made of a dot matrix like an electronic billboard, continuously scrolling from right to left, with clear contrast between lit and unlit dots. Medium scrolling speed, with a retro tech feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx68">`, preview text "Latest News •". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "LED Text".

### JavaScript — `FX[68]` from `site/fx.js`

```js
68(s,x,card){const cv=el('canvas');s.append(cv);const R=16;const off=document.createElement('canvas');const oc=off.getContext('2d');oc.font=`900 ${R-2}px "Noto Sans JP",sans-serif`;const tw=Math.ceil(oc.measureText(x).width)+R;off.width=tw;off.height=R;oc.font=`900 ${R-2}px "Noto Sans JP",sans-serif`;oc.fillStyle='#fff';oc.textBaseline='middle';oc.fillText(x,0,R/2+1);const px=oc.getImageData(0,0,tw,R).data;const on=(cx,cy)=>px[(cy*tw+((cx%tw)+tw)%tw)*4+3]>110;const ctx=cv.getContext('2d');
  ticks.set(card,t=>{const W=s.offsetWidth,H=s.offsetHeight;if(!W)return;const dpr=devicePixelRatio||1;if(cv.width!==W*dpr){cv.width=W*dpr;cv.height=H*dpr}const cell=cv.height/(R+6);const cols=Math.ceil(cv.width/cell);const sh=Math.floor(t*14);ctx.fillStyle='#161616';ctx.fillRect(0,0,cv.width,cv.height);for(let cy=0;cy<R;cy++)for(let cx=0;cx<cols;cx++){const o=on(cx+sh,cy);ctx.fillStyle=o?getComputedStyle(s).getPropertyValue('--a')||'#d9f53a':'#2a2a2a';if(o)ctx.fillStyle='#d9f53a';ctx.beginPath();ctx.arc(cx*cell+cell/2,(cy+3)*cell+cell/2,cell*.38,0,7);ctx.fill()}})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx68` rules from `site/fx.css`

```css
.fx68 canvas{position:absolute;inset:0;width:100%;height:100%}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #68
