
from odoo import models, fields, api

class ITInventory(models.Model):
    _name = 'parc_informatique.inventory'
    _description = 'IT Inventory Model'

    name = fields.Char(string='Inventory Name', required=True)
    assets = fields.One2many('parc_informatique.asset', 'inventory', string='Assets')
    total_assets = fields.Integer(string='Total Assets', compute='_compute_total_assets', store=True)
    total_hardware = fields.Integer(string='Total Hardware', compute='_compute_total_assets', store=True)
    total_software = fields.Integer(string='Total Software', compute='_compute_total_assets', store=True)

    @api.depends('assets')
    def _compute_total_assets(self):
        for inventory in self:
            inventory.total_assets = len(inventory.assets)
            inventory.total_hardware = len(inventory.assets.filtered(lambda a: a._name == 'parc_informatique.hardware'))
            inventory.total_software = len(inventory.assets.filtered(lambda a: a._name == 'parc_informatique.software'))
