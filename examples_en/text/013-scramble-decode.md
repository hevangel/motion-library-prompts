# 013 · Scramble Decode — 亂碼解讀

Decodes from gibberish into real text

- Component: Text (`text`)
- Timing: Entrance
- Tech: CSS
- Uses: Headline · Hero, Numbers & Data
- Style / keywords: Text Switching
- Tag: Hacker · SF
- Example text: "Decoded" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Scramble Decode (亂碼解讀)" motion effect: The text starts as constantly jumping gibberish (katakana, symbols and numbers), then decodes from left to right, character by character, into the correct text and switches to an accent color, pauses, then starts over. A pixel dot-matrix font, with a hacker sci-fi feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx13">`, preview text "Decoded". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Scramble Decode".

### JavaScript — `FX[13]` from `site/fx.js`

```js
13(s,x,card){const t=T(x);s.append(t);const tgt=chars(x),pool='アイウエオカキクケコ#$%&@01XZ暗号解読完了ﾊﾞｸ';let f=0;
  card._timers.push(setInterval(()=>{f++;const cyc=f%(tgt.length*7+40);t.innerHTML=tgt.map((c,i)=>cyc>8+i*7?`<span class="r">${c}</span>`:pool[Math.floor(Math.random()*pool.length)]).join('')},55))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx13` rules from `site/fx.css`

```css
.fx13 .t{font-family:"DotGothic16",monospace;font-weight:400;color:#fff}
.fx13 .t .r{color:var(--a)}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #13
