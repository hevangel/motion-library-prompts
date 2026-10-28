# 323 · 即時時鐘 — Analog Clock

顯示現在時間的指針時鐘，秒針每秒跳一格並帶一點回彈

- 元件 Component: 圖形・SVG (`shape`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 數字資訊、介面互動
- 風格／關鍵字 Style: 時鐘 指針 秒針 即時 時間 Clock Analog Watch Time Real-time 圖形 SVG
- 標籤 Tag: JS rAF
- 範例文字 Example text: 「現在時間」（預覽底色：dark）
- 收錄日期 Added: 2026-10-21

**AI 提示詞（網站複製格式）:**

```text
「即時時鐘（Analog Clock）」動態效果：一個顯示目前真實時間的指針時鐘：錶面有 60 個刻度（每 5 格較粗較長），時針、分針連續平滑移動，秒針用強調色、每一秒跳一格，跳動時在約 0.15 秒內微微超過再彈回定位，像真的機械錶。（JS requestAnimationFrame：讀取 Date 的時分秒毫秒，計算各指針角度；秒針角度 = (秒 − 1 + 回彈曲線(毫秒/150)) × 6 度；SVG line 用 transform rotate）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx323">`, preview text 「現在時間」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「即時時鐘」.

### JavaScript — `FX[323]` from `site/fx.js`

```js
323(s,x,card){const w=el('div','sv-clk');w.innerHTML=`<svg viewBox="-50 -50 100 100"><circle r="46" class="f"/>${[...Array(60)].map((_,i)=>`<line y1="-43" y2="${i%5?-40.5:-38}" class="${i%5?'m':'h'}" transform="rotate(${i*6})"/>`).join('')}<line class="hh" y1="5" y2="-22"/><line class="mh" y1="7" y2="-32"/><g class="sh"><line y1="10" y2="-37"/><circle r="2.4"/></g><circle r="1.6" class="c"/></svg><b></b>`;w.querySelector('b').textContent=x;s.append(w);const [hh,mh,sh]=['.hh','.mh','.sh'].map(q=>w.querySelector(q));
  ticks.set(card,()=>{const d=new Date(),ms=d.getMilliseconds(),sec=d.getSeconds()+ms/1000,mn=d.getMinutes()+sec/60,hr=d.getHours()%12+mn/60;
    // 秒針：每秒跳一格並帶一點回彈（前 150ms 內完成）
    const st=Math.floor(sec),k=Math.min(1,ms/150),e=1+2.2*Math.pow(k-1,3)+1.2*Math.pow(k-1,2);sh.setAttribute('transform',`rotate(${(st-1+e)*6})`);mh.setAttribute('transform',`rotate(${mn*6})`);hh.setAttribute('transform',`rotate(${hr*30})`)})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx323` rules from `site/fx.css`

_No dedicated `.fx323` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #323
