# 321 · Command Palette — 指令面板

Press ⌘K and a search panel pops up; as you type it filters the commands, the selected item lights up, and pressing Enter runs it

- Component: Layout · Pages (`layout`)
- Timing: Switch
- Tech: GSAP
- Uses: UI Interaction, App Interface
- Style / keywords: Command Palette Shortcut Search Cmd K Command Palette Spotlight Quick Search Layout Page
- Tag: GSAP timeline
- Example text: "" (stage background: dark, fixed text)
- Added: 2026-10-21

**AI prompt (English copy format):**

```text
"Command Palette (指令面板)" motion effect: A command palette like ⌘K: when the shortcut is pressed, the background blurs and darkens, and a search panel pops up at the top center of the screen (appearing by enlarging from a slightly smaller, slightly higher position); the input field has a blinking cursor, and all the commands are listed below; as the user types, the list filters in real time to keep only the matching items, and the first matching item lights up with an accent background color and shows a ↵ hint; pressing Enter makes that item flash once and closes the panel. (JS: a keydown listener for Meta/Ctrl + K opens it; an input event filters the list; CSS transitions the panel from opacity + scale(.95) → 1, and the background uses backdrop-filter:blur)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx321">`, preview text "". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Command Palette".

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
