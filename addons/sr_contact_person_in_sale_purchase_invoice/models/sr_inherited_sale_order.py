# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) Sitaram Solutions (<https://sitaramsolutions.in/>).
#
#    For Module Support : info@sitaramsolutions.in  or Skype : contact.hiren1188
#
##############################################################################

from odoo import fields, models


class Saleorder(models.Model):
    _inherit = "sale.order"

    partner_contact_person_id = fields.Many2one('res.partner',string="Contact Person", readonly=True, states={'draft': [('readonly', False)]})
