# 003 · Coin Flip — 硬幣翻轉

Text flips and bounces like a coin

- Component: Text (`text`)
- Timing: Loop · Idle
- Tech: CSS
- Uses: Emphasis
- Style / keywords: Letter-by-Letter Motion
- Tag: Try Your Luck · Game
- Example text: "Heads or Tails" (stage background: cream)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Coin Flip (硬幣翻轉)" motion effect: Each character flips two full turns around the Y axis like a coin and jumps upward, then bounces once more, small, when it lands, with a sequential delay of about 0.14 seconds between characters. About 2.4 seconds per cycle, light and playful.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx3">`, preview text "Heads or Tails". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Coin Flip".

### JavaScript — `FX[3]` from `site/fx.js`

```js
3(s,x){s.append(split(x))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx3` rules from `site/fx.css`

```css
.fx3 .c{animation:coin 2.4s calc(var(--i)*.14s) infinite}
@keyframes coin{0%{transform:translateY(0) rotateY(0)}28%{transform:translateY(-45%) rotateY(360deg)}42%{transform:translateY(0) rotateY(720deg)}48%{transform:translateY(-8%) rotateY(720deg)}54%,100%{transform:translateY(0) rotateY(720deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #3
