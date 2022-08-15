class Emissor(object):

    _local = (
        'Rio Grande do Sul', 
        'Distrito Federal, Goiás, Mato Grosso do Sul ou Tocantins;',
        'Pará, Amazonas, Acre, Amapá, Rondônia ou Roraima',
        'Ceará, Maranhão ou Piauí', 
        'Pernambuco, Rio Grande do Norte, Paraíba ou Alagoas',
        'Bahia ou Sergipe',
        'Minas Gerais',
        'Rio de Janeiro ou Espírito Santo',
        'São Paulo',
        'Paraná ou Santa Catarina'
    )

    _sigla = (
        'RS',
        'DF, GO, MS, TO',
        'PA, AM, AC, AP, RO, RR',
        'CE, MA, PI',
        'PE, RN, PB, AL',
        'BA, SE',
        'MG',
        'RJ, ES'
        'SP',
        'PR, SC'
    )


    def __init__(self):
        pass


    def _check_range(self, id):
        return (id > -1 and id < 10)


    def get_local(self, id):
        id = int(id) 
        if (self._check_range(id)):
            return self._local[id]
        else:
            return None


    def get_sigla(self, id):
        id = int(id) 
        if (self._check_range(id)):
            return self._sigla[id]
        else:
            return None