from odoo import models, fields, api

class PurchaseRequisition(models.Model):
    _inherit = "purchase.requisition"
    _description = "Purchase Requisition"

    def test_function(self):
        return
    
class PurchaseRequisitionType(models.Model):
    _inherit = "purchase.requisition.type"
    _description = "Purchase Requisition Type"

    def test_function(self):
        return
    
class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def test_function(self):
        return