# 077 · Scramble Reveal — 亂碼揭示

Scrambled characters gradually resolve into the correct text

- Component: Text (`text`)
- Timing: Entrance
- Tech: GSAP
- Uses: Headline · Hero, Numbers & Data
- Style / keywords: 
- Tag: ScrambleText
- Example text: "Decoded" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Scramble Reveal (亂碼揭示)" motion effect: The text starts as a string of constantly jittering scrambled characters (katakana, symbols, numbers) and gradually resolves into the correct text from left to right, the scrambled characters and the resolved ones distinguished by different colors; after lingering, it scrambles again. Dot-matrix typeface. (GSAP: ScrambleTextPlugin, revealDelay, speed, newClass)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx77">`, preview text "Decoded". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Scramble Reveal".

### JavaScript — `FX[77]` from `site/fx.js`

```js
77(s,x){const t=T(x);t.style.fontFamily='"DotGothic16",monospace';t.style.fontWeight=400;t.style.minHeight='1.15em';t.textContent='';s.append(t);const o={chars:'アイウエオカキク#%&01XZ',speed:.5,newClass:'r'};
  gsap.timeline({repeat:-1,repeatDelay:.3}).to(t,{duration:1.8,scrambleText:{...o,text:x,revealDelay:.4}}).to(t,{duration:.8,scrambleText:{...o,text:' '}},'+=1.4')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx77` rules from `site/fx.css`

```css
.fx77 .t{color:var(--a)}
.fx77 .t .r{color:#fff}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #77
