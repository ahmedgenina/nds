#coding=utf-8

from openerp import fields, api, models
from openerp.addons import crm


class ResPartner(models.Model):
    _inherit = 'res.partner'

    contract_indicator = fields.Selection([
        ('0', u'Não'),
        ('1', u'Sim')],
        string=u'Cliente com Contrato de HelpDesk', required=False,
        help=u'Indica cliente com contrato de HelpDesk.', default='0') 

    contract_date = fields.Date()
    
    contract_revenues_day = fields.Selection([
        ('0', u'1'),
        ('1', u'2'),
        ('2', u'3'),
        ('3', u'4'),
        ('4', u'5'),
        ('5', u'6'),
        ('6', u'7'),
        ('7', u'8'),
        ('8', u'9'),
        ('9', u'10'),
        ('10', u'11'),
        ('11', u'12'),
        ('12', u'13'),
        ('13', u'14'),
        ('14', u'15'),
        ('15', u'16'),
        ('16', u'17'),
        ('17', u'18'),
        ('18', u'19'),
        ('19', u'20'),
        ('20', u'21'),
        ('21', u'22'),
        ('22', u'23'),
        ('23', u'24'),
        ('24', u'25'),
        ('25', u'26'),
        ('26', u'27'),
        ('27', u'28'),
        ('28', u'29'),
        ('29', u'30'),
        ('30', u'31')],
        string=u'Dia de Faturamento do Contrato de HelpDesk', required=False,
        help=u'Indica o dia de Faturamento do contrato de HelpDesk.', default='0')
    
    
    old_id = fields.Integer(string="codigo de banco antigo",required=False)       
