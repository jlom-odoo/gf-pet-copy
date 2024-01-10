from odoo import models


class MailThread(models.AbstractModel):
    _inherit='mail.thread' 
    
    def get_base_url(self):
        if 'brand_id' in self.fields_get() and self.brand_id and self.brand_id.website_id and (brand_url:=self.brand_id.website_id.domain):
            return brand_url
        else:
            return super().get_base_url()
 