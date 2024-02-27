from math import *
print("Hello World")

nome = input("Digite o seu nome: ")
sobrenome = input("Digite o seu sobrenome:")
nome_completo = nome + ' ' + sobrenome
print('Nome completo ' + nome_completo)

# Exercicios aula 01
# Leia três números inteiros e imprima a média aritmética entre esses números.
n1 = int(input("Digite o primeiro valor "))
n2 = int(input("Digite o segundo valor "))
n3 = int(input("Digite o terceiro valor "))
media = (n1+n2+n3)/3
print (media)

"""Faça um programa que receba o ano de nascimento de uma pessoa, o ano atual e imprima:
A idade da pessoa no ano atual
A idade que a pessoa terá em 2050"""
anoNascimento = int(input("Digite seu ano de nasicmento "))
anoAtual = int(input("Digite o ano atual "))
print("Sua idade atualmente é igual a: ", anoAtual - anoNascimento)
print("Sua idade em 2050 será igual a: ", 2050 - anoNascimento)

"""Faça um programa que solicite ao usuário que informe os coeficientes a, b e c de uma equação de segundo grau, e que imprima as raízes desta equação"""
a = float(input("Digite o primeiro valor "))
b = float(input("Digite o segundo valor "))
c = float(input("Digite o terceiro valor "))
print('{}x² + {}x + {} = 0'.format(a, b, c))
delta = b**2 - (4 * a * c)
x1 = (-b + (sqrt(delta))/ (2*a))
x2 = (-b - (sqrt(delta))/ (2*a))
print('As raízes que satisfazem esta equação são S = {:.2f}, {:.2f}'.format(x1, x2))

"""Leia um número e imprima a tabuada de multiplicar deste número"""
numero = int(input("Digite um número "))
tabuada = print(numero * 1, numero *2, numero *3, numero *4, numero *5, numero *6, numero *7, numero *8, numero *9, numero *10)

"""Receba um número positivo, calcule e mostre:
O número digitado ao quadrado
O número digitado ao cubo
A raiz quadrada do número digitado
A raiz cúbica do número digitado."""
numero = float(input("Digite um número positivo "))
print(pow (numero, 2))
print(pow (numero, 3))
print(sqrt (numero))
print(cbrt (numero))

# Faça um programa que leia o valor gasto pelo cliente e informe o valor a ser pago de gorjeta.
valorGasto = float(input("Digite o Valor Gasto "))
gorjeta = valorGasto * 0.1
valorComGorjeta = print("O valor gasto foi de : ",valorGasto,"o valor da gorjeta é:", gorjeta, "o valor final é igual a ",(valorGasto + gorjeta))

# Faça um programa que receba um número inteiro e que imprima o antecessor, o sucessor, o dobro e a metade do número informado.
numero = int(input("Digite um número inteiro "))
print(numero - 1)
print(numero + 1)
print(numero * 2)
print(numero / 2)

"""Faça um programa que, tendo como dados de entrada a altura (H - em metros) de um homem, calcule e apresente seu peso ideal utilizando a seguinte fórmula: 
Peso ideal (P) = (72,7 * H) - 58. """
altura = float(input("Digite a sua altura "))
pesoIdeal = (72.7 * altura) - 58
print("Seu peso ideal é %.2f " %pesoIdeal)

"""Faça o mesmo programa do item anterior, utilizando a fórmula para o cálculo do peso ideal para mulheres:
Peso ideal (P) = (62,1 * H) – 44,7"""
altura = float(input("Digite a sua altura "))
pesoIdeal = (62.1 * altura) - 44.7
print("Seu peso ideal é %.2f " %pesoIdeal)

sexo = input("Digite o seu genêro (M/F) ")
altura = float(input("Digite sua altura "))
if (sexo == "M"):
    pesoIdeal = (72.7 * altura) - 58
    print("Seu peso ideal é %.2f " %pesoIdeal)
elif(sexo == "F"):
    pesoIdeal = (62.1 * altura) - 44.7
    print("Seu peso ideal é %.2f " %pesoIdeal)

"""Faça um programa que leia duas variáveis e troque o conteúdo dessas duas variáveis. Em seguida, imprima o valor dessas variáveis invertido. Exemplo: A = 7, B = 9. Saída: A = 9, B = 7."""
n1 = int(input("Digite o primero valor "))
n2 = int(input("Digite o segundo valor "))
n1, n2 = n2, n1
print(n1, n2)

# input para receber numero total de eleitor, votos de cand1, votos de cand2 e calcular porcentagem de cada cand e nulos
totaleleitores = int(input("Quantos eleitores tem ao total: "))
candidatoA = int(input("Quantos votaram no candidato A: "))
candidatoB = int(input("Quantos votaram no candidato B: "))
nulos = totaleleitores-(candidatoA+candidatoB)
perccandA = round((candidatoA/totaleleitores),2)*100
perccandB = round((candidatoB/totaleleitores),2)*100
percnulos = 100-(perccandA+perccandB)
print("%s %% (%s pessoas) dos eleitores votaram no candidato A" %(perccandA, candidatoA))
print("%s %% (%s pessoas) dos eleitores votaram no candidato B" %(perccandB, candidatoB))
print("%s %% (%s pessoas) dos eleitores votaram nulo" %(percnulos, nulos))
# Para colocar porcentagem(%) na string colocar %%
