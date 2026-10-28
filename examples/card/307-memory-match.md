# 307 · 翻牌配對遊戲 — Memory Match

點兩張卡片翻開，一樣就留下並彈一下，不一樣就翻回去

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 切換
- 技術 Tech: CSS
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 翻牌 配對 記憶 遊戲 小遊戲 互動 Memory Match Card Game Flip Pairs 卡片 群組
- 標籤 Tag: JS + CSS
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「翻牌配對遊戲（Memory Match）」動態效果：一個 4 × 2 的翻牌記憶小遊戲：所有卡片背面朝上，點擊時卡片以 3D 翻轉顯示正面圖案；翻開兩張後，若圖案相同，兩張留在正面、底色變成強調色並彈一下；若不同，停留約 0.8 秒後兩張一起翻回背面；下方文字顯示配對進度，全部配對成功後顯示慶祝文字並洗牌重來。（CSS：卡片 transform-style:preserve-3d，正反兩面 backface-visibility:hidden，.on 時 rotateY(180deg)；JS 管理翻開的卡片與配對判斷）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx307">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「翻牌配對遊戲」.

### JavaScript — `FX[307]` from `site/fx.js`

```js
307(s,x,card){const E=['🌙','⭐','🍀','🌸'];const deck=[...E,...E].sort(()=>Math.random()-.5);const g=el('div','cg-mm');const cs=deck.map(e=>{const c=el('button','cg-mc');c.innerHTML='<i class="f">?</i><i class="b">'+e+'</i>';c.dataset.e=e;g.append(c);return c});const st=el('div','cg-ms');st.textContent='翻兩張找出一樣的';s.append(g,st);let open=[],lock=false,real=0,done=0;
  const flip=c=>{if(lock||c.classList.contains('on'))return;c.classList.add('on');open.push(c);if(open.length<2)return;lock=true;const [a,b]=open;open=[];
    if(a.dataset.e===b.dataset.e){done++;setTimeout(()=>{[a,b].forEach(z=>{z.classList.add('ok')});lock=false;st.textContent=done===4?'全部配對成功！🎉':'配對成功 '+done+' / 4';if(done===4)setTimeout(reset,1600)},400)}
    else setTimeout(()=>{a.classList.remove('on');b.classList.remove('on');lock=false},800)};
  const reset=()=>{done=0;st.textContent='翻兩張找出一樣的';cs.forEach(c=>c.classList.remove('on','ok'));setTimeout(()=>{const d=[...E,...E].sort(()=>Math.random()-.5);cs.forEach((c,i)=>{c.dataset.e=d[i];c.querySelector('.b').textContent=d[i]})},500)};
  cs.forEach(c=>c.onclick=()=>{real=Date.now();flip(c)});
  card._timers.push(setInterval(()=>{if(Date.now()-real<6000||lock)return;const cl=cs.filter(c=>!c.classList.contains('on'));if(!cl.length)return;if(open.length===1){const m=cl.find(c=>c.dataset.e===open[0].dataset.e);flip(Math.random()<.6&&m?m:cl[Math.floor(Math.random()*cl.length)])}else flip(cl[Math.floor(Math.random()*cl.length)])},700))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx307` rules from `site/fx.css`

_No dedicated `.fx307` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #307
