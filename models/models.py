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
    articulosComprados = fields.One2many('sale.order', 'usuario_comprador')
    articulosVendidos = fields.One2many('sale.order', 'usuario_vendedor')
    valoracionesEmisor = fields.One2many('simarropop.valoracion', 'usuario_emisor')
    valoracionesReceptor = fields.One2many('simarropop.valoracion', 'usuario_receptor')
    mensajesEmisor = fields.One2many('simarropop.mensaje', 'usuario_emisor')
    mensajesReceptor = fields.One2many('simarropop.mensaje', 'usuario_receptor')

class articulo(models.Model):
    _name = 'sale.order'
    _description = 'Articulo'
    _inherit = 'sale.order'

    name = fields.Char(default="not even a name")
    titulo = fields.Char()
    likes = fields.Integer(default=0)
    descripcion = fields.Char()
    precio = fields.Float()
    estado = fields.Char() #buen estado, mal estado, casi nuevo, etc.
    vendido = fields.Boolean(default=False)
    usuario_comprador = fields.Many2one('res.partner')
    usuario_vendedor = fields.Many2one('res.partner')
    fotos = fields.One2many('simarropop.foto', 'articulo')
    categoria = fields.Many2one('simarropop.categoria')

class foto(models.Model):
    _name = 'simarropop.foto'
    _description = 'Foto'

    imagen = fields.Image(max_width=200, max_height=200)
    articulo = fields.Many2one('sale.order')

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

    contenido = fields.Char()
    hora = fields.Datetime()
    usuario_emisor = fields.Many2one('res.partner')
    usuario_receptor = fields.Many2one('res.partner')

class categoria(models.Model):
    _name = 'simarropop.categoria'
    _description = 'Categoria'

    tipo = fields.Char()
    articulos = fields.One2many('sale.order', 'categoria')
