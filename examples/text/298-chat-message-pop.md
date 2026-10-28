# 298 · 聊天訊息出現 — Chat Message Pop

對方先出現「輸入中」的三個點，接著變成訊息，再彈出你的回覆

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場、循環待機
- 技術 Tech: GSAP
- 情境 Uses: App 介面、介面互動
- 風格／關鍵字 Style: 聊天 訊息 對話框 泡泡 輸入中 打字中 客服 Chat Bubble Typing Indicator Message Pop 文字 標題 動態文字
- 標籤 Tag: GSAP timeline
- 範例文字 Example text: 「有的！歡迎詢問 😊」（預覽底色：dark）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「聊天訊息出現（Chat Message Pop）」動態效果：模擬聊天介面：左側先出現對方的對話泡泡，裡面是三個依序上下跳動的點（輸入中…），約 1.4 秒後泡泡變成一則訊息（例如「在嗎？想問一下～」）並輕彈一下；接著右側以強調色彈出你的回覆泡泡（從右下角放大出現）；停留後一起上移淡出，再重新開始。（GSAP timeline：泡泡 scale 0 → 1、transform-origin 設在泡泡尾巴的角落、ease back.out；三個點用 CSS keyframes 錯開 animation-delay）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx298">`, preview text 「有的！歡迎詢問 😊」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「聊天訊息出現」.

### JavaScript — `FX[298]` from `site/fx.js`

```js
298(s,x){const w=el('div','tx-ch');w.innerHTML='<div class="tx-b them"></div><div class="tx-b me"></div>';const me=w.querySelector('.me'),ty=w.querySelector('.them');me.textContent=x;s.append(w);
  const reset=()=>{ty.classList.remove('msg');ty.innerHTML='<i></i><i></i><i></i>';gsap.set([ty,me],{y:0,opacity:1});gsap.set(me,{scale:0,opacity:0})};reset();
  gsap.timeline({repeat:-1,repeatDelay:.6}).call(reset).fromTo(ty,{scale:0},{scale:1,transformOrigin:'0% 100%',duration:.35,ease:'back.out(2)'})
    .call(()=>{ty.classList.add('msg');ty.textContent='在嗎？想問一下～'},null,'+=1.4').fromTo(ty,{scale:.85},{scale:1,duration:.3,ease:'back.out(3)'})
    .fromTo(me,{scale:0,opacity:0},{scale:1,opacity:1,transformOrigin:'100% 100%',duration:.4,ease:'back.out(2)',immediateRender:false},'+=.7')
    .to([ty,me],{opacity:0,y:-10,duration:.4,stagger:.08},'+=1.8')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx298` rules from `site/fx.css`

_No dedicated `.fx298` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #298
