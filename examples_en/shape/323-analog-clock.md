# 323 · Analog Clock — 即時時鐘

An analog clock showing the current time, whose second hand ticks one mark each second with a slight bounce-back

- Component: Shapes · SVG (`shape`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Numbers & Data, UI Interaction
- Style / keywords: Clock Hands Second Hand Real-time Time Clock Analog Watch Time Real-time Graphics SVG
- Tag: JS rAF
- Example text: "Current Time" (stage background: dark)
- Added: 2026-10-21

**AI prompt (English copy format):**

```text
"Analog Clock (即時時鐘)" motion effect: An analog clock showing the actual current time: the dial has 60 tick marks (every 5th one thicker and longer), the hour and minute hands move continuously and smoothly, and the second hand, in the accent color, ticks one mark every second, slightly overshooting within about 0.15 seconds as it ticks and then bouncing back into place, like a real mechanical watch. (JS requestAnimationFrame: read the hours, minutes, seconds and milliseconds from Date and compute each hand's angle; second hand angle = (seconds − 1 + bounce-back curve(milliseconds/150)) × 6 degrees; SVG lines use transform rotate)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx323">`, preview text "Current Time". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Analog Clock".

### JavaScript — `FX[323]` from `site/fx.js`

```js
323(s,x,card){const w=el('div','sv-clk');w.innerHTML=`<svg viewBox="-50 -50 100 100"><circle r="46" class="f"/>${[...Array(60)].map((_,i)=>`<line y1="-43" y2="${i%5?-40.5:-38}" class="${i%5?'m':'h'}" transform="rotate(${i*6})"/>`).join('')}<line class="hh" y1="5" y2="-22"/><line class="mh" y1="7" y2="-32"/><g class="sh"><line y1="10" y2="-37"/><circle r="2.4"/></g><circle r="1.6" class="c"/></svg><b></b>`;w.querySelector('b').textContent=x;s.append(w);const [hh,mh,sh]=['.hh','.mh','.sh'].map(q=>w.querySelector(q));
  ticks.set(card,()=>{const d=new Date(),ms=d.getMilliseconds(),sec=d.getSeconds()+ms/1000,mn=d.getMinutes()+sec/60,hr=d.getHours()%12+mn/60;
    // 秒針：每秒跳一格並帶一點回彈（前 150ms 內完成）
    const st=Math.floor(sec),k=Math.min(1,ms/150),e=1+2.2*Math.pow(k-1,3)+1.2*Math.pow(k-1,2);sh.setAttribute('transform',`rotate(${(st-1+e)*6})`);mh.setAttribute('transform',`rotate(${mn*6})`);hh.setAttribute('transform',`rotate(${hr*30})`)})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx323` rules from `site/fx.css`

_No dedicated `.fx323` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #323
