# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    x_payment_link = fields.Char(string='Payment Link', default=None)
