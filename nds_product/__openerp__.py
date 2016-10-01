# -*- coding: utf-8 -*-
{
    'name': "nds_product",

    'summary': """
        Customized Product model for NDS brazil
        """,

    'description': """
        This module was created by Datashow inc to attend NDS informatica implementation
    """,

    'author': "Datashow",
    'website': "http://datashow.duckdns.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    #'depends': ['base','crm_helpdesk'],
    'depends': ['base','sale', 'product'],
    #'depends': ['base'],
    'application': 'True',

    # always loaded
    #'data': [
        # 'security/ir.model.access.csv',
        #'nds_helpdesk_view.xml',
        #'nds_helpdesk_menu.xml',
    #],
    # only loaded in demonstration mode
    #'demo': [
        #'demo.xml',
    #],
}