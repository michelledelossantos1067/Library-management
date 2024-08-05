from odoo import models,fields # type: ignore

class LibraryCategory(models.Model):
    _name = 'library.category'
    _description = 'Library Category'

    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
    