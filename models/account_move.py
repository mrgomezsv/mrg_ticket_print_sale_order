# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError

# Códigos oficiales del catálogo CAT-002 de Hacienda de El Salvador
DTE_CATALOG_CODES = {'01', '03', '04', '05', '06', '07', '08', '09', '11', '14', '15'}


class AccountMove(models.Model):
    _inherit = 'account.move'

    dte_tipo_catalogo_valido = fields.Boolean(
        string="Tipo de Documento DTE Válido",
        compute="_compute_dte_tipo_catalogo_valido",
    )

    @api.depends('doc_type_id', 'doc_type_id.type', 'doc_type_id.doc_type_id.code')
    def _compute_dte_tipo_catalogo_valido(self):
        for move in self:
            code = False
            if move.doc_type_id:
                code = (
                    move.doc_type_id.doc_type_id.code
                    or move.doc_type_id.type
                    or False
                )
            if code:
                code_str = str(code).strip()
                code_padded = code_str.zfill(2) if len(code_str) == 1 else code_str
                move.dte_tipo_catalogo_valido = (
                    code_str in DTE_CATALOG_CODES or code_padded in DTE_CATALOG_CODES
                )
            else:
                move.dte_tipo_catalogo_valido = False

    def action_facturar_dte(self):
        """Bloquea la facturación DTE si el tipo de documento no pertenece al catálogo de Hacienda."""
        for move in self:
            if not move.dte_tipo_catalogo_valido:
                raise UserError(_(
                    "No se puede emitir DTE para esta factura porque el tipo de documento '%s' "
                    "no está relacionado a un código del catálogo DTE de Hacienda."
                ) % (move.doc_type_id.name if move.doc_type_id else 'Sin tipo de documento'))
        return super(AccountMove, self).action_facturar_dte()

    def action_print_dte_ticket(self):
        """Imprime el ticket de venta en formato 80mm para la factura actual (soporta facturas normales y DTE)."""
        self.ensure_one()
        return self.env.ref(
            'mrg_ticket_print_sale_order.action_ticket_dte_account_move'
        ).report_action(self)
