from odoo import fields, api, models, _
from odoo.exceptions import ValidationError
class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    
    
    note = fields.Text(
        string='Note',readonly=True,
        default='use this form to report Any issues to TikTok' 
    )
    
    report_date = fields.Date(
        string='REPORT DATE',
        default=fields.Date.context_today,required=True
    )
    
    
    mfg = fields.Selection(
        string='MFG',
        selection=[('mfg1', 'MFG 1'),('mfg2', 'MFG 2')],required=True
    )
    
    model = fields.Selection(
        string='MODEL',
        selection=[('model1', 'Model 1'), ('model2', 'Model 2')],required=True
    )
    
    issue = fields.Selection(
        string='ISSUE',
        selection=[('issue1', 'Issue 1'), ('issue2', 'Issue 2')],required=True
    )
    
    issue_verification_ids = fields.Many2many(
        string='Issue Verification',
        comodel_name='ir.attachment',
    )
    
    action_items = fields.Char(
        string='ACTION ITEMS', required=True
    )
    
    status = fields.Selection(
        string='STATUS',
        selection=[('status1', 'Status1'),('status2', 'Status2')], required=True
    )
    
    close_date = fields.Date(
        string='CLOSE DATE',
        default=fields.Date.context_today,
    )
    
    solution = fields.Char(
        string='SOLUTION',
    )

    reported_to_id = fields.Many2one(
        string='REPORTED TO',
        comodel_name='hr.employee',
        ondelete='restrict', required=True
    )

    @api.model
    def create(self, vals):
        print("vals--- {}".format(vals))
        res = super(HelpdeskTicket, self).create(vals)
        return res


        

    
    
    
    
    
    
    
    
    