from odoo import models, fields
class MusicaCanco(models.Model):
    _name = 'musica.canco'
    titol = fields.Char(string='Títol', size=300, required=True)
    minuts = fields.Float(string='Duració', required=True)
    lletra = fields.Text(string='Lletra')
    artista_id = fields.Many2one('musica.artista', string='Artista')