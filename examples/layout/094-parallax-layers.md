# 094 · 視差圖層 — Parallax Layers

遠中近景以不同速度移動

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 捲動效果、背景裝飾
- 風格／關鍵字 Style: 
- 標籤 Tag: ScrollTrigger scrub
- 範例文字 Example text: 「視差」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「視差圖層（Parallax Layers）」動態效果：捲動時遠景大字、中景圓點、近景標題以不同速度上下移動，近景最快、遠景最慢，產生景深視差。（GSAP：一個 timeline 綁 ScrollTrigger scrub，三個圖層分別設定不同 yPercent 範圍）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx94">`, preview text 「視差」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「視差圖層」.

### JavaScript — `FX[94]` from `site/fx.js`

```js
94(s,x){const{sc,wrap,view}=scrollBox(s);view.classList.add('pv');view.innerHTML='<div class="l1">遠景</div><div class="l2"></div><div class="l3"></div>';view.querySelector('.l3').textContent=x;const l2=view.querySelector('.l2');
  [[12,20,9],[78,15,14],[60,62,6],[22,70,12],[88,72,8]].forEach(([l,t,z])=>{const i=el('i');i.style.cssText=`left:${l}%;top:${t}%;width:${z}cqw;height:${z}cqw;opacity:.85`;l2.append(i)});
  gsap.timeline({scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:.5}}).fromTo(view.querySelector('.l1'),{yPercent:15},{yPercent:-15,ease:'none'},0).fromTo(l2,{yPercent:45},{yPercent:-45,ease:'none'},0).fromTo(view.querySelector('.l3'),{yPercent:260},{yPercent:-260,ease:'none'},0);autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx94` rules from `site/fx.css`

_No dedicated `.fx94` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #94
