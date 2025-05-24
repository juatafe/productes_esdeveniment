from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    detailed_type = fields.Selection(
        selection_add=[('event', 'Event')],
        ondelete={'event': 'set default'},  # obligatori per a Odoo 16+
    )

    variable_price_event = fields.Boolean(
        string="Preu variable segons franja horària",
        help="Canvia el preu automàticament segons la franja horària de l'esdeveniment."
    )

    event_price_ids = fields.One2many(
        'product.esdeveniment.price', 'product_tmpl_id',
        string='Preus per franja horària'
    )

    @api.model
    def assign_event_category_to_products(self):
        category = self.env.ref('productes_esdeveniment.product_category_event')
        products = self.search([('type', '=', 'service')])  # o sense condició si vols TOTS
        for product in products:
            product.categ_id = category


