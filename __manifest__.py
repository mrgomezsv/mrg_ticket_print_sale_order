# -*- coding: utf-8 -*-
{
    'name': "Impresión de Tickets (Presupuestos y Facturas DTE / No DTE)",

    'summary': """
        Imprime ticket de presupuesto (sale.order) e imprime ticket de
        venta en formato 80mm para facturas (account.move) tanto normales como DTE.
        Controla visibilidad de facturación DTE según catálogo de Hacienda.""",

    'description': """
        Módulo de impresión de tickets:
        - Ticket de presupuesto (sale.order): accesible desde el menú de impresión.
        - Ticket de factura (account.move): botón habilitado en facturas publicadas.
          * Factura normal (sin DTE): imprime ticket de venta 80mm con número de factura,
            cliente, líneas, subtotales, totales y forma de pago.
          * Factura con DTE procesado: incluye además tipo DTE, número de control,
            código de generación, QR de verificación y sello de recepción MH.
        - Control de Facturación DTE: oculta el botón "Facturar DTE" si el tipo de documento
          no pertenece a los códigos oficiales del catálogo DTE de Hacienda.
    """,

    'author': "Mario Roberto Gomez",
    'website': "https://mrgomezsv.github.io/",

    'category': 'Accounting/Sales',
    'version': '19.0.1.3.0',
    'license': 'LGPL-3',

    'depends': ['base', 'sale', 'sale_management', 'account', 'mrg_dte_sv'],

    'data': [
        'views/templates.xml',           # Ticket existente para sale.order
        'views/ticket_dte_template.xml', # Ticket dual para account.move (Normal y DTE)
        'reports/report.xml',            # Ambos reportes (sale.order + account.move)
        'views/account_move_view.xml',   # Botón en formulario de factura y control DTE
    ],
    'installable': True,
}
