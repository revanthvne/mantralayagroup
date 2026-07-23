#!/usr/bin/env python3
"""Generate professional PDF brochures for all 6 Mantralaya Group companies."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    KeepTogether, PageBreak
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.platypus.flowables import Flowable
import os

# ── Brand Colors ──
ORANGE = HexColor('#E67E22')
DARK_ORANGE = HexColor('#D35400')
GUNMETAL = HexColor('#2C3E50')
LIGHT_GRAY = HexColor('#F8F9FA')
MED_GRAY = HexColor('#ECF0F1')
DARK_GRAY = HexColor('#34495E')
TEXT_COLOR = HexColor('#2C3E50')
ACCENT_GREEN = HexColor('#27AE60')

# ── Contact Info ──
PHONE = '7095 303 303'
LOCATION = 'Hyderabad, India'
EMAIL = 'info@mantralayagroup.com'
WEBSITE = 'www.mantralayagroup.com'
ADDRESS = 'DBS House, 1-7-43-46, SP Road, Paradise, Opp. to Metro Station, Secunderabad - 500 003'
GROUP_NAME = 'Mantralaya Group'

WIDTH, HEIGHT = A4


class ColorBar(Flowable):
    """A colored horizontal bar."""
    def __init__(self, width, height, color):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.rect(0, 0, self.width, self.height, fill=1, stroke=0)


class GradientHeader(Flowable):
    """A gradient-style header block."""
    def __init__(self, width, height, color1, color2):
        Flowable.__init__(self)
        self.width = width
        self.height = height
        self.color1 = color1
        self.color2 = color2

    def draw(self):
        steps = 50
        step_h = self.height / steps
        for i in range(steps):
            r = self.color1.red + (self.color2.red - self.color1.red) * i / steps
            g = self.color1.green + (self.color2.green - self.color1.green) * i / steps
            b = self.color1.blue + (self.color2.blue - self.color1.blue) * i / steps
            self.canv.setFillColor(HexColor('#%02x%02x%02x' % (int(r*255), int(g*255), int(b*255))))
            self.canv.rect(0, self.height - (i+1)*step_h, self.width, step_h+1, fill=1, stroke=0)


def get_styles():
    """Return all paragraph styles."""
    return {
        'company_name': ParagraphStyle(
            'CompanyName', fontName='Helvetica-Bold', fontSize=26,
            textColor=white, alignment=TA_CENTER, spaceAfter=6,
            leading=32
        ),
        'tagline': ParagraphStyle(
            'Tagline', fontName='Helvetica', fontSize=11,
            textColor=HexColor('#FFE0B2'), alignment=TA_CENTER,
            spaceAfter=4, leading=15
        ),
        'section_title': ParagraphStyle(
            'SectionTitle', fontName='Helvetica-Bold', fontSize=16,
            textColor=ORANGE, spaceBefore=14, spaceAfter=8,
            leading=20
        ),
        'subsection': ParagraphStyle(
            'Subsection', fontName='Helvetica-Bold', fontSize=13,
            textColor=GUNMETAL, spaceBefore=10, spaceAfter=6,
            leading=17
        ),
        'body': ParagraphStyle(
            'Body', fontName='Helvetica', fontSize=10,
            textColor=TEXT_COLOR, alignment=TA_JUSTIFY,
            spaceAfter=6, leading=14
        ),
        'bullet': ParagraphStyle(
            'Bullet', fontName='Helvetica', fontSize=10,
            textColor=TEXT_COLOR, leftIndent=20, spaceAfter=3,
            leading=13, bulletIndent=8
        ),
        'footer': ParagraphStyle(
            'Footer', fontName='Helvetica', fontSize=8,
            textColor=HexColor('#95A5A6'), alignment=TA_CENTER
        ),
        'contact_label': ParagraphStyle(
            'ContactLabel', fontName='Helvetica-Bold', fontSize=10,
            textColor=ORANGE, spaceAfter=2
        ),
        'contact_value': ParagraphStyle(
            'ContactValue', fontName='Helvetica', fontSize=10,
            textColor=TEXT_COLOR, spaceAfter=8, leading=13
        ),
        'group_badge': ParagraphStyle(
            'GroupBadge', fontName='Helvetica', fontSize=9,
            textColor=HexColor('#FFE0B2'), alignment=TA_CENTER,
            spaceAfter=12
        ),
        'highlight': ParagraphStyle(
            'Highlight', fontName='Helvetica-Bold', fontSize=11,
            textColor=GUNMETAL, alignment=TA_CENTER,
            spaceBefore=8, spaceAfter=8, leading=15
        ),
    }


def add_header_footer(canvas_obj, doc):
    """Add page footer with contact info."""
    canvas_obj.saveState()
    # Footer line
    canvas_obj.setStrokeColor(MED_GRAY)
    canvas_obj.setLineWidth(0.5)
    canvas_obj.line(25*mm, 15*mm, WIDTH - 25*mm, 15*mm)
    # Footer text
    canvas_obj.setFont('Helvetica', 7)
    canvas_obj.setFillColor(HexColor('#95A5A6'))
    canvas_obj.drawCentredString(WIDTH/2, 11*mm,
        f'{WEBSITE}  |  {EMAIL}  |  +91 {PHONE}')
    canvas_obj.drawCentredString(WIDTH/2, 7*mm,
        f'A {GROUP_NAME} Company  |  35+ Years of Excellence in Polymers')
    canvas_obj.restoreState()


def build_cover_page(story, styles, company_name, subtitle):
    """Build the cover/title page."""
    story.append(Spacer(1, 30*mm))
    # Top gradient block
    story.append(GradientHeader(WIDTH - 50*mm, 75*mm, GUNMETAL, DARK_GRAY))
    story.append(Spacer(1, -68*mm))
    story.append(Paragraph(f'A {GROUP_NAME} Company', styles['group_badge']))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph(company_name, styles['company_name']))
    story.append(Spacer(1, 4*mm))
    # Orange accent bar
    story.append(ColorBar(60*mm, 2*mm, ORANGE))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph('Company Brochure & Product Overview', styles['tagline']))
    story.append(Spacer(1, 25*mm))

    # Decorative orange bar
    story.append(ColorBar(WIDTH - 50*mm, 3*mm, ORANGE))
    story.append(Spacer(1, 15*mm))

    # About summary
    story.append(Paragraph('ABOUT', styles['section_title']))
    story.append(ColorBar(30*mm, 1*mm, ORANGE))
    story.append(Spacer(1, 6*mm))
    story.append(Paragraph(subtitle, styles['body']))
    story.append(Spacer(1, 10*mm))

    # Quick facts table
    facts_data = [
        ['Experience', 'Location', 'Contact'],
        ['35+ Years', LOCATION, f'+91 {PHONE}'],
    ]
    facts_table = Table(facts_data, colWidths=[(WIDTH-50*mm)/3]*3)
    facts_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), GUNMETAL),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BACKGROUND', (0, 1), (-1, 1), LIGHT_GRAY),
        ('TEXTCOLOR', (0, 1), (-1, 1), TEXT_COLOR),
        ('FONTNAME', (0, 1), (-1, 1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, 1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('BOX', (0, 0), (-1, -1), 0.5, MED_GRAY),
        ('GRID', (0, 0), (-1, -1), 0.5, MED_GRAY),
    ]))
    story.append(facts_table)
    story.append(PageBreak())


def build_products_page(story, styles, products):
    """Build the products/services page."""
    story.append(Paragraph('PRODUCTS & SERVICES', styles['section_title']))
    story.append(ColorBar(50*mm, 1*mm, ORANGE))
    story.append(Spacer(1, 8*mm))

    for product in products:
        # Product category header
        cat_table = Table(
            [[Paragraph(product['name'], ParagraphStyle(
                'CatName', fontName='Helvetica-Bold', fontSize=12,
                textColor=white, leading=16
            ))]],
            colWidths=[WIDTH - 50*mm]
        )
        cat_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), GUNMETAL),
            ('TOPPADDING', (0, 0), (-1, -1), 7),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('ROUNDEDCORNERS', [3, 3, 0, 0]),
        ]))

        # Items list
        items_content = []
        for item in product['items']:
            items_content.append([Paragraph(
                f'<bullet>&bull;</bullet> {item}',
                styles['bullet']
            )])

        items_table = Table(items_content, colWidths=[WIDTH - 50*mm])
        items_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), LIGHT_GRAY),
            ('TOPPADDING', (0, 0), (0, 0), 8),
            ('BOTTOMPADDING', (-1, -1), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('BOX', (0, 0), (-1, -1), 0.5, MED_GRAY),
        ]))

        block = KeepTogether([cat_table, items_table, Spacer(1, 6*mm)])
        story.append(block)


def build_why_choose_page(story, styles, company_name, strengths):
    """Build the Why Choose Us page."""
    story.append(Paragraph('WHY CHOOSE US', styles['section_title']))
    story.append(ColorBar(40*mm, 1*mm, ORANGE))
    story.append(Spacer(1, 8*mm))

    story.append(Paragraph(
        f'{company_name} stands apart through a commitment to quality, '
        f'reliability, and customer satisfaction built over 35+ years in the polymer industry.',
        styles['body']
    ))
    story.append(Spacer(1, 6*mm))

    # Strengths in a nice grid
    rows = []
    for i in range(0, len(strengths), 2):
        row = []
        for j in range(2):
            if i + j < len(strengths):
                cell_content = Paragraph(
                    f'<font color="#E67E22"><b>{strengths[i+j]["title"]}</b></font><br/>'
                    f'<font size="9">{strengths[i+j]["desc"]}</font>',
                    ParagraphStyle('StrCell', fontName='Helvetica', fontSize=10,
                                   textColor=TEXT_COLOR, leading=14, spaceAfter=4)
                )
                row.append(cell_content)
            else:
                row.append('')
        rows.append(row)

    col_w = (WIDTH - 54*mm) / 2
    grid = Table(rows, colWidths=[col_w, col_w], hAlign='LEFT')
    grid.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), LIGHT_GRAY),
        ('BOX', (0, 0), (-1, -1), 0.5, MED_GRAY),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, MED_GRAY),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(grid)
    story.append(Spacer(1, 10*mm))


def build_contact_page(story, styles):
    """Build the contact page."""
    story.append(Paragraph('CONTACT US', styles['section_title']))
    story.append(ColorBar(35*mm, 1*mm, ORANGE))
    story.append(Spacer(1, 10*mm))

    # Contact details in a box
    contact_items = [
        ('Office Address', ADDRESS),
        ('Phone', f'+91 {PHONE}'),
        ('Email', EMAIL),
        ('Website', WEBSITE),
    ]

    contact_rows = []
    for label, value in contact_items:
        contact_rows.append([
            Paragraph(f'<b>{label}</b>', ParagraphStyle(
                'CL', fontName='Helvetica-Bold', fontSize=10, textColor=ORANGE, leading=13
            )),
            Paragraph(value, ParagraphStyle(
                'CV', fontName='Helvetica', fontSize=10, textColor=TEXT_COLOR, leading=13
            ))
        ])

    contact_table = Table(contact_rows, colWidths=[35*mm, WIDTH - 85*mm])
    contact_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), LIGHT_GRAY),
        ('BOX', (0, 0), (-1, -1), 1, ORANGE),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('LINEBELOW', (0, 0), (-1, -2), 0.5, MED_GRAY),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(contact_table)
    story.append(Spacer(1, 15*mm))

    # Group info
    story.append(GradientHeader(WIDTH - 50*mm, 35*mm, GUNMETAL, DARK_GRAY))
    story.append(Spacer(1, -28*mm))
    story.append(Paragraph(
        f'<font color="#E67E22"><b>{GROUP_NAME}</b></font>',
        ParagraphStyle('GN', fontName='Helvetica-Bold', fontSize=14,
                       textColor=ORANGE, alignment=TA_CENTER, leading=18)
    ))
    story.append(Spacer(1, 2*mm))
    story.append(Paragraph(
        '6 Companies  |  35+ Years  |  Complete Polymer Solutions',
        ParagraphStyle('GS', fontName='Helvetica', fontSize=10,
                       textColor=white, alignment=TA_CENTER, leading=13)
    ))
    story.append(Spacer(1, 15*mm))


def generate_brochure(filename, company_name, subtitle, products, strengths):
    """Generate a single company brochure."""
    doc = SimpleDocTemplate(
        filename, pagesize=A4,
        topMargin=25*mm, bottomMargin=20*mm,
        leftMargin=25*mm, rightMargin=25*mm,
        title=f'{company_name} - Company Brochure',
        author=GROUP_NAME,
        subject='Company Brochure & Product Overview'
    )
    styles = get_styles()
    story = []

    build_cover_page(story, styles, company_name, subtitle)
    build_products_page(story, styles, products)
    story.append(PageBreak())
    build_why_choose_page(story, styles, company_name, strengths)
    build_contact_page(story, styles)

    doc.build(story, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
    print(f'  Created: {filename}')


# ══════════════════════════════════════════════════════════════
# COMPANY DATA
# ══════════════════════════════════════════════════════════════

companies = [
    {
        'filename': 'SMP-Brochure.pdf',
        'name': 'Sree Mantralaya Petrochem',
        'subtitle': (
            'Sree Mantralaya Petrochem (SMP) is the leading trader of all kinds of plastic raw materials '
            'and imported granules for domestic and imported polymers in Andhra Pradesh and Telangana. '
            'We are traders of GAIL, BCPL, HMEL, Haldia, OPAL, MRPL, '
            'HPCL, Reliance and Nayara for Polypropylene and Polyethylene. We also trade Metallocene, '
            'PVC, PS, PET, EVA, Polystyrene and Biodegradable Plastic (PBAT). With 35+ years of industry '
            'experience, SMP is a proud member of the Mantralaya Group.'
        ),
        'products': [
            {'name': 'Homopolymer (PP)', 'items': [
                'Textile wraps, garment bags, snack food packing',
                'Extrusion coating, fibre & filament',
                'Multifilament yarn, woven sacks, and non-woven fabric',
                'Rigid packing, thin wall containers, multicavity moulding',
                'Injection moulding & compounding applications'
            ]},
            {'name': 'Random Co-Polymer (PP)', 'items': [
                'High clarity bottles, containers, sheets',
                'Clarified random co-polymer rigid containers',
                'Housewares & consumer products',
                'Transparent & translucent packaging'
            ]},
            {'name': 'Impact Co-Polymer (PP)', 'items': [
                'Furniture, caps, and closures',
                'Sheets, blow moulded containers',
                'House wares, general products moulding',
                'Paint pans, luggage, industrial components',
                'Appliances, automotive compounding',
                'Batteries, automotive applications'
            ]},
            {'name': 'Polyethylene (PE)', 'items': [
                'Woven sacks for fertilizers, food grains',
                'Blown film / blow moulding (lamitube)',
                'Blow moulding up to 100 litres',
                'Drip lateral, overhead tanks',
                'Heavy duty bags, greenhouse films',
                'Extrusion coating with/without slip',
                'Imported granules & masterbatches'
            ]},
        ],
        'strengths': [
            {'title': 'Multi-Brand Trader', 'desc': 'Traders of GAIL, BCPL, HMEL, Haldia, OPAL, MRPL, HPCL, Reliance & Nayara'},
            {'title': '35+ Years Experience', 'desc': 'Over three decades of deep expertise in polymer trading and distribution'},
            {'title': 'Complete Product Range', 'desc': 'PP, PE, Metallocene, PVC, PS, PET, EVA & Polystyrene under one roof'},
            {'title': 'Domestic & Imported', 'desc': 'Both Indian and imported polymer granules and raw materials available'},
            {'title': 'Industry Leader', 'desc': 'Leading polymer trader in Andhra Pradesh & Telangana region'},
            {'title': 'Reliable Supply Chain', 'desc': 'Consistent availability and timely delivery across the region'},
        ]
    },
    {
        'filename': 'SRP-Brochure.pdf',
        'name': 'Sree Raviteja Polymers',
        'subtitle': (
            'Sree Raviteja Polymers is the industry best in offering quality plastic packaging solutions '
            'with the latest technology, state-of-the-art machinery, and a fully equipped production team. '
            'We manufacture PP bags, PE bags, rolls, and custom packing models for a wide range of '
            'industries including food, agriculture, retail, construction, and exports. '
            'A proud member of the Mantralaya Group with 35+ years of collective industry experience.'
        ),
        'products': [
            {'name': 'Packaging Products', 'items': [
                'Polypropylene (PP) bags',
                'Polyethylene (PE) bags',
                'Trusted rolls & packing models',
                'PP & PE varieties for diverse applications',
                'Custom packaging solutions'
            ]},
            {'name': 'Capabilities', 'items': [
                'Latest technology & machinery',
                'Fully equipped production team',
                'Customized packaging solutions',
                'Streamlined brand protection packaging',
                'Quality-focused manufacturing processes'
            ]},
            {'name': 'Industries Served', 'items': [
                'Food & agriculture packaging',
                'Industrial component wrapping',
                'Retail & consumer packaging',
                'Construction material packaging',
                'Export-grade packaging solutions'
            ]},
        ],
        'strengths': [
            {'title': 'Modern Infrastructure', 'desc': 'Latest technology and state-of-the-art machinery for consistent quality output'},
            {'title': 'Custom Solutions', 'desc': 'Tailored packaging solutions designed to meet specific client requirements'},
            {'title': 'Quality Assurance', 'desc': 'Rigorous quality control at every stage of manufacturing'},
            {'title': 'Expert Team', 'desc': 'Fully equipped production team with years of industry expertise'},
            {'title': 'Multi-Industry', 'desc': 'Serving food, agriculture, retail, construction, and export sectors'},
            {'title': 'Reliable Delivery', 'desc': 'On-time delivery with consistent supply chain management'},
        ]
    },
    {
        'filename': 'SSAMA-Brochure.pdf',
        'name': 'Sree Sai Ambica Marketing Agencies',
        'subtitle': (
            'Sree Sai Ambica Marketing Agencies is the trusted leader in the world of plastic products, '
            'spanning across various industries with a wide variety of end products. With an extensive '
            'network of manufacturers and a large, loyal client pool, we provide reliable raw material '
            'sourcing, virgin and recycled polymer resins, and commodity and engineering plastics. '
            'Our consistent thrust on quality and competitive pricing has made us a preferred partner '
            'for retailers, wholesalers, and industrial users alike.'
        ),
        'products': [
            {'name': 'Trading & Sourcing', 'items': [
                'Wide variety of plastic end products',
                'Extensive manufacturer network',
                'Reliable raw material sourcing',
                'Virgin & recycled polymer resins',
                'Commodity & engineering plastics'
            ]},
            {'name': 'Distribution', 'items': [
                'Retail & wholesale customers served',
                'Industrial user supply',
                'Customized solutions for specific needs',
                'Speedy deliveries across the region',
                'Bulk & retail quantities available'
            ]},
            {'name': 'Why Choose Us', 'items': [
                'Consistent thrust on quality',
                'Competitive pricing in the market',
                'Exceptional customer service',
                'Trusted brand with large client pool',
                'Extensive manufacturer network'
            ]},
        ],
        'strengths': [
            {'title': 'Trusted Brand', 'desc': 'A name synonymous with reliability in the plastic products industry'},
            {'title': 'Wide Network', 'desc': 'Extensive manufacturer network ensuring best sourcing options'},
            {'title': 'Competitive Pricing', 'desc': 'Market-leading prices without compromising on material quality'},
            {'title': 'Fast Delivery', 'desc': 'Quick turnaround with speedy deliveries across the region'},
            {'title': 'Diverse Products', 'desc': 'Virgin, recycled, commodity, and engineering plastics available'},
            {'title': 'Customer First', 'desc': 'Exceptional service and customized solutions for every client'},
        ]
    },
    {
        'filename': 'BGP-Brochure.pdf',
        'name': 'Bala Ganesha Polymers',
        'subtitle': (
            'Bala Ganesha Polymers is a futuristic plastic recycling company dedicated to transforming '
            'waste into valuable resources. We process industrial plastic waste into high-quality recycled '
            'materials and granules, manufacturing plastic products under multiple brands with various '
            'qualities and price ranges. Our commitment to environmental sustainability, cutting-edge '
            'recycling technology, and responsible consumption promotion drives us toward a cleaner, '
            'greener future for the polymer industry.'
        ),
        'products': [
            {'name': 'Recycling', 'items': [
                'Industrial plastic waste processing',
                'High-quality recycled materials',
                'Recycled plastic granules production',
                'Eco-friendly product range',
                'Responsible consumption promotion'
            ]},
            {'name': 'Manufacturing', 'items': [
                'Plastic products under multiple brands',
                'Various qualities & price ranges',
                'Stringent industry standards compliance',
                'Innovative packaging solutions',
                'Diverse industry applications'
            ]},
            {'name': 'Sustainability', 'items': [
                'Environmental sustainability focus',
                'Cutting-edge recycling technology',
                'Waste-to-value transformation',
                'Cleaner & greener future commitment',
                'Reducing plastic waste in the environment'
            ]},
        ],
        'strengths': [
            {'title': 'Eco-Friendly', 'desc': 'Dedicated to transforming plastic waste into valuable, reusable resources'},
            {'title': 'Advanced Technology', 'desc': 'Cutting-edge recycling technology for superior quality output'},
            {'title': 'Multiple Brands', 'desc': 'Products available across various quality grades and price points'},
            {'title': 'Industry Standards', 'desc': 'Strict adherence to all environmental and manufacturing standards'},
            {'title': 'Waste Reduction', 'desc': 'Actively reducing plastic waste through innovative recycling processes'},
            {'title': 'Future-Ready', 'desc': 'Building a sustainable polymer ecosystem for the next generation'},
        ]
    },
    {
        'filename': 'SPE-Brochure.pdf',
        'name': 'Sree Padmavathi Enterprises',
        'subtitle': (
            'Sree Padmavathi Enterprises is your one-stop shop for all polymer material needs with '
            'unparalleled customer service. We specialize in Metallocene PE & PP, PVC (suspension & '
            'emulsion), PET, EVA, and Polystyrene. Our extensive range also includes masterbatches '
            '(white, black & colour), UV stabilizers, antioxidants, slip & anti-block agents, processing '
            'aids, nucleators, and organic & inorganic pigments. We serve a diverse clientele with expert '
            'procurement guidance and no compromise on quality.'
        ),
        'products': [
            {'name': 'Specialty Resins', 'items': [
                'Metallocene PE & PP',
                'PVC - suspension & emulsion grades',
                'PET - bottles, containers, films',
                'EVA - footwear, solar encapsulants',
                'Polystyrene (PS) - packaging, disposables'
            ]},
            {'name': 'Additives & Masterbatch', 'items': [
                'Masterbatches - white, black & colour',
                'UV stabilizers & antioxidants',
                'Slip & anti-block agents',
                'Processing aids & nucleators',
                'Additive concentrates'
            ]},
            {'name': 'Pigments & Quality', 'items': [
                'Organic & inorganic pigments',
                'Reliable supplier network',
                'No compromise on quality',
                'Expert procurement guidance',
                'Diverse clientele served'
            ]},
        ],
        'strengths': [
            {'title': 'One-Stop Shop', 'desc': 'Complete range of specialty resins, additives, masterbatches, and pigments'},
            {'title': 'Specialty Focus', 'desc': 'Expert knowledge in Metallocene, PVC, PS, PET, EVA, and Polystyrene products'},
            {'title': 'Quality Promise', 'desc': 'Absolutely no compromise on material quality and consistency'},
            {'title': 'Expert Guidance', 'desc': 'Procurement guidance from specialists who understand your applications'},
            {'title': 'Wide Selection', 'desc': 'Masterbatches, stabilizers, pigments, and processing aids in stock'},
            {'title': 'Reliable Supply', 'desc': 'Strong supplier network ensuring consistent material availability'},
        ]
    },
    {
        'filename': 'SRPL-Brochure.pdf',
        'name': 'Sree Raviteja Polymers Limited',
        'subtitle': (
            'Sree Raviteja Polymers Limited (SRPL) is a specialized polymer trading and distribution '
            'company expanding our reach across domestic and international markets with quality raw '
            'materials. We offer domestic and imported polymer granules, PP & PE varieties, specialty '
            'and engineering plastics in both bulk and retail quantities. With a pan-India distribution '
            'network and a focus on timely, reliable delivery, SRPL serves the packaging, automotive, '
            'consumer goods, construction, and agricultural industries.'
        ),
        'products': [
            {'name': 'Trading', 'items': [
                'Domestic polymer raw materials',
                'Imported polymer granules',
                'PP & PE varieties for all applications',
                'Specialty & engineering plastics',
                'Bulk & retail supply options'
            ]},
            {'name': 'Distribution', 'items': [
                'Pan-India distribution network',
                'Timely & reliable delivery',
                'Competitive pricing across all products',
                'Quality-assured materials only',
                'Custom order fulfilment'
            ]},
            {'name': 'Markets Served', 'items': [
                'Packaging industry',
                'Automotive components',
                'Consumer goods manufacturing',
                'Construction materials',
                'Agricultural applications'
            ]},
        ],
        'strengths': [
            {'title': 'Pan-India Reach', 'desc': 'Distribution network spanning across India for nationwide delivery'},
            {'title': 'International Trade', 'desc': 'Expanding reach into international polymer markets'},
            {'title': 'Quality Assured', 'desc': 'Every material is quality-checked before reaching the customer'},
            {'title': 'Competitive Pricing', 'desc': 'Best-in-class pricing due to strong sourcing relationships'},
            {'title': 'Multi-Sector', 'desc': 'Serving packaging, automotive, consumer goods, construction & agriculture'},
            {'title': 'Custom Orders', 'desc': 'Flexible order sizes from bulk industrial to smaller retail quantities'},
        ]
    },
]


if __name__ == '__main__':
    output_dir = os.path.dirname(os.path.abspath(__file__))
    brochures_dir = os.path.join(output_dir, 'brochures')
    os.makedirs(brochures_dir, exist_ok=True)

    print(f'Generating {len(companies)} brochures...\n')
    for company in companies:
        filepath = os.path.join(brochures_dir, company['filename'])
        generate_brochure(
            filepath,
            company['name'],
            company['subtitle'],
            company['products'],
            company['strengths']
        )
    print(f'\nAll brochures saved to: {brochures_dir}')
