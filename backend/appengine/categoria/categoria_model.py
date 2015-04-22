# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaeforms.base import IntegerField
from gaeforms.ndb.form import ModelForm
from gaeforms.ndb.property import SimpleCurrency


class Categoria(ndb.Model):
    nome=ndb.StringProperty(required=True)
    quantidade=  ndb.IntegerProperty(required=True)
    criacao = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def query_ordenada_por_nome(cls):
        return cls.query().order(Categoria.nome)

class CategoriaForm(ModelForm):
    _model_class = Categoria
    _include = [Categoria.nome]
    quantidade=IntegerField(required=True,lower=0)


class Produto(ndb.Model):
    nome=ndb.StringProperty(required=True)
    preco=SimpleCurrency(required=True)
    categoria=ndb.KeyProperty( required=True)

    @classmethod
    def query_ordenada_por_nome(cls):
        return cls.query().order(Produto.nome)

    @classmethod
    def query_por_categoria_ordenada_por_nome(cls, categoria_selecionada):
        if isinstance(categoria_selecionada, basestring):
            categoria_selecionada=ndb.Key(Categoria, int(categoria_selecionada))
        return cls.query(cls.categoria==categoria_selecionada).order(cls.nome)


class ProdutoForm(ModelForm):


    _model_class = Produto
