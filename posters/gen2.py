# -*- coding: utf-8 -*-
"""Poster generator v2 — dark + light variants, photographic backgrounds."""
import json

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800;900&family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,700;0,800;1,700;1,800&display=swap" rel="stylesheet">'
GRAD = 'linear-gradient(105deg,#A80B0B 0%,#D83000 46%,#F07800 100%)'
GT_W = 'background:linear-gradient(100deg,#FF6A2B,#F6921E 60%,#FFC46B);-webkit-background-clip:text;background-clip:text;color:transparent;'
GT_D = 'background:linear-gradient(100deg,#A80B0B,#D83000 45%,#F07800);-webkit-background-clip:text;background-clip:text;color:transparent;'

def P(p): return f'../../products/{p}.jpg'

def base(w,h,dark):
    bg = '#150B07' if dark else '#FBF4EB'
    fg = '#fff' if dark else '#10141B'
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8">{FONTS}<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:{w}px;height:{h}px;overflow:hidden;position:relative;font-family:'Montserrat',sans-serif;background:{bg};color:{fg};display:flex;flex-direction:column}}
.hdr{{display:flex;align-items:center;justify-content:space-between;padding:34px 48px 0;position:relative;z-index:5}}
.hdr img{{height:60px}}
.hdr .co{{font-size:19px;font-weight:800;letter-spacing:4px;color:{'rgba(255,255,255,0.78)' if dark else '#5A6472'}}}
.rule{{height:5px;background:{GRAD};position:absolute;top:0;left:0;right:0;z-index:6}}
.label{{font-size:19px;font-weight:800;letter-spacing:8px;color:{'#F6921E' if dark else '#C43D00'}}}
.cap{{font-family:'Playfair Display',serif;font-weight:800;line-height:1.1;letter-spacing:-0.5px}}
.ftr{{margin-top:auto;background:{'rgba(12,6,5,0.94)' if dark else '#150B07'};padding:16px 48px;display:flex;justify-content:space-between;align-items:center;font-family:'Inter',sans-serif;font-size:16px;font-weight:600;color:rgba(255,255,255,0.85);position:relative;z-index:5}}
.ftr b{{color:#F6921E}}
.bgimg{{position:absolute;inset:0;z-index:0}}
.bgimg img{{width:100%;height:100%;object-fit:cover}}
.bgimg::after{{content:'';position:absolute;inset:0;background:{'linear-gradient(100deg, rgba(18,9,6,0.97) 0%, rgba(18,9,6,0.93) 45%, rgba(18,9,6,0.72) 100%)' if dark else 'linear-gradient(100deg, rgba(251,244,235,0.97) 0%, rgba(251,244,235,0.94) 45%, rgba(251,244,235,0.72) 100%)'}}}
.z{{position:relative;z-index:4}}
</style></head><body>"""

FOOT = '<div class="ftr"><span><b>+91 7095 303 303</b></span><span>www.mantralayagroup.com</span><span>info@mantralayagroup.com</span></div></body></html>'

def hdr(dark, co='MANTRALAYA GROUP'):
    logo = '../../mg-logo-dark.png' if dark else '../../mg-logo.png'
    return f'<div class="rule"></div><div class="hdr"><img src="{logo}"><div class="co">{co}</div></div>'

def bgimg(photo): return f'<div class="bgimg"><img src="{P(photo)}"></div>'

# ---------- templates (each takes dark:bool) ----------
def brandgrid(w,h,dark,label,cap,brands,cols,bgphoto,circles=None):
    card = 'rgba(255,255,255,0.06);border:1px solid rgba(240,120,0,0.4)' if dark else '#ffffff;border:1px solid rgba(168,11,11,0.15);box-shadow:0 8px 24px rgba(168,11,11,0.07)'
    bs = ''.join(f'<div class="b">{b}</div>' for b in brands)
    ph = ''.join(f'<div class="pt"><img src="{P(p)}"></div>' for p in (circles or []))
    return base(w,h,dark)+f"""<style>
.wrap{{padding:36px 48px 30px;display:flex;flex-direction:column;flex:1}}
.cap2{{font-size:52px;margin-top:12px;max-width:72%}}
.cap2 em{{{GT_W if dark else GT_D}font-style:italic}}
.bgrid{{margin-top:40px;display:grid;grid-template-columns:repeat({cols},1fr);gap:16px;flex:1;align-content:center}}
.b{{background:{card};border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:800;letter-spacing:1px;padding:34px 10px;text-align:center}}
.pts{{position:absolute;right:48px;top:130px;display:flex;gap:16px;z-index:5}}
.pt{{width:118px;height:118px;border-radius:50%;overflow:hidden;border:4px solid #F07800;box-shadow:0 10px 28px rgba(0,0,0,0.35)}}
.pt img{{width:100%;height:100%;object-fit:cover}}
</style>{bgimg(bgphoto)}{hdr(dark)}<div class="pts">{ph}</div>
<div class="wrap z"><div class="label">{label}</div><div class="cap cap2">{cap}</div><div class="bgrid">{bs}</div></div>{FOOT}"""

def photoposter(w,h,dark,label,cap,sub,photo):
    ov = ('linear-gradient(180deg,rgba(13,8,6,0.84) 0%,rgba(13,8,6,0.1) 36%,rgba(13,8,6,0.12) 55%,rgba(13,8,6,0.92) 82%,#0D0806 100%)' if dark
          else 'linear-gradient(180deg,rgba(251,244,235,0.92) 0%,rgba(251,244,235,0.08) 36%,rgba(251,244,235,0.1) 55%,rgba(251,244,235,0.94) 82%,#FBF4EB 100%)')
    fg = '#fff' if dark else '#10141B'
    return base(w,h,dark)+f"""<style>
.ph{{position:absolute;inset:0}}
.ph img{{width:100%;height:100%;object-fit:cover}}
.ph::after{{content:'';position:absolute;inset:0;background:{ov}}}
.bt{{margin-top:auto;padding:0 44px 40px;position:relative;z-index:4}}
.cap2{{font-size:{int(w*0.078)}px;margin-top:12px;color:{fg}}}
.sub{{margin-top:14px;font-family:'Inter',sans-serif;font-size:{int(w*0.030)}px;font-weight:500;color:{'rgba(255,255,255,0.85)' if dark else '#3A4250'};line-height:1.5}}
</style><div class="ph"><img src="{P(photo)}"></div>{hdr(dark)}
<div class="bt"><div class="label">{label}</div><div class="cap cap2">{cap}</div><div class="sub">{sub}</div></div></body></html>"""

def appsposter(w,h,dark,label,cap,cols_data,bgphoto):
    cardbg = 'rgba(24,12,8,0.92);border-top:5px solid #F07800' if dark else '#fff;border-top:5px solid #D83000;box-shadow:0 10px 30px rgba(168,11,11,0.08)'
    it = 'rgba(255,255,255,0.8)' if dark else '#3A4250'
    hcol = '#F6921E' if dark else '#A80B0B'
    cols = ''.join(f'<div class="col"><h4>{t}</h4>' + ''.join(f'<div class="it">{i}</div>' for i in items) + '</div>' for t,items in cols_data)
    return base(w,h,dark)+f"""<style>
.wrap{{padding:28px 48px 24px;flex:1;display:flex;flex-direction:column}}
.cap2{{font-size:44px;margin-top:8px}}
.cap2 em{{{GT_W if dark else GT_D}font-style:italic}}
.cols{{margin-top:26px;display:flex;gap:26px;flex:1}}
.col{{flex:1;background:{cardbg};border-radius:16px;padding:22px 26px}}
.col h4{{font-size:21px;font-weight:800;letter-spacing:1px;color:{hcol};margin-bottom:12px}}
.it{{font-family:'Inter',sans-serif;font-size:17.5px;font-weight:500;color:{it};padding:7px 0;border-bottom:1px solid {'rgba(255,255,255,0.08)' if dark else 'rgba(16,20,27,0.06)'};line-height:1.35}}
</style>{bgimg(bgphoto)}{hdr(dark)}
<div class="wrap z"><div class="label">{label}</div><div class="cap cap2">{cap}</div><div class="cols">{cols}</div></div>{FOOT}"""

def duoposter(w,h,dark,label,cap,sub,photos,bgphoto,co='MANTRALAYA GROUP',cohero=None,tile_ar=None,cohero_size=42):
    tcls = 'tiles three' if len(photos)==3 else 'tiles'
    hero = ''
    if cohero:
        hero = f'<div class="cohero">{cohero}</div><div class="cotag">A MANTRALAYA GROUP COMPANY</div>'
    ph = ''.join(f'<div class="tile"><img src="{P(p)}"></div>' for p in photos)
    return base(w,h,dark)+f"""<style>
.wrap{{padding:30px 48px 26px;flex:1;display:flex;gap:40px;align-items:center}}
.lt{{flex:1.1}}
.cap2{{font-size:47px;margin-top:12px}}
.cap2 em{{{GT_W if dark else GT_D}font-style:italic}}
.sub{{margin-top:16px;font-family:'Inter',sans-serif;font-size:21px;font-weight:500;color:{'rgba(255,255,255,0.78)' if dark else '#3A4250'};line-height:1.55}}
.cohero{{font-size:{cohero_size}px;font-weight:900;letter-spacing:1px;{GT_W if dark else GT_D}}}
.cotag{{margin-top:8px;margin-bottom:24px;font-size:15px;font-weight:800;letter-spacing:5px;color:{'rgba(255,255,255,0.6)' if dark else '#8A93A0'}}}
.tiles{{flex:1;display:grid;grid-template-columns:repeat(2,1fr);gap:16px}}
.tile{{border-radius:16px;overflow:hidden;border:3px solid {'rgba(240,120,0,0.7)' if dark else '#D83000'};aspect-ratio:{tile_ar or 1.25};box-shadow:0 12px 30px rgba(0,0,0,{'0.4' if dark else '0.12'})}}
.tile img{{width:100%;height:100%;object-fit:cover}}
.tiles.three .tile{{aspect-ratio:1.5}}
.tiles.three .tile:nth-child(3){{grid-column:span 2;aspect-ratio:3.8}}
</style>{bgimg(bgphoto)}{hdr(dark,co)}
<div class="wrap z"><div class="lt">{hero}<div class="label">{label}</div><div class="cap cap2">{cap}</div><div class="sub">{sub}</div></div><div class="{tcls}">{ph}</div></div>{FOOT}"""

def collageposter(w,h,dark,label,cap,sub,url,photos):
    ph = ''.join(f'<img src="{P(p)}">' for p in photos)
    ov = ('linear-gradient(180deg,rgba(13,8,6,0.86),rgba(13,8,6,0.4) 40%,rgba(13,8,6,0.92) 78%,#0D0806)' if dark
          else 'linear-gradient(180deg,rgba(251,244,235,0.93),rgba(251,244,235,0.42) 40%,rgba(251,244,235,0.95) 78%,#FBF4EB)')
    return base(w,h,dark)+f"""<style>
.coll{{position:absolute;inset:0;display:grid;grid-template-columns:repeat(2,1fr);grid-template-rows:repeat(3,1fr)}}
.coll img{{width:100%;height:100%;object-fit:cover}}
.coll::after{{content:'';position:absolute;inset:0;background:{ov}}}
.bt{{margin-top:auto;padding:0 52px 52px;text-align:center;position:relative;z-index:4}}
.cap2{{font-size:76px}}
.cap2 em{{{GT_W if dark else GT_D}font-style:italic}}
.sub{{margin-top:16px;font-family:'Inter',sans-serif;font-size:27px;font-weight:500;color:{'rgba(255,255,255,0.85)' if dark else '#3A4250'}}}
.pill{{display:inline-block;margin-top:30px;background:{GRAD};color:#fff;border-radius:100px;padding:22px 54px;font-size:31px;font-weight:800;letter-spacing:1px;box-shadow:0 14px 40px rgba(216,60,0,0.5)}}
</style><div class="coll">{ph}</div>{hdr(dark)}
<div class="bt"><div class="label">{label}</div><div class="cap cap2">{cap}</div><div class="sub">{sub}</div><div class="pill">{url}</div></div></body></html>"""

def totem(w,h,dark):
    brands_d = 'GAIL · BCPL · HMEL · HALDIA · OPAL<br>MRPL · HPCL · RELIANCE · NAYARA'
    brands_i = 'ARAMCO · BOROUGE · CABOT · CELANESE<br>CHEVRON PHILLIPS · EXXON MOBIL · FORMOSA<br>GC MARKETING · GULF POLYMERS · INEOS<br>LG CHEM · LYONDELL BASELL · MITSUBISHI<br>OQ (LUBAN) · SABIC · SCGC · WESTLAKE'
    tiles = ''.join(f'<div class="tw"><div class="tt"><img src="{P(p)}"></div><div class="tl">{l}</div></div>'
                    for p,l in [('natural-granules','PLASTIC GRANULES'),('coloured-granules','MASTER BATCHES'),('pigments','PIGMENTS')])
    logo = '../../mg-logo-dark.png' if dark else '../../mg-logo.png'
    return base(w,h,dark)+f"""<style>
.wrap{{flex:1;display:flex;flex-direction:column;align-items:center;text-align:center;padding:40px 40px 0;position:relative;z-index:4}}
.wrap img.lg{{height:92px}}
.label2{{margin-top:30px;font-size:24px;font-weight:800;letter-spacing:10px;color:{'#F6921E' if dark else '#C43D00'}}}
.cap2{{font-size:60px;margin-top:14px}}
.cap2 em{{{GT_W if dark else GT_D}font-style:italic}}
.tw{{margin-top:38px}}
.tt{{width:280px;height:280px;border-radius:50%;overflow:hidden;border:6px solid;margin:0 auto;box-shadow:0 16px 40px rgba(0,0,0,{'0.5' if dark else '0.15'})}}
.tw:nth-of-type(1) .tt{{border-color:#A80B0B}}.tw:nth-of-type(2) .tt{{border-color:#D83000}}.tw:nth-of-type(3) .tt{{border-color:#F07800}}
.tt img{{width:100%;height:100%;object-fit:cover}}
.tl{{margin-top:14px;font-size:19px;font-weight:800;letter-spacing:4px;color:{'rgba(255,255,255,0.85)' if dark else '#3A4250'}}}
.wetrade{{margin-top:52px;font-size:52px;font-weight:900;letter-spacing:6px;{GT_W if dark else GT_D}}}
.sec{{margin-top:34px;font-size:20px;font-weight:800;letter-spacing:6px;color:{'rgba(255,255,255,0.55)' if dark else '#8A93A0'}}}
.bl{{margin-top:12px;font-size:20px;font-weight:800;line-height:1.8;letter-spacing:0.5px}}
</style>{bgimg('natural-granules')}
<div class="rule"></div>
<div class="wrap"><img class="lg" src="{logo}">
<div class="label2">RAW MATERIALS</div>
<div class="cap cap2">Every polymer.<br><em>One counter.</em></div>
{tiles}
<div class="wetrade">WE TRADE</div>
<div class="sec">DOMESTIC</div><div class="bl">{brands_d}</div>
<div class="sec">IMPORTED</div><div class="bl">{brands_i}</div>
</div><div class="ftr" style="justify-content:center;font-size:19px;"><span>www.mantralayagroup.com</span></div></body></html>"""

def message(w,h,dark,label,cap,sub,extra='',capsize=None,sidephoto=None):
    cs = capsize or int(w*0.045)
    side = ''
    if sidephoto:
        side = f"""<div style="position:absolute;top:0;right:0;bottom:0;width:44%;z-index:1;">
<img src="{P(sidephoto)}" style="width:100%;height:100%;object-fit:cover;">
<div style="position:absolute;inset:0;background:linear-gradient(90deg,{'#150B07' if dark else '#FBF4EB'} 0%,{'rgba(21,11,7,0.55)' if dark else 'rgba(251,244,235,0.5)'} 40%,{'rgba(21,11,7,0.15)' if dark else 'rgba(251,244,235,0.1)'} 100%);"></div></div>"""
    return base(w,h,dark)+f"""<style>
.wrap{{flex:1;display:flex;flex-direction:column;justify-content:center;padding:20px 60px;position:relative;z-index:4;max-width:{('68%' if sidephoto else '100%')}}}
.cap2{{font-size:{cs}px;margin-top:14px}}
.cap2 em{{{GT_W if dark else GT_D}font-style:italic}}
.sub{{margin-top:18px;font-family:'Inter',sans-serif;font-size:{int(cs*0.42)}px;font-weight:500;color:{'rgba(255,255,255,0.82)' if dark else '#3A4250'};line-height:1.6}}
.extra{{margin-top:26px}}
</style>{side}{hdr(dark)}
<div class="wrap"><div class="label">{label}</div><div class="cap cap2">{cap}</div><div class="sub">{sub}</div>{extra}</div>{FOOT}"""

def statextra(dark):
    box = 'border:1px solid rgba(240,120,0,0.4)' if dark else 'background:#fff;border:1px solid rgba(168,11,11,0.15);box-shadow:0 8px 24px rgba(168,11,11,0.07)'
    lab = 'rgba(255,255,255,0.7)' if dark else '#5A6472'
    gt = GT_W if dark else GT_D
    def cell(v,l): return f'<div style="flex:1;{box};border-radius:18px;padding:26px;text-align:center;"><div style="font-size:58px;font-weight:900;{gt}">{v}</div><div style="margin-top:6px;font-size:18px;font-weight:700;letter-spacing:3px;color:{lab};">{l}</div></div>'
    return '<div class="extra" style="display:flex;gap:26px;">'+cell('35+','YEARS IN POLYMERS')+cell('2300+','CLIENTS SERVED')+cell('6','GROUP COMPANIES')+'</div>'

def branchextra(dark):
    chip = ('background:rgba(255,255,255,0.07);border:1px solid rgba(240,120,0,0.4);color:#fff' if dark
            else 'background:#fff;border:1px solid rgba(16,20,27,0.1);box-shadow:0 6px 18px rgba(0,0,0,0.05);color:#10141B')
    chips = ''.join(f'<span style="{chip};border-radius:100px;padding:14px 28px;font-size:21px;font-weight:700;">{c}</span>' for c in ['Hyderabad','Guntur','Visakhapatnam','Z. Medapadu','Tenali','Vijayawada','Nellore'])
    return f'<div class="extra" style="display:flex;flex-wrap:wrap;gap:14px;">{chips}<span style="background:{GRAD};color:#fff;border-radius:100px;padding:14px 28px;font-size:21px;font-weight:800;">Upcoming: Bengaluru &amp; Chennai</span></div>'

def jkplogo(dark, h=150):
    """JKP logo — untouched artwork; on dark posters it sits on a white card."""
    if dark:
        return f'<div style="display:inline-block;background:#fff;border-radius:18px;padding:16px 30px;box-shadow:0 12px 34px rgba(0,0,0,0.4);"><img src="../../jkp-logo.png" style="height:{h}px;display:block;"></div>'
    return f'<img src="../../jkp-logo.png" style="height:{h}px;display:block;margin:0 auto;">'

def dealerblock(dark, center=True, size=23):
    lab = 'rgba(255,255,255,0.65)' if dark else '#5A6472'
    gt = GT_W if dark else GT_D
    al = 'center' if center else 'left'
    return f"""<div style="text-align:{al};">
<div style="width:220px;height:2px;margin:{'26px auto 16px' if center else '26px 0 16px'};background:linear-gradient(90deg,{'transparent' if center else '#F07800'},#F07800,transparent);"></div>
<div style="font-size:16px;font-weight:800;letter-spacing:6px;color:{lab};">AUTHORISED DEALERS</div>
<div style="margin-top:12px;font-size:{int(size*1.18)}px;font-weight:900;letter-spacing:0.5px;line-height:1.55;"><span style="{gt}">SREE SAI AMBICA MARKETING AGENCIES</span><br><span style="{gt}">SREE PADMAVATHI ENTERPRISES</span></div>
</div>"""

def jkp1(w,h,dark):
    fg = '#fff' if dark else '#10141B'
    sub = 'rgba(255,255,255,0.82)' if dark else '#3A4250'
    return base(w,h,dark)+f"""<style>
.wrap{{flex:1;display:flex;flex-direction:column;align-items:center;text-align:center;padding:26px 44px 0;position:relative;z-index:4}}
.cap2{{font-size:47px;margin-top:10px;color:{fg}}}
.cap2 em{{{GT_W if dark else GT_D}font-style:italic}}
.sub{{margin-top:12px;font-family:'Inter',sans-serif;font-size:19px;font-weight:500;color:{sub};line-height:1.5}}
.card{{margin-top:22px;width:100%;background:#fff;border-radius:20px;overflow:hidden;border:3px solid {'rgba(240,120,0,0.7)' if dark else '#D83000'};box-shadow:0 14px 38px rgba(0,0,0,{'0.45' if dark else '0.12'})}}
.card img{{width:100%;height:218px;object-fit:cover;object-position:center 62%;background:#fff;display:block}}
</style>{hdr(dark)}
<div class="wrap">
{jkplogo(dark,132)}
<div class="label" style="margin-top:24px;">MASTER BATCHES</div>
<div class="cap cap2">Dream the shade.<br><em>We shall make it.</em></div>
<div class="sub">Colour, white, black &amp; additive masterbatches<br>for every polymer application.</div>
<div class="card"><img src="{P('jkp-granule-jars-wide')}"></div>
{dealerblock(dark, size=21)}
</div>{FOOT}"""

def jkp2(w,h,dark):
    fg = '#fff' if dark else '#10141B'
    sub = 'rgba(255,255,255,0.78)' if dark else '#3A4250'
    apps = [('jkp-multilayer','MULTILAYER PACKAGING'),('jkp-blow2','BLOW CONTAINERS'),('jkp-household','HOUSEHOLD'),('greenhouse-films','ADDITIVE MASTERBATCHES'),
            ('jkp-preforms','PET PREFORMS'),('jkp-nonwoven','WOVEN &amp; NON-WOVEN BAGS'),('jkp-agrifilm','AGRICULTURE FILMS'),('jkp-rope','ROPES')]
    borders=['#A80B0B','#D83000','#F07800','#F6921E','#F6921E','#F07800','#D83000','#A80B0B']
    tiles=''.join(f'<div class="aw"><div class="ac" style="border-color:{borders[i]};"><img src="{P(p)}"></div><div class="al">{l}</div></div>' for i,(p,l) in enumerate(apps))
    return base(w,h,dark)+f"""<style>
.wrap{{flex:1;display:flex;gap:36px;align-items:center;padding:20px 48px 14px;position:relative;z-index:4}}
.lt{{width:475px;flex:none}}
.cap2{{font-size:44px;margin-top:10px;color:{fg}}}
.cap2 em{{{GT_W if dark else GT_D}font-style:italic}}
.sub{{margin-top:10px;font-family:'Inter',sans-serif;font-size:17px;font-weight:500;color:{sub};line-height:1.5}}
.rt{{flex:1}}
.agrid{{display:grid;grid-template-columns:repeat(4,1fr);gap:26px 14px}}
.aw{{text-align:center}}
.ac{{width:196px;height:196px;border-radius:50%;overflow:hidden;border:5px solid;margin:0 auto;background:#fff;box-shadow:0 10px 26px rgba(0,0,0,{'0.4' if dark else '0.12'})}}
.ac img{{width:100%;height:100%;object-fit:cover}}
.al{{margin-top:10px;font-size:15px;font-weight:800;letter-spacing:1px;color:{'rgba(255,255,255,0.85)' if dark else '#3A4250'}}}
.also{{margin-top:16px;font-family:'Inter',sans-serif;font-size:14.5px;font-weight:600;color:{'rgba(255,255,255,0.6)' if dark else '#8A93A0'};text-align:center;letter-spacing:0.3px}}
</style>{hdr(dark)}
<div class="wrap">
<div class="lt">{jkplogo(dark,185)}
<div class="label" style="margin-top:22px;">JKP MASTERBATCHES</div>
<div class="cap cap2">One partner.<br><em>Every application.</em></div>
{dealerblock(dark, center=False, size=17)}
</div>
<div class="rt"><div class="agrid">{tiles}</div>
<div class="also">Also for: Polyester Fibre &middot; Toys &middot; Cables &amp; Wires &middot; Water Tanks &middot; Luggage &middot; Coolers &middot; Electrical &amp; Automotive &middot; Polycoat</div></div>
</div>{FOOT}"""

LOC_DATA = [
 ('SREE MANTRALAYA PETROCHEM (SMP)', [('Hyderabad','8977020177, 8977020175'),('Guntur','8886668998'),('Rajahmundry','9381579829'),('Visakhapatnam','8977020179')]),
 ('SREE RAVITEJA POLYMERS', [('Tenali','8886668921, 8886668915, 8886668912')]),
 ('SREE SAI AMBICA MARKETING AGENCIES', [('Tenali','8977020178'),('Vijayawada','8886668920'),('Rajahmundry','9381579829')]),
 ('BALA GANESHA POLYMERS', [('Tenali','8886668915, 8886668912')]),
 ('SREE PADMAVATHI ENTERPRISES', [('Hyderabad','8977020177, 8977020175, 8977020170')]),
 ('SREE RAVITEJA POLYMERS LIMITED', [('Hyderabad','8977020177, 8977020176'),('Nellore','8886668921')]),
]

def upcomingpill(dark, size=19):
    return f'<span style="display:inline-block;background:{GRAD};color:#fff;border-radius:100px;padding:12px 30px;font-size:{size}px;font-weight:800;letter-spacing:1px;box-shadow:0 10px 28px rgba(216,60,0,0.4);">Upcoming: Bengaluru &amp; Chennai</span>'

def loc_a(w,h,dark):
    """Variant A — 3x2 directory cards with cities + phone numbers."""
    card = 'background:rgba(255,255,255,0.05);border:1px solid rgba(240,120,0,0.4)' if dark else 'background:#fff;border:1px solid rgba(168,11,11,0.14);box-shadow:0 10px 28px rgba(168,11,11,0.07)'
    gt = GT_W if dark else GT_D
    city = '#fff' if dark else '#10141B'
    ph = 'rgba(255,255,255,0.62)' if dark else '#5A6472'
    cards=''
    for name,locs in LOC_DATA:
        rows=''.join(f'<div class="lr"><span class="dot"></span><span class="ct">{c}</span><span class="pn">{p}</span></div>' for c,p in locs)
        cards+=f'<div class="cc"><div class="cn">{name}</div>{rows}</div>'
    return base(w,h,dark)+f"""<style>
.wrap{{padding:30px 48px 22px;flex:1;display:flex;flex-direction:column;position:relative;z-index:4}}
.top{{display:flex;justify-content:space-between;align-items:flex-end}}
.cap2{{font-size:46px;margin-top:8px}}
.cap2 em{{{gt}font-style:italic}}
.grid{{margin-top:26px;display:grid;grid-template-columns:repeat(3,1fr);gap:18px;flex:1;align-content:stretch}}
.cc{{{card};border-radius:18px;padding:22px 26px}}
.cn{{font-size:21.5px;font-weight:900;letter-spacing:0.4px;{gt}line-height:1.3;min-height:56px}}
.lr{{display:flex;align-items:flex-start;gap:10px;margin-top:11px}}
.dot{{width:9px;height:9px;border-radius:50%;background:#F07800;flex:none;box-shadow:0 0 10px rgba(240,120,0,0.8);margin-top:7px}}
.ct{{font-size:18.5px;font-weight:800;color:{city};white-space:nowrap}}
.pn{{font-family:'Inter',sans-serif;font-size:14.5px;font-weight:600;color:{ph};margin-left:auto;text-align:right}}
</style>{bgimg('natural-granules')}{hdr(dark)}
<div class="wrap"><div class="top"><div><div class="label">OUR COMPANIES &amp; LOCATIONS</div>
<div class="cap cap2">One group. <em>Wherever you build.</em></div></div>{upcomingpill(dark)}</div>
<div class="grid">{cards}</div></div>{FOOT}"""

def loc_b(w,h,dark):
    """Variant B — wide: caption left, clean rows with city chips right."""
    gt = GT_W if dark else GT_D
    chip = ('background:rgba(255,255,255,0.07);border:1px solid rgba(240,120,0,0.45);color:#fff' if dark
            else 'background:#fff;border:1px solid rgba(16,20,27,0.1);box-shadow:0 5px 14px rgba(0,0,0,0.05);color:#10141B')
    rows=''
    for name,locs in LOC_DATA:
        chips=''.join(f'<span class="ch">{c}</span>' for c,_ in locs)
        rows+=f'<div class="row"><div class="rn">{name}</div><div class="chs">{chips}</div></div>'
    return base(w,h,dark)+f"""<style>
.wrap{{flex:1;display:flex;gap:48px;align-items:center;padding:20px 48px 16px;position:relative;z-index:4}}
.lt{{width:440px;flex:none}}
.cap2{{font-size:56px;margin-top:12px}}
.cap2 em{{{gt}font-style:italic}}
.sub{{margin-top:14px;font-family:'Inter',sans-serif;font-size:19px;font-weight:500;color:{'rgba(255,255,255,0.78)' if dark else '#3A4250'};line-height:1.55}}
.rt{{flex:1;display:flex;flex-direction:column;justify-content:center;gap:13px}}
.row{{display:flex;align-items:center;gap:18px;border-bottom:1px solid {'rgba(255,255,255,0.09)' if dark else 'rgba(16,20,27,0.08)'};padding-bottom:13px}}
.rn{{flex:1;font-size:21px;font-weight:900;letter-spacing:0.3px;{gt}}}
.chs{{display:flex;gap:9px;flex-wrap:wrap;justify-content:flex-end}}
.ch{{{chip};border-radius:100px;padding:8px 20px;font-size:16px;font-weight:700;white-space:nowrap}}
</style>{bgimg('coloured-granules')}{hdr(dark)}
<div class="wrap"><div class="lt"><div class="label">COMPANIES &amp; LOCATIONS</div>
<div class="cap cap2">Six companies.<br><em>Seven cities.</em></div>
<div class="sub">Andhra Pradesh &amp; Telangana — served from Hyderabad, Guntur, Tenali, Vijayawada, Nellore, Z.&nbsp;Medapadu and Visakhapatnam.</div>
<div style="margin-top:24px;">{upcomingpill(dark)}</div></div>
<div class="rt">{rows}</div></div>{FOOT}"""

def loc_c(w,h,dark):
    """Variant C — portrait stacked directory with numbers."""
    card = 'background:rgba(255,255,255,0.05);border-left:6px solid #F07800' if dark else 'background:#fff;border-left:6px solid #D83000;box-shadow:0 8px 22px rgba(168,11,11,0.07)'
    gt = GT_W if dark else GT_D
    city = '#fff' if dark else '#10141B'
    ph = 'rgba(255,255,255,0.62)' if dark else '#5A6472'
    cards=''
    for name,locs in LOC_DATA:
        rows=''.join(f'<div class="lr"><span class="ct">{c}</span><span class="pn">{p}</span></div>' for c,p in locs)
        cards+=f'<div class="cc"><div class="cn">{name}</div>{rows}</div>'
    return base(w,h,dark)+f"""<style>
.wrap{{padding:30px 52px 22px;flex:1;display:flex;flex-direction:column;position:relative;z-index:4}}
.cap2{{font-size:54px;margin-top:10px;text-align:center}}
.cap2 em{{{gt}font-style:italic}}
.label{{text-align:center}}
.stack{{margin-top:26px;display:flex;flex-direction:column;gap:15px;flex:1;justify-content:space-evenly}}
.cc{{{card};border-radius:14px;padding:18px 26px}}
.cn{{font-size:24px;font-weight:900;letter-spacing:0.4px;{gt}}}
.lr{{display:flex;align-items:baseline;margin-top:8px}}
.ct{{font-size:19px;font-weight:800;color:{city}}}
.pn{{font-family:'Inter',sans-serif;font-size:16px;font-weight:600;color:{ph};margin-left:auto}}
.up{{margin-top:20px;text-align:center}}
</style>{bgimg('pigments')}{hdr(dark)}
<div class="wrap"><div class="label">MANTRALAYA GROUP · COMPANIES &amp; LOCATIONS</div>
<div class="cap cap2">Always <em>within reach.</em></div>
<div class="stack">{cards}</div>
<div class="up">{upcomingpill(dark,21)}</div></div>{FOOT}"""

def loc_map(w,h,dark):
    """Variant D — South India map with company pins."""
    from mapdata import PATHS, CITIES
    gt = GT_W if dark else GT_D
    fg = '#fff' if dark else '#10141B'
    aptg = 'rgba(240,120,0,0.20)' if dark else 'rgba(216,60,0,0.14)'
    nb   = 'rgba(255,255,255,0.055)' if dark else 'rgba(16,20,27,0.055)'
    lbl  = '#fff' if dark else '#10141B'
    up   = '#F6921E' if dark else '#C43D00'
    halo = 'rgba(240,120,0,0.35)'
    focus = ''.join(f'<path d="{p}"/>' for s in ('andhra-pradesh','telangana') for p in PATHS[s])
    rest  = ''.join(f'<path d="{p}"/>' for s in ('karnataka','tamil-nadu','odisha','maharashtra','chhattisgarh','kerala') for p in PATHS[s])
    def pin(name, dx=16, anchor='start', dy=7, r=9, cluster=False):
        x,y = CITIES[name]
        return (f'<circle cx="{x}" cy="{y}" r="{r+9}" fill="{halo}"/>'
                f'<circle cx="{x}" cy="{y}" r="{r}" fill="url(#mg)" stroke="#fff" stroke-width="2.5"/>'
                f'<text x="{x+dx}" y="{y+dy}" text-anchor="{anchor}" font-size="26" font-weight="800" fill="{lbl}" font-family="Montserrat">{name}</text>')
    def upin(name, dx=16, anchor='start'):
        x,y = CITIES[name]
        return (f'<circle cx="{x}" cy="{y}" r="9" fill="none" stroke="{up}" stroke-width="2.5" stroke-dasharray="4 4"/>'
                f'<text x="{x+dx}" y="{y+7}" text-anchor="{anchor}" font-size="23" font-weight="700" font-style="italic" fill="{up}" font-family="Inter">{name}</text>')
    pins = (pin('Hyderabad', dx=-18, anchor='end')
          + pin('Visakhapatnam', dx=-16, anchor='end')
          + pin('Rajahmundry', dx=16, dy=-12)
          + pin('Vijayawada', dx=-12, anchor='end', dy=-12, r=7)
          + pin('Guntur', dx=-14, anchor='end', dy=8, r=7)
          + pin('Tenali', dx=14, dy=26, r=7)
          + pin('Nellore')
          + upin('Bengaluru', dx=-16, anchor='end') + upin('Chennai'))
    svg = f"""<svg viewBox="30 20 980 1030" style="position:absolute;top:0;bottom:0;left:50%;transform:translateX(-50%);height:100%;overflow:visible;">
<defs><linearGradient id="mg" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#A80B0B"/><stop offset="0.5" stop-color="#D83000"/><stop offset="1" stop-color="#F07800"/></linearGradient></defs>
<g fill="{nb}">{rest}</g>
<g fill="{aptg}">{focus}</g>
{pins}</svg>"""
    rows=''
    for name,locs in LOC_DATA:
        cities=' &middot; '.join(c.replace(' (Near Rajahmundry)','') for c,_ in locs)
        rows+=f'<div class="row"><div class="rn">{name}</div><div class="rc">{cities}</div></div>'
    return base(w,h,dark)+f"""<style>
.wrap{{flex:1;display:flex;gap:30px;align-items:stretch;padding:14px 48px 10px;position:relative;z-index:4}}
.lt{{width:620px;flex:none;display:flex;flex-direction:column;justify-content:center}}
.cap2{{font-size:47px;margin-top:8px;color:{fg}}}
.cap2 em{{{gt}font-style:italic}}
.rows{{margin-top:18px;display:flex;flex-direction:column;gap:8px}}
.row{{border-left:4px solid #F07800;padding-left:16px}}
.rn{{font-size:19px;font-weight:900;letter-spacing:0.3px;{gt}}}
.rc{{margin-top:1px;font-family:'Inter',sans-serif;font-size:14.5px;font-weight:600;color:{'rgba(255,255,255,0.75)' if dark else '#3A4250'}}}
.mapbox{{flex:1;position:relative}}
</style>{hdr(dark)}
<div class="wrap"><div class="lt"><div class="label">COMPANIES &amp; LOCATIONS</div>
<div class="cap cap2">Six companies.<br><em>On the map.</em></div>
<div class="rows">{rows}</div>
<div style="margin-top:18px;">{upcomingpill(dark,17)}</div></div>
<div class="mapbox">{svg}</div></div>{FOOT}"""

def loc_map_p(w,h,dark):
    """Portrait 800x1000 — map + compact company list."""
    from mapdata import PATHS, CITIES
    gt = GT_W if dark else GT_D
    fg = '#fff' if dark else '#10141B'
    aptg = 'rgba(240,120,0,0.20)' if dark else 'rgba(216,60,0,0.14)'
    nb   = 'rgba(255,255,255,0.055)' if dark else 'rgba(16,20,27,0.055)'
    lbl  = '#fff' if dark else '#10141B'
    up   = '#F6921E' if dark else '#C43D00'
    halo = 'rgba(240,120,0,0.35)'
    focus = ''.join(f'<path d="{p}"/>' for st in ('andhra-pradesh','telangana') for p in PATHS[st])
    rest  = ''.join(f'<path d="{p}"/>' for st in ('karnataka','tamil-nadu','odisha','maharashtra','chhattisgarh','kerala') for p in PATHS[st])
    def pin(name, dx=16, anchor='start', dy=8, r=10):
        x,y = CITIES[name]
        return (f'<circle cx="{x}" cy="{y}" r="{r+9}" fill="{halo}"/>'
                f'<circle cx="{x}" cy="{y}" r="{r}" fill="url(#mg2)" stroke="#fff" stroke-width="2.5"/>'
                f'<text x="{x+dx}" y="{y+dy}" text-anchor="{anchor}" font-size="30" font-weight="800" fill="{lbl}" font-family="Montserrat">{name}</text>')
    def upin(name, dx=16, anchor='start'):
        x,y = CITIES[name]
        return (f'<circle cx="{x}" cy="{y}" r="10" fill="none" stroke="{up}" stroke-width="2.5" stroke-dasharray="4 4"/>'
                f'<text x="{x+dx}" y="{y+8}" text-anchor="{anchor}" font-size="26" font-weight="700" font-style="italic" fill="{up}" font-family="Inter">{name}</text>')
    pins = (pin('Hyderabad', dx=-20, anchor='end')
          + pin('Visakhapatnam', dx=-18, anchor='end')
          + pin('Rajahmundry', dx=18, dy=-14)
          + pin('Vijayawada', dx=-14, anchor='end', dy=-14, r=8)
          + pin('Guntur', dx=-16, anchor='end', dy=10, r=8)
          + pin('Tenali', dx=16, dy=30, r=8)
          + pin('Nellore')
          + upin('Bengaluru', dx=-18, anchor='end') + upin('Chennai'))
    svg = f"""<svg viewBox="130 120 880 700" style="width:100%;height:100%;overflow:visible;" preserveAspectRatio="xMidYMid meet">
<defs><linearGradient id="mg2" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#A80B0B"/><stop offset="0.5" stop-color="#D83000"/><stop offset="1" stop-color="#F07800"/></linearGradient></defs>
<g fill="{nb}">{rest}</g>
<g fill="{aptg}">{focus}</g>
{pins}</svg>"""
    rows=''
    for name,locs in LOC_DATA:
        cities=' &middot; '.join(c for c,_ in locs)
        rows+=f'<div class="row"><div class="rn">{name}</div><div class="rc">{cities}</div></div>'
    return base(w,h,dark)+f"""<style>
.wrap{{flex:1;display:flex;flex-direction:column;padding:18px 40px 12px;position:relative;z-index:4;text-align:center}}
.cap2{{font-size:40px;margin-top:6px;color:{fg}}}
.cap2 em{{{gt}font-style:italic}}
.mapbox{{flex:1;position:relative;margin-top:4px;min-height:0}}
.mapbox svg{{position:absolute;inset:0}}
.rows{{margin-top:8px;display:grid;grid-template-columns:1fr 1fr;gap:9px 22px;text-align:left}}
.row{{border-left:3px solid #F07800;padding-left:12px}}
.rn{{font-size:14px;font-weight:900;letter-spacing:0.2px;{gt}}}
.rc{{margin-top:1px;font-family:'Inter',sans-serif;font-size:12.5px;font-weight:600;color:{'rgba(255,255,255,0.75)' if dark else '#3A4250'}}}
.up2{{margin-top:12px}}
</style>{hdr(dark)}
<div class="wrap"><div class="label">COMPANIES &amp; LOCATIONS</div>
<div class="cap cap2">Six companies. <em>Seven cities.</em></div>
<div class="mapbox">{svg}</div>
<div class="rows">{rows}</div>
<div class="up2">{upcomingpill(dark,15)}</div>
</div>{FOOT}"""

def promiseposter(w,h,dark):
    """Poster 19 — promise quote + SRPL highlight + stats + granules & plant photos."""
    gt = GT_W if dark else GT_D
    fg = '#fff' if dark else '#10141B'
    box = 'border:1px solid rgba(240,120,0,0.4)' if dark else 'background:#fff;border:1px solid rgba(168,11,11,0.15);box-shadow:0 8px 24px rgba(168,11,11,0.07)'
    lab = 'rgba(255,255,255,0.7)' if dark else '#5A6472'
    def cell(v,l):
        return f'<div style="flex:1;{box};border-radius:18px;padding:20px 24px;text-align:center;"><div style="font-size:52px;font-weight:900;{gt}">{v}</div><div style="margin-top:5px;font-size:15px;font-weight:700;letter-spacing:2.5px;color:{lab};">{l}</div></div>'
    stats = '<div style="margin-top:30px;display:flex;gap:22px;max-width:640px;">'+cell('35+','YEARS IN POLYMERS')+cell('2300+','CLIENTS SERVED EVERY YEAR')+'</div>'
    return base(w,h,dark)+f"""<style>
.side{{position:absolute;top:0;right:0;bottom:0;width:40%;z-index:1;display:flex;flex-direction:column}}
.side .im{{flex:1;position:relative;overflow:hidden}}
.side .im img{{width:100%;height:100%;object-fit:cover;display:block}}
.side::after{{content:'';position:absolute;inset:0;background:linear-gradient(90deg,{'#150B07' if dark else '#FBF4EB'} 0%,{'rgba(21,11,7,0.45)' if dark else 'rgba(251,244,235,0.4)'} 34%,{'rgba(21,11,7,0.05)' if dark else 'rgba(251,244,235,0.05)'} 100%)}}
.wrap{{flex:1;display:flex;flex-direction:column;justify-content:center;padding:20px 60px;position:relative;z-index:4;max-width:64%}}
.who1{{font-size:19px;font-weight:800;letter-spacing:6px;color:{'rgba(255,255,255,0.65)' if dark else '#5A6472'}}}
.who2{{margin-top:8px;font-size:33px;font-weight:900;letter-spacing:0.5px;{gt}}}
.cap2{{font-size:72px;margin-top:18px;color:{fg}}}
.cap2 em{{{gt}font-style:italic}}
.sub{{margin-top:16px;font-family:'Inter',sans-serif;font-size:26px;font-weight:500;color:{'rgba(255,255,255,0.82)' if dark else '#3A4250'};line-height:1.5}}
</style>
<div class="side"><div class="im"><img src="{P('natural-granules')}"></div><div class="im"><img src="{P('polymer-plant')}"></div></div>
{hdr(dark)}
<div class="wrap">
<div class="who1">MANTRALAYA GROUP</div>
<div class="who2">SREE RAVITEJA POLYMERS LIMITED</div>
<div class="cap cap2">&ldquo;We deliver <em>what we promise.&rdquo;</em></div>
<div class="sub">35+ years of consistent supply, honest pricing and relationships that last.</div>
{stats}
</div>{FOOT}"""

def build(dark):
    v = {}
    em = lambda t: f"<em>{t}</em>"
    v['poster-01-raw-domestic'] = (1500,900, brandgrid(1500,900,dark,'RAW MATERIALS · DOMESTIC POLYMERS',
      f"India's biggest polymer names. {em('One trusted trader.')}",
      ['GAIL','BCPL','HMEL','HALDIA','OPAL','MRPL','HPCL','RELIANCE','NAYARA'],3,'natural-granules',circles=['natural-granules','coloured-granules','pigments']))
    v['poster-02-raw-imported'] = (1650,900, brandgrid(1650,900,dark,'RAW MATERIALS · IMPORTED POLYMERS',
      f"Sourced from the world's finest. {em('Delivered here.')}",
      ['ARAMCO','BOROUGE','CABOT','CELANESE','CHEVRON PHILLIPS','EXXON MOBIL','FORMOSA','GC MARKETING','GULF POLYMERS','INEOS (INOVYN)','LG CHEM','LYONDELL BASELL','MITSUBISHI CORP.','OQ (LUBAN)','SABIC','SCGC','WESTLAKE','&amp; MORE'],6,'coloured-granules',circles=['natural-granules','coloured-granules','pigments']))
    v['poster-03-pigments'] = (700,1000, photoposter(700,1000,dark,'PIGMENTS','Colour, mastered.','Organic &amp; inorganic pigments for every application.','pigments'))
    v['poster-04-moisture'] = (800,1000, photoposter(800,1000,dark,'MOISTURE POWDER','Dry. Consistent. Reliable.','Moisture powder &amp; moisture dana — quality you can measure.','moisture-powder-full'))
    v['poster-05-jkp-masterbatch'] = (700,1000, jkp1(700,1000,dark))
    v['poster-jkp-applications-2200x1200'] = (1650,900, jkp2(1650,900,dark))
    v['poster-06-pp-apps'] = (1500,600, appsposter(1500,600,dark,'POLYPROPYLENE (PP)',f"One granule. {em('A thousand products.')}",
      [('Homopolymer',['Textile wraps &amp; garment bags','Woven sacks &amp; non-woven fabric','Thin-wall containers &amp; moulding']),
       ('Random Co-Polymer',['High-clarity bottles &amp; containers','House wares &amp; consumer products','Transparent packaging']),
       ('Impact Co-Polymer',['Furniture, caps &amp; closures','Luggage &amp; industrial components','Appliances &amp; automotive'])],'pp-bags'))
    v['poster-07-pe-apps'] = (1500,600, appsposter(1500,600,dark,'POLYETHYLENE (PE)',f"From woven sacks to {em('greenhouse films.')}",
      [('Films &amp; Bags',['Blown film &amp; lamitube','Heavy-duty bags','Greenhouse &amp; canal-lining films']),
       ('Moulding',['Blow moulding up to 100 litres','Overhead tanks','Drip laterals']),
       ('Specialty',['Extrusion coating','Imported granules &amp; master batches','Adhesive lamination &amp; foam film'])],'greenhouse-films'))
    v['poster-08-sutli-ropes'] = (1500,600, duoposter(1500,600,dark,'END PRODUCTS',f"Sutli, ropes &amp; twine — {em('every budget.')}",
      'Sutli under multiple brands · Reprocessed plastic granules from recycled waste.',['plastic-sutli','rope-yellow','recycled-granules'],'ropes',cohero='BALA GANESHA POLYMERS'))
    v['poster-09-bags'] = (1500,600, duoposter(1500,600,dark,'END PRODUCTS',f"Bags for {em('every business.')}",
      'PP &amp; PE bags · BOPP bags · Non-woven bags · Garment &amp; jewellery packing',['pp-bags','non-woven-bags','garment-bags','bopp-bags'],'non-woven-bags',cohero='SREE RAVITEJA POLYMERS',tile_ar=1.8,cohero_size=33))
    v['poster-10-films'] = (1000,1000, photoposter(1000,1000,dark,'POLY FILMS','Films that protect what you make.','Treated rolls · Stretch film · Packaging films','treated-rolls'))
    v['poster-11-pands'] = (1000,1500, collageposter(1000,1500,dark,'PRODUCTS &amp; STORES',f"Everything plastic.<br>{em('Off the shelf.')}",
      'Retail &amp; bulk — explore the full catalogue.','productsandstores.com',['coloured-granules','plastic-sutli','pp-bags','pigments','ropes','non-woven-bags']))
    v['poster-12-totem'] = (600,2133, totem(600,2133,dark))
    v['poster-13-credit-1'] = (1500,750, message(1500,750,dark,'CREDIT FACILITY',f"Your growth. {em('Our credit.')}",
      'Flexible credit facilities for trusted trade partners — built on 35+ years of relationships. Talk to our team today.',sidephoto='coloured-granules'))
    v['poster-15-credit-2'] = (900,750, message(900,750,dark,'CREDIT FACILITY',f"Terms that move {em('with your business.')}",
      'Credit cycles tailored to your trade. Ask us how.',capsize=52))
    v['poster-17-pands-qr'] = (900,750, message(900,750,dark,'PRODUCTS &amp; STORES',f"Take the store {em('with you.')}",
      'Scan to browse the complete catalogue at productsandstores.com.',
      extra='<div class="extra"><img src="../qr-ps.png" style="width:190px;height:190px;border-radius:14px;border:5px solid #D83000;"></div>',capsize=52))
    v['poster-14-trust'] = (1650,750, message(1650,750,dark,'THE MANTRALAYA GROUP',f"Trust, {em('measured.')}",'',capsize=72,extra=statextra(dark)))
    v['poster-19-promise'] = (1500,750, promiseposter(1500,750,dark))
    v['poster-20-branches'] = (1650,750, message(1650,750,dark,'OUR NETWORK',f"Wherever you build, {em('we&rsquo;re nearby.')}",'',extra=branchextra(dark)))
    v['poster-locations-a'] = (1500,900, loc_a(1500,900,dark))
    v['poster-locations-b'] = (1650,750, loc_b(1650,750,dark))
    v['poster-locations-c'] = (1000,1500, loc_c(1000,1500,dark))
    v['poster-locations-d-map'] = (1650,750, loc_map(1650,750,dark))
    v['poster-locations-map-800x1000'] = (800,1000, loc_map_p(800,1000,dark))
    return v

manifest = {}
for dark in (True, False):
    sub = 'dark' if dark else 'light'
    for name,(w,h,html) in build(dark).items():
        fn = f'src/{name}--{sub}.html'
        open(fn,'w').write(html)
        manifest[fn] = (w,h,sub,name)
json.dump(manifest, open('manifest2.json','w'))
print('wrote', len(manifest), 'poster HTMLs')
