# 101 · 捲動導覽點 — Scroll Spy Dot Nav

側邊導覽點隨捲動亮起，點了跳到該段

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 捲動觸發、懸停・點擊
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、捲動效果
- 風格／關鍵字 Style: 捲動導覽 側邊導覽點 錨點導覽 頁面進度導覽 Scroll Spy Navigation Dot Navigation
- 標籤 Tag: ScrollTrigger
- 範例文字 Example text: 「簡介 作品 服務 聯絡」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「捲動導覽點（Scroll Spy Dot Nav）」動態效果：捲動導覽／側邊導覽點（Scroll Spy / Dot Navigation，也稱錨點導覽、頁面進度導覽）：頁面右側固定一排小圓點，每個點對應一個區段；捲到哪一段，對應的點就放大並以強調色填滿，旁邊浮出該段名稱的膠囊標籤；點與點之間有一條細軌道，軌道裡的進度條隨整頁捲動比例往下長；點擊任一個點會平滑捲動到該段，滑鼠移到點上也會顯示名稱。各區段底色深淺交錯。（GSAP：每段一個 ScrollTrigger，start "top center"、end "bottom center"，onToggle 切換 active；進度條用 scrub:true 的 scaleY；點擊用 gsap.to(scroller,{scrollTop}) 或 ScrollToPlugin）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx101">`, preview text 「簡介 作品 服務 聯絡」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「捲動導覽點」.

### JavaScript — `FX[101]` from `site/fx.js`

```js
101(s,x){const sc=el('div','scr nopad');const nav=el('nav','dnav');const fill=el('i');const track=el('div','dtrack');track.append(fill);nav.append(track);s.append(sc,nav);
  const dots=[];words(x).slice(0,6).forEach((n,i)=>{const sec=el('section','dsec');sec.innerHTML=`<small>0${i+1}</small><b></b>`;sec.querySelector('b').textContent=n;sc.append(sec);
    const d=el('button','dd');d.setAttribute('aria-label',n);const lab=el('span');lab.textContent=n;d.append(lab);nav.append(d);dots.push(d);
    d.onclick=()=>gsap.to(sc,{scrollTop:sec.offsetTop,duration:.8,ease:'power3.inOut',overwrite:true});
    ScrollTrigger.create({trigger:sec,scroller:sc,start:'top center',end:'bottom center',onToggle:t=>{if(t.isActive)dots.forEach((o,k)=>o.classList.toggle('on',k===i))}})});
  gsap.fromTo(fill,{scaleY:0},{scaleY:1,ease:'none',scrollTrigger:{scroller:sc,start:0,end:'max',scrub:true}});autoScroll(sc,nav)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx101` rules from `site/fx.css`

_No dedicated `.fx101` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #101
