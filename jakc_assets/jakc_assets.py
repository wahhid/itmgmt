from openerp.osv import fields, osv
from datetime import datetime
import logging

_logger = logging.getLogger(__name__)
maint_requester_email = 'whidayat@jakc.com'

class asset_category(osv.osv):
    _name = "asset.category"
    _description = "Asset Category"
    _columns = {
        'name': fields.char('Name', size=100, required=True),
    }    
asset_category()

class asset_type(osv.osv):
    _name = "asset.type"
    _description = "Asset Type"
    _columns = {
        'type_id': fields.char('Type ID', size=2, required=True),            
        'name': fields.char('Name', size=100, required=True),
        'iface_maintenance': fields.boolean('Maintenance'),
        'iface_pi': fields.boolean('Physical Inspection'),
    }    
asset_type()

class asset_status(osv.osv):
    _name = "asset.status"
    _description = "Asset Status"
    _columns = {
        'name': fields.char('Name', size=100, required=True),            
    }    
asset_status()


class asset_software(osv.osv):
    _name = "asset.software"
    _description = "Asset Software"
    _columns = {
        'name': fields.char('Name', size=100, required=True),            
        'managed': fields.boolean('Managed'),     
        'assets_ids': fields.one2many('asset.assets.software','sofware_id','Assets'),
    }    
asset_software()

class asset_assets_memory(osv.osv):
    _name = "asset.assets.memory"
    _description = "Assets Memory"
    _columns = {
        'assets_id': fields.many2one('asset.assets', 'Memory'),
        'banklabel': fields.char('Bank Label',size=100),
        'capacity': fields.char('Capacity',size=100),
        'devicelocator': fields.char('Locator',size=100),
    }

asset_assets_memory()

class asset_assets_disk(osv.osv):
    _name = "asset.assets.disk"
    _description = "Assets Disk"
    _columns = {
        'assets_id': fields.many2one('asset.assets', 'Physical Disk'),
        'caption': fields.char('Caption',size=100),
        'size': fields.char('Size',size=100),        
    }

asset_assets_disk()
    
class asset_assets_software(osv.osv):
    _name = "asset.assets.software"
    _description = "Assets Software"    
    _columns = {
        'assets_id': fields.many2one('asset.assets', 'Asset'),
        'sofware_id': fields.many2one('asset.software','Software'),
    }
asset_assets_software()

class asset_location(osv.osv):
    _name = "asset.location"
    _description = "Asset Location"
    _columns = {
        'name': fields.char('Location', size=100, required=True),            
    }

asset_location()

class asset_maintenance(osv.osv):
    _name = "asset.maintenance"
    _description = "Asset Maintenance"
    _columns = {
        'ticket_id': fields.integer('Ticket ID'),
        'assets_id': fields.integer('Assets ID'),
        'maint_date': fields.datetime('Maintenance Date'),
        'hidden_state':  fields.selection([('draft','Wait for Maintenance'),('done','Finish')],'Hidden Status'),
        'state': fields.selection([('draft','Wait for Maintenance'),('done','Finish')],'Status'),
    }
    _defaults = {                
        'maint_date': lambda *a: fields.datetime.now(),
        'hidden_state': lambda *a: 'draft',
        'state': lambda *a: 'draft',        
    }    
    
asset_maintenance()


class asset_assets(osv.osv):
    _name = "asset.assets"
    _description = "Assets"
    def get_day_selection(self,cursor, user_id, context=None):
        return (
            ('1','1'),
            ('2','2'),
            ('3','3'),
            ('4','4'),
            ('5','5'),
            ('6','6'),
            ('7','7'),
            ('8','8'),
            ('9','9'),
            ('10','10'),
            ('11','11'),
            ('12','12'),
            ('13','13'),
            ('14','14'),
            ('15','15'),
            ('16','16'),
            ('17','17'),
            ('18','18'),
            ('19','19'),
            ('20','20'),
            ('21','21'),
            ('22','22'),
            ('23','23'),
            ('24','24'),
            ('25','25'),
            ('26','26'),
            ('27','27'),
            ('28','28'),
            ('29','29'),
            ('30','30'),
            ('31','31'),
        )
    
    def get_month_selection(self,cursor, user_id, context=None):
        return(
            ('1','January'),
            ('2','February'),
            ('3','March'),
            ('4','April'),
            ('5','May'),
            ('6','June'),
            ('7','July'),
            ('8','August'),
            ('9','September'),
            ('10','October'),
            ('11','November'),
            ('12','December'),
        )    
    _columns = {
        'barcode': fields.char('Barcode', size=20, readonly=True),            
        'type': fields.many2one('asset.type','Type', required=True),
        'status': fields.many2one('asset.status','Status', required=True),
        'location': fields.many2one('asset.location','Location', required=True),
        'label': fields.boolean('Labeled'),        
        
        'image1': fields.binary('Image 1'),
        'image2': fields.binary('Image 2'),
        'image3': fields.binary('Image 3'),
        'image4': fields.binary('Image 4'),
        'image5': fields.binary('Image 5'),
        
        'model': fields.char('Model', size=200),            
        'serial_number': fields.char('Serial Number', size=200),            
        'vendor': fields.many2one('itms.vendor','Vendor'),
        
        'purchase_order': fields.char('Purchase Order #', size=20),
        'purchase_date': fields.date('Purchase Date'),
        'supplier': fields.many2one('res.partner','Supplier'),
        'warranty': fields.date('Warranty'),
        'decomission_date': fields.date('Decomission Date'),
        
        'company': fields.many2one('itms.company','Company', required=True),
        'department': fields.many2one('hr.department','Department', required=True),        
        'owner': fields.many2one('hr.employee','Owner'), 
        'login_name': fields.char('Login Name', size=30),
        
        'ismaintenance' : fields.boolean('Is Maintenance'),
        'maint_owner': fields.many2one('hr.employee','Technician'),
        'repeat': fields.selection([('1','Daily'),('2','Monthly'),('3','Quaterly'),('4','Half Yearly'),('5','Yearly')],'Repeat'),
        'maint_day': fields.selection(get_day_selection,'Day'),        
        'maint_month': fields.selection(get_month_selection,'Month'),
        'maint_date': fields.date('Maintenance Date'),

        'ispi': fields.boolean('Is PI'),
        'pi_owner': fields.many2one('hr.employee','PI Technician'),
        'pi_repeat': fields.selection([('1', 'Daily'), ('2', 'Monthly'), ('3', 'Quaterly'), ('4', 'Half Yearly'), ('5', 'Yearly')], 'Repeat'),
        'pi_day': fields.selection(get_day_selection, 'PI Day'),
        'pi_month': fields.selection(get_month_selection,'PI Month'),
        'pi_date': fields.date('PI Date'),

        'name': fields.char('Name', size=100),                    
        'os': fields.char('Operating System', size=200),
        'processor': fields.char('Processor', size=200),
        'last_scan': fields.datetime('Last Scan'),
        'scan_status': fields.selection([('success','Success'),('failed','Failed')],'Scan Status'),
        'memory_ids': fields.one2many('asset.assets.memory', 'assets_id', 'Memory'),
        'harddisk_ids': fields.one2many('asset.assets.disk', 'assets_id', 'Physical Disk'),        
        'assets_software_ids': fields.one2many('asset.assets.software', 'assets_id', 'Softwares'),
        'assets_maintenance_ids': fields.one2many('asset.maintenance','assets_id','Maintenances'),
        
    }        
    
    
    def _create_maint_ticket(self, cr, uid, employee, assets, context=None):
        _logger.info("Start Create Ticket for Maintenance")
        #create ticket
        ticket_data = {}
        ticket_data['employee'] = employee.id
        ticket_data['name'] = 'Maintenance Alert - Maintenance for asset ' + assets.name
        ticket_data['asset'] = assets.id
        ticket_data['description'] = "Please process maintenance for " + assets.name
        ticket_id = self.pool.get('helpdesk.ticket').create(cr, uid, ticket_data,context=context)           
        _logger.info("End Create Ticket for Maintenance")
        return ticket_id

    def _create_pi_ticket(self, cr, uid, employee, assets, context=None):
        _logger.info("Start Create Ticket for PI")
        #create ticket
        ticket_data = {}
        ticket_data['employee'] = employee.id
        ticket_data['name'] = 'PI Alert - PI for asset ' + assets.name
        ticket_data['asset'] = assets.id
        ticket_data['description'] = "Please process pi for " + assets.name
        ticket_id = self.pool.get('helpdesk.ticket').create(cr, uid, ticket_data,context=context)
        _logger.info("End Create Ticket for PI")
        return ticket_id


    
    def get_employee_by_email(self, cr, uid, email_from, context=None):
        obj = self.pool.get('hr.employee')
        ids = obj.search(cr, uid, [('work_email','=',email_from)], context=context)
        if len(ids) > 0:
            employees = obj.browse(cr, uid, ids, context=context)
            return employees[0]
        else:
            return None    
        
    def maint_schedule_yearly(self, cr, uid, context=None):
        _logger.info("Start Yearly Maintenance Schedule")
        day = datetime.today().day
        month = datetime.today().month
        employee = self.get_employee_by_email(cr, uid, 'whidayat@taman-anggrek-mall.com', context=context)
        args = [('ismaintenance','=',True),('repeat','=','5'),('maint_month','=',month),('maint_day','=',day)]
        assets_ids = self.pool.get('asset.assets').search(cr, uid, args, context=context)
        assetss = self.pool.get('asset.assets').browse(cr, uid, assets_ids, context=context)
	for assets in assetss:
            _logger.info("Star Process " + assets.name)
            ticket_id = self._create_maint_ticket(cr, uid, employee, assets, context=context)
        _logger.info("End Yearly Maintenance Schedule")

    def maint_schedule_monthly(self, cr, uid, context=None):
        _logger.info("Start Monthly Maintenance Schedule")
        day = datetime.today().day
        month = datetime.today().month
        employee = self.get_employee_by_email(cr, uid, 'whidayat@taman-anggrek-mall.com', context=context)
        args = [('ismaintenance','=',True),('repeat','=','2'),('maint_day','=',day)]
        assets_ids = self.pool.get('asset.assets').search(cr, uid, args, context=context)
        assetss = self.pool.get('asset.assets').browse(cr, uid, assets_ids, context=context)
        for assets in assetss:
            _logger.info("Star Process " + assets.name)
            ticket_id = self._create_maint_ticket(cr, uid, employee, assets, context=context)
        _logger.info("End Monthly Maintenance Schedule")

    def pi_schedule_yearly(self, cr, uid, context=None):
        _logger.info("Start Yearly PI Schedule")
        day = datetime.today().day
        month = datetime.today().month
        employee = self.get_employee_by_email(cr, uid, 'whidayat@taman-anggrek-mall.com', context=context)
        args = [('pi_month','=',month)]
        assets_ids = self.pool.get('asset.assets').search(cr, uid, args, context=context)
        assetss = self.pool.get('asset.assets').browse(cr, uid, assets_ids, context=context)
        for assets in assetss:
            _logger.info("Star Process " + assets.name)
            ticket_id = self._create_pi_ticket(cr, uid, employee, assets, context=context)
        _logger.info("End Yearly PI Schedule")

  
    def maint_schedule(self, cr, uid, context=None):
        _logger.info("Start Maintenance Schedule")
        day = datetime.today().day
        month = datetime.today().month    
        employee = self.get_employee_by_email(cr, uid, 'whidayat@taman-anggrek-mall.com', context=context)    
        args = [('ismaintenance','=',True),('maint_month','=',month),('maint_day','=',day)]
        assets_ids = self.pool.get('asset.assets').search(cr, uid, args, context=context)
        assetss = self.pool.get('asset.assets').browse(cr, uid, assets_ids, context=context)        
        for assets in assetss:
            _logger.info("Start Process " + assets.name)
            maint_repeat = assets.repeat
            if maint_repeat == '1':            
                ticket_id = self._create_maint_ticket(cr, uid, employee, assets, context=context)
                maintenance = {}
                maintenance['ticket_id'] = ticket_id
                maintenance['assets_id'] = assets.id            
                self.pool.get('asset.maintenance').create(cr, uid ,maintenance, context=context)                
            elif maint_repeat == '2':                
                if assets.maint_day == day:
                    ticket_id = self._create_maint_ticket(cr, uid, employee, assets, context=context)
                    maintenance = {}
                    maintenance['ticket_id'] = ticket_id
                    maintenance['assets_id'] = assets.id            
                    self.pool.get('asset.maintenance').create(cr, uid ,maintenance, context=context)                    
            elif maint_repeat == '3':
                if assets.maint_day == day and assets.maint_month == 3 or assets.maint_month == 6 or assets.maint_month == 9 or assets.main_month == 12:
                    ticket_id = self._create_maint_ticket(cr, uid, employee, assets, context=context)
                    maintenance = {}
                    maintenance['ticket_id'] = ticket_id
                    maintenance['assets_id'] = assets.id            
                    self.pool.get('asset.maintenance').create(cr, uid ,maintenance, context=context)
            elif maint_repeat == '4':
                if assets.maint_day == day and assets.maint_month == 6 or assets.main_month == 12:
                    ticket_id = self._create_maint_ticket(cr, uid, employee, assets, context=context)
                    maintenance = {}
                    maintenance['ticket_id'] = ticket_id
                    maintenance['assets_id'] = assets.id            
                    self.pool.get('asset.maintenance').create(cr, uid ,maintenance, context=context)                    
            elif maint_repeat == '5':
                if assets.maint_day == day and assets.maint_month == month:
                    ticket_id = self._create_maint_ticket(cr, uid, employee, assets, context=context)
                    maintenance = {}
                    maintenance['ticket_id'] = ticket_id
                    maintenance['assets_id'] = assets.id            
                    self.pool.get('asset.maintenance').create(cr, uid ,maintenance, context=context)
            _logger.info("End Process " + assets.name)
        _logger.info("End Maintenance Schedule")    
        
    def pi_schedule(self, cr, uid, context=None):
        day = datetime.today().day
        month = datetime.today().month    
        employee_ids = self.pool.get('hr_employee').search(cr, uid, [('work_email','=',maint_requester_email)], context=context)
        employee = self.pool.get('hr.employee').browse(cr, uid, employee_ids[0], context=context)                
        month = datetime.today().month
        assets_ids = self.pool.get('asset.assets').search(cr, uid, [('pi_month','=',month)], context=context)
        assetss = self.pool.get('asset.assets').browse(cr, uid, assets_ids, context=context)        
        for assets in assetss:
            ticket_id = self.pool.get('helpdesk.ticket').create()
            
        
    def _check_unique_insesitive(self, cr, uid, ids, context=None):
        sr_ids = self.search(cr, 1 , [], context=context)
        lst = [x.name.lower() for x in self.browse(cr, uid, sr_ids, context=context) if x.name and x.id not in ids]
        for self_obj in self.browse(cr, uid, ids, context=context):
            if self_obj.name and self_obj.name.lower() in  lst:
                return False
            return True
        
    _sql_constraints = [('asset_name_unique', 'unique(name)', 'Name already exists'),('asset_barcode_unique', 'unique(barcode)', 'Barcode already exists')]
    #_constraints = [(_check_unique_insesitive, 'Asset name already exists', ['name'])]
    
    def _get_company(self, cr, uid, id, context):
        obj = self.pool.get('itms.company')
        ids = []
        ids.append(id)
        return obj.read(cr, uid, ids,[], context)    
        
    def _get_department(self, cr, uid, id, context):				
        obj = self.pool.get('hr.department')
        ids = []
        ids.append(id)
        return obj.read(cr, uid, ids, [], context)    
    
    def _get_asset_type(self, cr, uid, id, context):				
        obj = self.pool.get('asset.type')
        ids = []
        ids.append(id)
        return obj.read(cr, uid, ids, [], context)      
    
    def _generate_barcode(self,cr,uid,values,context):    
        company_id = values['company']
        companys = self._get_company(cr,uid,company_id,context)
        company = companys[0]
        print company
        
        department_id = values['department']
        departments = self._get_department(cr,uid,department_id,context)        
        department = departments[0]
        
        type_id = values['type']
        types = self._get_asset_type(cr,uid,type_id,context)    
        type = types[0]
        
        return company['company_id'] + department['department_code'] + type['type_id']
        
    def create(self, cr, uid, values, context=None):		                        
        if 'name' in values:
            values['name'] = values['name'].upper()
        asset_type = self.pool.get('asset.type').browse(cr, uid, values.get('type'), context=context)
        if asset_type:
            if asset_type.iface_maintenance:
                if 'type' in values.keys() and 'is_maintenance' in values.keys():
                    if  values.get('is_maintenance') != True:
                        raise osv.except_osv('Warning!',"Please define maintenance schedule for this asset.")
                else:
                    raise osv.except_osv('Warning!',"Please define maintenance schedule for this asset.")
        if asset_type.iface_pi:
            if 'type' in values.keys() and 'is_pi' in values.keys():
                if values.get('is_pi') != True:
                    raise osv.except_osv('Warning!', "Please define physical inspection schedule for this asset.")
            else:
                raise osv.except_osv('Warning!', "Please define physical schedule for this asset.")

        prefix = self._generate_barcode(cr,uid,values,context)    
        sequence = self.pool.get('ir.sequence').get(cr, uid, 'asset.barcode.sequence')    
        barcode = prefix + sequence
        values.update({'barcode':barcode})
	return super(asset_assets, self).create(cr, uid, values, context = context)
    
    def write(self, cr, uid, ids, values, context=None):
        print "write asset"
        if 'name' in values:
            values['name'] = values['name'].upper()                
        return super(asset_assets, self).write(cr, uid, ids, values, context = context)
    
    def _maintenance_asset(self, cr, uid, context=None):
        print 'Start Maintenance Asset'
        ids = self.search(cr, uid, [('ismaintenance','=',True)])
        assets = self.read(cr, uid, ids, [], context)
        for asset in assets:
            print asset
                
asset_assets()
