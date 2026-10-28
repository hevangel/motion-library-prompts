# 295 · Image Filled Text — 圖片填字

A landscape image fills the inside of large text, and the image slowly pans and zooms inside the letters

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Headline · Hero
- Style / keywords: Image Text Fill Knockout Background Text Mask Image Text Background Clip Knockout Mask Text Heading Animated Text
- Tag: background-clip
- Example text: "WILD" (stage background: dark)
- Added: 2026-10-20

**AI prompt (English copy format):**

```text
"Image Filled Text (圖片填字)" motion effect: An extra-large, extra-bold English heading whose letters are filled with a landscape photo (the image is not visible anywhere outside the letters); the photo slowly pans and enlarges slightly inside the letters, going back and forth about once every 9 seconds, like looking at scenery through a text-shaped window; there is a very faint thin outline around the outer edges of the letters. (CSS: color:transparent + background-image + background-clip:text, with keyframes changing background-position and background-size)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx295">`, preview text "WILD". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Image Filled Text".

### JavaScript — `FX[295]` from `site/fx.js`

```js
295(s,x){const t=el('div','tx-if');t.style.fontSize=Math.min(19,80/chars(x).length)+'cqw';t.textContent=x;s.append(t);t.style.backgroundImage=`url("data:image/svg+xml,${encodeURIComponent(scene(...MD_P[3]).replace('<svg ','<svg xmlns="http://www.w3.org/2000/svg" '))}")`}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx295` rules from `site/fx.css`

_No dedicated `.fx295` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #295
