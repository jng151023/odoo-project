# -*- coding: utf-8 -*-
{
    'name': "Pharmacy Management",

    'summary': """
        Managing the pharmacy.

        """,

    'description': """
        Pharmacy management
    """,

    'author': "Jamsheena KC",

    'category': 'Medical',
    'version': '17.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['hr_contract', 'hr', 'stock', 'account', 'purchase', 'sale_management', 'mail'],
    # 'product',

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/medicine_expiry_report_wizard_view.xml',
        'views/medicine_type_view.xml',
        'views/medicine_category_view.xml',
        'views/medicine_company_view.xml',
        'views/pharmacy_sale_order_view.xml',
        'views/pharmacy_medicine_view.xml',
        'views/pharmacy_purchase_order_view.xml',
        'views/customer_invoice_analysis_view.xml',
        'report/medicine_expiry_report_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'images': ['static/description/banner.png'],
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3'
}
