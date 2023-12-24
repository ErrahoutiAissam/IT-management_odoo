from odoo import models, fields

class Maintenance(models.Model):
    _name = 'parc_informatique.maintenance'

    maintenance_date = fields.Date(string='Maintenance Date')
    maintenance_type = fields.Char(string='Maintenance Type')
    description = fields.Text(string='Description')
    cost = fields.Float(string='Cost')
    asset_id = fields.Many2one('parc_informatique.asset', string='Asset')
