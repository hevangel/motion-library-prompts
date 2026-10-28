# 025 · 卡拉OK小球 — Karaoke Ball

小球跳動，逐字點亮

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 強調重點
- 風格／關鍵字 Style: 逐字律動
- 標籤 Tag: 歌曲・字幕
- 範例文字 Example text: 「ボールが跳ねる」（預覽底色：dark）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「卡拉OK小球（Karaoke Ball）」動態效果：一顆發光小球在文字上方一字一字往右跳，每落在一個字上，該字就從暗淡亮起並帶光暈，像卡拉 OK 字幕。每字約 0.38 秒，整句跳完後重來。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx25">`, preview text 「ボールが跳ねる」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「卡拉OK小球」.

### JavaScript — `FX[25]` from `site/fx.js`

```js
25(s,x,card){const w=el('div','w');const t=split(x);const ball=el('div','ball');w.append(t,ball);s.append(w);const cs=[...t.querySelectorAll('.c')];const per=.38,n=cs.length,cyc=n*per+1.2;
  ticks.set(card,tt=>{const ph=tt%cyc;const k=ph/per;const idx=Math.min(n-1,Math.floor(k));const fr=Math.min(1,k-idx);const c=cs[idx];if(!c)return;const cx=c.offsetLeft+c.offsetWidth/2;ball.style.left=cx+'px';ball.style.transform=`translateY(${-Math.sin(Math.PI*fr)*w.offsetHeight*.35}px)`;cs.forEach((e,i)=>e.classList.toggle('on',ph<n*per+1?i<=idx&&(i<idx||fr>.5):false))})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx25` rules from `site/fx.css`

```css
.fx25 .w{position:relative}
.fx25 .c{color:#555;transition:color .15s}
.fx25 .c.on{color:#fff;text-shadow:0 0 8px var(--a)}
.fx25 .ball{position:absolute;width:3cqw;height:3cqw;border-radius:50%;background:var(--a);top:-4cqw;margin-left:-1.5cqw;box-shadow:0 0 10px var(--a)}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #25
