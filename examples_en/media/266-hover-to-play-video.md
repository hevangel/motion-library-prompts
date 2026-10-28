# 266 · Hover to Play Video — 滑過預覽影片

A video thumbnail is normally still; on hover the play button shrinks and disappears, the picture starts playing, and the progress bar advances

- Component: Images · Media (`media`)
- Timing: Hover · Click
- Tech: CSS
- Uses: UI Interaction
- Style / keywords: Video Preview Autoplay Thumbnail Play Button YouTube Video Preview Hover Play Thumbnail Image Media
- Tag: CSS hover
- Example text: "Travel Journal" (stage background: dark)
- Added: 2026-10-19

**AI prompt (English copy format):**

```text
"Hover to Play Video (滑過預覽影片)" motion effect: Video thumbnail card: normally the picture is slightly dark and still, with a round play button in the middle and the duration shown in the lower right corner; when the mouse hovers, the play button shrinks and fades out, the picture brightens and starts playing (in the demo a slow push-in is used instead), and a progress bar appears at the bottom and starts advancing; when moving away it pauses and returns to the still state. (Implementation: on hover call video.play(), on leave pause() and reset currentTime to zero; the play button transitions with scale and opacity; the video is set to muted and playsinline so it can autoplay)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx266">`, preview text "Travel Journal". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Hover to Play Video".

### JavaScript — `FX[266]` from `site/fx.js`

```js
266(s,x,card){const f=el('div','md-vd');f.innerHTML=mdImg(3,'kb')+'<div class="md-pl"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></div><div class="md-vb"><i></i></div><span class="md-du">0:42</span><b class="md-vt"></b>';f.querySelector('.md-vt').textContent=x;s.append(f);autoHover(f,[f],card,2400)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx266` rules from `site/fx.css`

_No dedicated `.fx266` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #266
