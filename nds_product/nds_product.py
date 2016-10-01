# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.addons import product

class nds_product(models.Model):

     _inherit = 'product.template'    
     id_old = fields.Integer()
     #name = fields.Char()


