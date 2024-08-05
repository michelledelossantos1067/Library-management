from odoo import models,fields # type: ignore

class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Library Loan'

    user_id = fields.Many2one('res.partner',string='User', required=True)
    book_id = fields.Many2one('library.book',string="Book",required=True)
    loan_date = fields.Date('Loan Date', default=fields.Date.today)
    return_date = fields.Date('Return Date')
    