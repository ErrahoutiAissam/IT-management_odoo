from odoo import models, fields

class ITDepartment(models.Model):
    _name = 'parc_informatique.department'
    _description = 'IT Department Model'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    users = fields.Many2many('parc_informatique.user', string='Users')
    assets = fields.Many2many('parc_informatique.asset', string='Assets')
