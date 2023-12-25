from odoo import models, fields

class Asset(models.Model):
    _name = 'parc_informatique.asset'
    _description = 'Base Asset Model'

    name = fields.Char(string='Asset Name', required=True)
    asset_id = fields.Char(string='Asset ID', required=True)
    model = fields.Char(string='Model')
    image = fields.Binary(string='Image', attachment=True, help="Select image here", widget='image')
    manufacturer = fields.Char(string='Manufacturer')
    purchase_date = fields.Date(string='Purchase Date')
    warranty_information = fields.Char(string='Warranty Information')
    specifications = fields.Text(string='Specifications')
    current_user = fields.Many2one('parc_informatique.user', string='Current User')
    location = fields.Many2one('parc_informatique.location', string='Location')
    maintenance_history = fields.One2many('parc_informatique.maintenance', 'asset_id', string='Maintenance History')
    inventory = fields.Many2one('parc_informatique.inventory', string='Inventory')