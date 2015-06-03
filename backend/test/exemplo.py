# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from unittest.case import TestCase


def soma(param, param1):
    return param+param1


class OperacaoesTests(TestCase):
    def test_soma(self):
        resultado=soma(2,2)
        self.assertEqual(4, resultado)
        self.assertEqual(6.1, soma(0.1,6))

    def test_balh(self):
        self.assertAlmostEqual(5.1,5.10000001)
        self.assertListEqual([1,2],[1,2])