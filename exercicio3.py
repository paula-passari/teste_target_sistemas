# Importa biblioteca
import json

# Abre arquivo .json
with open('dados.json', encoding='UTF-8') as meu_json:
    dados = json.load(meu_json)


# Calcula menor valor
def menorValor():
    menor_valor = 99999999.99
    for i in dados:
        if i['valor'] < menor_valor and i['valor'] != 0:
            menor_valor = i['valor']

    print(f'O menor valor de faturamento foi de {menor_valor}')

# Calcula maior valor
def maiorValor():
    maior_valor = 0
    for i in dados:
        if i['valor'] > maior_valor:
            maior_valor = i['valor']

    print(f'O maior valor de faturamento foi de {maior_valor}')

# Calcula dias de faturamento maior que a media
def faturamentoSuperior():
    faturamento_total = 0
    dias_totais = 0

    # calcula faturamento total
    for i in dados:
        if i['valor'] != 0:
            faturamento_total = faturamento_total + i['valor']
            dias_totais += 1
    

    # calcula média mensal
    media_mensal = faturamento_total / dias_totais


    # Compara número de dias que o faturamento foi maior que a média mensal
    dias_superiores = 0
    for i in dados:
        if i['valor'] > media_mensal:
            dias_superiores = dias_superiores + 1

    print(f'Durante {dias_superiores} o valor de faturamento diário foi superior a média mensal de {media_mensal:.4f}')


menorValor()
maiorValor()
faturamentoSuperior()


