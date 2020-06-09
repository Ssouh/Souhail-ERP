# -*- coding: utf-8 -*-
{
    "name": "Souhail_ERP",
    "author": "Souhail_Amghar",
    "company": "Agence Urbaine de Casablanca (AUC)",
    "website": "https://www.google.com/maps/place/Casablanca+Urban+Agency/@33.5916208,-7.6223512,15z/data=!4m2!3m1!1s0x0:0x893d7614e3a489ae?sa=X&ved=2ahUKEwiH55mgxurpAhUHxoUKHT6UAfEQ_BIwCnoECBEQCA",

    

    
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Purchase Management",
    
    # any module necessary for this one to work correctly
    "depends": ["base"],
    # always loaded
    "data": [
        #'security/ir.model.access.csv',
        "views/views.xml",
        #"views/templates.xml",
    ], 
    'demo': [],
    "license": "AGPL-3",
    "installable": True,
    'application': True,
    #'auto_install': False,
}
