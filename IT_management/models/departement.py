from odoo import models, fields

class ITDepartment(models.Model):
    _name = 'parc_informatique.department'
    _description = 'IT Department Model'

    name = fields.Char(string='Department Name', required=True)
    description = fields.Text(string='Description')
    users = fields.One2many('parc_informatique.user', 'department', string='Users')
