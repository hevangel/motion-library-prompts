# 130 · 行動按鈕提示 — Gentle CTA Cue

內容出現後，按鈕外圍輕輕擴散光暈，把視線帶到按鈕

- 元件 Component: 按鈕 (`button`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: 強調重點、介面互動
- 風格／關鍵字 Style: CTA 行動呼籲 按鈕 提示 光暈 擴散 注意力 溫和 柔和 輕柔 引導 動線 視線 閱讀順序 低調 Subtle Gentle Soft Entrance Visual Flow Hierarchy
- 標籤 Tag: CTA cue
- 範例文字 Example text: 「免費試用」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「行動按鈕提示（Gentle CTA Cue）」動態效果：內容區塊（標題、兩行內文、按鈕）先依序柔和地淡入上浮；全部出現後約 0.3 秒，行動按鈕外圍輕輕擴散出一圈半透明光暈並淡掉，連續兩次，同時按鈕微微上浮 3px 再回原位，像是溫和地提醒「下一步在這裡」，之後保持靜止，不持續閃爍。（GSAP：先 stagger 淡入，再用 tween CSS 變數 --ring 0→1 控制 ::after 的 box-shadow 擴散與透明度，repeat:1；整段只播放一次）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx130">`, preview text 「免費試用」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「行動按鈕提示」.

### JavaScript — `FX[130]` from `site/fx.js`

```js
130(s,x){const w=el('div','gs');w.innerHTML='<b>準備好開始了嗎？</b><i class="ln"></i><i class="ln s"></i><span class="bt ctaa"></span>';const bt=w.querySelector('.bt');bt.textContent=x;s.append(w);const it=[...w.children];
  gsap.timeline({repeat:-1,repeatDelay:.3}).fromTo(it,{opacity:0,y:14},{opacity:1,y:0,duration:.8,ease:'power2.out',stagger:.12})
    .fromTo(bt,{'--ring':0},{'--ring':1,duration:1.3,ease:'power2.out',repeat:1},'+=.3').fromTo(bt,{y:0},{y:-3,duration:.5,ease:'power2.out',yoyo:true,repeat:1},'<').to(it,{opacity:0,duration:.5},'+=1.2')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx130` rules from `site/fx.css`

_No dedicated `.fx130` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #130
