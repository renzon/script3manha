# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from categoria.categoria_model import Categoria
from config.template_middleware import TemplateResponse
from routes import categorias
from tekton.gae.middleware.redirect import RedirectResponse


def salvar(nome, quantidade):
    erros={}
    numero = 0
    try:
        numero = int(quantidade)
    except:
        erros['quantidade']='Deve ser um número inteiro'
    if nome =='':
        erros['nome']='Campo Obrigatório'
    if not erros:
        categoria = Categoria(nome=nome, quantidade=numero)
        categoria.put()
        return RedirectResponse(categorias)
    else:
        categoria = {'nome': nome, 'quantidade': quantidade}
        ctx = {'categoria': categoria, 'erros':erros}
        return TemplateResponse(ctx, 'categorias/categorias_form.html')