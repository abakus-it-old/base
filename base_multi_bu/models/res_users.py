# -*- coding: utf-8 -*-
# (c) AbAKUS IT Solutions
import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class ResUsersBusinessUnit(models.Model):
    _inherit = 'res.users'

    business_unit_ids = fields.Many2many('business.unit', 'busines_unit_users_rel',
                                         'user_id', 'bu_id',
                                         string='Allowed Business Unit')
    business_unit_id = fields.Many2one('business.unit',
                                       string='Current Business Unit')
