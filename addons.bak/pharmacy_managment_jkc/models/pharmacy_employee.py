from odoo import models, fields

class PharmacyEmployee(models.Model):
    _name = 'pharmacy.employee'
    _description = 'Pharmacy Employee'
    _inherit = ['hr.employee']

    # contract_ids = fields.One2many('hr.contract', 'employee_id', string='Contracts')
