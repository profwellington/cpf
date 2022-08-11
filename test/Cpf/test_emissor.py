import unittest

from src import Cpf


class Test_Emissor(unittest.TestCase):

    def test_get_emissor(self):

        # arrange 
        model = 5
        
        # act 
        result = Cpf()
        result.set_cpf(5)
        
        # assert 
        self.assertEqual(result.get_cpf(), model)