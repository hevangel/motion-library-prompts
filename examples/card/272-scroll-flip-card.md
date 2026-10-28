# 272 · 捲動翻轉卡片 — Scroll Flip Card

往下捲時卡片立體翻轉到背面，同時微微放大

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 捲動效果、介面互動
- 風格／關鍵字 Style: 翻轉 翻面 3D 卡片 正反面 捲動 Scroll Flip Card 3D RotateY 捲動觸發 ScrollTrigger
- 標籤 Tag: ScrollTrigger
- 範例文字 Example text: 「背面的故事」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「捲動翻轉卡片（Scroll Flip Card）」動態效果：一張卡片位於畫面中央，正面是圖片、背面是文字（背面使用強調色）：使用者往下捲動時，卡片依捲動進度沿著垂直軸立體翻轉 180 度，同時從 0.85 倍放大到 1 倍，捲到一半時剛好側面朝向觀者，捲完時完整顯示背面；往回捲則翻回正面。（GSAP ScrollTrigger scrub：容器 pin 或 sticky，timeline fromTo rotationY 0 → 180；父層設 perspective，卡片 transform-style:preserve-3d，正反兩面 backface-visibility:hidden，背面預先 rotateY(180deg)）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx272">`, preview text 「背面的故事」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「捲動翻轉卡片」.

### JavaScript — `FX[272]` from `site/fx.js`

```js
272(s,x){const{sc,wrap,view}=scrollBox(s);view.classList.add('cen','sx-pv');const c=el('div','sx-fc');c.innerHTML='<div class="f">'+mdImg(0)+'</div><div class="b"><b></b><small>捲動翻到背面</small></div>';c.querySelector('b').textContent=x;view.append(c);
  gsap.timeline({scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:.6}}).fromTo(c,{rotationY:0,scale:.85},{rotationY:180,scale:1,ease:'none'});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx272` rules from `site/fx.css`

_No dedicated `.fx272` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #272
