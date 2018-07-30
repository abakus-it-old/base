# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
{
    'name': "Multi Business Units Management",
    'version': '10.0.1.0.0',
    'author': "AbAKUS it-solutions SARL",
    'license': 'AGPL-3',
    'depends': [
        'sale',
        'account',
    ],
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Business Unit',
    'qweb': [
        'static/src/xml/base.xml',
    ],
    'data': [
        'data/ir_rule.xml',

        'views/business_unit_view.xml',
        'views/webclient_templates.xml',
        'views/res_users.xml',
        'views/res_partner.xml',
    ],
    'installable': True,
    'application': False,
}
