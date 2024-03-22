#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até dez. Seu programa deverá ler um número pelo teclado (entre 0 e 10) e mostrá-lo por extenso.
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    num = int(input("Digite um número entre 0 e 10: "))
    if 0 <= num <= 10:
        break 
    print("Digite um número entre 0 (ZERO) e 10 (DEZ): TENTE NOVAMENTE!!")  
print(f'Você digitou o número {cont[num]}')

#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
num = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Os valores sorteados foram {num}')
print(f'O maior valor sorteado foi {max(num)} e o menos valor foi {min(num)}')

#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
valor = (int(input("Digite um valor ")), int(input("Digite um valor ")), int(input("Digite um valor ")), int(input("Digite um valor ")))
print(f"Você digitou os valores {valor}")
print(f"O valor 9 (NOVE) apareceu {valor.count(9)} vezes")
if 3 in valor:
    print(f"O valor 3 (TRÊS) apareceu na posição {valor.index(3)+1 }º")
else:
    print("O valor 3 (TRÊS) não foi digitado")
for n in valor:
    if n % 2 == 0:
        print(n)

#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
listagem = ("Lápis", 1.50, "Caneta", 2.25, "Estojo", 5, "Caderno", 10)
print("-" * 40)
print(f"{'MENU':^40}")
print("-" * 40)
for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end=' ')
    else:
        print(f"R$ {listagem[pos]:>4.2f}")

#Crie um programa que tenha uma tupla com várias palavras. Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavra = ("Aprender", "Estudar", "Programar", "Café", "Codar", "Python")
for p in palavra:
    print(f"\n na palavra {p.upper()} temos ", end= " ")
    for letra in p:
        if letra.lower() in 'aeiouáàãéèíìóòúù':
            print(f'{letra}', end=' ')