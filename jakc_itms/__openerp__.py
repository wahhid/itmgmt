{
    'name' : 'IT Service Management',
    'version' : '1.0',
    'author' : 'JakC',
    'category' : 'Generic Modules/ITMS Management',
    'depends' : ['base_setup','base','hr'],
    'init_xml' : [],
    'data' : [			
        'security/jakc_itms_security.xml',
        'security/ir.model.access.csv',	
        'jakc_itms_view.xml',        
        'hr_department_view.xml',        
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}