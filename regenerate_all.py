#!/usr/bin/env python3
"""Regenerate all 6 brochures with July-2026 content (docx refresh): new subtitles, branches, SRPL gallery."""
import sys; sys.path.insert(0, '.')
import generate_brochures as gb
from reportlab.platypus import SimpleDocTemplate, PageBreak, Spacer, Table, TableStyle, Paragraph, Image as RLImage
from reportlab.lib.units import mm
from reportlab.lib.colors import white
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER

IMP = ('Aramco, Borouge, CABOT, Celanese, Chevron Phillips, Exxon Mobil, Formosa, GC Marketing, '
       'Gulf Polymers, INEOS (Inovyn), LG Chem, Lyondell Basell, Mitsubishi Corporation, OQ (LUBAN), '
       'Sabic, SCGC, Westlake etc.')

NEW = {
 'SMP-Brochure.pdf': dict(
   subtitle=('Sree Mantralaya Petrochem (SMP) is the leading trader of all kinds of plastic raw materials '
     'for domestic and imported polymers in Andhra Pradesh and Telangana. We deal the domestic products of '
     'GAIL, BCPL, HMEL, Haldia, OPAL, MRPL, HPCL, Reliance and Nayara for Polypropylene and '
     'Polyethylene granules, and imported granules of ' + IMP + ' We also trade Metallocene, PVC, PET, EVA, '
     'Polystyrene and Biodegradable Plastic (PBAT). With 35+ years of industry experience, SMP is the '
     'flagship company of the Mantralaya Group.'),
   products=[
     {'name': 'Homopolymer (PP)', 'items': ['Textile wraps, garment bags, snack food packing','Extrusion coating, fibre & filament','Multifilament yarn, woven sacks, and non-woven fabric','Rigid packing, thin wall containers, multicavity moulding','Injection moulding & compounding applications']},
     {'name': 'Random Co-Polymer (PP)', 'items': ['High clarity bottles, containers, sheets','Clarified random co-polymer rigid containers','House wares & consumer products','Transparent & translucent packaging']},
     {'name': 'Impact Co-Polymer (PP)', 'items': ['Furniture, caps and closures','Sheets, blow moulded containers','House wares, general products moulding','Paint pans, luggage, industrial components','Appliances, automotive compounding','Batteries, automotive applications']},
     {'name': 'Polyethylene (PE)', 'items': ['Woven sacks for fertilizers, food grains','Blown film / blow moulding (lamitube)','Blow moulding up to 100 litres','Drip lateral, overhead tanks','Heavy duty bags, greenhouse films, canal lining','Extrusion coating with/without slip','Imported granules & master batches','Adhesive lamination and foam film']},
   ],
   branches=[('Hyderabad','8977020177, 8977020175'),('Guntur','8886668998'),('Z. Medapadu (Near Rajahmundry)','9381579829'),('Visakhapatnam','8977020179')]),
 'SRP-Brochure.pdf': dict(
   subtitle=('Sree Raviteja Polymers is the industry best in offering quality plastic packaging solutions with the '
     'latest technology, state-of-the-art machinery, and a fully equipped production team. We manufacture '
     'Polypropylene bags, Polyethylene bags, treated rolls and custom packing models for a wide range of industries '
     'including food, agriculture, retail, construction and export packaging. We also manufacture BOPP garment bags '
     'and non-woven customised shopping bags. A proud member of the Mantralaya Group with 35+ years of collective '
     'industry experience.'),
   branches=[('Tenali','8886668921, 8886668915, 8886668912')]),
 'SSAMA-Brochure.pdf': dict(
   subtitle=('Sree Sai Ambica Marketing Agencies is the trusted leader in the world of plastic products, spanning '
     'across various industries with a wide variety of end products. With an extensive network of manufacturers and '
     'a large, loyal client pool, we specialize both in sourcing and supplying a range of plastic raw materials, '
     'additives, pigments, masterbatches and moisture powder to churn out a wide variety of end products. Our '
     'consistent thrust on quality and competitive pricing has made us a preferred partner for retailers, '
     'wholesalers, and industrial users alike.'),
   branches=[('Tenali','8977020178'),('Vijayawada','8886668920'),('Z. Medapadu (Near Rajahmundry)','9381579829')]),
 'BGP-Brochure.pdf': dict(
   subtitle=('Bala Ganesha Polymers is a futuristic plastic recycling company dedicated to transforming waste into '
     'valuable resources. We process industrial plastic waste and different kinds of plastic waste into high-quality '
     'recycled materials and granules, manufacturing plastic products of sutli under multiple brands with various '
     'qualities and price ranges. Our commitment to environmental sustainability, cutting-edge recycling technology, '
     'and responsible consumption promotion drives us toward a cleaner, greener future for the polymer industry.'),
   branches=[('Tenali (AP)','8886668915, 8886668912')]),
 'SPE-Brochure.pdf': dict(
   subtitle=('Sree Padmavathi Enterprises is your one-stop shop for all polymer material needs with unparalleled '
     'customer service. We specialize in Metallocene PE & PP, PVC (suspension & emulsion), PET, EVA, Polystyrene and '
     'Biodegradable PBAT. Our extensive range also includes masterbatches (white, black & colour), UV stabilizers, '
     'antioxidants, slip & anti-block agents, processing aids, nucleators, organic & inorganic pigments, moisture '
     'powders, moisture dana and reprocessing granules. We serve a diverse clientele with expert procurement '
     'guidance and no compromise on quality.'),
   branches=[('Hyderabad','8977020177, 8977020175, 8977020170')]),
 'SRPL-Brochure.pdf': dict(
   products=[
     {'name': 'Trading', 'items': ['Domestic polymer raw materials','Imported polymer granules','PP & PE granules for all applications','Specialty & engineering plastics','Bulk & retail supply']},
     {'name': 'Distribution', 'items': ['Pan-India distribution network','Timely & reliable delivery','Competitive pricing','Quality-assured materials','Custom order fulfillment']},
   ],
   subtitle=('Sree Raviteja Polymers Ltd (SRPL) has established itself as a trusted name in the polymer industry. '
     'With over three decades of expertise, the company has built a reputation for delivering on its promises, '
     'ensuring consistent supply and quality, and maintaining strong ethical business practices. Long-standing '
     'relationships with leading petrochemical corporations ensure uninterrupted supply and a competitive advantage. '
     'By consistently meeting commitments, SRPL has earned a loyal customer base across Andhra Pradesh and '
     'Telangana. Today, SRPL stands as a symbol of integrity, reliability, and excellence in the polymer sector.'),
   branches=[('Hyderabad','8977020177, 8977020176'),('Nellore','8886668921')]),
}

GALLERY = [
 ('packaging-products','Packaging Products'),('pp-bags','Polypropylene (PP) Bags'),('pe-bags','Polyethylene (PE) Bags'),
 ('plastic-sutli','Plastic Sutli & Twine'),('garment-bags','Garment Bags'),('non-woven-bags','Non-Woven Bags - Printed & Plain'),
 ('jewellery-bags','Jewellery Package Bags'),('milk-pouches','Milk Pouches'),('bopp-bags','BOPP Bags - Garment & Jewellery Packing'),
 ('treated-rolls','Treated Rolls & Packaging Films'),('ropes','Ropes'),('woven-sacks','Woven Sacks'),
 ('garbage-bags','Garbage Bags & Dustbins'),('stretch-film','Stretch Film Rolls'),('greenhouse-films','Greenhouse Films'),
]

def build_branches(story, styles, branches):
    story.append(Spacer(1, 14))
    story.append(Paragraph('OUR BRANCHES', styles['section_title']))
    rows = [[Paragraph(f'<b>{loc}</b>', styles['body']), Paragraph(num, styles['body'])] for loc, num in branches]
    t = Table(rows, colWidths=[80*mm, 80*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1), gb.LIGHT_GRAY),
        ('GRID',(0,0),(-1,-1),0.5, gb.MED_GRAY),
        ('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),
        ('LEFTPADDING',(0,0),(-1,-1),12),
    ]))
    story.append(t)

def build_gallery(story, styles):
    cap = ParagraphStyle('Cap', fontName='Helvetica-Bold', fontSize=8.5, textColor=gb.GUNMETAL, alignment=TA_CENTER, leading=11)
    story.append(PageBreak())
    story.append(gb.ColorBar(160*mm, 3, gb.ORANGE)); story.append(Spacer(1, 6))
    story.append(Paragraph('OUR PRODUCTS', styles['section_title']))
    story.append(Paragraph('A visual overview of our complete plastic products range.', styles['body'])); story.append(Spacer(1, 6))
    rows, row = [], []
    for key, label in GALLERY:
        cell = Table([[RLImage(f'products/{key}.jpg', width=46*mm, height=46*mm)],[Paragraph(label, cap)]], colWidths=[50*mm])
        cell.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
            ('TOPPADDING',(0,1),(0,1),4),('BOTTOMPADDING',(0,1),(0,1),6),('BOX',(0,0),(-1,-1),1.2, gb.ORANGE),('BACKGROUND',(0,0),(-1,-1), white)]))
        row.append(cell)
        if len(row)==3: rows.append(row); row=[]
    if row:
        while len(row)<3: row.append('')
        rows.append(row)
    t = Table(rows, colWidths=[54*mm]*3)
    t.setStyle(TableStyle([('ALIGN',(0,0),(-1,-1),'CENTER'),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
    story.append(t)

def make(filename):
    c = next(x for x in gb.companies if x['filename']==filename)
    new = NEW[filename]
    subtitle = new['subtitle']
    products = new.get('products', c['products'])
    doc = SimpleDocTemplate('brochures/'+filename, pagesize=gb.A4, topMargin=25*mm, bottomMargin=20*mm,
        leftMargin=25*mm, rightMargin=25*mm, title=f"{c['name']} - Company Brochure", author=gb.GROUP_NAME,
        subject='Company Brochure & Product Overview')
    styles = gb.get_styles(); story=[]
    gb.build_cover_page(story, styles, c['name'], subtitle)
    gb.build_products_page(story, styles, products)
    if filename=='SRPL-Brochure.pdf': build_gallery(story, styles)
    story.append(PageBreak())
    gb.build_why_choose_page(story, styles, c['name'], c['strengths'])
    build_branches(story, styles, new['branches'])
    gb.build_contact_page(story, styles)
    doc.build(story, onFirstPage=gb.add_header_footer, onLaterPages=gb.add_header_footer)
    print('Created', filename)

if __name__ == '__main__':
    for fn in NEW: make(fn)
