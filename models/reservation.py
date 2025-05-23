from odoo import models, fields

class ProductTicketReservation(models.Model):
    _name = 'product.ticket.reservation'
    _description = 'Reserva de tiquets associats a esdeveniments'

    partner_id = fields.Many2one('res.partner', required=True)
    product_id = fields.Many2one('product.product', required=True)
    quantity = fields.Integer(default=1)
    event_id = fields.Many2one('event.event')
    state = fields.Selection([
        ('reserved', 'Reservat'),
        ('paid', 'Pagat')
    ], default='reserved')
    reservation_date = fields.Datetime(default=fields.Datetime.now)
    sale_order_id = fields.Many2one('sale.order', string="Comanda associada")