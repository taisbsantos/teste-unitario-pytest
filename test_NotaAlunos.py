# escrever uma função que testa se a nota passada pra função é menor que 60 ou se é >=
# e retorna se foi aprovado ou não
# escrever 2 testes para essa função, um em que é passada uma nota e o aluno
# é reprovado, outro em que a nota é suficiente para o aluno ser aprovado

#testes foram criados pra falhar só pra ver o comportamento, num cenário real testes não tem objetivo de falhar

import unittest


def nota_final(nota):
    if (nota >= 60):
        return 'aprovado'
    else:
        return 'reprovado'

class TestNota(unittest.TestCase):
    # testes criados pra passar
    def test_nota(self):
        self.assertEqual(nota_final(70), 'aprovado')

    # teste criado para falhar
    def test_nota2(self):
        self.assertEqual(nota_final(40), 'aprovado')

    def test_nota3(self):
        self.assertEqual(nota_final(60), 'reprovado')
