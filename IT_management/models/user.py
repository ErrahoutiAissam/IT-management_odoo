# user_model.py

from odoo import models, fields

class User(models.Model):
    _name = 'parc_informatique.user'
    _description = 'IT User Model'

    name = fields.Char(string='Name', required=True)
    department = fields.Many2one('parc_informatique.department', string='Department')
    contact_information = fields.Char(string='Contact Information')
    assigned_assets = fields.One2many('parc_informatique.base_asset', 'current_user', string='Assigned Assets')
