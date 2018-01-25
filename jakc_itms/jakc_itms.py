from openerp.osv import fields, osv
from datetime import datetime

class itms_company(osv.osv):
    _name = "itms.company"
    _description = "Company"
    _columns = {
        'company_id': fields.char('Company ID', size=4, required=True),            
        'name': fields.char('Name', size=100, required=True),            
    }    
itms_company()

class itms_vendor(osv.osv):
    _name = "itms.vendor"
    _description = "vendor"
    _columns = {
        'name': fields.char('Name', size=100, required=True),            
    }    
itms_vendor()
