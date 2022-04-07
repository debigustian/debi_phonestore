# -*- coding: utf-8 -*-
# from odoo import http


# class PhoneStore(http.Controller):
#     @http.route('/phone_store/phone_store/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/phone_store/phone_store/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('phone_store.listing', {
#             'root': '/phone_store/phone_store',
#             'objects': http.request.env['phone_store.phone_store'].search([]),
#         })

#     @http.route('/phone_store/phone_store/objects/<model("phone_store.phone_store"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('phone_store.object', {
#             'object': obj
#         })
