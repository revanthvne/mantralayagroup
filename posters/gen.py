# -*- coding: utf-8 -*-
import json

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800;900&family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,700;0,800;1,700;1,800&display=swap" rel="stylesheet">'
GRAD = 'linear-gradient(105deg,#A80B0B 0%,#D83000 46%,#F07800 100%)'
GRADTXT = 'background:linear-gradient(100deg,#FF6A2B,#F6921E 60%,#FFC46B);-webkit-background-clip:text;background-clip:text;color:transparent;'
GRADTXTD = 'background:linear-gradient(100deg,#A80B0B,#D83000 45%,#F07800);-webkit-background-clip:text;background-clip:text;color:transparent;'

def base(w,h,dark=True):
    bg = '#150B07' if dark else '#FBF4EB'
    fg = '#fff' if dark else '#10141B'
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8">{FONTS}<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{w}px;height:{h}px;overflow:hidden;position:relative;font-family:'Montserrat',sans-serif;background:{bg};color:{fg};display:flex;flex-direction:column}}
.hdr{{display:flex;align-items:center;justify-content:space-between;padding:34px 48px 0}}
.hdr img{{height:60px}}
.hdr .co{{font-size:19px;font-weight:800;letter-spacing:4px;color:{'rgba(255,255,255,0.75)' if dark else '#5A6472'}}}
.rule{{height:5px;background:{GRAD};position:absolute;top:0;left:0;right:0}}
.label{{font-size:19px;font-weight:800;letter-spacing:8px;color:#F6921E}}
.cap{{font-family:'Playfair Display',serif;font-weight:800;line-height:1.1;letter-spacing:-0.5px}}
.grid-bg{{position:absolute;inset:0;background:linear-gradient(rgba(255,255,255,0.025) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,0.025) 1px,transparent 1px);background-size:64px 64px;pointer-events:none}}
.glow{{position:absolute;width:70%;height:60%;border-radius:50%;background:radial-gradient(circle,rgba(216,60,0,0.18),transparent 65%);top:-10%;right:-10%;filter:blur(50px);pointer-events:none}}
.ftr{{margin-top:auto;background:{'#0C0605' if dark else '#150B07'};padding:16px 48px;display:flex;justify-content:space-between;align-items:center;font-family:'Inter',sans-serif;font-size:16px;font-weight:600;color:rgba(255,255,255,0.85)}}
.ftr b{{color:#F6921E}}
</style></head><body>"""

FOOT = '<div class="ftr"><span><b>+91 7095 303 303</b></span><span>www.mantralayagroup.com</span><span>info@mantralayagroup.com</span></div></body></html>'

def hdr(dark=True, co='MANTRALAYA GROUP'):
    logo = '../mg-logo-dark.png' if dark else '../mg-logo.png'
    return f'<div class="rule"></div><div class="hdr"><img src="{logo}"><div class="co">{co}</div></div>'

def brandgrid(w,h,label,cap,brands,cols,photos):
    ph = ''.join(f'<div class="pt"><img src="../products/{p}.jpg"></div>' for p in photos)
    bs = ''.join(f'<div class="b">{b}</div>' for b in brands)
    return base(w,h,True)+f"""<style>
.wrap{{padding:36px 48px 30px;display:flex;flex-direction:column;flex:1}}
.cap2{{font-size:52px;margin-top:12px}}
.bgrid{{margin-top:40px;display:grid;grid-template-columns:repeat({cols},1fr);gap:16px;flex:1;align-content:center}}
.b{{border:1px solid rgba(240,120,0,0.35);background:rgba(255,255,255,0.05);border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:800;letter-spacing:1px;padding:34px 10px;text-align:center}}
.pts{{position:absolute;right:48px;top:120px;display:flex;gap:14px;z-index:3}}
.pt{{width:96px;height:96px;border-radius:50%;overflow:hidden;border:3px solid #F07800}}
.pt img{{width:100%;height:100%;object-fit:cover}}
</style>{hdr(True)}<div class="grid-bg"></div><div class="glow"></div><div class="pts">{ph}</div>
<div class="wrap"><div class="label">{label}</div><div class="cap cap2">{cap}</div><div class="bgrid">{bs}</div></div>{FOOT}"""

def photoposter(w,h,label,cap,sub,photo):
    return base(w,h,True)+f"""<style>
.ph{{position:absolute;inset:0}}
.ph img{{width:100%;height:100%;object-fit:cover}}
.ph::after{{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(13,8,6,0.82) 0%,rgba(13,8,6,0.12) 38%,rgba(13,8,6,0.14) 55%,rgba(13,8,6,0.9) 82%,#0D0806 100%)}}
.hdr,.bt{{position:relative;z-index:2}}
.bt{{margin-top:auto;padding:0 44px 40px}}
.cap2{{font-size:{int(w*0.078)}px;margin-top:12px}}
.sub{{margin-top:14px;font-family:'Inter',sans-serif;font-size:{int(w*0.030)}px;font-weight:500;color:rgba(255,255,255,0.85);line-height:1.5}}
</style><div class="ph"><img src="../products/{photo}.jpg"></div>{hdr(True)}
<div class="bt"><div class="label">{label}</div><div class="cap cap2">{cap}</div><div class="sub">{sub}</div></div></body></html>"""

def appsposter(w,h,label,cap,cols_data,photos):
    cols = ''.join(f'<div class="col"><h4>{t}</h4>' + ''.join(f'<div class="it">{i}</div>' for i in items) + '</div>' for t,items in cols_data)
    ph = ''.join(f'<div class="pt"><img src="../products/{p}.jpg"></div>' for p in photos)
    return base(w,h,False)+f"""<style>
.wrap{{padding:28px 48px 24px;flex:1;display:flex;flex-direction:column}}
.cap2{{font-size:44px;margin-top:8px;color:#10141B}}
.cap2 em{{{GRADTXTD}font-style:italic}}
.cols{{margin-top:26px;display:flex;gap:26px;flex:1}}
.col{{flex:1;background:#fff;border-radius:16px;padding:22px 26px;box-shadow:0 10px 30px rgba(168,11,11,0.08);border-top:5px solid #D83000}}
.col h4{{font-size:21px;font-weight:800;letter-spacing:1px;color:#A80B0B;margin-bottom:12px}}
.it{{font-family:'Inter',sans-serif;font-size:17.5px;font-weight:500;color:#3A4250;padding:7px 0;border-bottom:1px solid rgba(16,20,27,0.06);line-height:1.35}}
.pts{{position:absolute;right:48px;top:150px;display:flex;gap:12px;z-index:3}}
.pt{{width:76px;height:76px;border-radius:50%;overflow:hidden;border:3px solid #F07800}}
.pt img{{width:100%;height:100%;object-fit:cover}}
</style>{hdr(False)}<div class="pts">{ph}</div>
<div class="wrap"><div class="label" style="color:#C43D00;">{label}</div><div class="cap cap2">{cap}</div><div class="cols">{cols}</div></div>{FOOT}"""

def duoposter(w,h,label,cap,sub,photos):
    ph = ''.join(f'<div class="tile"><img src="../products/{p}.jpg"></div>' for p in photos)
    return base(w,h,True)+f"""<style>
.wrap{{padding:30px 48px 26px;flex:1;display:flex;gap:40px;align-items:center}}
.lt{{flex:1.1}}
.cap2{{font-size:47px;margin-top:12px}}
.cap2 em{{{GRADTXT}font-style:italic}}
.sub{{margin-top:16px;font-family:'Inter',sans-serif;font-size:21px;font-weight:500;color:rgba(255,255,255,0.75);line-height:1.55}}
.tiles{{flex:1;display:grid;grid-template-columns:repeat(2,1fr);gap:16px}}
.tile{{border-radius:16px;overflow:hidden;border:3px solid rgba(240,120,0,0.7);aspect-ratio:1.25}}
.tile img{{width:100%;height:100%;object-fit:cover}}
</style>{hdr(True)}<div class="grid-bg"></div><div class="glow"></div>
<div class="wrap"><div class="lt"><div class="label">{label}</div><div class="cap cap2">{cap}</div><div class="sub">{sub}</div></div><div class="tiles">{ph}</div></div>{FOOT}"""

def collageposter(w,h,label,cap,sub,url,photos):
    ph = ''.join(f'<img src="../products/{p}.jpg">' for p in photos)
    return base(w,h,True)+f"""<style>
.coll{{position:absolute;inset:0;display:grid;grid-template-columns:repeat(2,1fr);grid-template-rows:repeat(3,1fr)}}
.coll img{{width:100%;height:100%;object-fit:cover}}
.coll::after{{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(13,8,6,0.85),rgba(13,8,6,0.45) 40%,rgba(13,8,6,0.92) 78%,#0D0806)}}
.hdr,.bt{{position:relative;z-index:2}}
.bt{{margin-top:auto;padding:0 52px 52px;text-align:center}}
.cap2{{font-size:76px}}
.cap2 em{{{GRADTXT}font-style:italic}}
.sub{{margin-top:16px;font-family:'Inter',sans-serif;font-size:27px;font-weight:500;color:rgba(255,255,255,0.85)}}
.pill{{display:inline-block;margin-top:30px;background:{GRAD};border-radius:100px;padding:22px 54px;font-size:31px;font-weight:800;letter-spacing:1px;box-shadow:0 14px 40px rgba(216,60,0,0.5)}}
</style><div class="coll">{ph}</div>{hdr(True)}
<div class="bt"><div class="label">{label}</div><div class="cap cap2">{cap}</div><div class="sub">{sub}</div><div class="pill">{url}</div></div></body></html>"""

def totem(w,h):
    brands_d = 'GAIL · BCPL · HMEL · HALDIA · OPAL<br>MRPL · HPCL · RELIANCE · NAYARA'
    brands_i = 'ARAMCO · BOROUGE · CABOT · CELANESE<br>CHEVRON PHILLIPS · EXXON MOBIL · FORMOSA<br>GC MARKETING · GULF POLYMERS · INEOS<br>LG CHEM · LYONDELL BASELL · MITSUBISHI<br>OQ (LUBAN) · SABIC · SCGC · WESTLAKE'
    tiles = ''.join(f'<div class="tt"><img src="../products/{p}.jpg"></div>' for p in ['coloured-granules','pigments'])
    return base(w,h,True)+f"""<style>
.wrap{{flex:1;display:flex;flex-direction:column;align-items:center;text-align:center;padding:44px 40px 0;position:relative;z-index:2}}
.wrap img.lg{{height:96px}}
.label2{{margin-top:36px;font-size:24px;font-weight:800;letter-spacing:10px;color:#F6921E}}
.cap2{{font-size:64px;margin-top:18px}}
.cap2 em{{{GRADTXT}font-style:italic}}
.tt{{width:330px;height:330px;border-radius:50%;overflow:hidden;border:6px solid;margin-top:44px}}
.tt:nth-of-type(1){{border-color:#A80B0B}}.tt:nth-of-type(2){{border-color:#D83000}}.tt:nth-of-type(3){{border-color:#F07800}}
.tt img{{width:100%;height:100%;object-fit:cover}}
.sec{{margin-top:46px;font-size:20px;font-weight:800;letter-spacing:6px;color:rgba(255,255,255,0.55)}}
.bl{{margin-top:14px;font-size:20px;font-weight:800;line-height:1.85;letter-spacing:0.5px}}
.stall{{margin-top:70px;background:{GRAD};border-radius:24px;padding:34px 46px;font-size:28px;font-weight:900;letter-spacing:2px;line-height:1.6;white-space:nowrap}}
</style><div class="grid-bg"></div><div class="glow"></div>
<div class="rule"></div>
<div class="wrap"><img class="lg" src="../mg-logo-dark.png">
<div class="label2">RAW MATERIALS</div>
<div class="cap cap2">Every polymer.<br><em>One counter.</em></div>
{tiles}
<div class="sec">DOMESTIC</div><div class="bl">{brands_d}</div>
<div class="sec">IMPORTED</div><div class="bl">{brands_i}</div>
<div class="stall">HIPLEX 2026<br>HALL 4<br>STALLS C 05 &amp; C 06</div>
</div><div class="ftr" style="justify-content:center;font-size:19px;"><span>www.mantralayagroup.com</span></div></body></html>"""

def message(w,h,label,cap,sub,extra='',dark=False,capsize=None):
    cs = capsize or int(w*0.045)
    return base(w,h,dark)+f"""<style>
.wrap{{flex:1;display:flex;flex-direction:column;justify-content:center;padding:20px 60px;position:relative;z-index:2}}
.cap2{{font-size:{cs}px;margin-top:14px;{'color:#fff' if dark else 'color:#10141B'}}}
.cap2 em{{{GRADTXT if dark else GRADTXTD}font-style:italic}}
.sub{{margin-top:18px;font-family:'Inter',sans-serif;font-size:{int(cs*0.42)}px;font-weight:500;color:{'rgba(255,255,255,0.8)' if dark else '#3A4250'};line-height:1.6;max-width:88%}}
.extra{{margin-top:26px}}
</style>{hdr(dark)}{'<div class="grid-bg"></div><div class="glow"></div>' if dark else ''}
<div class="wrap"><div class="label" style="{'color:#F6921E' if dark else 'color:#C43D00'}">{label}</div><div class="cap cap2">{cap}</div><div class="sub">{sub}</div>{extra}</div>{FOOT}"""

posters = {}
posters['poster-01-raw-domestic.html'] = (1500,900, brandgrid(1500,900,'RAW MATERIALS · DOMESTIC POLYMERS',
  "India's biggest polymer names. <em style='"+GRADTXT+"font-style:italic'>One trusted trader.</em>",
  ['GAIL','BCPL','HMEL','HALDIA','OPAL','MRPL','HPCL','RELIANCE','NAYARA'],3,['coloured-granules','natural-granules']))
posters['poster-02-raw-imported.html'] = (1650,900, brandgrid(1650,900,'RAW MATERIALS · IMPORTED POLYMERS',
  "Sourced from the world's finest. <em style='"+GRADTXT+"font-style:italic'>Delivered here.</em>",
  ['ARAMCO','BOROUGE','CABOT','CELANESE','CHEVRON PHILLIPS','EXXON MOBIL','FORMOSA','GC MARKETING','GULF POLYMERS','INEOS (INOVYN)','LG CHEM','LYONDELL BASELL','MITSUBISHI CORP.','OQ (LUBAN)','SABIC','SCGC','WESTLAKE','&amp; MORE'],6,['pigments']))
posters['poster-03-pigments.html'] = (700,1000, photoposter(700,1000,'PIGMENTS','Colour, mastered.','Organic &amp; inorganic pigments for every application.','pigments'))
posters['poster-04-moisture.html'] = (800,1000, photoposter(800,1000,'MOISTURE POWDER &amp; DANA','Dry. Consistent. Reliable.','Moisture powder &amp; moisture dana — quality you can measure.','natural-granules'))
posters['poster-05-masterbatch.html'] = (700,1000, photoposter(700,1000,'MASTER BATCHES','The right shade. Every batch.','White, black &amp; colour master batches.','coloured-granules'))
posters['poster-06-pp-apps.html'] = (1500,600, appsposter(1500,600,'POLYPROPYLENE (PP)','One granule. <em>A thousand products.</em>',
  [('Homopolymer',['Textile wraps &amp; garment bags','Woven sacks &amp; non-woven fabric','Thin-wall containers &amp; moulding']),
   ('Random Co-Polymer',['High-clarity bottles &amp; containers','House wares &amp; consumer products','Transparent packaging']),
   ('Impact Co-Polymer',['Furniture, caps &amp; closures','Luggage &amp; industrial components','Appliances &amp; automotive'])],['pp-bags','woven-sacks']))
posters['poster-07-pe-apps.html'] = (1500,600, appsposter(1500,600,'POLYETHYLENE (PE)','From woven sacks to <em>greenhouse films.</em>',
  [('Films &amp; Bags',['Blown film &amp; lamitube','Heavy-duty bags','Greenhouse &amp; canal-lining films']),
   ('Moulding',['Blow moulding up to 100 litres','Overhead tanks','Drip laterals']),
   ('Specialty',['Extrusion coating','Imported granules &amp; master batches','Adhesive lamination &amp; foam film'])],['greenhouse-films','stretch-film']))
posters['poster-08-sutli-ropes.html'] = (1500,600, duoposter(1500,600,'END PRODUCTS','Sutli, ropes &amp; twine — <em>every budget.</em>',
  'Manufactured under multiple brands with various qualities and price ranges.',['plastic-sutli','ropes']))
posters['poster-09-bags.html'] = (1500,600, duoposter(1500,600,'END PRODUCTS','Bags for <em>every business.</em>',
  'PP &amp; PE bags · BOPP bags · Non-woven bags · Garment &amp; jewellery packing',['pp-bags','non-woven-bags','garment-bags','bopp-bags']))
posters['poster-10-films.html'] = (1000,1000, photoposter(1000,1000,'POLY FILMS','Films that protect what you make.','Treated rolls · Stretch film · Packaging films','treated-rolls'))
posters['poster-11-pands.html'] = (1000,1500, collageposter(1000,1500,'PRODUCTS &amp; STORES','Everything plastic.<br><em>Off the shelf.</em>',
  'Retail &amp; bulk — explore the full catalogue.','productsandstores.com',['coloured-granules','plastic-sutli','pp-bags','pigments','ropes','non-woven-bags']))
posters['poster-12-totem.html'] = (600,2133, totem(600,2133))
posters['poster-13-credit-1.html'] = (1500,750, message(1500,750,'CREDIT FACILITY','Your growth. <em>Our credit.</em>',
  'Flexible credit facilities for trusted trade partners — built on 35+ years of relationships. Talk to our team today.'))
posters['poster-15-credit-2.html'] = (900,750, message(900,750,'CREDIT FACILITY','Terms that move <em>with your business.</em>',
  'Credit cycles tailored to your trade. Ask us how.',capsize=52))
posters['poster-17-pands-qr.html'] = (900,750, message(900,750,'PRODUCTS &amp; STORES','Take the store <em>with you.</em>',
  'Scan to browse the complete catalogue at productsandstores.com.',
  extra='<div class="extra"><img src="qr-ps.png" style="width:190px;height:190px;border-radius:14px;border:5px solid #D83000;"></div>',capsize=52))
posters['poster-14-trust.html'] = (1650,750, message(1650,750,'THE MANTRALAYA GROUP','Trust, <em>measured.</em>',
  '',dark=True,capsize=72,extra='''<div class="extra" style="display:flex;gap:26px;">
  <div style="flex:1;border:1px solid rgba(240,120,0,0.4);border-radius:18px;padding:26px;text-align:center;"><div style="font-size:58px;font-weight:900;'''+GRADTXT+'''">35+</div><div style="margin-top:6px;font-size:18px;font-weight:700;letter-spacing:3px;color:rgba(255,255,255,0.7);">YEARS IN POLYMERS</div></div>
  <div style="flex:1;border:1px solid rgba(240,120,0,0.4);border-radius:18px;padding:26px;text-align:center;"><div style="font-size:58px;font-weight:900;'''+GRADTXT+'''">2300+</div><div style="margin-top:6px;font-size:18px;font-weight:700;letter-spacing:3px;color:rgba(255,255,255,0.7);">CLIENTS SERVED</div></div>
  <div style="flex:1;border:1px solid rgba(240,120,0,0.4);border-radius:18px;padding:26px;text-align:center;"><div style="font-size:58px;font-weight:900;'''+GRADTXT+'''">6</div><div style="margin-top:6px;font-size:18px;font-weight:700;letter-spacing:3px;color:rgba(255,255,255,0.7);">GROUP COMPANIES</div></div></div>'''))
posters['poster-19-promise.html'] = (1500,750, message(1500,750,'MANTRALAYA GROUP &amp; SREE RAVITEJA POLYMERS LIMITED',
  '&ldquo;We deliver <em>what we promise.&rdquo;</em>','35+ years of consistent supply, honest pricing and relationships that last.',dark=True,capsize=76))
posters['poster-20-branches.html'] = (1650,750, message(1650,750,'OUR NETWORK','Wherever you build, <em>we&rsquo;re nearby.</em>',
  '',extra='''<div class="extra" style="display:flex;flex-wrap:wrap;gap:14px;">'''+
  ''.join(f'<span style="background:#fff;border:1px solid rgba(16,20,27,0.1);border-radius:100px;padding:14px 28px;font-size:21px;font-weight:700;box-shadow:0 6px 18px rgba(0,0,0,0.05);">{c}</span>' for c in ['Hyderabad','Guntur','Visakhapatnam','Z. Medapadu','Tenali','Vijayawada','Nellore'])+
  '<span style="background:'+GRAD+';color:#fff;border-radius:100px;padding:14px 28px;font-size:21px;font-weight:800;">Upcoming: Bengaluru &amp; Chennai</span></div>'))

manifest = {}
for fn,(w,h,html) in posters.items():
    open(fn,'w').write(html)
    manifest[fn] = (w,h)
json.dump(manifest, open('manifest.json','w'))
print('wrote', len(posters), 'posters')
