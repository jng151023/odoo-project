from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'Pharmacy Sale Order'

    def action_confirm(self):
        """
        Override the action_confirm method to check for expired products before confirming the sale order.
        """
        for order in self:
            expired_products = order.order_line.filtered(
                lambda line: line.product_id.expiry_date and line.product_id.expiry_date <= fields.Date.today()
            )
            if expired_products:
                warning_message = _("Cannot create sale order. Some medicines may have expired.")
                for line in expired_products:
                    warning_message += "\n- %s (%s)" % (line.product_id.display_name, line.product_id.expiry_date)
                raise UserError(warning_message)

        # Continue with the original action_confirm method
        return super(SaleOrder, self).action_confirm()
