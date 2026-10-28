# 036 · Ink Bleed — 墨水暈開

Ink bleeds into shape

- Component: Text (`text`)
- Timing: Entrance
- Tech: CSS
- Uses: Headline · Hero
- Style / keywords: Textured Fill
- Tag: Japanese Style · Handwritten Feel
- Example text: "Ink Bleed" (stage background: dark)
- Added: 2026-10-15

**AI prompt (English copy format):**

```text
"Ink Bleed (墨水暈開)" motion effect: The text is like ink dropped on paper: it starts as a blurred, bleeding blob of ink and gradually converges into a clear, sharp character shape, pauses, then bleeds out and disappears, with each character staggered in sequence. About 3.4 seconds per cycle, with a Japanese-style handwritten feel.
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx36">`, preview text "Ink Bleed". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Ink Bleed".

### JavaScript — `FX[36]` from `site/fx.js`

```js
36(s,x){const g=el('div','goo');g.append(split(x));s.append(g)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx36` rules from `site/fx.css`

```css
.fx36{background:#000!important}
.fx36 .goo{filter:contrast(16);background:#000;padding:4cqw 6cqw}
.fx36 .c{color:#fff;animation:ink 3.4s calc(var(--i)*.22s) infinite}
@keyframes ink{0%{filter:blur(16px);opacity:0;transform:scale(1.3)}15%{opacity:1}55%,80%{filter:blur(0);transform:none;opacity:1}100%{filter:blur(16px);opacity:0;transform:scale(1.2)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #36
