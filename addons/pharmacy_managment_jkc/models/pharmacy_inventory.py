from odoo import models, fields, api

class PickingType(models.Model):
    _inherit = "stock.picking.type"
    _description = "Picking Type"

    def test_function(self):
        return
    
class StockQuant(models.Model):
    _inherit = 'stock.quant'
    _description = 'Quants'

    def test_function(self):
        return
    
class StockValuationLayer(models.Model):
    _inherit = 'stock.valuation.layer'
    _description = 'Stock Valuation Layer'

    def test_function(self):
        return
    
class StockLot(models.Model):
    _inherit = 'stock.lot'
    _description = 'Lot/Serial'

    def test_function(self):
        return
    
class Location(models.Model):
    _inherit = "stock.location"
    _description = "Inventory Locations"

    def test_function(self):
        return

class StockPutawayRule(models.Model):
    _inherit = 'stock.putaway.rule'
    _description = 'Putaway Rule'

    def test_function(self):
        return