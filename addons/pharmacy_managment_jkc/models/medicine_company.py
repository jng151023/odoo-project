from odoo import api, fields, models, _
import re
from odoo.exceptions import ValidationError




class MedicineCompany(models.Model):
    _name = 'medicine.company'
    _description = 'Medicine Company'

    name = fields.Char(string='Manufactured Company', required=True)
    # contact_person = fields.Char(string='Contact Person')
    supplier_id = fields.Many2one('res.partner',
                                  string='Vendor', store=True)
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')

    @api.onchange('phone')
    def _onchange_phone(self):
        if self.phone:
            if re.match("^[0-9]{10}$", self.phone) == None:
                raise ValidationError(_("Enter valid 10 digits Mobile number"))
