from odoo import models, fields


class SaleOrder(models.Model):
    _inherit='sale.order'

    brand_id = fields.Many2one(string='Brand', comodel_name='brand.brand', related='partner_id.brand_id')
    
    def _create_invoices(self, grouped=False, final=False, date=None):
        return super()._create_invoices(True,final,date)
