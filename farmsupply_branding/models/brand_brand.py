from odoo import models, fields, api


class BrandBrand(models.Model):
    _name='brand.brand'
    _description='Divisions for document branding'

    name = fields.Char(string='Division Name', required=True)
    email = fields.Char(string='Division Email Address')
    image = fields.Image(string='Division Image', attachment=False)
    mobile = fields.Char(string='Mobile Phone Number')
    phone = fields.Char(string='Phone Number')
    website_id = fields.Many2one(string='Division Website', comodel_name='website')
    website_name = fields.Char(string='Division Website Name')
    document_header = fields.Html(string='HTML header for pdf documents', required=True)
        