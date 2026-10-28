# 018 · Letter Bounce — 逐字彈跳

Text bounces letter by letter

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Headline · Hero
- Style / keywords: Letter-by-Letter Motion Canva Style Canva Bounce Bounce
- Tag: Cute · MV
- Example text: "Bouncy Letters" (stage background: acc)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Letter Bounce (逐字彈跳)" motion effect: Each character in sequence squashes flat, springs up, lands and squashes and rebounds again, with the squash-and-stretch elasticity of a small ball, only one character jumping at a time. About 2.2 seconds per cycle, with a cute MV feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage acc fx18">`, preview text "Bouncy Letters". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Letter Bounce".

### JavaScript — `FX[18]` from `site/fx.js`

```js
18(s,x){s.append(split(x))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx18` rules from `site/fx.css`

```css
.fx18 .c{transform-origin:50% 100%;animation:bnc 2.2s calc(var(--i)*.18s) infinite}
.fx18 .c:nth-child(n+4){color:#fff}
@keyframes bnc{0%,40%,100%{transform:none}8%{transform:scale(1.2,.8)}18%{transform:translateY(-45%) scale(.9,1.1)}28%{transform:scale(1.15,.85)}34%{transform:scale(.97,1.03)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #18
