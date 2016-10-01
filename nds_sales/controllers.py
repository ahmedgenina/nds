# -*- coding: utf-8 -*-
from openerp import http

# class NdsSales(http.Controller):
#     @http.route('/nds_sales/nds_sales/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nds_sales/nds_sales/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nds_sales.listing', {
#             'root': '/nds_sales/nds_sales',
#             'objects': http.request.env['nds_sales.nds_sales'].search([]),
#         })

#     @http.route('/nds_sales/nds_sales/objects/<model("nds_sales.nds_sales"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nds_sales.object', {
#             'object': obj
#         })