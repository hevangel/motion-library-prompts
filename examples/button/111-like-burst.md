# 111 · 愛心按讚爆開 — Like Burst

點擊愛心時彈跳放大，周圍噴出小圓點與光圈

- 元件 Component: 按鈕 (`button`)
- 時機 Timing: 懸停・點擊、進場
- 技術 Tech: CSS
- 情境 Uses: 介面互動
- 風格／關鍵字 Style: 按鈕 按讚 喜歡 愛心 點擊 回饋 微互動 Like Heart Burst Micro-interaction Twitter
- 標籤 Tag: CSS keyframes
- 範例文字 Example text: 「喜歡」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「愛心按讚爆開（Like Burst）」動態效果：點擊「喜歡」按鈕時，空心愛心瞬間填滿並從小彈跳放大，同時從愛心周圍往外噴出 8 顆小圓點、擴散一圈光環後消失，旁邊的數字 +1；再點一次取消，愛心變回空心、數字 −1。整段約 0.5 秒，有彈性回饋感。（CSS：切換 .on class；愛心用 scale 彈跳 keyframes，小圓點用 rotate(var(--r)) translateY 向外飛並縮小淡出，光環用 scale + opacity；重播前先移除 class 並觸發 reflow）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx111">`, preview text 「喜歡」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「愛心按讚爆開」.

### JavaScript — `FX[111]` from `site/fx.js`

```js
111(s,x,card){const b=el('button','like');b.innerHTML='<span class="hw"><i class="ring"></i>'+[...Array(8)].map((_,i)=>`<i class="p" style="--r:${i*45}deg"></i>`).join('')+'<svg viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg></span><span class="lt"></span><span class="ct">128</span>';
  b.querySelector('.lt').textContent=x;s.append(b);const ct=b.querySelector('.ct');let real=false;
  const tog=()=>{const on=!b.classList.contains('on');b.classList.remove('on');void b.offsetWidth;b.classList.toggle('on',on);ct.textContent=on?129:128};
  b.onclick=tog;b.addEventListener('pointerenter',()=>real=true);b.addEventListener('pointerleave',()=>real=false);card._timers.push(setInterval(()=>{if(!real)tog()},1600))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx111` rules from `site/fx.css`

_No dedicated `.fx111` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #111
