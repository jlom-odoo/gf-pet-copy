{
    "name": "Farm Supply Branding",

    "summary": "Branding for Farm Supply documents",

    "description": """
        Task ID: 3486881
        Written by: jden

        Allowing documents to have different branding
    """,
    "author": "Odoo Development Services",
    "maintainer": "Odoo Development Services",
    "website": "https://www.odoo.com/",
    "category": "Custom Development",
    "version": "1.0.1",
    "license": "OPL-1",
    "depends": [
        "website",
        "web",
        "sale"
    ],            
    "data": [
        "security/ir.model.access.csv",
        "views/brand_brand_form.xml",
        "views/res_partner_form.xml",
        "views/report_template.xml",
        "views/sale_order_form.xml",
        "views/mail_template.xml"
    ],
}
