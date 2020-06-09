# -*- coding: utf-8 -*-
# from odoo import http


# class SouhailErp(http.Controller):
#     @http.route('/souhail__erp/souhail__erp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/souhail__erp/souhail__erp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('souhail__erp.listing', {
#             'root': '/souhail__erp/souhail__erp',
#             'objects': http.request.env['souhail__erp.souhail__erp'].search([]),
#         })

#     @http.route('/souhail__erp/souhail__erp/objects/<model("souhail__erp.souhail__erp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('souhail__erp.object', {
#             'object': obj
#         })
