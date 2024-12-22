# -*- coding: utf-8 -*-
# from odoo import http


# class Manageisaac(http.Controller):
#     @http.route('/manageisaac/manageisaac', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manageisaac/manageisaac/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('manageisaac.listing', {
#             'root': '/manageisaac/manageisaac',
#             'objects': http.request.env['manageisaac.manageisaac'].search([]),
#         })

#     @http.route('/manageisaac/manageisaac/objects/<model("manageisaac.manageisaac"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manageisaac.object', {
#             'object': obj
#         })
