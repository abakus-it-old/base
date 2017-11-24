# -*- coding: utf-8 -*-
{
    'name': "Decimal precision in UOM",

    'summary': """
    """,

    'description': """
        Decimal precision in UOM

        This module adds a field "decimal precision for report" in the UOM.
        In the reports, it will show the correct number of decimal of the UORM regarding the settings.
        
        This module has been developed by Valentin THIRION @ AbAKUS it-solutions.
    """,

    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Base',
    'version': '10.0.1.0',

    'depends': [
        'base',
        'product'
    ],

    'data': [
        'views/product_uom_view.xml',

        'reports/sale_order_report.xml',
    ],
}