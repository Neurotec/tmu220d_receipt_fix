# -*- coding: utf-8 -*-
{
    'name': "tmu220d_receipt_fix/",

    'summary': """
    Fix print width of receipt with tmu220d epson 
    """,

    'description': """
    Cambia el ancho del recibo del punto de venta.
    """,

    'author': "Neurotec Tecnologia S.A.S",
    'website': "http://www.neurotec.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'point_of_sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],
    'qweb': ['static/src/xml/pos.xml'],
}
