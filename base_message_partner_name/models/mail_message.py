from openerp import models, fields, api

import datetime
import logging
_logger = logging.getLogger(__name__)


class mail_message_improved(models.Model):
    _inherit = 'mail.message'

    @api.model
    def get_partner_name(self):
        if self.model:
            related_object = self.env[self.model].search([('id', '=', self.res_id)])
            if (related_object):
                if related_object.partner_id:
                    return related_object.partner_id.name
        return ""