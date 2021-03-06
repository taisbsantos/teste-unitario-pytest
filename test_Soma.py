import unittest

def soma(a, b):
    return a+b 

def subtracao(a, b):
    return a-b 

def multiplicacao(a, b):
    return a-b 
def divisao(a, b):
    return a-b 

class TestCalculadora(unittest.TestCase):
    #testes criados pra passar
    def test_soma(self):
        self.assertEqual(soma(3, 1), 4)
    def test_substracao(self):
        self.assertEqual(subtracao(3, 1), 2)
    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(3, 1), 3)
    def test_divisao(self):
        self.assertEqual(divisao(3, 1), 3)
        
    #teste criado pra falhar
    def test_soma2(self):
        self.assertEqual(soma(3, 1), 5)
