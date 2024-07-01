from odoo import models, fields

class MedicineCategory(models.Model):
    _inherit = 'product.category'
    _description = 'Medicine Category'

    # custom fields specific to medicine category
    is_medicine = fields.Boolean(string='Is Medicine',default=True)
