from odoo import models, fields

class Software(models.Model):
    _name = 'parc_informatique.software'
    _description = 'Software Model'

    name = fields.Char(string='Software Name', required=True)
    manufacturer = fields.Char(string='Manufacturer')
    purchase_date = fields.Date(string='Purchase Date')
    specifications = fields.Text(string='Specifications')
    current_users = fields.Many2many('parc_informatique.user', string='Current Users')  # Update field type to Many2many
    maintenance_history = fields.One2many('parc_informatique.maintenance', 'software_id', string='Maintenance History')
    inventory = fields.Many2one('parc_informatique.inventory', string='Inventory')

    license_key = fields.Char(string='License Key')
    version = fields.Char(string='Version')
    software_type = fields.Selection([
        ('operating_system', 'Operating System'),
        ('application', 'Application'),
        ('utility', 'Utility'),
        ('other', 'Other'),
    ], string='Software Type')
    additional_software_info = fields.Text(string='Additional Software Information')
    install_date = fields.Date(string='Install Date')
