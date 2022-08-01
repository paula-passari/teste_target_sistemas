def calculaFibonacci(x):
    num1 = 0
    num2 = 1
    contador = 0
    pertence = False
    
    while contador <= x:
        fibonacci = num1 + num2
        if fibonacci == x:
            pertence = True
            break
        
        num1 = num2
        num2 = fibonacci
        contador += 1
    
    if pertence == True:
        print('O número', x, 'pertence a sequência de Fibonacci.')
    else:
        print('O número', x, 'não pertence a sequência de Fibonacci.')
        


numero = int(input('Digite um número: '))
if numero == 0 or numero == 1:
    print('O número', numero, 'pertence a sequência de Fibonacci.')
else:
    calculaFibonacci(numero)