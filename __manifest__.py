# __manifest__.py

{
    'name': 'Invoice Payment Link',
    'version': '17.0.1.0.0',
    'category': 'Accounting',
    'author': 'Oleksii Panpukha',
    'website': 'https://github.com/3xecut0r',
    'depends': ['account'],
    'data': [
        'data/mail_template_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',
}
