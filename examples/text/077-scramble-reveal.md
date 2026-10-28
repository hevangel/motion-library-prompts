# 077 · 亂碼揭示 — Scramble Reveal

亂碼逐步解出正確文字

- 元件 Component: 文字 (`text`)
- 時機 Timing: 進場
- 技術 Tech: GSAP
- 情境 Uses: 標題・Hero、數字資訊
- 風格／關鍵字 Style: 
- 標籤 Tag: ScrambleText
- 範例文字 Example text: 「解碼完成」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「亂碼揭示（Scramble Reveal）」動態效果：文字先是一串不斷跳動的亂碼（片假名、符號、數字），由左到右逐步解出正確文字，亂碼與解出的字用不同顏色區分，停留後再打散。點陣字體。（GSAP：ScrambleTextPlugin，revealDelay、speed、newClass）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx77">`, preview text 「解碼完成」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「亂碼揭示」.

### JavaScript — `FX[77]` from `site/fx.js`

```js
77(s,x){const t=T(x);t.style.fontFamily='"DotGothic16",monospace';t.style.fontWeight=400;t.style.minHeight='1.15em';t.textContent='';s.append(t);const o={chars:'アイウエオカキク#%&01XZ',speed:.5,newClass:'r'};
  gsap.timeline({repeat:-1,repeatDelay:.3}).to(t,{duration:1.8,scrambleText:{...o,text:x,revealDelay:.4}}).to(t,{duration:.8,scrambleText:{...o,text:' '}},'+=1.4')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx77` rules from `site/fx.css`

```css
.fx77 .t{color:var(--a)}
.fx77 .t .r{color:#fff}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #77
