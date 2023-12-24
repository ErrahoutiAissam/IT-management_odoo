# hardware_model.py

from odoo import models, fields
from .asset import Asset  


class Hardware(Asset):
    _name = 'parc_informatique.hardware'
    _description = 'Hardware Model'

    processor_type = fields.Char(string='Processor Type')
    memory_size = fields.Float(string='Memory Size (GB)')
    storage_size = fields.Float(string='Storage Size (GB)')
    graphics_card = fields.Char(string='Graphics Card')
    network_adapter = fields.Char(string='Network Adapter')
    additional_hardware_info = fields.Text(string='Additional Hardware Information')
