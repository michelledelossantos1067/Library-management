from odoo import models,fields # type: ignore

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char('Title', required=True)
    author_id = fields.Many2one('library.author',string="Author",required=True)
    category_id = fields.Many2one('library.category',string="Category",required=True)
    publication_date = fields.Date('Publication Date')
    