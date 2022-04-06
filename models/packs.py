from odoo import fields, models, api


class Packs(models.Model):
    _name = 'phone.packs'
    _description = 'Packs'

    name = fields.Char(
        string='Name',
        required=True)

    items_ids = fields.Many2many(
        comodel_name='phone.items',
        string='Items')

    total = fields.Integer(phone='_phone_total', string='Total', store=True)

    @api.depends('items_ids')
    def _phone_total(self):
        for record in self:
            record.total = sum(record.items_ids.mapped('price'))
