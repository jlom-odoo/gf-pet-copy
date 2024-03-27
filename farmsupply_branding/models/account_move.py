from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    latest_picking_id = fields.Many2one('stock.picking',string="Latest Picking")

    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)
        for rec in res:
            source_order = rec.line_ids.sale_line_ids.order_id
            if source_order:
                picking_ids = source_order.picking_ids.filtered(lambda p : p.state=='done' and p.picking_type_code == 'outgoing').sorted(lambda p : p.date_done, reverse = True)
                if picking_ids:
                    rec.latest_picking_id = picking_ids[0].id
                    rec.invoice_date = picking_ids[0].date_done
        return res
            



