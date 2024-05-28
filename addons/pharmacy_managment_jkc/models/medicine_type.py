from odoo import models, fields

class MedicineType(models.Model):
    _name = 'medicine.type'
    _description = 'Medicine Type'

    name = fields.Char(string='Name', required=True)
