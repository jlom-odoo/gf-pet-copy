from odoo import models, fields


class SaleOrder(models.Model):
    _inherit='sale.order'

    brand_id = fields.Many2one(string='Brand', comodel_name='brand.brand', related='partner_id.brand_id')
  