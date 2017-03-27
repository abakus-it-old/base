# -*- coding: utf-8 -*-

{
    'name': "Partner name in mail message notifications",
    'version': '9.0.1.0.0',
    'depends': [
        'mail'
    ],
    'author': "Valentin Thirion, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Social',
    'description': """
This module adds a function on the 'mail.message' object that can be called from a mail template
to get the Partner name from any object in Odoo (if the field exists).

To have it in the mail, you have to add a called for this method and HTML code to print it.
Example (added in the mail template for message discussion):
Customer name: ${object.get_partner_name()}

This module has been developed by Valentin Thirion @ AbAKUS it-solutions""",
    'data': [],
}