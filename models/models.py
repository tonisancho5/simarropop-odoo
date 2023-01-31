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
    is_user = fields.Boolean(default=False)
    articulos = fields.One2many('simarropop.articulo', 'usuario')
    valoracionesEmisor = fields.One2many('simarropop.valoracion', 'usuarioEmisor')
    valoracionesReceptor = fields.One2many('simarropop.valoracion', 'usuarioReceptor')
    mensajesEmisor = fields.One2many('simarropop.mensaje', 'usuarioEmisor')
    mensajesReceptor = fields.One2many('simarropop.mensaje', 'usuarioReceptor')

class articulo(models.Model):
    _name = 'simarropop.articulo'
    _description = 'Articulo'

    titulo = fields.Char()
    likes = fields.Integer()
    descripcion = fields.Char()
    precio = fields.Float()
    estado = fields.Char() #buen estado, mal estado, casi nuevo, etc.
    usuario = fields.Many2one('res.partner',ondelete="cascade")
    fotos = fields.One2many('simarropop.foto', 'articulo')
    categoria = fields.Many2one('simarropop.categoria',ondelete="cascade")

class foto(models.Model):
    _name = 'simarropop.foto'
    _description = 'Foto'

    imagen = fields.Image(max_width=200, max_height=200)
    articulo = fields.Many2one('simarropop.articulo',ondelete="cascade")

class valoracion(models.Model):
    _name = 'simarropop.valoracion'
    _description = 'Valoracion'

    estrellas = fields.Integer() #valor del 1-5
    opinion = fields.Char()
    usuarioEmisor = fields.Many2one('res.partner',ondelete="cascade")
    usuarioReceptor = fields.Many2one('res.partner',ondelete="cascade")

class mensaje(models.Model):
    _name = 'simarropop.mensaje'
    _description = 'Mensaje'

    contenido = fields.Char()
    hora = fields.Datetime()
    usuarioEmisor = fields.Many2one('res.partner',ondelete="cascade")
    usuarioReceptor = fields.Many2one('res.partner',ondelete="cascade")

class categoria(models.Model):
    _name = 'simarropop.categoria'
    _description = 'Categoria'

    tipo = fields.Char()
    articulos = fields.One2many('simarropop.articulo', 'categoria')