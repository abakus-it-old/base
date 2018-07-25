# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class BusinessUnit(models.Model):
    _name = 'business.unit'

    def _get_default_journal(self):
        journal = self.env['account.invoice'].default_get(['journal_id'])['journal_id']
        journal_id = self.env['account.journal'].search([('id', '=', journal)])
        return journal_id

    name = fields.Char(required=True)
    company_id = fields.Many2one('res.company', 'Company', required=True)
    description = fields.Text()
    partner_id = fields.Many2one('res.partner', 'Partner')
    user_id = fields.Many2one('res.user', 'User')
    journal_id = fields.Many2one('account.journal',
                                 string="Accounting Journal",
                                 required=True,
                                 default=lambda self: self._get_default_journal())
