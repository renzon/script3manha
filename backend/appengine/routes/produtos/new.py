# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from categoria.categoria_model import ProdutoForm, Categoria
from tekton.gae.middleware.redirect import RedirectResponse
from routes import produtos


def salvar(**propriedades):
    propriedades['categoria']=ndb.Key(Categoria,int(propriedades['categoria']))
    form= ProdutoForm(**propriedades)
    erros=form.validate()
    if erros:
        return
    produto=form.fill_model()
    produto.put()
    return RedirectResponse(produtos)