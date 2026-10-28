// 排除自己的瀏覽紀錄（Vercel Web Analytics），做法與作品集相同
// 每台裝置、每個瀏覽器開一次「網址?notrack」，之後這個瀏覽器的瀏覽都不送統計；「網址?track」解除。
// 記號存在 localStorage：無痕視窗、清除瀏覽資料、換瀏覽器都要重設一次。
(function(){
  var KEY='hannah-notrack';
  function read(){try{return localStorage.getItem(KEY)==='1'}catch(e){return false}}
  // Vercel Analytics 的指令佇列：script 還沒載入前呼叫的指令會先排隊
  window.va=window.va||function(){(window.vaq=window.vaq||[]).push(arguments)};
  // 有記號就整筆不送
  window.va('beforeSend',function(ev){return read()?null:ev});

  // 處理網址上的暗號，處理完從網址拿掉（不會被分享出去、也不會出現在統計網址裡）
  var url=new URL(location.href),off=url.searchParams.has('notrack'),on=url.searchParams.has('track');
  if(!off&&!on)return;
  try{if(off)localStorage.setItem(KEY,'1');else localStorage.removeItem(KEY)}catch(e){}
  url.searchParams.delete('notrack');url.searchParams.delete('track');
  history.replaceState(history.state,'',url.pathname+url.search+url.hash);
  var text=off?'已排除這個瀏覽器的瀏覽紀錄':'這個瀏覽器的瀏覽會重新計入統計';
  addEventListener('DOMContentLoaded',function(){
    var el=document.createElement('div');el.textContent=text;
    el.style.cssText='position:fixed;right:16px;bottom:16px;z-index:9999;padding:10px 16px;border-radius:999px;background:#c8f03c;color:#111;font:600 14px/1.4 "Noto Sans JP",sans-serif;box-shadow:0 8px 24px rgba(0,0,0,.35);transition:opacity .4s';
    document.body.appendChild(el);setTimeout(function(){el.style.opacity='0'},2600);setTimeout(function(){el.remove()},3100);
  });
})();
