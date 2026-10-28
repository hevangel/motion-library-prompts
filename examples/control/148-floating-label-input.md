# 148 · 輸入框浮動標籤 — Floating Label Input

點進輸入框時，提示文字縮小浮到上方，底線從中間展開

- 元件 Component: 表單・控制項 (`control`)
- 時機 Timing: 懸停・點擊、進場
- 技術 Tech: CSS
- 情境 Uses: App 介面、介面互動
- 風格／關鍵字 Style: 輸入框 表單 標籤 浮動 聚焦 Floating Label Input Focus Form Material App 手機 行動裝置 微互動 Mobile App Micro-interaction
- 標籤 Tag: Floating label
- 範例文字 Example text: 「電子郵件」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「輸入框浮動標籤（Floating Label Input）」動態效果：表單輸入框平常只顯示一個像 placeholder 的提示標籤；點進去（focus）時，標籤縮小並往上浮到輸入框上方，同時底線從中央往兩側展開成強調色，游標開始閃爍；輸入內容後離開，標籤會保持在上方的小字狀態，清空時才回到原位。約 0.3–0.4 秒、減速。（CSS：label 絕對定位，用 :focus-within 或 :not(:placeholder-shown) 改變 top 與 font-size；底線用 transform:scaleX(0→1)）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx148">`, preview text 「電子郵件」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「輸入框浮動標籤」.

### JavaScript — `FX[148]` from `site/fx.js`

```js
148(s,x,card){const f=el('div','fli');f.innerHTML='<label></label><div class="val"><span class="tx"></span><i class="caret"></i></div><i class="ul"></i>';f.querySelector('label').textContent=x;s.append(f);const tx=f.querySelector('.tx');const word='hello@example.com';
  const cycle=()=>{f.classList.remove('fo','filled');tx.textContent='';setTimeout(()=>{f.classList.add('fo');[...word].forEach((c,i)=>setTimeout(()=>tx.textContent=word.slice(0,i+1),400+i*70))},500);setTimeout(()=>{f.classList.remove('fo');f.classList.add('filled')},500+400+word.length*70+900)};
  cycle();card._timers.push(setInterval(cycle,4600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx148` rules from `site/fx.css`

_No dedicated `.fx148` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #148
