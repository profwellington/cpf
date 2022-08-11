import unittest

from src import Cpf


class Test_Init(unittest.TestCase):

    def test_construtor_vazio_none(self):
        # arrange 
        result = Cpf()
        
        # act 
        
        # assert 
        self.assertIsNone(result.get_cpf())


    def test_construtor_model_model(self):
        # arrange 
        model = 5
        result = Cpf(model)

        # act 

        # assert 
        self.assertEqual(result.get_cpf(), model)


    def test_set_cpf(self):
        # arrange 
        model = 5
        result = Cpf()
        
        # act 
        result.set_cpf(model)
        
        # assert 
        self.assertEqual(result.get_cpf(), model)