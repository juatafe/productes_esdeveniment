from odoo import models, fields

class EventEvent(models.Model):
    _inherit = 'event.event'

    allow_ticket_reservation = fields.Boolean("Permetre reserves sense saldo?")

    def action_generate_event_tickets(self):
        product_model = self.env['product.template']
        ticket_templates = product_model.search([('is_event_ticket', '=', True), ('event_id', '=', False)])
        for template in ticket_templates:
            product_model.create({
                'name': f"{template.name} - {self.name}",
                'default_code': f"{template.default_code or ''}-{self.id}",
                'list_price': template.list_price,
                'image_1920': template.image_1920,
                'is_event_ticket': False,
                'event_id': self.id,
                'parent_template_id': template.id,
                'type': 'product',
            })