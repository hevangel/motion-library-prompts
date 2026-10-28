# 306 · 3D 環形輪播 — 3D Ring Carousel

卡片圍成一圈在 3D 空間緩慢旋轉，可以用滑鼠左右拖轉

- 元件 Component: 卡片・群組 (`card`)
- 時機 Timing: 循環待機、拖曳手勢
- 技術 Tech: GSAP
- 情境 Uses: 標題・Hero、介面互動
- 風格／關鍵字 Style: 3D 環形 旋轉木馬 輪播 圓環 Ring Carousel 3D Rotate Gallery Drag 卡片 群組
- 標籤 Tag: GSAP 3D
- 範例文字 Example text: 「海邊 山林 夜空 午後 城市 森林 湖畔 沙漠」（預覽底色：dark）
- 收錄日期 Added: 2026-10-20

**AI 提示詞（網站複製格式）:**

```text
「3D 環形輪播（3D Ring Carousel）」動態效果：八張圖片卡片在 3D 空間中圍成一個圓環，整個圓環以約 24 秒一圈的速度緩慢自轉，前方的卡片較大較近、後方的較小較遠，背面朝向觀者的卡片隱藏；使用者可以按住左右拖曳轉動圓環，放開後從目前角度繼續自轉。（CSS 3D：容器 perspective，圓環 transform-style:preserve-3d，每張卡片 rotateY(i × 360/N) translateZ(半徑)、backface-visibility:hidden；GSAP 讓圓環 rotationY 循環，Draggable 拖曳時暫停並依位移設定角度）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx306">`, preview text 「海邊 山林 夜空 午後 城市 森林 湖畔 沙漠」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「3D 環形輪播」.

### JavaScript — `FX[306]` from `site/fx.js`

```js
306(s,x,card){const ws=words(x);const sc=el('div','abs gl cg-rs');const ring=el('div','cg-rg');const N=8;const cs=[...Array(N)].map((_,i)=>{const c=el('div','cg-rc');c.innerHTML=mdImg(i)+'<b></b>';c.querySelector('b').textContent=ws[i%ws.length];c.style.transform=`rotateY(${i*360/N}deg) translateZ(var(--r))`;ring.append(c);return c});sc.append(ring);s.append(sc);
  const tw=gsap.to(ring,{rotationY:-360,duration:24,ease:'none',repeat:-1});const dr=Draggable.create(el('div'),{trigger:sc,type:'x',onPress(){tw.pause();this.r0=gsap.getProperty(ring,'rotationY')},onDrag(){gsap.set(ring,{rotationY:this.r0+(this.x-this.startX)*.4})},onRelease(){const r=gsap.getProperty(ring,'rotationY');tw.progress(((-r%360)+360)%360/360).resume()}})[0];card._kill.push(()=>dr.kill())}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx306` rules from `site/fx.css`

_No dedicated `.fx306` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #306
