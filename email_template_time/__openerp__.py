{
    'name': 'Email Template Time',
    'version': '9.0.1.0',
    'author': "Bernard DELHEZ, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",

    'category': 'Email Template',
    'description': 
    """
    Time filter in emails

    This module adds an extra time filter in email templates

    Example: ${ '%m/%d/%Y'|time() }

    This module has been developed by Bernard DELHEZ @ AbAKUS it-solutions.
    """,
    'depends': [
        'mail',
    ],
    'data': [
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}
