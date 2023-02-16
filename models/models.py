# -*- coding: utf-8 -*-

from odoo import models, fields, api

class usuario(models.Model):
    _name = 'res.partner'
    _description = 'Usuario'
    _inherit = 'res.partner'

    apellidos = fields.Char()
    ubicacion = fields.Char()
    correo = fields.Char()
    contrasenya = fields.Char()
    avatar = fields.Image(max_width=200, max_height=200)
    is_user = fields.Boolean(default=True)
    articulosComprados = fields.One2many('simarropop.articulo', 'usuario_comprador')
    articulosVendidos = fields.One2many('simarropop.articulo', 'usuario_vendedor')
    valoracionesEmisor = fields.One2many('simarropop.valoracion', 'usuario_emisor')
    valoracionesReceptor = fields.One2many('simarropop.valoracion', 'usuario_receptor')
    mensajesEmisor = fields.One2many('simarropop.mensaje', 'usuario_emisor')
    mensajesReceptor = fields.One2many('simarropop.mensaje', 'usuario_receptor')

    articulosComprados_qty = fields.Integer(compute='_get_articulosComprados_qty', string='Cantidad articulos comprados', default=0)
    articulosVendidos_qty = fields.Integer(compute='_get_articulosVendidos_qty', string='Cantidad articulos vendidos', default=0)
    
    def _get_articulosComprados_qty(self):
        for usuario in self:
            usuario.articulosComprados_qty = len(usuario.articulosComprados)

    def _get_articulosVendidos_qty(self):
        for usuario in self:
            usuario.articulosVendidos_qty = len(usuario.articulosVendidos)

class articulo(models.Model):
    _name = 'simarropop.articulo'
    _description = 'Articulo'

    titulo = fields.Char(required=True)
    likes = fields.Integer(default=0)
    descripcion = fields.Char(required=True)
    precio = fields.Float(required=True)
    estado = fields.Char() #buen estado, mal estado, casi nuevo, etc.
    vendido = fields.Boolean(default=False)
    usuario_comprador = fields.Many2one('res.partner')
    usuario_vendedor = fields.Many2one('res.partner')
    fotos = fields.One2many('simarropop.foto', 'articulo')
    categoria = fields.Many2one('simarropop.categoria')

    @api.onchange('precio')
    def _verificar_precio(self):
        if self.precio < 0:
            return {
                'warning': {
                    'title': " Preu incorrecte ",
                    'message': "El preu no pot ser negatiu",
                    },      
                }
    
class foto(models.Model):
    _name = 'simarropop.foto'
    _description = 'Foto'

    imagen = fields.Image(max_width=200, max_height=200)
    articulo = fields.Many2one('simarropop.articulo')

class valoracion(models.Model):
    _name = 'simarropop.valoracion'
    _description = 'Valoracion'

    estrellas = fields.Integer(required=True) #valor del 1-5
    opinion = fields.Char()
    usuario_emisor = fields.Many2one('res.partner')
    usuario_receptor = fields.Many2one('res.partner')

class mensaje(models.Model):
    _name = 'simarropop.mensaje'
    _description = 'Mensaje'

    contenido = fields.Char(required=True)
    hora = fields.Datetime()
    usuario_emisor = fields.Many2one('res.partner')
    usuario_receptor = fields.Many2one('res.partner')

class categoria(models.Model):
    _name = 'simarropop.categoria'
    _description = 'Categoria'

    tipo = fields.Char()
    articulos = fields.One2many('simarropop.articulo', 'categoria')

class wizard_articulo(models.TransientModel):
     _name = 'simarropop.wizard_articulo'
     