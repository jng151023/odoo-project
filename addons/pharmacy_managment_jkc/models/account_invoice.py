from odoo import models, fields, api, _
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        """
        Override the action_post method to check for expired products before confirming the invoice.
        """
        for inv in self:
            expired_products = inv.invoice_line_ids.filtered(
                lambda line: line.product_id.expiry_date and line.product_id.expiry_date <= fields.Date.today()
            )
            if expired_products:
                warning_message = _("Cannot confirm invoice. Some medicines may have expired.")
                for line in expired_products:
                    warning_message += "\n- %s (%s)" % (line.product_id.display_name, line.product_id.expiry_date)
                raise UserError(warning_message)

        # Continue with the original action_confirm method
        return super(AccountMove, self).action_post()
