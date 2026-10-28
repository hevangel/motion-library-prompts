# 161 · 圓形擴張轉場 — Circle Reveal Transition

捲動時圓形遮罩從中央擴大，揭開下一章

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 捲動觸發、切換
- 技術 Tech: GSAP
- 情境 Uses: 轉場切換、捲動效果
- 風格／關鍵字 Style: 轉場 圓形 遮罩 擴張 揭開 章節 Circle Reveal Clip Path Transition Section 捲動 滾動 scroll ScrollTrigger scrub 捲動觸發
- 標籤 Tag: clip-path scrub
- 範例文字 Example text: 「第二章」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「圓形擴張轉場（Circle Reveal Transition）」動態效果：兩個章節之間的轉場：捲動時下一章從畫面中央以一個圓形遮罩出現，圓形隨捲動進度從 0 擴大到蓋滿整個畫面，同時上一章的標題慢慢縮小變淡，下一章的標題從 1.2 倍縮回原尺寸；往回捲時圓形縮回。（GSAP：timeline 綁 ScrollTrigger scrub，區塊 pin 或 sticky；tween clipPath "circle(0% at 50% 50%)" → "circle(75% at 50% 50%)"）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx161">`, preview text 「第二章」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「圓形擴張轉場」.

### JavaScript — `FX[161]` from `site/fx.js`

```js
161(s,x){const{sc,wrap,view}=scrollBox(s);view.classList.add('crv');view.innerHTML='<div class="c1"></div><div class="c2"></div>';const a=T('第一章',12),b=T(x,Math.min(12,56/chars(x).length));view.firstChild.append(a);view.lastChild.append(b);
  gsap.timeline({scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:true}}).fromTo(view.lastChild,{clipPath:'circle(0% at 50% 50%)'},{clipPath:'circle(75% at 50% 50%)',ease:'none'},0).fromTo(a,{scale:1,opacity:1},{scale:.8,opacity:.3,ease:'none'},0).fromTo(b,{scale:1.2},{scale:1,ease:'none'},0);autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx161` rules from `site/fx.css`

_No dedicated `.fx161` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #161
