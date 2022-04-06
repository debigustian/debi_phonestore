# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class phone_store(models.Model):
#     _name = 'phone_store.phone_store'
#     _description = 'phone_store.phone_store'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(phone="_value_hp", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
