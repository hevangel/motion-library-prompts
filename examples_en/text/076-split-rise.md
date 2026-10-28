# 076 · Split Rise — 逐字升起

Each character slides up from below a mask

- Component: Text (`text`)
- Timing: Entrance, Exit
- Tech: GSAP
- Uses: Headline · Hero
- Style / keywords: Canva Style Canva Ascend Rise Rise
- Tag: SplitText
- Example text: "Rise Letter by Letter" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Split Rise (逐字升起)" motion effect: The text is split into individual characters, each placed inside a clipping mask, sliding up in sequence from below the mask (about 0.06 seconds between characters, with strong deceleration); after lingering, they slide out upward. (GSAP: SplitText with type chars + mask, from yPercent: 110, ease power4.out, stagger)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx76">`, preview text "Rise Letter by Letter". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Split Rise".

### JavaScript — `FX[76]` from `site/fx.js`

```js
76(s,x){const t=T(x);s.append(t);const sp=SplitText.create(t,{type:'chars',mask:'chars'});
  gsap.timeline({repeat:-1,repeatDelay:.5}).from(sp.chars,{yPercent:110,duration:.8,ease:'power4.out',stagger:.06}).to(sp.chars,{yPercent:-110,duration:.5,ease:'power3.in',stagger:.04},'+=1.3')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx76` rules from `site/fx.css`

_No dedicated `.fx76` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #76
