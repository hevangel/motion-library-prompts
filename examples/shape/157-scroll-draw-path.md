# 157 · 捲動繪製路徑 — Scroll Draw Path

一條曲線隨捲動一路畫下去，串起各個段落

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 捲動觸發
- 技術 Tech: GSAP
- 情境 Uses: 捲動效果、數字資訊
- 風格／關鍵字 Style: 路徑 曲線 線條 繪製 時間軸 旅程 故事 Scroll Path Draw SVG Line Journey Story 捲動 滾動 scroll ScrollTrigger scrub 捲動觸發
- 標籤 Tag: DrawSVG scrub
- 範例文字 Example text: 「起點 探索 成長 抵達」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「捲動繪製路徑（Scroll Draw Path）」動態效果：頁面背景有一條左右蜿蜒、貫穿整段內容的曲線，底下先有一條很淡的軌跡；往下捲動時，強調色的線條沿著軌跡一路畫下去，捲到哪畫到哪，往回捲時線條縮回；沿線的幾個節點（圓點＋標題）在線條接近時從兩側交錯淡入。適合品牌故事、旅程、歷程介紹。（GSAP：DrawSVGPlugin drawSVG 0%→100% 綁 ScrollTrigger scrub；SVG 高度與內容同高、preserveAspectRatio:none；節點各自用 toggleActions 淡入）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx157">`, preview text 「起點 探索 成長 抵達」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「捲動繪製路徑」.

### JavaScript — `FX[157]` from `site/fx.js`

```js
157(s,x){const{sc,wrap}=scrollBox(s);wrap.classList.add('dpw');wrap.insertAdjacentHTML('afterbegin','<svg class="dpath" viewBox="0 0 100 400" preserveAspectRatio="none"><path class="bg2" d="M50,0 C92,40 92,60 50,100 C8,140 8,160 50,200 C92,240 92,260 50,300 C8,340 8,360 50,400"/><path class="fg2" d="M50,0 C92,40 92,60 50,100 C8,140 8,160 50,200 C92,240 92,260 50,300 C8,340 8,360 50,400"/></svg>');
  words(x).slice(0,4).forEach((v,i)=>{const m=el('div','dms'+(i%2?' r':''));m.style.top=(12+i*25)+'%';m.innerHTML='<i></i><b></b>';m.querySelector('b').textContent=v;wrap.append(m);
    gsap.fromTo(m,{opacity:0,x:i%2?16:-16},{opacity:1,x:0,duration:.5,ease:'power2.out',scrollTrigger:{trigger:m,scroller:sc,start:'top 65%',toggleActions:'play none none reverse'}})});
  gsap.fromTo(wrap.querySelector('.fg2'),{drawSVG:'0%'},{drawSVG:'100%',ease:'none',scrollTrigger:{trigger:wrap,scroller:sc,start:'top top',end:'bottom bottom',scrub:.5}});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx157` rules from `site/fx.css`

_No dedicated `.fx157` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #157
