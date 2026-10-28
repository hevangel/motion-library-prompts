# 143 · 底部抽屜 — Bottom Sheet

背景變暗，選單從底部帶一點彈性滑上來

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 進場、退場
- 技術 Tech: GSAP
- 情境 Uses: App 介面、介面互動
- 風格／關鍵字 Style: 底部抽屜 底部選單 彈出 分享 動作選單 Bottom Sheet Action Sheet Drawer Modal App 手機 行動裝置 微互動 Mobile App Micro-interaction
- 標籤 Tag: Bottom sheet
- 範例文字 Example text: 「分享到」（預覽底色：dark）
- 收錄日期 Added: 2026-10-16

**AI 提示詞（網站複製格式）:**

```text
「底部抽屜（Bottom Sheet）」動態效果：點擊「分享」等操作後，畫面加上一層半透明遮罩逐漸變暗，選單面板從螢幕底部滑上來並帶一點點回彈（約 0.6 秒），面板頂端有一條小把手，裡面的選項依序從下方 8px 淡入；關閉時面板快速往下滑出（約 0.35 秒、加速）、遮罩淡出。（GSAP：面板 yPercent 100→0，ease back.out(1.1)；選項 stagger 0.06；關閉用 power2.in；實際 App 可讓使用者拖曳把手往下關閉）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx143">`, preview text 「分享到」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「底部抽屜」.

### JavaScript — `FX[143]` from `site/fx.js`

```js
143(s,x){const ph=phone(s);const list=el('div','pl');for(let i=0;i<6;i++)list.append(mrow(i));const bd=el('i','bd');const sh=el('div','sh2');sh.innerHTML='<i class="hd3"></i><b></b>'+[0,1,2].map(()=>'<div class="op"><i></i><span></span></div>').join('');sh.querySelector('b').textContent=x;ph.append(list,bd,sh);
  gsap.timeline({repeat:-1,repeatDelay:.5}).set(sh,{yPercent:100},0).set(bd,{opacity:0},0).to(bd,{opacity:.55,duration:.35},.4).to(sh,{yPercent:0,duration:.6,ease:'back.out(1.1)'},.4)
    .fromTo(sh.querySelectorAll('.op'),{y:8,opacity:0},{y:0,opacity:1,duration:.4,stagger:.06,ease:'power2.out'},.65).to(sh,{yPercent:100,duration:.35,ease:'power2.in'},'+=1.6').to(bd,{opacity:0,duration:.3},'<')}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx143` rules from `site/fx.css`

_No dedicated `.fx143` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #143
