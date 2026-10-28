# 042 · Letter Sequence — 逐字敲擊

Letters slam in one by one

- Component: Text (`text`)
- Timing: Entrance
- Tech: CSS
- Uses: Headline · Hero
- Style / keywords: Impact Entrance
- Tag: Rhythm·Lyrics
- Example text: "Slam Down" (stage background: acc)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Letter Sequence (逐字敲擊)" motion effect: The text slams down into place one character at a time from above at large size, each character squashing slightly and rebounding as it lands, spaced about 0.2 seconds apart in sequence; after all have appeared, they fade out together. About 3 seconds per cycle.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx42">`, preview text "Slam Down". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Letter Sequence".

### JavaScript — `FX[42]` from `site/fx.js`

```js
42(s,x){s.append(split(x))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx42` rules from `site/fx.css`

```css
.fx42 .c{animation:seq 3s calc(var(--i)*.22s) infinite both}
.fx42 .c:nth-child(odd){color:#fff}
@keyframes seq{0%{opacity:0;transform:scale(2.6) translateY(-20%)}7%{opacity:1;transform:scale(.88)}11%{transform:scale(1.06)}14%,78%{transform:none;opacity:1}90%,100%{opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #42
