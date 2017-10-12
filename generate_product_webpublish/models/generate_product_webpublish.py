# -*- coding: utf-8 -*-
#################################################################################
# Author      : Boubaker Abdallah. (<www.boubaker.tk>)
# All Rights Reserved.
#
#
#################################################################################

from openerp import models, fields, api, _
from datetime import datetime


class generate_product_webpublish(models.TransientModel):
    _name = 'generate.product.webpublish'

    overwrite_webpublish = fields.Boolean(String="Publier Sur Siteweb")
    overwrite_webnonpublish = fields.Boolean(String="Cacher au Siteweb")

    @api.multi
    def generate_product_webpublish(self):
        for rec in self.env['product.template'].browse(self._context.get('active_ids')):
            if not self.overwrite_webpublish and rec.website_published:
                continue
            rec.write({'website_published': True
            })
        return True


    @api.multi
    def generate_product_webnonpublish(self):
        for rec in self.env['product.template'].browse(self._context.get('active_ids')):
            if not self.overwrite_webnonpublish and rec.website_published:
                continue
            rec.write({'website_published': False
            })
        return True

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
