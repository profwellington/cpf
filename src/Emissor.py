class Emissor(object()):

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


    def get_local(self, id):
        return self._local(id)


    def get_sigla(self, id):
        return self._sigla(id)