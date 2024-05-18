# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) Sitaram Solutions (<https://sitaramsolutions.in/>).
#
#    For Module Support : info@sitaramsolutions.in  or Skype : contact.hiren1188
#
##############################################################################

{
    'name': "Contact Person in Sale, Purchase and Invoice Orders",
    'version': "15.0.0.0",
    'summary': "Contact Person in Sale, Purchase and Invoice Orders",
    'category': 'Extra Addons',
    'description': """
    Contact person in sale order
    Contact person in purchase order
    Contact person in invoice order
    Contact person in sale order report
    Contact person in invoice order report
    Contact person in purchase order report
    
    Alternet contact in sale order
    Alternet contact in purchase order
    Alternet contact in invoice order
    Alternet contact in sale order report
    Alternet contact in invoice order report
    Alternet contact in purchase order report
    
    reference contact in sale order
    reference contact in purchase order
    reference contact in invoice order
    reference contact in sale order report
    reference contact in invoice order report
    reference contact in purchase order report
    
    inherit sale.order
    inherit account.move
    inherit purchase.order
    
    """,
    'author': "Sitaram",
    'website':"www.sitaramsolutions.in",
    'depends': ['base','sale','account','purchase'],
    'data': [
        'views/sr_inherited_sale_order.xml',
        'views/sr_inherited_invoice_order.xml',
        'views/sr_inherited_purchase_order.xml',
        'reports/sr_inherited_sale_order_report.xml',
        'reports/sr_inherited_invoice_order_report.xml',
        'reports/sr_inherited_purchase_order_report.xml'
    ],
    'demo': [],
    "external_dependencies": {},
    "license": "OPL-1",
    'installable': True,
    'auto_install': False,
    'live_test_url':'https://youtu.be/aEc1a6rOhv4',
    'images': ['static/description/banner.png'],
}
