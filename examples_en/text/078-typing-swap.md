# 078 · Typing Swap — 打字換句

Type, delete, swap to the next sentence

- Component: Text (`text`)
- Timing: Switch
- Tech: GSAP
- Uses: Headline · Hero
- Style / keywords: Canva Style Canva Typewriter Typewriter
- Tag: TextPlugin
- Example text: "Typing with GSAP" (stage background: cream)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Typing Swap (打字換句)" motion effect: Like a typewriter, type out a sentence character by character, the cursor blinking behind it; after lingering for about 1 second, delete it character by character from the end, then type the next sentence, cycling through three sentences. (GSAP: TextPlugin typing + a timeline chaining the deletions)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage cream fx78">`, preview text "Typing with GSAP". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Typing Swap".

### JavaScript — `FX[78]` from `site/fx.js`

```js
78(s,x){const ph=[x,'讓介面動起來','換一句再打'];const w=el('div','tw2');const t=el('span');w.append(t,el('span','cur2'));w.style.fontSize=Math.min(9,64/Math.max(...ph.map(v=>chars(v).length)))+'cqw';s.append(w);
  const tl=gsap.timeline({repeat:-1});ph.forEach(v=>{const n=chars(v).length,o={n};tl.to(t,{duration:n*.1,text:{value:v},ease:'none'}).to(o,{n:0,duration:n*.05,ease:'none',onUpdate:()=>t.textContent=chars(v).slice(0,Math.round(o.n)).join('')},'+=1.1').set(o,{n})})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx78` rules from `site/fx.css`

_No dedicated `.fx78` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #78
