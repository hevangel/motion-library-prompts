# 005 · 粒子消散 — Disintegrate

文字化為粒子消散

- 元件 Component: 文字 (`text`)
- 時機 Timing: 退場
- 技術 Tech: CSS
- 情境 Uses: 轉場切換
- 風格／關鍵字 Style: 消散退場
- 標籤 Tag: 消滅・戲劇
- 範例文字 Example text: 「消滅」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「粒子消散（Disintegrate）」動態效果：文字由左到右逐字變模糊、往右上飄散並淡出，同時周圍冒出許多小方塊粒子往外飄走，消失後再重新浮現。約 3 秒一輪，戲劇化。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx5">`, preview text 「消滅」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「粒子消散」.

### JavaScript — `FX[5]` from `site/fx.js`

```js
5(s,x){const w=el('div');w.style.position='relative';const t=split(x,18);w.append(t);for(let i=0;i<46;i++){const p=el('i','p');p.style.left=rnd(5,95)+'%';p.style.top=rnd(10,90)+'%';p.style.setProperty('--dx',rnd(5,40)+'cqw');p.style.setProperty('--dy',rnd(-25,5)+'cqw');p.style.animationDelay=(parseFloat(p.style.left)/100*.5)+'s';w.append(p)}s.append(w)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx5` rules from `site/fx.css`

```css
.fx5 .c{animation:dis 3s calc(var(--i)*.25s) infinite}
.fx5 .c:nth-child(1){color:var(--a)}
.fx5 .p{position:absolute;width:1.2cqw;height:1.2cqw;background:var(--a);opacity:0;animation:prt 3s infinite}
@keyframes dis{0%,25%{opacity:1;filter:none;transform:none}60%{opacity:0;filter:blur(6px);transform:translate(12%,-25%) scale(1.25)}85%{opacity:0;transform:none;filter:blur(6px)}100%{opacity:1;filter:none}}
@keyframes prt{0%,25%{opacity:0;transform:none}35%{opacity:1}70%{opacity:0;transform:translate(var(--dx),var(--dy))}100%{opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #5
