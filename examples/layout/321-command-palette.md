# 321 · 指令面板 — Command Palette

按 ⌘K 跳出搜尋面板，邊打字邊篩選指令，選中的那項亮起、按 Enter 執行

- 元件 Component: 版面・頁面 (`layout`)
- 時機 Timing: 切換
- 技術 Tech: GSAP
- 情境 Uses: 介面互動、App 介面
- 風格／關鍵字 Style: 指令面板 快捷鍵 搜尋 Cmd K Command Palette Spotlight Quick Search 版面 頁面
- 標籤 Tag: GSAP timeline
- 範例文字 Example text: 「」（預覽底色：dark，固定文字）
- 收錄日期 Added: 2026-10-21

**AI 提示詞（網站複製格式）:**

```text
「指令面板（Command Palette）」動態效果：類似 ⌘K 的指令面板：按下快捷鍵時，背景模糊變暗，畫面上方中央彈出一個搜尋面板（從略小略高處放大出現），輸入框有閃爍游標，下方列出所有指令；使用者邊打字，清單即時篩選只留下符合的項目，第一個符合項目以強調底色亮起並顯示 ↵ 提示；按 Enter 時該項閃一下並關閉面板。（JS：keydown 監聽 Meta/Ctrl + K 開啟；input 事件篩選清單；CSS 面板 opacity + scale(.95) → 1 過渡、背景 backdrop-filter:blur）
配色：請依照網站既有的主題色與風格自行搭配，不要另外指定顏色。
```

## 範例實作 Example implementation

Preview stage: `<div class="stage dark fx321">`, preview text 「」. Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`) and searching 「指令面板」.

### JavaScript — `FX[321]` from `site/fx.js`

```js
321(s,x,card){const f=lyPage(s);f.insertAdjacentHTML('beforeend','<div class="pg-pc"><b>專案</b><i class="ly-bl"></i><i class="ly-bl s"></i></div><div class="pg-kb">⌘ K</div><div class="pg-cbd"></div><div class="pg-cp"><div class="pg-ci"><span>⌕</span><em></em><i class="pg-cur"></i></div><ul></ul></div>');
  const R=['新增專案','邀請成員','切換主題','開啟設定','搜尋文件','登出'];const ul=f.querySelector('.pg-cp ul');R.forEach(r=>{const li=el('li');li.innerHTML='<b></b><kbd>↵</kbd>';li.querySelector('b').textContent=r;ul.append(li)});const lis=[...ul.children],em=f.querySelector('.pg-ci em'),cp=f.querySelector('.pg-cp'),kb=f.querySelector('.pg-kb');
  const q='設定';const filt=t=>{lis.forEach(li=>li.style.display=!t||li.textContent.includes(t)?'':'none');const v=lis.filter(li=>li.style.display!=='none');lis.forEach(li=>li.classList.remove('on'));v[0]&&v[0].classList.add('on')};
  const tl=gsap.timeline({repeat:-1,repeatDelay:.8});tl.call(()=>{em.textContent='';filt('');f.classList.remove('pg-copen')}).to(kb,{scale:.85,duration:.1,yoyo:true,repeat:1},.6).call(()=>f.classList.add('pg-copen'),null,'+=.05');
  [...q].forEach((c,i)=>tl.call(()=>{em.textContent=q.slice(0,i+1);filt(q.slice(0,i+1))},null,'+='+(i?.25:.6)));tl.call(()=>lis.find(li=>li.classList.contains('on')).classList.add('hit'),null,'+=.7').call(()=>{lis.forEach(li=>li.classList.remove('hit'));f.classList.remove('pg-copen')},null,'+=.4').to({},{duration:1})}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx321` rules from `site/fx.css`

_No dedicated `.fx321` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #321
