from odoo import models, fields, api

class ITInventory(models.Model):
    _name = 'parc_informatique.inventory'
    _description = 'IT Inventory Model'

    name = fields.Char(string='Inventory Name', required=True)
    hardware_assets = fields.One2many('parc_informatique.hardware', 'inventory', string='Hardware Assets')
    software_assets = fields.One2many('parc_informatique.software', 'inventory', string='Software Assets')
    total_assets = fields.Integer(string='Total Assets', compute='_compute_total_assets', store=True)
    total_hardware = fields.Integer(string='Total Hardware', compute='_compute_total_assets', store=True)
    total_software = fields.Integer(string='Total Software', compute='_compute_total_assets', store=True)

    @api.depends('hardware_assets', 'software_assets')
    def _compute_total_assets(self):
        for inventory in self:
            inventory.total_hardware = len(inventory.hardware_assets)
            inventory.total_software = len(inventory.software_assets)
            inventory.total_assets = inventory.total_hardware + inventory.total_software
