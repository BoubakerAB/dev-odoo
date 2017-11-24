# -*- coding: utf-8 -*-
#################################################################################
# Author      : Boubaker Abdallah. (<www.boubaker.tk>)
# All Rights Reserved.
#
#################################################################################

{
    'name': 'Generate Product Web Publish',
    'version': '1.0', 
    'summary': "Generate  product web publish",
    'category': 'Sales Management',  
    'description': """Publish several articles at once to the mass""",
    'author': 'Boubaker',
    'website': 'http://www.boubaker.tk',
    'depends': ['base','product', 'sale'],
    'data': [
        'views/generate_product_webpublish_view.xml',
        'views/res_config_view.xml'
    ],
    'images': ['static/description/main_screenshot.png'],
    'installable': True,
    'auto_install': False
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
