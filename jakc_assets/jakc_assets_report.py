from openerp.osv import fields, osv
from datetime import datetime
import logging

_logger = logging.getLogger(__name__)

class assets_report(osv.osv_memory):
    _name = "assets.report"
    _columns = {
        'report_id' : fields.selection([
            ('01','Asset Detail'),
            ('02','Hardware Type Summary All Company'),
            ('03','Hardware Type Summary Per Company'),
            ],'Report Name'),
        '_03_company_id': fields.integer('Company ID')
    }
    
    def generate_report(self, cr, uid, ids, context=None):
        params = self.browse(cr, uid, ids, context=context)
        param = params[0]   
        if param.report_id == '01':
            serverUrl = 'http://172.16.0.3:8080/jasperserver'
            j_username = 'itms_operator'
            j_password = 'itms123'
            ParentFolderUri = '/itms'
            reportUnit = '/itms/asset_detail_report'
            url = serverUrl + '/flow.html?_flowId=viewReportFlow&standAlone=true&_flowId=viewReportFlow&ParentFolderUri=' + ParentFolderUri + '&reportUnit=' + reportUnit + '&decorate=no&j_username=' + j_username + '&j_password=' + j_password
            return {
                'type':'ir.actions.act_url',
                'url': url,
                'nodestroy': True,
                'target': 'new' 
            }
        if param.report_id == '02':
            serverUrl = 'http://172.16.0.3:8080/jasperserver'
            j_username = 'itms_operator'
            j_password = 'itms123'
            ParentFolderUri = '/itms'
            reportUnit = '/itms/hardware_type_summary_all_company'
            url = serverUrl + '/flow.html?_flowId=viewReportFlow&standAlone=true&_flowId=viewReportFlow&ParentFolderUri=' + ParentFolderUri + '&reportUnit=' + reportUnit + '&decorate=no&j_username=' + j_username + '&j_password=' + j_password
            return {
                'type':'ir.actions.act_url',
                'url': url,
                'nodestroy': True,
                'target': 'new' 
            }            
        if param.report_id == '03':
            serverUrl = 'http://172.16.0.3:8080/jasperserver'
            j_username = 'itms_operator'
            j_password = 'itms123'
            ParentFolderUri = '/itms'
            reportUnit = '/itms/hardware_type_summary_per_company'
            url = serverUrl + '/flow.html?_flowId=viewReportFlow&standAlone=true&_flowId=viewReportFlow&ParentFolderUri=' + ParentFolderUri + '&reportUnit=' + reportUnit + '&COMPANYID=' + str(param._03_company_id)  + '&decorate=no&j_username=' + j_username + '&j_password=' + j_password
            return {
                'type':'ir.actions.act_url',
                'url': url,
                'nodestroy': True,
                'target': 'new' 
            }
            
assets_report()
