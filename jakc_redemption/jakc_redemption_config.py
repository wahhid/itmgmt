from openerp.osv import fields, osv
import logging

_logger = logging.getLogger(__name__)

class rdm_config(osv.osv):
    _name = 'rdm.config'
    _description = 'Redemption Config'
    
    def get_config(self, cr, uid, context=None):
        ids = self.search(cr, uid, [('state','=', True),], context=context)
        if ids:
            return self.browse(cr, uid, ids[0], context=context)
        else:
            return None
            
    _columns = {
        'rdm_server': fields.char('RDM Server', size=50),        
        'enable_email' : fields.boolean('Enable Email'),
        'pop3_download': fields.boolean('POP3 Download'),
        'pop3_server': fields.char('POP3 Server', size=50),
        'pop3_user': fields.char('POP3 User', size=50),
        'pop3_password': fields.char('POP3 Password', size=50),
        'email_from': fields.char('Email From', size=50),
        'report_server': fields.char('Report Server', size=50),
        'report_server_port': fields.char('Report Server Port', size=50),
        'report_user': fields.char('Report User', size=50),
        'report_password': fields.char('Report Password', size=50),
        'trans_delete_allowed': fields.boolean('Allow Delete Transaction'),
        'trans_delete_approver': fields.integer('Delete Transaction Approver'),
        'state': fields.boolean('Status'),
    }
    
    _defaults = {
        'rdm_server': lambda *a:'localhost',         
        'enable_email': lambda *a: False,
        'pop3_download': lambda *a: False,
        'state': lambda *a: True,
    }
    
rdm_config()

class rdm_config_settings(osv.osv_memory):
    _name = 'rdm.config.settings'
    _inherit = 'res.config.settings'
    _columns = {
        'rdm_server': fields.char('RDM Server', size=50),
        'enable_email' : fields.boolean('Enable Email'),
        'pop3_download': fields.boolean('POP3 Download'),
        'pop3_server': fields.char('POP3 Server', size=50),
        'pop3_user': fields.char('POP3 User', size=50),
        'pop3_password': fields.char('POP3 Password', size=50),
        'email_from': fields.char('Email From', size=50),
        'report_server': fields.char('Report Server', size=50),
        'report_server_port': fields.char('Report Server Port', size=50),
        'report_user': fields.char('Report User', size=50),
        'report_password': fields.char('Report Password', size=50),        
        'trans_delete_allowed': fields.boolean('Allow Delete Transaction'),
        'trans_delete_approver': fields.many2one('hr.employee','Delete Transaction Approver'),
    }

    def _get_config(self, cr, uid, context=None):
        ids = self.pool.get('rdm.config').search(cr, uid, [('state','=', True),], context=context)
        if ids:
            config  = self.pool.get('rdm.config').browse(cr, uid, ids[0], context=context)
        else:
            config = None
        return config

    def get_default_rdm_server(self, cr, uid, fields, context=None):
        config = self._get_config(cr, uid, context)
        if config:
            rdm_server = config.rdm_server 
        else: 
            data = {}
            result_id = self.pool.get('rdm.config').create(cr, uid, data, context=context)
            rdm_server = None
        return {'rdm_server': rdm_server}


    def set_default_rdm_server(self, cr, uid, ids, context=None):
        config = self._get_config(cr, uid, context)
        setting = self.browse(cr, uid, ids[0], context)
        rdm_server = setting.rdm_server
        self.pool.get('rdm.config').write(cr, uid, [config.id], {'rdm_server': rdm_server})

    
    def get_default_enable_email(self, cr, uid, fields, context=None):
        config = self._get_config(cr, uid, context)
        if config:
            enable_email = config.enable_email 
        else: 
            data = {}
            result_id = self.pool.get('rdm.config').create(cr, uid, data, context=context)
            enable_email = False
        return {'enable_email': enable_email}


    def set_default_enable_email(self, cr, uid, ids, context=None):
        config = self._get_config(cr, uid, context)
        setting = self.browse(cr, uid, ids[0], context)
        enable_email = setting.enable_email
        self.pool.get('rdm.config').write(cr, uid, [config.id], {'enable_email': enable_email})

    def get_default_pop3_download(self, cr, uid, fields, context=None):
        config = self._get_config(cr, uid, context)
        if config:
            pop3_download = config.pop3_download 
        else: 
            data = {}
            result_id = self.pool.get('rdm.config').create(cr, uid, data, context=context)
            pop3_download = False
        return {'pop3_download': pop3_download}


    def set_default_pop3_download(self, cr, uid, ids, context=None):
        config = self._get_config(cr, uid, context)
        setting = self.browse(cr, uid, ids[0], context)
        pop3_download = setting.pop3_download
        self.pool.get('rdm.config').write(cr, uid, [config.id], {'pop3_download': pop3_download})    
        
    def get_default_pop3_server(self, cr, uid, fields, context=None):
        config = self._get_config(cr, uid, context)
        if config:
            pop3_server = config.pop3_server 
        else: 
            data = {}
            result_id = self.pool.get('rdm.config').create(cr, uid, data, context=context)
            pop3_server = False
        return {'pop3_server': pop3_server}


    def set_default_pop3_server(self, cr, uid, ids, context=None):
        config = self._get_config(cr, uid, context)
        setting = self.browse(cr, uid, ids[0], context)
        pop3_server = setting.pop3_server
        self.pool.get('rdm.config').write(cr, uid, [config.id], {'pop3_server': pop3_server})
        
    def get_default_pop3_user(self, cr, uid, fields, context=None):
        config = self._get_config(cr, uid, context)
        if config:
            pop3_user = config.pop3_user
        else: 
            data = {}
            result_id = self.pool.get('rdm.config').create(cr, uid, data, context=context)
            pop3_user = None
        return {'pop3_user': pop3_user}

    def set_default_pop3_user(self, cr, uid, ids, context=None):
        config = self._get_config(cr, uid, context)
        setting = self.browse(cr, uid, ids[0], context)
        pop3_user = setting.pop3_user
        self.pool.get('rdm.config').write(cr, uid, [config.id], {'pop3_user': pop3_user})

    def get_default_pop3_password(self, cr, uid, fields, context=None):
        config = self._get_config(cr, uid, context)
        if config:
            pop3_password = config.pop3_password
        else: 
            data = {}
            result_id = self.pool.get('rdm.config').create(cr, uid, data, context=context)
            pop3_password = None
        return {'pop3_password': pop3_password}

    def set_default_pop3_password(self, cr, uid, ids, context=None):
        config = self._get_config(cr, uid, context)
        setting = self.browse(cr, uid, ids[0], context)
        pop3_password = setting.pop3_password
        self.pool.get('rdm.config').write(cr, uid, [config.id], {'pop3_password': pop3_password})

    def get_default_email_from(self, cr, uid, fields, context=None):
        config = self._get_config(cr, uid, context)
        if config:
            email_from = config.email_from
        else: 
            data = {}
            result_id = self.pool.get('rdm.config').create(cr, uid, data, context=context)
            email_from = False
        return {'email_from': email_from}

    def set_default_email_from(self, cr, uid, ids, context=None):
        config = self._get_config(cr, uid, context)
        setting = self.browse(cr, uid, ids[0], context)
        email_from = setting.email_from
        self.pool.get('rdm.config').write(cr, uid, [config.id], {'email_from': email_from})

        
    def get_default_report_server(self, cr, uid, fields, context=None):
        config = self._get_config(cr, uid, context)
        if config:
            report_server = config.report_server
        else: 
            data = {}
            result_id = self.pool.get('rdm.config').create(cr, uid, data, context=context)
            report_server = None
        return {'report_server': report_server}

    def set_default_report_server(self, cr, uid, ids, context=None):
        config = self._get_config(cr, uid, context)
        setting = self.browse(cr, uid, ids[0], context)
        report_server = setting.report_server
        self.pool.get('rdm.config').write(cr, uid, [config.id], {'report_server': report_server})


    def get_default_report_server_port(self, cr, uid, fields, context=None):
        config = self._get_config(cr, uid, context)
        if config:
            report_server_port = config.report_server_port
        else: 
            data = {}
            result_id = self.pool.get('rdm.config').create(cr, uid, data, context=context)
            report_server_port = None
        return {'report_server_port': report_server_port}

    def set_default_report_server_port(self, cr, uid, ids, context=None):
        config = self._get_config(cr, uid, context)
        setting = self.browse(cr, uid, ids[0], context)
        report_server_port = setting.report_server_port
        self.pool.get('rdm.config').write(cr, uid, [config.id], {'report_server_port': report_server_port})

        
    def get_default_report_user(self, cr, uid, fields, context=None):
        config = self._get_config(cr, uid, context)
        if config:
            report_user = config.report_user
        else: 
            data = {}
            result_id = self.pool.get('rdm.config').create(cr, uid, data, context=context)
            report_user = None
        return {'report_user': report_user}

    def set_default_report_user(self, cr, uid, ids, context=None):
        config = self._get_config(cr, uid, context)
        setting = self.browse(cr, uid, ids[0], context)
        report_user = setting.report_user
        self.pool.get('rdm.config').write(cr, uid, [config.id], {'report_user': report_user})
    
    def get_default_report_password(self, cr, uid, fields, context=None):
        config = self._get_config(cr, uid, context)
        if config:
            report_password = config.report_password
        else: 
            data = {}
            result_id = self.pool.get('rdm.config').create(cr, uid, data, context=context)
            report_password = None
        return {'report_password': report_password}

    def set_default_report_password(self, cr, uid, ids, context=None):
        config = self._get_config(cr, uid, context)
        setting = self.browse(cr, uid, ids[0], context)
        report_password = setting.report_password
        self.pool.get('rdm.config').write(cr, uid, [config.id], {'report_password': report_password})    
     
    def get_default_trans_delete_allowed(self, cr, uid, fields, context=None):
        config = self._get_config(cr, uid, context)
        if config:
            trans_delete_allowed = config.trans_delete_allowed
        else: 
            data = {}
            result_id = self.pool.get('rdm.config').create(cr, uid, data, context=context)
            trans_delete_allowed = False
        return {'trans_delete_allowed': trans_delete_allowed}

    def set_default_trans_delete_allowed(self, cr, uid, ids, context=None):
        config = self._get_config(cr, uid, context)
        setting = self.browse(cr, uid, ids[0], context)
        trans_delete_allowed = setting.trans_delete_allowed
        self.pool.get('rdm.config').write(cr, uid, [config.id], {'trans_delete_allowed': trans_delete_allowed})  
        
    def get_default_trans_delete_approver(self, cr, uid, fields, context=None):
        config = self._get_config(cr, uid, context)
        if config:
            trans_delete_approver = config.trans_delete_approver
        else: 
            data = {}
            result_id = self.pool.get('rdm.config').create(cr, uid, data, context=context)
            trans_delete_approver = None
        return {'trans_delete_approver': trans_delete_approver}

    def set_default_trans_delete_approver(self, cr, uid, ids, context=None):
        config = self._get_config(cr, uid, context)
        setting = self.browse(cr, uid, ids[0], context)
        trans_delete_approver = setting.trans_delete_approver
        self.pool.get('rdm.config').write(cr, uid, [config.id], {'trans_delete_approver': trans_delete_approver})   
     