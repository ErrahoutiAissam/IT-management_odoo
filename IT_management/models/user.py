import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class User(models.Model):
    _name = 'parc_informatique.user'
    _description = 'IT User Model'
    _inherit = ['hr.employee']

    # Your additional fields for the IT User Model
    assigned_hardware = fields.One2many('parc_informatique.hardware', 'current_user', string='Assigned Hardware')
    assigned_software = fields.Many2many('parc_informatique.software', 'parc_informatique_user_software_rel', 'user_id', 'software_id', string='Assigned Software')
    category_ids = fields.Many2many(
        'parc_informatique.category',
        'parc_informatique_user_category_rel',
        'user_id',
        'category_id',
        string='Categories'
    )
    department_id = fields.Many2one('hr.department', string='Department')
    name = fields.Many2one('hr.employee', string='Employee')  # Change to 'hr.employee'

    @api.onchange('department_id')
    def onchange_department_id(self):
        if self.department_id:
            domain = [('department_id', '=', self.department_id.id)]
        else:
            domain = []
        _logger.info(f"Department change - Domain: {domain}")
        return {'domain': {'name': domain}}

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or []
        domain = []
        if name and self._context.get('department_id'):
            domain += [('department_id', '=', self._context['department_id']), ('name', operator, name)]
        elif name:
            domain += [('name', operator, name)]

        _logger.info(f"Name search - Name: {name}, Domain: {domain}")
        return super(User, self).name_search(name=name, args=args + domain, operator=operator, limit=limit)
