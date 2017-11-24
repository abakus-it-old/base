# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class UOM(models.Model):
    _inherit = 'product.uom'

    report_decimal_precision = fields.Integer(string="Decimal precision for reports")

    @api.model
    def getQuantityWithPrecision(self, quantity):
        format = "%." + str(self.report_decimal_precision) + "f"
        
        return str(format % quantity)
    