{
    'name': "Attachments for Company auto sent for specific emails",
    'version': '9.0.1.0.2',
    'depends': [
        'base',
        'mail',
    ],
    'author': "Valentin Thirion, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Base',
    'description': """
    Attachments for Company auto sent for specific emails

    This modules adds list of possible attachments on a company for different languages. Each attachment can be linked to a mail template and when one of this email is sent, the attachments specified are auto added in the receiver's language.

    To be flexible, this module also adds a checkbox (default=True) on each partner which is a company and sends the documents only if this checkbox is still checked.

    This module has been developed by Valentin Thirion @ AbAKUS it-solutions.
    """,
    'data': [
        'views/base_company_view.xml',
        'views/res_partner_view.xml',

        'security/ir.model.access.csv',
    ],
    'demo': [],
}