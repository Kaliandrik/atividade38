# Inicialize uma lista de 20 números inteiros. Armazene
# os números pares em uma lista PAR e os números
# ímpares em uma lista IMPAR. Imprima as listas PAR
# e IMPAR.

numerosinteiros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
numerospar = []
numerosimpar = []

for i in numerosinteiros:
    if i % 2 == 0:
        numerospar.append(i)
    else:
        numerosimpar.append(i)
    
print(f"numeros pares: {numerospar}")
print(f"números impares: {numerosimpar}



