from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_event_ticket = fields.Boolean("És una plantilla de tiquet?")
    parent_template_id = fields.Many2one('product.template', string="Producte base (si és tiquet d'esdeveniment)")
    event_id = fields.Many2one('event.event', string="Esdeveniment (si és un tiquet d'esdeveniment)")