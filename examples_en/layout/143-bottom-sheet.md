# 143 · Bottom Sheet — 底部抽屜

The background dims and a menu slides up from the bottom with a little spring

- Component: Layout · Pages (`layout`)
- Timing: Entrance, Exit
- Tech: GSAP
- Uses: App Interface, UI Interaction
- Style / keywords: Bottom Sheet Bottom Menu Popup Share Action Menu Bottom Sheet Action Sheet Drawer Modal App Mobile Mobile Device Micro-interaction Mobile App Micro-interaction
- Tag: Bottom sheet
- Example text: "Share to" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Bottom Sheet (底部抽屜)" motion effect: After tapping an action such as 'Share,' the screen gets a translucent overlay that gradually darkens, and a menu panel slides up from the bottom of the screen with a slight bounce (about 0.6 seconds). The panel has a small handle at its top, and the options inside fade in in sequence from 8px below; on close, the panel slides quickly down and out (about 0.35 seconds, accelerating) and the overlay fades out. (GSAP: panel yPercent 100→0, ease back.out(1.1); options stagger 0.06; closing uses power2.in; in a real app, the user can drag the handle down to close it)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx143">`, preview text "Share to". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Bottom Sheet".

### JavaScript — `FX[143]` from `site/fx.js`

```js
143(s,x){const ph=phone(s);const list=el('div','pl');for(let i=0;i<6;i++)list.append(mrow(i));const bd=el('i','bd');const sh=el('div','sh2');sh.innerHTML='<i class="hd3"></i><b></b>'+[0,1,2].map(()=>'<div class="op"><i></i><span></span></div>').join('');sh.querySelector('b').textContent=x;ph.append(list,bd,sh);
  gsap.timeline({repeat:-1,repeatDelay:.5}).set(sh,{yPercent:100},0).set(bd,{opacity:0},0).to(bd,{opacity:.55,duration:.35},.4).to(sh,{yPercent:0,duration:.6,ease:'back.out(1.1)'},.4)
    .fromTo(sh.querySelectorAll('.op'),{y:8,opacity:0},{y:0,opacity:1,duration:.4,stagger:.06,ease:'power2.out'},.65).to(sh,{yPercent:100,duration:.35,ease:'power2.in'},'+=1.6').to(bd,{opacity:0,duration:.3},'<')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx143` rules from `site/fx.css`

_No dedicated `.fx143` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #143
