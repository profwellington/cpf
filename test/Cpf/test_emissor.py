import unittest

from src import Emissor


class Test_Emissor(unittest.TestCase):

    def test_get_sigla_id_rs(self):
        # arrange 
        id = 0
        sigla = 'RS'
        emissor = Emissor()
        
        # act 
        result = emissor.get_sigla(id)

        # assert 
        self.assertEqual(result, sigla)


    def test_get_sigla_str_id_rs(self):
        # arrange 
        id = '0'
        sigla = 'RS'
        emissor = Emissor()
        
        # act 
        result = emissor.get_sigla(id)

        # assert 
        self.assertEqual(result, sigla)


    def test_get_sigla_id_regiao_norte(self):
        # arrange 
        id = 2
        sigla = 'PA, AM, AC, AP, RO, RR'
        emissor = Emissor()
        
        # act 
        result = emissor.get_sigla(id)

        # assert 
        self.assertEqual(result, sigla)


    def test_get_sigla_str_id_regiao_norte(self):
        # arrange 
        id = 2
        sigla = 'PA, AM, AC, AP, RO, RR'
        emissor = Emissor()
        
        # act 
        result = emissor.get_sigla(id)

        # assert 
        self.assertEqual(result, sigla)


    def test_get_sigla_id_invalido(self):
        # arrange 
        id = 11
        emissor = Emissor()
        
        # act 
        result = emissor.get_sigla(id)

        # assert 
        self.assertIsNone(result)


    def test_get_sigla_str_id_invalido(self):
        # arrange 
        id = '11'
        emissor = Emissor()
        
        # act 
        result = emissor.get_sigla(id)

        # assert 
        self.assertIsNone(result)


    def test_get_local_id_rio_grande_do_sul(self):
        # arrange 
        id = 0
        estado = 'Rio Grande do Sul'
        emissor = Emissor()
        
        # act 
        result = emissor.get_local(id)

        # assert 
        self.assertEqual(result, estado)


    def test_get_local_str_id_rio_grande_do_sul(self):
        # arrange 
        id = '0'
        estado = 'Rio Grande do Sul'
        emissor = Emissor()
        
        # act 
        result = emissor.get_local(id)

        # assert 
        self.assertEqual(result, estado)


    def test_get_sigla_id_regiao_Minas_Gerais(self):
        # arrange 
        id = 6
        estado = 'Minas Gerais'
        emissor = Emissor()
        
        # act 
        result = emissor.get_local(id)

        # assert 
        self.assertEqual(result, estado)


    def test_get_local_str_id_BH_ou_SE(self):
        # arrange 
        id = 5
        estado = 'Bahia ou Sergipe'
        emissor = Emissor()
        
        # act 
        result = emissor.get_local(id)

        # assert 
        self.assertEqual(result, estado)


    def test_get_sigla_id_invalido(self):
        # arrange 
        id = 11
        emissor = Emissor()
        
        # act 
        result = emissor.get_local(id)

        # assert 
        self.assertIsNone(result)


    def test_get_sigla_str_id_invalido(self):
        # arrange 
        id = '11'
        emissor = Emissor()
        
        # act 
        result = emissor.get_local(id)

        # assert 
        self.assertIsNone(result)