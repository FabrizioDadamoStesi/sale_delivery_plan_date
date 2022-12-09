# -*- coding: utf-8 -*-
{
    'name': "Sale Subscription Split",

    'summary': """
        Gestione di un Delivery Plan""",

    'description': """
        Modulo per poter frazionare in più date l'invio dei prodotti in abbonamento
    """,

    'author': "SteSi S.r.l.",
    'website': "http://www.stesi.eu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'sequence': -100,
    'version': '14.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_subscription',],
    'installable': True,
    'application': False,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/delivery_id_lines.xml',
        'views/sale_order_line.xml',



    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
