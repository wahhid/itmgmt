{
    'name' : 'Redemption and Point Management',
    'version' : '2.0',
    'author' : 'JakC',
    'category' : 'Generic Modules/Redemption And Point Management',
    'depends' : ['base_setup','base','hr'],
    'init_xml' : [],
    'data' : [			
        'security/jakc_rdm_security.xml',
        'security/ir.model.access.csv',             
        'jakc_redemption_view.xml',
        'jakc_redemption_menu.xml',        
        'jakc_redemption_config_view.xml',
        'jakc_redemption_config_menu.xml',                
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}