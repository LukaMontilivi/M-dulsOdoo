from odoo import models, fields
class MusicaArtista(models.Model):
    _name = 'musica.artista'
    nom = fields.Char(string='Nom', size=200, required=True)
    datanaix = fields.Date(string='Data naix.')