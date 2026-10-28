# 047 · 擠壓彈跳 — Text Squeeze

像橡皮一樣壓扁再換字

- 元件 Component: 文字 (`text`)
- 時機 Timing: 切換
- 技術 Tech: CSS
- 情境 Uses: 強調重點、轉場切換
- 風格／關鍵字 Style: 逐字律動
- 標籤 Tag: 彈性・切換
- 範例文字 Example text: 「反彈 彈力」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「擠壓彈跳（Text Squeeze）」動態效果：文字像橡皮一樣被壓扁成一條線，再彈起拉高、回彈定位，停住後又壓扁，壓到最扁時換成下一個詞。約 1.5 秒一輪，彈性切換。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx47">`, preview text 「反彈 彈力」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「擠壓彈跳」.

### JavaScript — `FX[47]` from `site/fx.js`

```js
47(s,x){const ws=words(x);let i=0;const e=el('div','sq');e.textContent=ws[0];e.addEventListener('animationiteration',()=>{i++;e.textContent=ws[i%ws.length];e.style.color=i%2?'var(--a)':'#fff'});s.append(e)}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx47` rules from `site/fx.css`

```css
.fx47 .sq{font-weight:900;font-size:17cqw;color:#fff;transform-origin:50% 90%;animation:sq 1.5s infinite}
@keyframes sq{0%{transform:scale(1.45,.12)}18%{transform:scale(.82,1.28)}32%{transform:scale(1.1,.9)}44%,80%{transform:none}100%{transform:scale(1.45,.12)}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #47
