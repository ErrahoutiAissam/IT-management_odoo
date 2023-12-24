# maintenance_model.py

from odoo import models, fields

class Maintenance(models.Model):
    _name = 'parc_informatique.maintenance'
    _description = 'Maintenance Model'

    asset_id = fields.Many2one('parc_informatique.base_asset', string='Asset', required=True)
    maintenance_date = fields.Date(string='Maintenance Date', required=True)
    description = fields.Text(string='Description')
    responsible_technician = fields.Char(string='Responsible Technician')
