from odoo import models, fields

class ProductEsdevenimentPrice(models.Model):
    _name = 'product.esdeveniment.price'
    _description = 'Preus segons hora de l\'esdeveniment'

    product_tmpl_id = fields.Many2one('product.template', required=True, ondelete='cascade')
    hour_from = fields.Float(string='Des de (hora)', required=True)
    hour_to = fields.Float(string='Fins a (hora)', required=True)
    price = fields.Float(string='Preu', required=True)
