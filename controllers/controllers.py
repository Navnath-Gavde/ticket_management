# -*- coding: utf-8 -*-
# from odoo import http


# class TicketManagement(http.Controller):
#     @http.route('/ticket_management/ticket_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ticket_management/ticket_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ticket_management.listing', {
#             'root': '/ticket_management/ticket_management',
#             'objects': http.request.env['ticket_management.ticket_management'].search([]),
#         })

#     @http.route('/ticket_management/ticket_management/objects/<model("ticket_management.ticket_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ticket_management.object', {
#             'object': obj
#         })
