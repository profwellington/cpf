import unittest

from src import Cpf
from src import Emissor


class Test_Aggregation(unittest.TestCase):

    def test_emissor_eh_RS(self):
        # arrange 
        sigla = "RS"
        model = "04282855037"
        cpf = Cpf(model)

        # act 
        result = cpf.get_sigla()

        # assert 
        self.assertEqual(result, sigla)


    def test_emissor_eh_rio_grande_do_sul(self):
        # arrange 
        sigla = "Rio Grande do Sul"
        model = "04282855037"
        cpf = Cpf(model)

        # act 
        result = cpf.get_local()

        # assert 
        self.assertEqual(result, sigla)
