from odoo import fields, models, api


class Voucher(models.Model):
    _name = 'phone.voucher'
    _description = 'Voucher'

    name = fields.Char(
        string='Voucher',
        required=True)

    percentage = fields.Integer(
        string='Percentage',
        required=True)