# -*- coding: utf-8 -*-
from odoo import models


class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_print_dte_ticket(self):
        """Imprime el ticket de venta en formato 80mm para la factura actual (soporta facturas normales y DTE)."""
        self.ensure_one()
        return self.env.ref(
            'mrg_ticket_print_sale_order.action_ticket_dte_account_move'
        ).report_action(self)
