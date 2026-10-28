# 152 · Scroll Text Reveal — 捲動逐字點亮

The characters of a paragraph brighten one by one from faint as you scroll

- Component: Text (`text`)
- Timing: Scroll-triggered
- Tech: GSAP
- Uses: Headline · Hero, Scroll Effects
- Style / keywords: Character by Character Light Up Paragraph Copy Apple Official Site Text Reveal Highlight On Scroll Scroll Scroll scroll ScrollTrigger scrub Scroll-triggered
- Tag: ScrollTrigger scrub
- Example text: "Great motion design lights up word by word as you scroll, guiding your eyes down through this sentence." (stage background: dark)
- Added: 2026-10-16

**AI prompt (English copy format):**

```text
"Scroll Text Reveal (捲動逐字點亮)" motion effect: A passage in large type is fixed at the center of the screen, with all characters very faint at first; as the user scrolls down, the characters become clear in sequence starting from the first one — scroll progress equals the proportion lit — and scrolling back dims them in sequence again, like copy presentation on Apple's official site. (GSAP: SplitText splits the characters, fromTo opacity 0.15→1, stagger 0.1, ease none, bound to ScrollTrigger scrub:true; the section is fixed with pin or position:sticky, and the outer height is about 3–4 viewports)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx152">`, preview text "Great motion design lights up word by word as you scroll, guiding your eyes down through this sentence.". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Scroll Text Reveal".

### JavaScript — `FX[152]` from `site/fx.js`

```js
152(s,x){const{sc,wrap,view}=scrollBox(s);view.classList.add('cen');const p=el('div','sfill');p.textContent=x;view.append(p);const sp=SplitText.create(p,{type:'chars'});
  gsap.fromTo(sp.chars,{opacity:.15},{opacity:1,stagger:.1,ease:'none',scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:true}});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx152` rules from `site/fx.css`

_No dedicated `.fx152` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #152
