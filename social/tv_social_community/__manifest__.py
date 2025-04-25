# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Social Community Module',
    'version': '1.0',
    'summary': 'A module for managing Social Community Members',
    'author': 'Techvertis', 
    'category': 'Social',
    'depends': ['membership'],
    'data': [
        'security/ir.model.access.csv',
        'data/member_relation_data.xml',
        'data/membership_sequence.xml',
        'views/membership_view.xml',
        'views/member_relation_view.xml',
    ],

    'installable': True,
    'application': True,
}