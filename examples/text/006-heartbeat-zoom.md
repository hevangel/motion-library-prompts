# 006 · 心跳放大 — Heartbeat Zoom

隨心跳放大並擴散波紋

- 元件 Component: 文字 (`text`)
- 時機 Timing: 循環待機
- 技術 Tech: CSS
- 情境 Uses: 強調重點
- 風格／關鍵字 Style: 衝擊登場
- 標籤 Tag: 感動・戲劇
- 範例文字 Example text: 「鼓動」（預覽底色：acc）
- 收錄日期 Added: 2026-10-15

**AI 提示詞（網站複製格式）:**

```text
「心跳放大（Heartbeat Zoom）」動態效果：文字像心跳一樣「咚咚」連續放大兩次再回原尺寸，每次跳動同時從中心擴散出兩圈圓形波紋並淡出。約 1.3 秒一拍。
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage acc fx6">`, preview text 「鼓動」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「心跳放大」.

### JavaScript — `FX[6]` from `site/fx.js`

```js
6(s,x){s.append(el('div','ring'),el('div','ring b'),T(x,18))}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx6` rules from `site/fx.css`

```css
.fx6 .t{animation:beat 1.3s infinite}
.fx6 .ring{position:absolute;left:50%;top:50%;width:30cqw;height:30cqw;margin:-15cqw 0 0 -15cqw;border:2px solid #111;border-radius:50%;animation:rng 1.3s infinite ease-out;opacity:0}
.fx6 .ring.b{animation-delay:.18s}
@keyframes beat{0%{transform:scale(1)}12%{transform:scale(1.2)}24%{transform:scale(1)}36%{transform:scale(1.12)}60%,100%{transform:scale(1)}}
@keyframes rng{0%{transform:scale(.4);opacity:.7}100%{transform:scale(2.6);opacity:0}}
```

Source: https://kittenjam-motion-library.vercel.app/ — item #6
