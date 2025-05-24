from odoo import models, fields, api, _

class AssignEventCategoryWizard(models.TransientModel):
    _name = 'assign.event.category.wizard'
    _description = 'Assigna la categoria d’esdeveniment als productes'

    product_ids = fields.Many2many('product.template', string='Productes')

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        if 'active_ids' in self.env.context:
            res['product_ids'] = [(6, 0, self.env.context['active_ids'])]
        return res

    def action_assign_category(self):
        category = self.env.ref('productes_esdeveniment.product_category_events')
        for product in self.product_ids:
            product.write({
                'categ_id': category.id,
                'detailed_type': 'event',
            })
        return {'type': 'ir.actions.act_window_close'}
