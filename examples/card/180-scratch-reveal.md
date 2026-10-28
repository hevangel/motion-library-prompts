# 180 · 刮刮樂揭示 — Scratch Reveal

用游標或手指刮開表層，露出底下的內容

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 拖曳手勢
- 技術 Tech: Canvas
- 情境 Uses: 介面互動、強調重點、App 介面
- 風格／關鍵字 Style: 刮刮樂 刮開 揭曉 抽獎 優惠券 遊戲化 Scratch Card Reveal Lottery Coupon Gamification Canvas 粒子 particles requestAnimationFrame 互動背景
- 標籤 Tag: Canvas erase
- 範例文字 Example text: 「免運優惠券」（預覽底色：dark）
- 收錄日期 Added: 2026-10-17

**AI 提示詞（網站複製格式）:**

```text
「刮刮樂揭示（Scratch Reveal）」動態效果：卡片上覆蓋一層帶金屬漸層質感與「刮開看看」字樣的表層，使用者按住滑鼠或手指拖過的地方會被刮掉（圓頭粗筆刷），露出底下的獎項或優惠內容；刮開面積超過約一半時，剩下的表層自動淡出，完整揭曉。適合抽獎、優惠券、活動頁。（Canvas 2D：表層畫在 canvas 上，拖曳時用 globalCompositeOperation = "destination-out" 沿路徑畫線擦除；定期取樣 getImageData 的透明比例判斷是否揭曉；手機設 touch-action:none）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx180">`, preview text 「免運優惠券」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「刮刮樂揭示」.

### JavaScript — `FX[180]` from `site/fx.js`

```js
180(s,x,card){const pr=el('div','scp');pr.innerHTML='<small>恭喜你</small><b></b>';pr.querySelector('b').textContent=x;s.append(pr);let real=0;
  const cv=cfx(s,card,{init:(c,W,H)=>{cover(c,W,H);return{lx:null,ly:null,cnt:0}},
    frame:(c,W,H,t,dt,m,o)=>{let px,py,on=false;if(m.down){px=m.x;py=m.y;on=true;real=Date.now()}else if(Date.now()-real>4000){const p=(t%7)/7;if(p<.7){const q=p/.7;px=W*(.12+.76*((q*5)%1));py=H*(.2+.6*q);on=true;if((q*5)%1<.04)o.lx=null}
        else if(p<.72){cv.style.opacity=0}else if(p>.95&&cv.style.opacity==='0'){cover(c,W,H);cv.style.opacity=1;o.lx=null}}
      if(on){c.globalCompositeOperation='destination-out';c.lineCap='round';c.lineWidth=W*.08;c.beginPath();c.moveTo(o.lx??px,o.ly??py);c.lineTo(px,py);c.stroke();c.globalCompositeOperation='source-over';o.lx=px;o.ly=py}else{o.lx=null;o.ly=null}
      if(m.down&&++o.cnt%20===0){const d=c.getImageData(0,0,c.canvas.width,c.canvas.height).data;let a=0,n=0;for(let i=3;i<d.length;i+=400){n++;if(d[i]>0)a++}if(a/n<.45){cv.style.opacity=0;setTimeout(()=>{cover(c,W,H);cv.style.opacity=1},2200)}}}});
  cv.classList.add('scr2');
  function cover(c,W,H){c.globalCompositeOperation='source-over';const g=c.createLinearGradient(0,0,W,H);g.addColorStop(0,'#b9bcc6');g.addColorStop(.5,'#e6e8ee');g.addColorStop(1,'#9fa3ad');c.fillStyle=g;c.fillRect(0,0,W,H);
    c.fillStyle='rgba(0,0,0,.35)';c.font=`800 ${W*.045}px "Noto Sans JP",sans-serif`;c.textAlign='center';c.textBaseline='middle';c.fillText('刮開看看 ✦',W/2,H/2)}}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx180` rules from `site/fx.css`

_No dedicated `.fx180` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #180
