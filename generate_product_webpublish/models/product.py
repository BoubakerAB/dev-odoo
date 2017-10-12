# -*- coding: utf-8 -*-
#################################################################################
# Author      : Boubaker Abdallah. (<www.boubaker.tk>)
# All Rights Reserved.
#
#
#################################################################################

from openerp import models, api, _
from datetime import datetime


class product_template(models.Model):
    _inherit = "product.template"

    @api.model
    def create(self, vals):
        res = super(product_template, self).create(vals)
        if res:
            if not vals.get('website_published'):
                website_published_str = True
                res.write({'website_published' : website_published_str})
        return res

    @api.model
    def ncreate(self, vals):
        res = super(product_template, self).create(vals)
        if res:
            if not vals.get('website_published'):
                website_published_str = False
                res.write({'website_published' : website_published_str})
        return res



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
