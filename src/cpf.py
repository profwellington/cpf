class Cpf(object):

    def __init__(self):
        self._cpf = None


    def __init__(self, cpf = None):
        self._cpf = cpf


    def set_cpf(self, cpf):
        self._cpf = cpf


    def get_cpf(self): 
        return self._cpf
