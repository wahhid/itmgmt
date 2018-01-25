import time

from openerp.report import report_sxw
from openerp import pooler


class itms_assets_detail_report(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(itms_assets_detail_report, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({'time': time})

report_sxw.report_sxw('report.itms.assets.detail.webkit',
                      'asset.assets',
                      'addons/jakc_assets_webkit_report/report/itms_assets_detail.mako',
                      parser=itms_assets_detail_report)

class itms_assets_list_report(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(itms_assets_list_report, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({'time': time})

report_sxw.report_sxw('report.itms.assets.list.webkit',
                      'asset.assets',
                      'addons/jakc_assets_webkit_report/report/itms_assets_list.mako',
                      parser=itms_assets_list_report)
    