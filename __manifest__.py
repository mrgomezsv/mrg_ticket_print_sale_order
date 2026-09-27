# -*- coding: utf-8 -*-
{
    'name': "Impresión de Ticket desde Presupuestos",

    'summary': """
        Agrega opcion de imprimir ticket en sale order""",

    'description': """
        Agrega opcion de imprimir ticket en sale order
    """,

    'author': "Link Tech",
    'website': "https://www.linktechsv.com/",

    'category': 'Sales',
    'version': '18.0.1.0.0',
    'license': 'LGPL-3',

    'depends': ['base', 'sale', 'sale_management'],

    'data': [
        'views/templates.xml',
        'reports/report.xml',
    ],
    'installable': True,
}
