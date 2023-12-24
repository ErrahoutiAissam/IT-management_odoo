from odoo import models, fields

class Location(models.Model):
    _name = 'parc_informatique.location'
    _description = 'Asset Location'

    name = fields.Char(string='Location Name', required=True)
    description = fields.Text(string='Description')
    assets = fields.One2many('parc_informatique.asset', 'location', string='Assets')
