# 118 · Toast Stack — 通知堆疊

Notifications pop in and stack from the bottom-right corner in sequence, then slide out and disappear after a few seconds

- Component: Cards · Groups (`card`)
- Timing: Entrance, Exit
- Tech: CSS
- Uses: UI Interaction, Numbers & Data
- Style / keywords: Notification Prompt Message Toast Pop-up Toast Notification Snackbar Alert Stack
- Tag: Toast
- Example text: "Changes Saved" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Toast Stack (通知堆疊)" motion effect: When an operation completes, a notification pops up in the bottom-right corner of the screen (a checkmark in a circle icon on the left, a message in the middle, a "just now" time on the right), entering from below with a slight scale and elastic feel; a new notification stacks below, pushing the old ones up; at most 3 are shown at the same time, and each one slides out to the right and fades away after about 3.4 seconds, with the remaining notifications smoothly moving up to fill the gap. (CSS + JS: the notification wrapper uses display:grid + grid-template-rows 1fr→0fr to collapse the height so filling the gap is smooth; entrance uses keyframes translateY + scale; for exit, add an .out class and then remove the element)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx118">`, preview text "Changes Saved". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Toast Stack".

### JavaScript — `FX[118]` from `site/fx.js`

```js
118(s,x,card){const box=el('div','tst');s.append(box);const msgs=[x,'上傳完成','有 3 則新留言','已加入收藏'];let k=0;
  const push=()=>{const t=el('div','ti');t.innerHTML='<div><div class="tb"><i>✓</i><b></b><small>剛剛</small></div></div>';t.querySelector('b').textContent=msgs[k++%msgs.length];box.append(t);
    const live=[...box.querySelectorAll('.ti:not(.out)')];if(live.length>3)live[0].classList.add('out');setTimeout(()=>t.classList.add('out'),3400);setTimeout(()=>t.remove(),4000)};
  push();card._timers.push(setInterval(push,1100))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx118` rules from `site/fx.css`

_No dedicated `.fx118` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #118
