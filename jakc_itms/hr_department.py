from openerp.osv import fields,osv
from

class hr_department(osv.osv):    
    _name = 'hr.department'
    _inherit = 'hr.department'    
    _columns = {
        'department_code': fields.char('Department Code', size=4),            
    }
    
hr_department()