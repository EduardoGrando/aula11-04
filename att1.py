#Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem “Números iguais”.

nota1= float(input('Digite um valor:'))

nota2= float(input('Digite um valor:'))

if n1>n2:
    print(f'{nota1} é maior')
elif n2>n1:
    print(f'{nota2} é maior')
else:
    print('os valor sao iguais')