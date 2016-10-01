# -*- coding: utf-8 -*-
from openerp import http

# class Helpdesknds(http.Controller):
#     @http.route('/nds_helpdesk/nds_helpdesk/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nds_helpdesk/nds_helpdesk/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('helpdesknds.listing', {
#             'root': '/nds_helpdesk/nds_helpdesk',
#             'objects': http.request.env['nds_helpdesk.nds_helpdesk'].search([]),
#         })

#     @http.route('/nds_helpdesk/nds_helpdesk/objects/<model("nds_helpdesk.nds_helpdesk"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('helpdesknds.object', {
#             'object': obj
#         })