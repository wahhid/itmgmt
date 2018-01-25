from openerp.osv import fields, osv

class rdm_customer_point(osv.osv):
    _name = "rdm.customer.point"
    _inherit = "rdm.customer.point"
    _columns = {
        'reward_trans_id': fields.many2one('rdm.reward.trans','Reward Transaction ID',readonly=True),        
    }
rdm_customer_point()