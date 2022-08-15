from .Emissor import Emissor


class Cpf(object):
    _emissor = Emissor()

    def __init__(self):
        self._cpf = None


    def __init__(self, cpf = None):
        self._cpf = cpf


    def set_cpf(self, cpf):
        self._cpf = cpf


    def get_cpf(self): 
        return self._cpf


    def get_local(self):
        digito_emissor = self._cpf[8]

        return self._emissor.get_local(digito_emissor)

    
    def get_sigla(self):
        digito_emissor = self._cpf[8]

        return self._emissor.get_sigla(digito_emissor)