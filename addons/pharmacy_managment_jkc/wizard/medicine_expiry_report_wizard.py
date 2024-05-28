# models/report_wizard.py

from odoo import models, fields,api, _
from odoo.exceptions import ValidationError


class MedicineExpiryReportWizard(models.TransientModel):
    _name = 'expiry.report.wizard'
    _description = 'Medicine Expiry Report Wizard'

    @api.onchange('start_date', 'end_date')
    def check_date(self):
        if self.start_date and self.end_date and self.start_date > self.end_date:
            warning = {
                'title': _('Validation Error!'),
                'message': _('From date should be less than To date!'),
            }
            return {'warning': warning}

    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')

    # code for button cancel

    # @api.multi
    def print_cancel(self):
        return {'type': 'ir.actions.act_window_close'}

    # code for pdf report printing

    # @api.multi
    def print_medicine_exp_report_pdf(self):
        pharm_domain = []
        pharm_domain.append(('expiry_date', '>=', self.start_date))
        pharm_domain.append(('expiry_date', '<=', self.end_date))
        pharm_domain.append(('qty_available', '!=', 0))
        if pharm_domain:
            pharm_ids = self.env['product.template'].search((pharm_domain))
        if pharm_ids:
            pharm_list = []
            for pharm in pharm_ids:
                pharm_data = {
                    'name': pharm.name,
                    'expiry_date': pharm.expiry_date,
                    'available_qty': pharm.qty_available,
                    'medicine_type_id': pharm.medicine_type_id.name,
                    'category_id': pharm.category_id.name,
                    'medicine_company_id': pharm.medicine_company_id.name,
                }
                pharm_list.append(pharm_data)
            data = {
                'ids': self.ids,
                'model': self._name,
                'pharm_list': pharm_list or '',
                'form': {
                    'start_date': self.start_date,
                    'end_date': self.end_date,
                },
            }
            return self.env.ref('pharmacy_managment_jkc.medicine_exp_report_action').report_action(
                self, data=data)
        else:
            raise ValidationError(
                _('No records found!!')
            )
