from odoo import models, fields

class User(models.Model):
    _name = 'parc_informatique.user'
    _description = 'IT User Model'

    name = fields.Char(string='Name', required=True)
    department = fields.Many2one('parc_informatique.department', string='Department')
    phone_number = fields.Char(string='Phone Number')
    email = fields.Char(string='Email')
    assigned_assets = fields.One2many('parc_informatique.asset', 'current_user', string='Assigned Assets')
