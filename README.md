# Cadastro de Pessoa Física

[![Maintainability](https://api.codeclimate.com/v1/badges/1f2ef1b01cbe4292321d/maintainability)](https://codeclimate.com/github/profwellington/cpf/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/1f2ef1b01cbe4292321d/test_coverage)](https://codeclimate.com/github/profwellington/cpf/test_coverage)

## Verificar o estado emissor do CPF

De acordo com o número do CPF informar o estado emissor.
Para isto, é necessário verificar o o nono dígito do CPF.
Exemplo de CPF: 000.000.002-00 que corresponde ao Estado do Pará, Amazonas, Acre, Amapá, Rondônia e Roraima. 

A tabela dos códidos estados emissores é a seguinte:
0. Rio Grande do Sul;
1. Distrito Federal, Goiás, Mato Grosso do Sul e Tocantins;
2. Pará, Amazonas, Acre, Amapá, Rondônia e Roraima;
3. Ceará, Maranhão e Piauí;
4. Pernambuco, Rio Grande do Norte, Paraíba e Alagoas;
5. Bahia e Sergipe;
6. Minas Gerais;
7. Rio de Janeiro e Espírito Santo;
8. São Paulo;
9. Paraná e Santa Catarina.

### Coverage
```bash
#python -m coverage run -m unittest discover /test/ #precisa agrupar os teste em arquivo main.py
python -m coverage run test/Cpf/test_aggregation.py
```

## Referência:
0. http://clubes.obmep.org.br/blog/a-matematica-nos-documentos-cpf/
1. https://www.geradorcpf.com/algoritmo_do_cpf.htm
2. https://www.macoratti.net/alg_cpf.htm
3. https://ogeradordecpf.com.br/algoritmo/