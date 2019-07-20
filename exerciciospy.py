# # Exercicio 1

# nome=input('Qual o seu nome?')
# valor_horas = float(input('Digite o valor da hora de trabalho: '))
# horas_trabalhadas = float(input('Digite a quantidade de hora trabalhada no mês: '))

# def calcular_salario (valor_horas,horas_trabalhadas):
#   return valor_horas*horas_trabalhadas
  
# salario = calcular_salario(valor_horas,horas_trabalhadas)

# def calcular_hora(calcular_salario,valor_horas):
#   return calcular_salario/valor_horas

# ganho_hora = calcular_hora(salario,valor_horas)

# print(nome)
# print(f'O Valor da suas horas é :{ganho_hora}')
# print(f'Seu Salario é :{salario}')

# # Exercicio 2

# import random
# lista = []
# numeros = 0

# while numeros < 30:
#     lista.append(random.randrange(1,200))
#     numeros +=1
# def maior_numero(lista):
#     valormax = lista[0]
#     for numeros in lista:
#       if numeros>valormax:
#         valormax = numeros
#     return valormax

# def maior_numero(lista):
#     return max(lista, key=int)

# print(f'Maior valor:{maior_numero(lista)}')

# print (f'ESSA È SUA : {lista}')

# Exercicio 3

# import random
# lista_par = []
# lista_impar = []
# lista_vazia = []
# n = 0

# while n<10:
#     lista_vazia.append(random.randint(0, 100))
#     if lista_vazia[n]%2 == 0:
#         lista_par.append(lista_vazia[n])
#     else:
#         lista_impar.append(lista_vazia[n])
#     n +=1

# print('Essa foi a lista gerada aleatóriamente:')
# print(lista_vazia)
# print('ímpares: '+str(lista_impar))
# print('pares: '+str(lista_par))

# Exercicio 4

# import math
# a=int(input('Digite o A:'))
# b=int(input('Digite o B:'))
# c=int(input('Digite o C:'))
# d = ( (b*b) - (4* (a*c)) )
# if d<0:


#     print (f'Valor de delta negativos, não tem raiz de numero negativo') 

# else:
#     print (f'Delta e igual %s.' % d) 

#     m1=math.sqrt(d)
#     x1 = ( (-b)+(m1) )/(2*a)
#     x2=(-b-m1)/(2*a)
#     print (f'Raiz de X1= %s.' % x1)
#     print (f'Raiz de X2= %s.' % x2)


# Exercicio 5

import math
pi = 3.14
raio = int(input('Digite a area do circulo :'))
a= pi*(raio*raio)

print (f'A area do circulo e, {a} m²)