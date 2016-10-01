# -*- coding: utf-8 -*-
{
    'name': "nds_sales",

    'summary': """
        Customers Contracts Identifier model for NDS brazil
        """,

    'description': """
        This module was created by Datashow inc to attend NDS informatica implementation
    """,

    'author': "Datashow",
    'website': "http://datashow.duckdns.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Customized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    #'depends': ['base','crm_helpdesk'],
    'depends': ['base','sale'],
    #'depends': ['base'],
    'application': 'True',

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'nds_view.xml'        
    ]
}