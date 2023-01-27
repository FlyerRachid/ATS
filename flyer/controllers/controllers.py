# -*- coding: utf-8 -*-
from odoo import http


class Flyer(http.Controller):
    @http.route('/flyer', auth='public')
    def index(self, **kw):
        return "Hello, flyer"

#     @http.route('/flyer/flyer/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('flyer.listing', {
#             'root': '/flyer/flyer',
#             'objects': http.request.env['flyer.flyer'].search([]),
#         })

#     @http.route('/flyer/flyer/objects/<model("flyer.flyer"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('flyer.object', {
#             'object': obj
#         })
