# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _

import logging
_logger = logging.getLogger(__name__)

class IrMailServer(models.Model):
    _inherit = 'ir.mail_server'

    @api.model
    def send_email(self, message, mail_server_id=None, smtp_server=None, smtp_port=None,
                   smtp_user=None, smtp_password=None, smtp_encryption=None, smtp_debug=False,
                   smtp_session=None):
        email_to = message['To'][message['To'].index('<')+1:message['To'].index('>')]
        # Check if email is member of the organization (if one user has this email)
        if (len(self.env['res.users'].search(['|', ('alias_id', '=', email_to), ('email', '=', email_to)])) == 0):

            # Else, not send the emaill
            raise exceptions.ValidationError(_('The email was not sent to  ') + email_to + _(' because emails for outside the organization are blocked.'))
            return False

        _logger.debug("\n\n SEND EMAIL ADDRESS: %s", email_to)
        return super(IrMailServer, self).send_email(message, mail_server_id=mail_server_id, smtp_server=smtp_server, smtp_port=smtp_port, smtp_user=smtp_user, smtp_password=smtp_password, smtp_encryption=smtp_encryption, smtp_debug=smtp_debug)

        
        
