from openerp import models, fields, api

import datetime
import logging
_logger = logging.getLogger(__name__)


class mail_message_improved(models.Model):
    _inherit = 'mail.message'

    @api.model
    def _get_related(self, condition=False):
        if not self.model:
            return False
        if not condition:
            condition = [self.model]
        if self.model not in condition:
            return False
        return self.env[self.model].search([('id', '=', self.res_id)])

    @api.model
    def get_project_name(self, condition=False):
        related = self._get_related(condition)
        if related and related.project_id and related.project_id.name:
            return related.project_id.name
        return False

    @api.model
    def get_partner_name(self, condition=False):
        related = self._get_related(condition)
        if related and related.partner_id and related.partner_id.name:
            return related.partner_id.name
        return False