{
    'name' : 'Assets Management',
    'version' : '1.0',
    'author' : 'JakC',
    'category' : 'Generic Modules/Assets Management',
    'depends' : ['base_setup','base','jakc_itms'],
    'init_xml' : [],
    'data' : [			
        'security/ir.model.access.csv',                
        'jakc_assets_view.xml',		
        'jakc_assets_report_view.xml',
        'jakc_assets_menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}