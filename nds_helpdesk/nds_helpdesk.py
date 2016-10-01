# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.addons import sale

class nds_helpdesk(models.Model):

     _inherit = 'crm.helpdesk'
     _name = 'nds.helpdesk'
     #contract = fields.boolean('contratado', required = 'True',default = 'True')
     #name = fields.Char()

class nds_os(models.Model):
    _inherit = 'sale.order'
    _name = 'nds.os'
    #name = fields.char()
