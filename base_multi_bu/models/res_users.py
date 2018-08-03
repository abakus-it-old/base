# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class ResUsersBusinessUnit(models.Model):
    _inherit = 'res.users'

    def _business_units_count(self):
        return self.env['business.unit'].sudo().search_count([])

    business_unit_ids = fields.Many2many('business.unit',
                                         'busines_unit_users_rel',
                                         'user_id', 'bu_id',
                                         string='Allowed Business Unit')
    business_unit_id = fields.Many2one('business.unit',
                                       string='Current Business Unit')
    business_units_count = fields.Integer(compute='_compute_business_units_count',
                                          string="Number of Business Units",
                                          default=_business_units_count)

    @api.multi
    def _compute_business_units_count(self):
        business_units_count = self._business_units_count()
        for user in self:
            user.business_units_count = business_units_count
