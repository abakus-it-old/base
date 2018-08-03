# -*- coding: utf-8 -*-
import json

from odoo import models
from odoo.http import request


class HttpBusinessUnit(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        session_info = super(HttpBusinessUnit, self).session_info()
        user = request.env.user
        # TODO: add a base.group_multi_bu
        display_switch_business_unit_menu = len(user.business_unit_ids) > 1
        session_info['business_unit_id'] = request.env.user.business_unit_id.id if request.session.uid else None
        if display_switch_business_unit_menu:
            session_info['user_business_units'] = {
                'current_business_unit': (user.business_unit_id.id, user.business_unit_id.name),
                'allowed_business_units': [(bu.id, bu.name) for bu in user.business_unit_ids]
            }
        else:
            session_info['user_business_units'] = False
        return session_info
