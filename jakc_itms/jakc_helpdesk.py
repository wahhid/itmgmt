from openerp import models, fields, api
from openerp.exceptions import ValidationError


class HelpdeskCategory(models.Model):
    _name = 'helpdesk.category'

    name = fields.Char('Name', size=100, required=True)


class HelpdeskPriority(models.Model):
    _name = 'helpdesk.priority'

    name = fields.Char('Name', size=100, required=True)

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
