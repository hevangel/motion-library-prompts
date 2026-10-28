# 155 · 數據捲到才計數 — Count Up on Scroll

數據區塊捲進畫面時，數字才從零開始累加

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 捲動觸發、進場
- 技術 Tech: GSAP
- 情境 Uses: 數字資訊、捲動效果
- 風格／關鍵字 Style: 數據 統計 計數 數字 成果 KPI Count Up Stats Numbers On Scroll 捲動 滾動 scroll ScrollTrigger scrub 捲動觸發
- 標籤 Tag: ScrollTrigger
- 範例文字 Example text: 「完成專案 客戶滿意度 平均評分」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「數據捲到才計數（Count Up on Scroll）」動態效果：頁面中段的成果數據區（三格：數字＋說明），捲到數據區進入畫面約 80% 位置時，三格依序從下方淡入，數字同時從 0 累加到目標值（例如 128、99%、4.9，可有小數），約 1.6 秒、減速；捲回上方離開時重置，下次捲到再播一次（或只播一次）。（GSAP：ScrollTrigger.create { start:"top 80%", onEnter, onLeaveBack }，數字 tween 物件數值 + onUpdate，用 toFixed 控制小數位）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx155">`, preview text 「完成專案 客戶滿意度 平均評分」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「數據捲到才計數」.

### JavaScript — `FX[155]` from `site/fx.js`

```js
155(s,x){const sc=el('div','scr nopad');const ws=words(x);const T3=[[128,'',0],[99,'%',0],[4.9,'',1]];sc.innerHTML='<div class="sp1">↓ 往下捲到數據區</div><div class="stg"></div><div class="sp2"></div>';const g=sc.querySelector('.stg');
  const its=T3.map(([v,u,d],i)=>{const e=el('div','sti');e.innerHTML='<b>0</b><span></span>';e.querySelector('span').textContent=ws[i%ws.length];g.append(e);return [e,v,u,d]});s.append(sc);
  const play=()=>{gsap.fromTo(its.map(a=>a[0]),{y:16,opacity:0},{y:0,opacity:1,duration:.6,stagger:.12,ease:'power2.out',overwrite:true});its.forEach(([e,v,u,d])=>{const o={v:0},b=e.querySelector('b');gsap.to(o,{v,duration:1.6,ease:'power2.out',onUpdate:()=>b.textContent=o.v.toFixed(d)+u})})};
  const reset=()=>its.forEach(([e])=>{gsap.set(e,{opacity:0});e.querySelector('b').textContent='0'});reset();
  ScrollTrigger.create({trigger:g,scroller:sc,start:'top 80%',onEnter:play,onLeaveBack:reset});autoScroll(sc)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx155` rules from `site/fx.css`

_No dedicated `.fx155` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #155
