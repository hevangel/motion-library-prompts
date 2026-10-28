# 064 · Typewriter — 打字機

Typed out character by character, then replaced

- Component: Text (`text`)
- Timing: Switch
- Tech: CSS
- Uses: Headline · Hero, Numbers & Data
- Style / keywords: Text Switching Canva Style Canva Typewriter Typewriter
- Tag: Story·Subtitles
- Example text: "Before Dawn Goodbye" (stage background: cream)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Typewriter (打字機)" motion effect: Text appears over two lines character by character like a typewriter, with a blinking cursor behind it; after finishing and lingering, it is quickly deleted character by character and the next sentence is typed. Serif (Mincho) typeface, the second line fainter, typing at about 0.14 seconds per character.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx64">`, preview text "Before Dawn Goodbye". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Typewriter".

### JavaScript — `FX[64]` from `site/fx.js`

```js
64(s,x,card){const sets=[words(x),['說好的事','明天見']];const tw=el('div','tw');const l1=el('div'),l2=el('div');const cur=el('span','cur');tw.append(l1,l2);s.append(tw);let si=0,p=0,phase=0,hold=0;
  card._timers.push(setInterval(()=>{const set=sets[si%2];const full=set.join('\n');if(phase===0){p++;if(p>=chars(full).length){phase=1;hold=14}}else if(phase===1){if(--hold<=0)phase=2}else{p--;if(p<=0){phase=0;si++}}
    const sh=chars(full).slice(0,p).join('').split('\n');l1.textContent=sh[0]||'';l2.textContent=sh[1]||'';(sh.length>1?l2:l1).append(cur)},phase===2?60:140))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx64` rules from `site/fx.css`

```css
.fx64 .tw{font-family:"Noto Serif JP",serif;font-weight:400;font-size:9cqw;line-height:1.45;color:#111;width:76%}
.fx64 .tw div:nth-child(2){color:#999}
.fx64 .cur{display:inline-block;width:.4cqw;height:1em;background:#111;vertical-align:-10%;margin-left:.5cqw;animation:blink .8s steps(1) infinite}
@keyframes blink{50%{opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #64
