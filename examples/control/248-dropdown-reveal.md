# 248 · 下拉選單展開 — Dropdown Reveal

點開下拉選單時面板從上方彈出，選項一個接一個滑入，箭頭翻轉

- 元件 Component: 表單・控制項 (`control`)
- 時機 Timing: 切換
- 技術 Tech: CSS
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 下拉選單 選單 展開 選項 依序 Dropdown Select Menu Stagger Reveal 表單 控制項
- 標籤 Tag: transition-delay
- 範例文字 Example text: 「台北 台中 高雄 花蓮 台南」（預覽底色：dark）
- 收錄日期 Added: 2026-10-19

**AI 提示詞（網站複製格式）:**

```text
「下拉選單展開（Dropdown Reveal）」動態效果：下拉選單：點擊選單按鈕時，右側箭頭翻轉 180 度，下方的選項面板從上緣帶點回彈地展開（scaleY 0.6 → 1、淡入），裡面的選項一個接一個（每個間隔約 0.05 秒）往下滑入淡入；滑過選項時背景淡淡亮起；選擇後面板收起、按鈕顯示選中的值。（CSS：面板 transform-origin:top，transition 用 cubic-bezier(.3,1.3,.5,1)；每個選項設 --i，展開時 transition-delay: calc(var(--i) × 0.05s)）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx248">`, preview text 「台北 台中 高雄 花蓮 台南」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「下拉選單展開」.

### JavaScript — `FX[248]` from `site/fx.js`

```js
248(s,x,card){const ws=words(x);const w=el('div','fm-dd');w.innerHTML='<button type="button" class="fm-dh"><span></span><svg viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></svg></button><ul></ul>';const sp=w.querySelector('.fm-dh span'),ul=w.querySelector('ul');sp.textContent=ws[0];
  ws.slice(0,4).forEach((t,i)=>{const li=el('li');li.style.setProperty('--i',i);li.textContent=t;li.onclick=()=>{real=Date.now();sp.textContent=t;w.classList.remove('open')};ul.append(li)});s.append(w);let real=0;
  w.querySelector('.fm-dh').onclick=()=>{real=Date.now();w.classList.toggle('open')};card._timers.push(setInterval(()=>{if(Date.now()-real<5000)return;w.classList.toggle('open')},1600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx248` rules from `site/fx.css`

_No dedicated `.fx248` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #248
