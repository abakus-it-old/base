# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class BusinessUnit(models.Model):
    _name = 'business.unit'
    _description = 'Business Units'
    _order = 'sequence, name'

    def _get_default_journal(self):
        journal = self.env['account.invoice'].default_get(['journal_id'])['journal_id']
        journal_id = self.env['account.journal'].search([('id', '=', journal)])
        return journal_id

    name = fields.Char(related='partner_id.name', string='Business Unit Name', required=True, store=True)
    company_id = fields.Many2one('res.company', 'Company', required=True)
    description = fields.Text()
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    user_ids = fields.Many2many('res.users', 'business_unit_users_rel', 'bu_id', 'user_id', string='Accepted Users')
    journal_id = fields.Many2one('account.journal',
                                 string="Accounting Journal",
                                 required=True,
                                 default=lambda self: self._get_default_journal())
    sequence = fields.Integer(help='Used to order BUs in the switcher', default=10)
