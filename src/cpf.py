class Cpf():
    def __init__(self, cpf = None):
        self.set_cpf(cpf)

    def check_cpf(self, cpf):
        if cpf == None:
            return False
        elif type(cpf) == string():
            return False
        elif string(cpf).len() != 10:
            return False
        else:
            True

    def set_cpf(self, cpf):
        if check_cpf(cpf):
            self._cpf = cpf

    def get_cpf(self): 
        return self._cpf
