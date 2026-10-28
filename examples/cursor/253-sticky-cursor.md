# 253 · 黏性游標 — Sticky Cursor

游標靠近按鈕時被吸附，變形包住整顆按鈕，按鈕也被輕輕拉動

- 元件 Component: 游標 (`cursor`)
- 時機 Timing: 懸停・點擊
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、強調重點
- 風格／關鍵字 Style: 黏性 吸附 磁吸 變形 包覆 導覽 Sticky Cursor Magnetic Morph Nav 游標 滑鼠
- 標籤 Tag: GSAP
- 範例文字 Example text: 「作品 關於 聯絡」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「黏性游標（Sticky Cursor）」動態效果：導覽列的一排按鈕，游標是一顆小圓：游標靠近某顆按鈕時，小圓被「吸」過去，變形成圓角長方形把整顆按鈕包起來，且位置仍隨滑鼠在按鈕內輕微偏移；按鈕本身也朝滑鼠方向被輕輕拉動、文字與底色反轉；移開按鈕時小圓縮回、按鈕彈回原位。（GSAP：mousemove 判斷游標是否在按鈕範圍內（含一點外擴），在範圍內就 tween 游標的 x/y/width/height 到按鈕中心與尺寸 + 偏移 × 0.12，否則 tween 回小圓；按鈕 x/y = 偏移 × 0.15，power3.out）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx253">`, preview text 「作品 關於 聯絡」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「黏性游標」.

### JavaScript — `FX[253]` from `site/fx.js`

```js
253(s,x,card){const l=el('div','abs gl cr-st');const row=el('div','cr-sr');const ws=words(x).slice(0,3);const bs=ws.map(t=>{const b=el('button','cr-sb');b.textContent=t;row.append(b);return b});const c=el('i','cr-sc');l.append(row,c);s.append(l);
  const st={x:0,y:0,w:16,h:16,r:8};let tg=st;
  vpointer(l,card,(px,py)=>{const r=l.getBoundingClientRect();let hit=null;bs.forEach(b=>{const q=b.getBoundingClientRect();const on=px>q.left-r.left-6&&px<q.right-r.left+6&&py>q.top-r.top-6&&py<q.bottom-r.top+6;b.classList.toggle('on',on);if(on)hit=q});
    if(hit){const bx=hit.left-r.left+hit.width/2,by=hit.top-r.top+hit.height/2;gsap.to(c,{x:bx+(px-bx)*.12,y:by+(py-by)*.12,width:hit.width+10,height:hit.height+10,borderRadius:99,duration:.35,ease:'power3.out',overwrite:'auto'});
      bs.forEach(b=>{if(b.classList.contains('on'))gsap.to(b,{x:(px-bx)*.15,y:(py-by)*.2,duration:.35,overwrite:'auto'});else gsap.to(b,{x:0,y:0,duration:.5,overwrite:'auto'})})}
    else{gsap.to(c,{x:px,y:py,width:16,height:16,borderRadius:99,duration:.25,ease:'power3.out',overwrite:'auto'});bs.forEach(b=>gsap.to(b,{x:0,y:0,duration:.5,overwrite:'auto'}))}});gsap.set(c,{xPercent:-50,yPercent:-50})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx253` rules from `site/fx.css`

_No dedicated `.fx253` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #253
