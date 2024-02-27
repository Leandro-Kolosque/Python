from math import *
def imprimirLinha():
    print("*****************")
imprimirLinha()
print("LEANDRO!!")  
imprimirLinha()

def imprimirLinha(qntLinhas):
    for i in range(qntLinhas):
        print("*****************")
imprimirLinha(2)
print("LEANDRO!!")
imprimirLinha(3)

def imprimir_linha(qtd_linhas, caractere, qtd_caracteres):  
  linha = ""
  for i in range(qtd_caracteres):
    linha = linha + caractere
  for i in range(qtd_linhas):
    print(linha)
inicio = int(input("Digite a qtde de linhas no inicio: "))
car_inicial = input("Digite o caractere da linha inicial: ")
qtd_inicial = int(input("Digite a qtde de caracteres no inicio: "))
fim = int(input("Digite a qtde de linhas no fim: "))
car_final = input("Digite o caractere da linha final: ")
qtd_final = int(input("Digite a qtde de caracteres no fim: ")) 
imprimir_linha(inicio, car_inicial, qtd_inicial)
print("LEANDRO!!")
imprimir_linha(fim, car_final, qtd_final)

def imprimir_linha(qtd_linhas = 3, caractere = '*', qtd_caracteres = 15):  
  linha = ""
  for i in range(qtd_caracteres):
    linha = linha + caractere
  for i in range(qtd_linhas):
    print(linha)
imprimir_linha(3, '*', 10)
imprimir_linha(4, '@')
imprimir_linha(2)
imprimir_linha()
imprimir_linha(qtd_caracteres = 3)

#Um número inteiro e que retorne o dobro deste número
def dobro(numero):
    doisX = numero * 2
    return doisX
numero = int(input("Digite um numero: "))
n = dobro(numero)
print("Dobro: ", n)

#Dois números inteiros e que retorne o maior entre eles
def maior(a, b):
    return max(a,b)
n1 = int(input("Digite o primeiro valor "))
n2 = int(input("Digite o segundo valor "))
maiorValor = maior(n1,n2)
print("Maior: ", maiorValor)

#Um número inteiro e que retorne True se o número for par, e False caso contrário
def par(numero):
    return (numero % 2 == 0)
n = int(input("Digite um valor "))
if(par(n)):
    print("O número é par")
else:
    print("O número é ímpar")

#Um número inteiro e que retorne o valor do fatorial deste número
def calcular_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)
numero = int(input("Digite um número inteiro: "))
resultado = calcular_fatorial(numero)
print("O fatorial de", numero, "é:", resultado)

#Um número inteiro e positivo, que retorne a soma dos elementos inteiros existentes entre 1 e o número (inclusive)
def somar_elementos(numero):
    soma = 0 
    for i in range(1, numero + 1):
        soma += i
    return soma
numero = int(input("Digite um número inteiro positivo: "))
resultado = somar_elementos(numero)
print("A soma dos elementos entre 1 e", numero, "é:", resultado)