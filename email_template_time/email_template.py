import datetime
from datetime import date
from pytz import timezone
import pytz
from jinja2 import contextfilter

from openerp.addons.mail.models import mail_template

@contextfilter
def time(context, dtformat, tz=None):
    if not dtformat:
        return dtformat

    local_tz = timezone('Europe/Brussels')
    now = datetime.datetime.now(local_tz)
    
    return now.strftime(dtformat)

mail_template.mako_template_env.filters.update(
    time=time,
)