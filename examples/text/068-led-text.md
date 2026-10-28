# 068 · LED 看板 — LED Text

點點組成的電子字

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 數字資訊、背景裝飾
- 風格／關鍵字 Style: 流動背景
- 標籤 Tag: 復古・科技
- 範例文字 Example text: 「最新消息・」（預覽底色：cream）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「LED 看板（LED Text）」動態效果：像電子看板一樣由圓點矩陣組成的文字，持續由右往左捲動，亮點與暗點對比明顯。捲動速度中等，復古科技感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx68">`, preview text 「最新消息・」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「LED 看板」.

### JavaScript — `FX[68]` from `site/fx.js`

```js
68(s,x,card){const cv=el('canvas');s.append(cv);const R=16;const off=document.createElement('canvas');const oc=off.getContext('2d');oc.font=`900 ${R-2}px "Noto Sans JP",sans-serif`;const tw=Math.ceil(oc.measureText(x).width)+R;off.width=tw;off.height=R;oc.font=`900 ${R-2}px "Noto Sans JP",sans-serif`;oc.fillStyle='#fff';oc.textBaseline='middle';oc.fillText(x,0,R/2+1);const px=oc.getImageData(0,0,tw,R).data;const on=(cx,cy)=>px[(cy*tw+((cx%tw)+tw)%tw)*4+3]>110;const ctx=cv.getContext('2d');
  ticks.set(card,t=>{const W=s.offsetWidth,H=s.offsetHeight;if(!W)return;const dpr=devicePixelRatio||1;if(cv.width!==W*dpr){cv.width=W*dpr;cv.height=H*dpr}const cell=cv.height/(R+6);const cols=Math.ceil(cv.width/cell);const sh=Math.floor(t*14);ctx.fillStyle='#161616';ctx.fillRect(0,0,cv.width,cv.height);for(let cy=0;cy<R;cy++)for(let cx=0;cx<cols;cx++){const o=on(cx+sh,cy);ctx.fillStyle=o?getComputedStyle(s).getPropertyValue('--a')||'#d9f53a':'#2a2a2a';if(o)ctx.fillStyle='#d9f53a';ctx.beginPath();ctx.arc(cx*cell+cell/2,(cy+3)*cell+cell/2,cell*.38,0,7);ctx.fill()}})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx68` rules from `site/fx.css`

```css
.fx68 canvas{position:absolute;inset:0;width:100%;height:100%}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #68
