# -*- coding: utf-8 -*-
{
    'name': "fix Many2one Search limit odoo",

    'summary': """
        default limit in odoo many2one is 160,it increases its limit""",

    'description': """
       default limit in odoo many2one is 160,it increases its limit
    """,

    'author': "kashif",
    'website': "http://www.odoo.com",


    'depends':['base','web'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/template.xml',

    ],

}