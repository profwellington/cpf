import unittest

from src import Cpf


class Test_Cpf(unittest.TestCase):

    def test_construtor_vazio_none(self):
        # arrange 
        cpf = Cpf()
        
        # act 

        # assert 
        self.assertIsNone(cpf.get_cpf())


    def test_construtor_model_model(self):
        # arrange 
        model = "5"
        cpf = Cpf(model)

        # act 
        result = cpf.get_cpf()

        # assert 
        self.assertEqual(result, model)


    def test_set_cpf_get_cpf(self):
        # arrange 
        model = "04282855037"
        cpf = Cpf()
        
        # act 
        cpf.set_cpf(model)
        result = cpf.get_cpf()
        
        # assert 
        self.assertEqual(result, model)