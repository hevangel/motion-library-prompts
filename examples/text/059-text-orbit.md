# 059 · 軌道 — Text Orbit

單字帶著景深繞圈

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: Logo・品牌
- 風格／關鍵字 Style: 3D 空間旋轉
- 標籤 Tag: Logo・標題
- 範例文字 Example text: 「軌道」（預覽底色：acc）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「軌道（Text Orbit）」動態效果：文字沿著一條橢圓虛線軌道繞圈，轉到前方時變大變清楚、轉到後方時變小變淡，呈現景深。約 5 秒繞一圈，Logo 標題感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx59">`, preview text 「軌道」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「軌道」.

### JavaScript — `FX[59]` from `site/fx.js`

```js
59(s,x,card){s.append(el('div','ell'));const o=el('div','ob');o.textContent=x;s.append(o);ticks.set(card,t=>{const W=s.offsetWidth;const a=t*1.3;const sc=.55+.45*(1+Math.sin(a))/2;o.style.transform=`translate(-50%,-50%) translate(${Math.cos(a)*W*.31}px,${Math.sin(a)*W*.08}px) scale(${sc})`;o.style.opacity=.45+.55*(1+Math.sin(a))/2;o.style.zIndex=Math.sin(a)>0?3:0})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx59` rules from `site/fx.css`

```css
.fx59 .ell{position:absolute;left:50%;top:50%;width:62cqw;height:16cqw;margin:-8cqw 0 0 -31cqw;border:.3cqw dashed #1115;border-radius:50%}
.fx59 .ob{position:absolute;left:50%;top:50%;font-weight:900;font-size:13cqw;color:#111;white-space:nowrap}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #59
