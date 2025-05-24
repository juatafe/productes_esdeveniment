from odoo import models, fields

class ProductEsdevenimentPrice(models.Model):
    _name = 'product.esdeveniment.price'
    _description = 'Preu per franja horària en esdeveniment'

    product_tmpl_id = fields.Many2one('product.template', required=True, ondelete='cascade')
    hour_start = fields.Float(string="Hora inici", required=True)
    hour_end = fields.Float(string="Hora fi", required=True)
    price = fields.Float(string="Preu")
