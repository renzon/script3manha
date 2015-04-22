# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from categoria.categoria_model import Categoria, Produto
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes.produtos.new import salvar
from tekton.router import to_path


@login_not_required
@no_csrf
def index(categoria_selecionada=None):
    ctx={'categorias':Categoria.query_ordenada_por_nome().fetch(),
         'salvar_path':to_path(salvar)}
    if categoria_selecionada is None:
        ctx['produtos']=Produto.query_ordenada_por_nome().fetch()
        ctx['categoria_selecionada'] = None
    else:
        ctx['categoria_selecionada'] = Categoria.get_by_id(int(categoria_selecionada))
        ctx['produtos']=Produto.query_por_categoria_ordenada_por_nome(categoria_selecionada).fetch()
    return TemplateResponse(ctx,'/produtos/home.html')




