faturamento = {'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'Outros': 19849.53}
total_faturamento = 0

# Calcula faturamento total
for key in faturamento:
    total_faturamento = total_faturamento + faturamento[key]
    
# Calcula percentual
percentual = []
calculo = 0
for key in faturamento:
    calculo = (faturamento[key] / total_faturamento) * 100
    percentual.append(calculo)

# Print
cont = 0
print('O percentual do faturamento mensal da distribuidora foi: ')
for key in faturamento:
    print(f'{key} = {percentual[cont]:.2f}%')
    cont += 1

    


