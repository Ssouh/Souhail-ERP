# -*- coding: utf-8 -*-

from odoo import models, fields, api


class __souhail__gestion_bc(models.Model): #une commande de bon de commande
    _name = 'souhail.element.order'
    _description = 'one element of the purchase order'
    
    _rec_name = 'designation'
    _order = 'designation asc'

    designation = fields.Text(string='Designation')
    description = fields.Text(string='Description')
    quantity = fields.Float(default=0.00)
    unit_price = fields.Monetary(string='Price', currency_field='currency_id')

    # RELATIONSHIPS
    # ----------------------------------------------------------
    currency_id = fields.Many2one('res.currency', readonly=True,
                                  default=lambda self: self.env.user.company_id.currency_id) 
    po_id = fields.Many2one('souhail.purchase.order', string='Purchase Order')

    # COMPUTE FIELDS
    # ----------------------------------------------------------
    revised_unit_price = fields.Monetary(string='Revised Price',
                                         compute='_compute_revised_unit_price',
                                         inverse='_inverse_revised_unit_price',
                                         currency_field='currency_id')

    total_amount = fields.Monetary(currency_field='currency_id',
                                   store=True,
                                   compute="_compute_total_amount",
                                   string='Amount')

    
    @api.depends('unit_price', 'quantity')
    def _compute_total_amount(self):
      for record in self:
        record.total_amount = record.revised_unit_price * record.quantity



    @api.depends('unit_price')
    def _compute_revised_unit_price(self):
      for record in self:
        if record.revised_unit_price in [0, 0.0, False]:
            record.revised_unit_price = record.unit_price
      return

    

    
    def _inverse_revised_unit_price(self):
        pass

    # POLYMORPH FUNCTIONS
    # ----------------------------------------------------------
    
    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, "{}: {}".format(record.po_id.no,
                                                      record.designation)
                           )
                          )
        return result