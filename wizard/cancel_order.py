from odoo import api, fields, models

class CancelOrder(models.TransientModel):
    _name = 'phone.cancel'
    _description = 'Cancel Order'

    notes = fields.Text(string='Reason')

    def action_cancel(self):
        self.env['phone.order'].browse(self.env.context['active_id']).update({'notes':self.notes, 'state':'cancelled'})