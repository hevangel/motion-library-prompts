# 033 · 文字漩渦 — Text Spiral

文字沿漩渦旋轉

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 背景裝飾、轉場切換
- 風格／關鍵字 Style: 3D 空間旋轉
- 標籤 Tag: 奇幻・吸入
- 範例文字 Example text: 「うずまき」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「文字漩渦（Text Spiral）」動態效果：文字沿螺旋線排列，從中心小字逐漸往外變大，整個漩渦持續旋轉，字的透明度輪流明暗。約 9 秒轉一圈，奇幻吸入感。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx33">`, preview text 「うずまき」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「文字漩渦」.

### JavaScript — `FX[33]` from `site/fx.js`

```js
33(s,x){const sp=el('div','sp');const cs=chars(x);for(let i=0;i<46;i++){const e=el('span');e.textContent=cs[i%cs.length];const a=i*.48,r=2.5+i*.85;e.style.fontSize=(1.6+i*.09)+'cqw';e.style.transform=`rotate(${a}rad) translate(${r}cqw,0) rotate(90deg)`;e.style.color=i%3?'#fff':'var(--a)';e.style.animationDelay=(-i*.15)+'s';sp.append(e)}s.append(sp)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx33` rules from `site/fx.css`

```css
.fx33 .sp{position:absolute;left:50%;top:50%;width:0;height:0;animation:spin 9s linear infinite}
.fx33 .sp span{position:absolute;left:0;top:0;font-weight:900;transform-origin:0 0;line-height:1;animation:sin 9s linear infinite}
@keyframes sin{0%,100%{opacity:.35}50%{opacity:1}}
@keyframes spin{to{transform:rotate(360deg)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #33
