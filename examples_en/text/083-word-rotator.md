# 083 · Word Rotator — 遮罩換詞

A fixed prefix, with the word after it rotating through replacements

- Component: Text (`text`)
- Timing: Switch
- Tech: GSAP
- Uses: Headline · Hero, Transitions
- Style / keywords: 
- Tag: SplitText mask
- Example text: "Design Animation Interaction Experience" (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Word Rotator (遮罩換詞)" motion effect: A fixed prefix "We make", with the word after it rotating inside a mask: each new word slides up letter by letter from below, stays for a while, then slides up and out, followed by the next word; the rotating words use the accent color. (GSAP: SplitText chars + mask, a timeline chains each word in sequence)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx83">`, preview text "Design Animation Interaction Experience". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Word Rotator".

### JavaScript — `FX[83]` from `site/fx.js`

```js
83(s,x){const ws=words(x);const w=el('div','wm');const pre=el('span');pre.textContent='我們做';const box=el('span','box');w.append(pre,box);w.style.fontSize=Math.min(11,62/(3+Math.max(...ws.map(v=>chars(v).length))))+'cqw';s.append(w);
  const tl=gsap.timeline({repeat:-1});ws.forEach(v=>{const e=el('span','it');e.textContent=v;box.append(e);const sp=SplitText.create(e,{type:'chars',mask:'chars'});tl.fromTo(sp.chars,{yPercent:110},{yPercent:0,duration:.6,ease:'power3.out',stagger:.04}).to(sp.chars,{yPercent:-110,duration:.45,ease:'power3.in',stagger:.03},'+=1')})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx83` rules from `site/fx.css`

_No dedicated `.fx83` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #83
