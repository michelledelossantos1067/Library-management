from odoo import models,fields # type: ignore

class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Author'

    name = fields.Char('Name', required=True)
    biography = fields.Text('Biography')
   