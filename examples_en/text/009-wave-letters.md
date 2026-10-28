# 009 · Wave Letters — 波浪文字

Text undulates like a wave

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Headline · Hero
- Style / keywords: Letter-by-Letter Motion
- Tag: Joyful · Summer
- Example text: "Waves" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Wave Letters (波浪文字)" motion effect: Each character rises and falls in sequence and sways slightly from side to side, forming a continuously flowing wave, with the characters alternating between two tones. About 1.4 seconds per wave, with a relaxed, joyful summer feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx9">`, preview text "Waves". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Wave Letters".

### JavaScript — `FX[9]` from `site/fx.js`

```js
9(s,x){s.append(split(x))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx9` rules from `site/fx.css`

```css
.fx9 .c{animation:wv 1.4s calc(var(--i)*-.18s) ease-in-out infinite}
.fx9 .c:nth-child(even){color:var(--a)}
@keyframes wv{0%,100%{transform:translateY(14%) rotate(-4deg)}50%{transform:translateY(-14%) rotate(4deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #9
