# -*- coding: utf-8 -*-
{
    'name': "library_management",

    'summary': """
        Manage Library Books, Authors, and Loans""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Dianny Michelle DLS",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts','stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/library_book.xml',
        'views/library_author.xml',
        'views/library_category.xml',
        'views/library_loan.xml',
        'views/library_menu.xml'
    ],
    'application':True,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
