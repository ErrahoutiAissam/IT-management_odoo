# software_model.py

from odoo import models, fields

class Software(Asset):
    _name = 'parc_informatique.software'
    _description = 'Software Model'

    license_key = fields.Char(string='License Key')
    version = fields.Char(string='Version')
    software_type = fields.Selection([
        ('operating_system', 'Operating System'),
        ('application', 'Application'),
        ('utility', 'Utility'),
        ('antivirus', 'Antivirus'),
    ], string='Software Type')
    additional_software_info = fields.Text(string='Additional Software Information')
