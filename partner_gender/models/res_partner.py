# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    gender = fields.Selection([
    	('male', 'Male'),
    	('female', 'Female')
    ], string="Gender")