from odoo import models,fields
class zoo_zoo(models.Model):
    _name ='zoo.zoo'
    id = fields.Integer('id', required=True)
    nom = fields.Char('nom')
    pais = fields.Char('pais')
    ciutat = fields.Char('ciutat')
    grandaria = fields.Char ('grandaria')