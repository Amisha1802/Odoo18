# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from datetime import date

class Partner(models.Model):
    _inherit = 'res.partner'


    is_member =fields.Boolean(string="Member", default=True , help="Active if present in membership module.")
    position = fields.Selection([
        ('member', 'Family Member'),
        ('head', 'Family Head'),
    ], string="Family Role",default='member', required=True, help="Hidden for Individual/Company.")
    unique_member_no = fields.Char(string="Member No.", readonly=True, copy=False, help="Membership No.")
    relation_id = fields.Many2one('member.relation', string="Relation", help="Relation with the Contact.")
    date_of_birth = fields.Date(string="DOB", required=True, help="Date of Birth")
    age = fields.Integer(string="Age", compute="_compute_age", help="Age")
    #native address
    native_street = fields.Char(string="Native Street")
    native_street2 = fields.Char(string="Native Street2")
    native_city = fields.Char(string="Native City")
    native_state_id = fields.Many2one(
        "res.country.state", string="Native State",
        domain="[('country_id', '=?', native_country_id)]")
    native_zip = fields.Char(string="Native Zip")
    native_country_id = fields.Many2one("res.country", string="Native Country")
    income = fields.Monetary(string="Income", help="Annual Income")
    family_income = fields.Selection([
        ('low', 'Below ₹2,00,000'),
        ('lower_middle', '₹2,00,000 - ₹5,00,000'),
        ('middle', '₹5,00,000 - ₹10,00,000'),
        ('upper_middle', '₹10,00,000 - ₹25,00,000'),
        ('high', '₹25,00,000 - ₹50,00,000'),
        ('very_high', 'Above ₹50,00,000'),
        ],string="Family Income", help="Annual Family Income")
    occupation = fields.Selection([
        ('retired', 'Retired'), 
        ('job', 'Job'), 
        ('business', 'Business'), 
        ('school', 'School'), 
        ('college', 'College')
        ],string="Occupation", required=True, help="Occupation")
    gender = fields.Selection([
    	('male', 'Male'),
    	('female', 'Female'),
    	('other', 'Other'),
    	], string='Gender', required=True, help="Gender")
    marital_status = fields.Selection([
    	('married', 'Married'),
    	('single', 'Single'),
    	('engaged', 'Engaged'),
        ('divorced', 'Divorced'),
    	('widowed', 'Widowed'),
    	], string='Marital Status', required=True, help="Marital Status")
    blood_group = fields.Char(string="Blood Group", help="Blood Group")

    @api.model
    def create(self, vals):
        if vals.get('is_member'):
            vals['unique_member_no'] = self.env['ir.sequence'].next_by_code('res.partner') or 'New'
        return super().create(vals)

    @api.depends('date_of_birth')
    def _compute_age(self):
        today = date.today()
        for record in self:
            if record.date_of_birth:
                birth_date = record.date_of_birth
                record.age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            else:
                record.age = 0 