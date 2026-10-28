// ===== Language toggle 中文 / EN (added for this clone; not part of the original site) =====
// Chinese is the original language and the default. English strings for the
// 327 effects live in data_en.js (ITEMS_EN, built by tools/build_en.py from
// translations/en.json). The choice persists in localStorage ('ml-lang')
// and can be forced with ?lang=en / ?lang=zh.
// This script runs after app.js and reuses its globals (ITEMS, COMPS,
// WHENS, USES, COMP, WHEN, PALETTE, LATEST, cards, render, build,
// legacyCopy, showPrompt, $). Taxonomy labels are swapped in place, card
// meta is repainted, preview text/tag are swapped on the items themselves
// (so build()/teardown() pick them up), and the copy button produces the
// prompt in the current language.
(function () {
  const EN = typeof ITEMS_EN !== 'undefined' ? ITEMS_EN : {};
  const COMP_EN = { text: 'Text', button: 'Button', control: 'Form · Controls', card: 'Cards · Groups', media: 'Images · Media', shape: 'Shapes · SVG', bg: 'Background · Ambience', layout: 'Layout · Pages', cursor: 'Cursor' };
  const WHEN_EN = { enter: 'Entrance', exit: 'Exit', switch: 'Switch', loop: 'Loop · Idle', hover: 'Hover · Click', scroll: 'Scroll-triggered', drag: 'Drag Gesture' };
  const USE_EN = { hero: 'Headline · Hero', emph: 'Emphasis', data: 'Numbers & Data', bg: 'Background Decoration', trans: 'Transitions', logo: 'Logo · Brand', ui: 'UI Interaction', scroll: 'Scroll Effects', app: 'App Interface' };
  const PALETTE_EN = "\nColors: please match the website's existing theme colors and style yourself; do not specify any additional colors.";
  const ZH = {
    comps: COMPS.map(c => c[1]), whens: WHENS.map(w => w[1]), uses: Object.assign({}, USES),
    h1: document.querySelector('h1').innerHTML,
    sub: document.querySelector('.sub').innerHTML,
    by: document.querySelector('footer .by').innerHTML,
    footText: (() => { const f = document.querySelector('footer'); for (const n of f.childNodes) if (n.nodeType === 3 && n.textContent.includes('參考來源')) return n.textContent; return ''; })(),
    empty: $('empty').innerHTML
  };
  let lang = 'zh';
  try {
    const q = new URLSearchParams(location.search).get('lang');
    lang = q || localStorage.getItem('ml-lang') || 'zh';
    if (lang !== 'en') lang = 'zh';
  } catch (e) { lang = 'zh'; }

  ITEMS.forEach(it => {
    it._tagZh = it.tag; it._txtZh = it.txt;
    const e = EN[it.id] || {};
    it._q2 = [it.zh, it.en, it.desc, e.desc || '', it.tag, e.tag || '', it.style, e.style || '', it.tech,
      COMP[it.comp].label, COMP_EN[it.comp] || '', ...it.when.map(w => WHEN[w]), ...it.when.map(w => WHEN_EN[w] || ''),
      ...it.uses.map(u => USES[u]), ...it.uses.map(u => USE_EN[u] || ''), it.prompt, e.prompt || ''].join(' ').toLowerCase();
  });
  cards.forEach(c => { c._q = c._it._q2; });

  function promptFor(it) {
    const e = EN[it.id] || {};
    return lang === 'en'
      ? `"${it.en} (${it.zh})" motion effect: ${e.prompt || it.prompt}${PALETTE_EN}`
      : `「${it.zh}（${it.en}）」動態效果：${it.prompt}${PALETTE}`;
  }
  function copyFor(it, btn) {
    const t = promptFor(it);
    const label = lang === 'en' ? 'Copy AI Prompt' : '複製 AI 提示詞';
    const done = () => { btn.textContent = lang === 'en' ? 'Copied ✓' : '已複製 ✓'; setTimeout(() => btn.textContent = label, 1600); };
    (async () => {
      try { if (navigator.clipboard && window.isSecureContext) { await navigator.clipboard.writeText(t); return done(); } } catch (e) {}
      if (legacyCopy(t)) return done();
      showPrompt(t);
      if (lang === 'en') { const m = $('pm'); if (m) { m.querySelector('.pm-h').textContent = 'Auto-copy failed — please select all and copy manually (already selected for you)'; m.querySelector('button').textContent = 'Close'; } }
    })();
  }

  function paintCard(card) {
    const it = card._it, e = EN[it.id] || {};
    const badge = it.added === LATEST ? '<span class="new">NEW</span>' : '';
    card.querySelector('.nm').innerHTML = lang === 'en'
      ? `${it.en}　<span class="en">${it.zh}</span>${badge}`
      : `${it.zh}　<span class="en">${it.en}</span>${badge}`;
    card.querySelector('.zh').textContent = lang === 'en' ? (e.desc || it.desc) : it.desc;
    card.querySelector('.uses').innerHTML =
      [...it.when.map(w => `<em class="w">${WHEN[w]}</em>`), ...it.uses.map(u => `<em>${USES[u]}</em>`), `<em class="tech">${it.tech}</em>`].join('');
    const btn = card.querySelector('.cp');
    btn.textContent = lang === 'en' ? 'Copy AI Prompt' : '複製 AI 提示詞';
    btn.onclick = ev => copyFor(it, ev.target);
    const tagEl = card._st.querySelector('.tag');
    if (tagEl) tagEl.textContent = it.tag;
  }

  function setText(el, txt) { if (el) el.textContent = txt; }
  function setFirstText(el, txt) { if (!el) return; for (const n of el.childNodes) if (n.nodeType === 3 && n.textContent.trim()) { n.textContent = txt; return; } }
  function setLabel(labelEl, main, small) {
    if (!labelEl) return;
    setFirstText(labelEl, main);
    const sm = labelEl.querySelector('small'); if (sm) sm.textContent = small;
  }

  function paintStatic() {
    const en = lang === 'en';
    document.documentElement.lang = en ? 'en' : 'zh-Hant';
    document.title = en ? 'Motion Library — Motion Collection' : 'Motion Library 動態收藏';
    setText(document.querySelector('.kick'), en ? 'MOTION LIBRARY / MOTION COLLECTION' : 'MOTION LIBRARY / 動態收藏');
    const h1 = document.querySelector('h1');
    if (en) h1.innerHTML = 'Motion <b>Library</b>'; else h1.innerHTML = ZH.h1;
    const sub = document.querySelector('.sub');
    if (en) {
      sub.innerHTML = 'A collection of good-looking web motion effects — <b id="cnt"></b> in total. <span class="sub-more">Filter by component and timing together, e.g. “Button × Hover”, “Cards · Groups × Entrance”. Every tile is a schematic preview; click “Copy AI Prompt” to get a description of the look and how to build it. Interactive effects can be tried right here with your mouse, scrolling or dragging.</span>';
      $('cnt').textContent = ITEMS.length;
    } else { sub.innerHTML = ZH.sub; const c = $('cnt'); if (c) c.textContent = ITEMS.length; }
    $('q').placeholder = en ? 'Search names, descriptions or tags (e.g. flip, button, Bounce)' : '搜尋名稱、描述或標籤（例：翻牌、按鈕、Bounce）';
    $('q2').placeholder = en ? 'Search effects, tags…' : '搜尋效果、標籤…';
    $('custom').placeholder = en ? 'Custom preview text (blank = original sample)' : '自訂預覽文字（留空用原範例）';
    const tech = $('tech'); tech.options[0].textContent = en ? 'All technologies' : '全部技術';
    const sort = $('sort');
    sort.options[0].textContent = en ? 'Grouped by component' : '依元件分組';
    sort.options[1].textContent = en ? 'Newest first' : '最新收錄';
    setFirstText($('fTog'), en ? 'Filter ' : '篩選 ');
    setFirstText($('mFilt'), en ? 'Filter' : '篩選');
    setText($('mClear'), en ? 'Clear' : '清除');
    document.querySelectorAll('.fl-lab').forEach((el, i) => el.textContent = en ? ['Component', 'Timing', 'Use'][i] : ['元件', '時機', '情境'][i]);
    $('empty').innerHTML = en
      ? 'No effects have been collected for this combination yet.<br>Spotted a motion you like? Send it over and it can be added here!'
      : ZH.empty;
    setText(document.querySelector('#sub span'), en ? 'Submit an effect' : '我要投稿');
    // submission dialog
    setText(document.querySelector('#subDlg h3'), en ? 'Submit an effect to collect' : '投稿想收錄的效果');
    setText(document.querySelector('#subDlg p'), en ? 'Seen a good-looking motion effect? Tell me about it and I may add it to the collection.' : '看到好看的動態效果嗎？告訴我，我會考慮收錄進來。');
    const labels = document.querySelectorAll('#subDlg label');
    if (en) {
      setLabel(labels[0], 'Effect name or description', '');
      setLabel(labels[1], 'Reference link ', '(optional — website, video or Threads post)');
      setLabel(labels[2], 'Image or video ', '(optional, up to 3 files, 10MB total)');
      setLabel(labels[3], 'Your name ', '(optional)');
      const sn = $('sName'); if (sn) sn.placeholder = 'e.g. A button whose text ripples like water on hover';
      setText(document.querySelector('#sDrop span'), 'Click to choose, or drag files here');
    } else {
      setLabel(labels[0], '效果名稱或描述', '');
      setLabel(labels[1], '參考連結 ', '（選填，網站、影片、Threads 貼文都可以）');
      setLabel(labels[2], '圖片或影片 ', '（選填，最多 3 個，合計 10MB 以內）');
      setLabel(labels[3], '你的稱呼 ', '（選填）');
      const sn2 = $('sName'); if (sn2) sn2.placeholder = '例：滑過時文字會像水波一樣晃動的按鈕';
      setText(document.querySelector('#sDrop span'), '點這裡選擇，或把檔案拖進來');
    }
    setText($('subX'), en ? 'Cancel' : '取消');
    setText($('subGo'), en ? 'Submit' : '送出投稿');
    // footer
    const by = document.querySelector('footer .by');
    if (en) by.innerHTML = 'Collected and curated by <b>Hannah</b> (UI/UX Designer) · <a href="https://hannahchao-portfolio.vercel.app/" target="_blank" rel="noopener">See my portfolio →</a>';
    else by.innerHTML = ZH.by;
    const f = document.querySelector('footer');
    for (const n of f.childNodes) if (n.nodeType === 3 && (n.textContent.includes('參考來源') || n.textContent.includes('Sources:'))) {
      n.textContent = en
        ? 'Sources: threads.com/@ai_yunon_ai/post/DeeJRUjkXlM · threads.com/@ai_tjb/post/DeeHoA3ktZ5 · Names and descriptions are the original author’s curation; preview animations are schematic recreations, for personal reference and learning only. GSAP animations are self-made demos with GSAP 3.13; official docs: gsap.com/docs.'
        : ZH.footText;
    }
    document.querySelectorAll('#langToggle button').forEach(b => {
      const on = b.dataset.lang === lang;
      b.classList.toggle('on', on); b.setAttribute('aria-pressed', on);
    });
  }

  function postFix() {
    // strings app.js render() hardcodes in Chinese
    const total = cards.filter(c => c.style.display !== 'none').length;
    $('mCnt').textContent = lang === 'en' ? `Showing ${total} / ${cards.length}` : `顯示 ${total} / ${cards.length}`;
    if (lang === 'en') document.querySelectorAll('#sections .sec span').forEach(s => {
      const m = s.textContent.match(/\d+/); if (m) s.textContent = `${m[0]} effects`;
    });
    [['sComp', 'All components', '全部元件'], ['sWhen', 'All timings', '全部時機'], ['sUse', 'All uses', '全部情境'], ['sTech', 'All technologies', '全部技術']]
      .forEach(([id, en, zh]) => { const s = $(id); if (s && s.options[0]) s.options[0].textContent = lang === 'en' ? en : zh; });
    document.querySelectorAll('.chips').forEach(box => {
      const b = box.querySelector('.chip'); if (!b) return;
      for (const n of b.childNodes) if (n.nodeType === 3 && n.textContent.trim()) { n.textContent = lang === 'en' ? 'All' : '全部'; break; }
    });
  }

  const origRender = render;
  render = function () { origRender(); postFix(); };

  function apply(next, save) {
    lang = next === 'en' ? 'en' : 'zh';
    const en = lang === 'en';
    COMPS.forEach((c, i) => { c[1] = en ? COMP_EN[c[0]] : ZH.comps[i]; COMP[c[0]].label = c[1]; });
    WHENS.forEach((w, i) => { w[1] = en ? WHEN_EN[w[0]] : ZH.whens[i]; WHEN[w[0]] = w[1]; });
    Object.keys(USES).forEach(k => { USES[k] = en ? USE_EN[k] : ZH.uses[k]; });
    ITEMS.forEach(it => {
      const e = EN[it.id] || {};
      it.tag = en ? (e.tag || it._tagZh) : it._tagZh;
      it.txt = en ? (e.txt !== undefined ? e.txt : it._txtZh) : it._txtZh;
    });
    paintStatic();
    cards.forEach(paintCard);
    laidOut = ''; // force layout() to rebuild section headers in the new language
    origRender(); postFix();
    cards.forEach(c => { if (c._live) build(c); }); // re-run previews with the new sample text/tag
    if (save !== false) try { localStorage.setItem('ml-lang', lang); } catch (e) {}
  }

  document.querySelectorAll('#langToggle button').forEach(b =>
    b.addEventListener('click', () => { if (b.dataset.lang !== lang) apply(b.dataset.lang); }));
  if (lang === 'en') apply('en', false); else paintStatic();
})();
