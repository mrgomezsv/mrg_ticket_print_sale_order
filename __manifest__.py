# -*- coding: utf-8 -*-
{
    'name': "Impresión de Tickets (Presupuestos y Facturas DTE)",

    'summary': """
        Imprime ticket de presupuesto (sale.order) e imprime ticket de
        venta DTE (account.move) cuando el DTE ha sido procesado por Hacienda.""",

    'description': """
        Módulo de impresión de tickets:
        - Ticket de presupuesto (sale.order): accesible desde el menú de impresión.
        - Ticket DTE de factura (account.move): botón habilitado cuando
          el DTE tiene estado "PROCESADO" (sellado por Hacienda).
          Incluye: tipo DTE, número control, datos receptor, líneas,
          totales, QR de verificación y sello de recepción.
    """,

    'author': "Mario Roberto Gomez",
    'website': "https://mrgomezsv.github.io/",

    'category': 'Accounting/Sales',
    'version': '16.0.1.1.0',
    'license': 'LGPL-3',

    'depends': ['base', 'sale', 'sale_management', 'account', 'mrg_dte_sv'],

    'data': [
        'views/templates.xml',           # Ticket existente para sale.order
        'views/ticket_dte_template.xml', # Nuevo ticket para account.move DTE
        'reports/report.xml',            # Ambos reportes (sale.order + account.move)
        'views/account_move_view.xml',   # Botón en formulario de factura
    ],
}
