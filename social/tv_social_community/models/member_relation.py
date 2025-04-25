# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class MemberRelation(models.Model):
    _name = 'member.relation'
    _description = "Member Relations"

    name = fields.Char(string="Relation", required=True)