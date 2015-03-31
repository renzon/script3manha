# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from categoria.categoria_model import Categoria
from routes import categorias
from tekton.gae.middleware.redirect import RedirectResponse


def salvar(nome):
    categoria = Categoria(nome=nome)
    categoria.put()
    return RedirectResponse(categorias)