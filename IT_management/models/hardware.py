from odoo import models, fields

class Hardware(models.Model):
    _name = 'parc_informatique.hardware'
    _description = 'Hardware Model'

    name = fields.Char(string='Asset Name', required=True)
    manufacturer = fields.Char(string='Manufacturer')
    purchase_date = fields.Date(string='Purchase Date')
    specifications = fields.Text(string='Specifications')
    current_user = fields.Many2one('parc_informatique.user', string='Current User')
    maintenance_history = fields.One2many('parc_informatique.maintenance', 'hardware_id', string='Maintenance History')
    inventory = fields.Many2one('parc_informatique.inventory', string='Inventory')

    processor_type = fields.Char(string='Processor Type')
    memory_size = fields.Float(string='Memory Size (GB)')
    storage_size = fields.Float(string='Storage Size (GB)')
    graphics_card = fields.Char(string='Graphics Card')
    network_adapter = fields.Char(string='Network Adapter')
    additional_hardware_info = fields.Text(string='Additional Hardware Information')
