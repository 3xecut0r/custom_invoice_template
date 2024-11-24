# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.addons.payment import utils as payment_utils
from werkzeug import urls


class AccountMoveSend(models.TransientModel):
    _inherit = 'account.move.send'

    amount = fields.Monetary(currency_field='currency_id', required=True)
    currency_id = fields.Many2one('res.currency')
    partner_id = fields.Many2one('res.partner')

    @api.onchange('amount', 'currency_id', 'partner_id', 'company_id')
    def _compute_link(self):
        for payment_link in self:
            related_document = self.env['account.move'].browse(self.env.context.get('active_id'))
            payment_link.amount = related_document.amount_total
            payment_link.amount = related_document.amount_total
            url_params = {
                'amount': payment_link.amount,
                'access_token': payment_link._get_access_token(),
                **payment_link._get_additional_link_values(),
            }
            related_document.x_payment_link = f'{related_document.get_base_url()}/payment/pay?{urls.url_encode(url_params)}'


    def _get_access_token(self):
        self.ensure_one()
        return payment_utils.generate_access_token(
            self.partner_id.id, self.amount, self.currency_id.id
        )

    def _get_additional_link_values(self):
        """ Return the additional values to append to the payment link.

        Note: self.ensure_one()

        :return: The additional payment link values.
        :rtype: dict
        """
        self.ensure_one()
        return {
            'currency_id': self.currency_id.id,
            'partner_id': self.partner_id.id,
            'company_id': self.company_id.id,
        }
