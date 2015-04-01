# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb


class Categoria(ndb.Model):
    nome=ndb.StringProperty(required=True)
    quantidade=  ndb.IntegerProperty(required=True)

    @classmethod
    def query_ordenada_por_nome(cls):
        return cls.query().order(Categoria.nome)