# 179 · Water Ripple — 水波漣漪

Wherever the cursor glides or clicks, the screen ripples like a water surface

- Component: Background · Ambience (`bg`)
- Timing: Hover · Click
- Tech: Canvas
- Uses: Background Decoration, Headline · Hero
- Style / keywords: water ripples water surface ripples refraction Water Ripple Wave Refraction Liquid Canvas particles particles requestAnimationFrame interactive background
- Tag: Canvas pixels
- Example text: "Water Surface" (stage background: dark)
- Added: 2026-10-17

**AI prompt (English copy format):**

```text
"Water Ripple (水波漣漪)" motion effect: The whole section is like a sheet of water. As the cursor glides over it, it creates small ripples along its path; clicking creates larger ripples. The ripples spread outward, interfere with each other and gradually calm down, and the graphics and text beneath the water surface are refractively distorted along with the ripples; when there is no interaction, a drop of water occasionally falls automatically. (Canvas: on a low resolution, use two height buffers to run the classic water ripple algorithm next = (average of the four neighbors × 2 − prev) × damping; when drawing, offset the sampling of the base image's pixels according to the height gradient, then scale up to the canvas)
Colors: please match the website's existing theme colors and style yourself; do not specify any additional colors.
```

## Example implementation

Preview stage: `<div class="stage dark fx179">`, preview text "Water Surface". Run it live by opening `site/index.html` (serve the folder, e.g. `python3 -m http.server`), switching to EN, and searching "Water Ripple".

### JavaScript — `FX[179]` from `site/fx.js`

```js
179(s,x,card){cfx(s,card,{init:(c,W,H,m)=>{const g=2,gw=Math.ceil(W/g),gh=Math.ceil(H/g),base=document.createElement('canvas');base.width=gw;base.height=gh;const b=base.getContext('2d');
    const gr=b.createLinearGradient(0,0,gw,gh);gr.addColorStop(0,'#0f3d4c');gr.addColorStop(1,'#1d8a8a');b.fillStyle=gr;b.fillRect(0,0,gw,gh);b.strokeStyle='rgba(255,255,255,.08)';for(let i=0;i<gw;i+=8){b.beginPath();b.moveTo(i,0);b.lineTo(i,gh);b.stroke()}
    b.fillStyle='#fff';b.font=`900 ${Math.min(gh*.4,gw*1.4/Math.max(2,chars(x).length))}px "Noto Sans JP",sans-serif`;b.textAlign='center';b.textBaseline='middle';b.fillText(x,gw/2,gh/2);
    const out=document.createElement('canvas');out.width=gw;out.height=gh;const ocx=out.getContext('2d');
    const o={g,gw,gh,src:b.getImageData(0,0,gw,gh).data,out,ocx,img:ocx.createImageData(gw,gh),a:new Float32Array(gw*gh),b:new Float32Array(gw*gh),drop:0};
    m.click=(px,py)=>drop(o,px/g,py/g,90);return o},
  frame:(c,W,H,t,dt,m,o)=>{const{gw,gh}=o;if(m.in&&Math.hypot(m.x-m.px,m.y-m.py)>1)drop(o,m.x/o.g,m.y/o.g,40);else if(!m.in){o.drop+=dt;if(o.drop>.7){o.drop=0;drop(o,rnd(.15,.85)*gw,rnd(.2,.8)*gh,110)}}
    const A=o.a,B=o.b;for(let y=1;y<gh-1;y++)for(let x=1;x<gw-1;x++){const i=y*gw+x;B[i]=((A[i-1]+A[i+1]+A[i-gw]+A[i+gw])/2-B[i])*.965}o.a=B;o.b=A;
    const d=o.img.data,S=o.src,C=o.a;for(let y=1;y<gh-1;y++)for(let x=1;x<gw-1;x++){const i=y*gw+x,dx=(C[i-1]-C[i+1])*.12,dy=(C[i-gw]-C[i+gw])*.12;const sx=Math.min(gw-1,Math.max(0,x+dx|0)),sy=Math.min(gh-1,Math.max(0,y+dy|0)),j=(sy*gw+sx)*4,k=i*4,sh=dx*2;
      d[k]=S[j]+sh;d[k+1]=S[j+1]+sh;d[k+2]=S[j+2]+sh;d[k+3]=255}o.ocx.putImageData(o.img,0,0);c.drawImage(o.out,0,0,W,H)}});
  function drop(o,x,y,v){x|=0;y|=0;for(let j=-2;j<=2;j++)for(let i=-2;i<=2;i++){const xx=x+i,yy=y+j;if(xx>0&&yy>0&&xx<o.gw-1&&yy<o.gh-1)o.a[yy*o.gw+xx]+=v*(1-Math.hypot(i,j)/3)}}}
```

Helpers used by these functions (`T`, `split`, `el`, `rnd`, `chars`, `ticks`, GSAP helpers, …) are defined at the top of `site/fx.js`.

### CSS — direct `.fx179` rules from `site/fx.css`

_No dedicated `.fx179` rules — this effect is driven by its JavaScript above and/or the shared category CSS (class prefixes such as `ly-`, `kd-`, `bga-`, `bx-`, `fm-`, `cr-`, `md-`, `sx-`, `ho-`, `tx-`, `cg-`, `pg-`, `sv-`) in `site/fx.css`._

Source: https://kittenjam-motion-library.vercel.app/ — item #179
