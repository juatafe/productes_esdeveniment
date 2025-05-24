from odoo import models, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_id', 'order_id.event_id')
    def _onchange_product_event_price(self):
        if self.product_id and self.order_id.event_id and self.product_id.product_tmpl_id.variable_price_event:
            dt = self.order_id.event_id.date_begin
            hour = dt.hour + dt.minute / 60.0
            self.price_unit = self.product_id.product_tmpl_id.get_price_for_hour(hour)
