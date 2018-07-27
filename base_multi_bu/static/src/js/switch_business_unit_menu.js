odoo.define('web.SwitchBusinessUnitMenu', function(require) {
"use strict";

var Model = require('web.Model'); // to access model res.users through ajax rpc
var session = require('web.session');
var SystrayMenu = require('web.SystrayMenu');
var Widget = require('web.Widget');

var SwitchBusinessUnitMenu = Widget.extend({
    template: 'SwitchBusinessUnitMenu',
    willStart: function() {
        if (!session.user_business_units) {
            return $.Deferred().reject();
        }
        return this._super();
    },
    start: function() {
        var self = this;
        this.$el.on('click', '.dropdown-menu li a[data-menu]', _.debounce(function(ev) {
            ev.preventDefault();
            var business_unit_id = $(ev.currentTarget).data('business-unit-id');
            new Model('res.users').call('write', [[session.uid], {'business_unit_id': business_unit_id}]).then(function() {
                location.reload();
            });
        }, 1500, true));

        self.$('.oe_topbar_name').text(session.user_business_units.current_business_unit[1]);

        var business_units_list = '';
        _.each(session.user_business_units.allowed_business_units, function(business_unit) {
            var a = '';
            if (business_unit[0] === session.user_business_units.current_business_unit[0]) {
                a = '<i class="fa fa-check o_current_business_unit"></i>';
            } else {
                a = '<span class="o_business_unit"/>';
            }
            business_units_list += '<li><a href="#" data-menu="business_unit" data-business-unit-id="' + business_unit[0] + '">' + a + business_unit[1] + '</a></li>';
        });
        self.$('.dropdown-menu').html(business_units_list);
        return this._super();
    },
});

SystrayMenu.Items.push(SwitchBusinessUnitMenu);

return SwitchBusinessUnitMenu;

});
