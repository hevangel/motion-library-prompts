# 064 · 打字機 — Typewriter

一個字一個字打出來再換掉

- 元件 Component: 文字 (`text`)
- 時機 Timing: 切換
- 技術 Tech: CSS
- 情境 Uses: 標題・Hero、數字資訊
- 風格／關鍵字 Style: 文字切換 Canva 風格 Canva Typewriter 打字機
- 標籤 Tag: 故事・字幕
- 範例文字 Example text: 「天亮以前 再見」（預覽底色：cream）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「打字機（Typewriter）」動態效果：文字像打字機一樣一個字一個字出現在兩行，後面有閃爍的游標，打完停留後再快速逐字刪除，換成下一句繼續打。明體字、第二行較淡，打字約每字 0.14 秒。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage cream fx64">`, preview text 「天亮以前 再見」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「打字機」.

### JavaScript — `FX[64]` from `site/fx.js`

```js
64(s,x,card){const sets=[words(x),['說好的事','明天見']];const tw=el('div','tw');const l1=el('div'),l2=el('div');const cur=el('span','cur');tw.append(l1,l2);s.append(tw);let si=0,p=0,phase=0,hold=0;
  card._timers.push(setInterval(()=>{const set=sets[si%2];const full=set.join('\n');if(phase===0){p++;if(p>=chars(full).length){phase=1;hold=14}}else if(phase===1){if(--hold<=0)phase=2}else{p--;if(p<=0){phase=0;si++}}
    const sh=chars(full).slice(0,p).join('').split('\n');l1.textContent=sh[0]||'';l2.textContent=sh[1]||'';(sh.length>1?l2:l1).append(cur)},phase===2?60:140))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx64` rules from `site/fx.css`

```css
.fx64 .tw{font-family:"Noto Serif JP",serif;font-weight:400;font-size:9cqw;line-height:1.45;color:#111;width:76%}
.fx64 .tw div:nth-child(2){color:#999}
.fx64 .cur{display:inline-block;width:.4cqw;height:1em;background:#111;vertical-align:-10%;margin-left:.5cqw;animation:blink .8s steps(1) infinite}
@keyframes blink{50%{opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #64
