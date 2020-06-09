# -*- coding: utf-8 -*-

from odoo import models, fields, api
import math


def choices_tuple(choices, is_sorted=True):
    choices = [(i.lower(), i.upper()) for i in choices]

    if is_sorted:
        return sorted(choices, key=lambda tup: tup[0])

    return choices
    
class gestion_bc(models.Model): #Bon de commande
        _name = 'souhail.purchase.order'
        _rec_name = 'no'
        _description = 'the hole purchase order'
        _order = 'no'

        # CHOICES
        # ----------------------------------------------------------
        STATES = choices_tuple(['draft', 'active', 'closed', 'cancelled'], is_sorted=False) # pour avoir une vision sur le suivi
        TYPES = choices_tuple(['standard', 'approved', 'not approved'], is_sorted=False)  # pour avoir une vision sur le processus de consultation

        # BASIC FIELDS
        # ----------------------------------------------------------
        state = fields.Selection(STATES, default='draft')

        is_parent = fields.Boolean(default=True)
        type = fields.Selection(TYPES, default='standard')
        no = fields.Char(string='Purchase Order')
        date = fields.Date(string='Date')
       
        remark = fields.Text(string='Remark')

        # RELATIONSHIPS
        # ----------------------------------------------------------
        currency_id = fields.Many2one('res.currency', string="Currency",
                                      default=lambda self: self.env.user.company_id.currency_id)

        contractor_id1 = fields.Many2one('res.users', string='Contractor') # contracteur == Fournisseur 
        contractor_id2 = fields.Text(string='Contractor name')
        contractor_address = fields.Text(string='Contractor address')

        po_line_ids = fields.One2many('souhail.element.order',
                                      'po_id',
                                      string="Lines") # Lines == commandes 

        # parent is the main PO
        parent_id = fields.Many2one('souhail.purchase.order',
                                    domain=[('is_parent', '=', True)],
                                    string='Parent Purchase Order')

        

        # ONCHANGE FIELDS
        # ----------------------------------------------------------
        @api.onchange('parent_id')
        def _onchange_is_parent(self):
            self.is_parent = not self.parent_id

       

        # BUTTONS/TRANSITIONS
        # ----------------------------------------------------------
        
        def set2draft(self):
            self.state = 'draft'

        
        def set2active(self):
            self.state = 'active'

        
        def set2closed(self):
            self.state = 'closed'

        
        def set2cancelled(self):
            self.state = 'cancelled'