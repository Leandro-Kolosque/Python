nome = "Leandro"
for c in nome:
    print(c)

idade = int(input("Digite sua idade atual "))
while(idade <=0 ):
    idade = int(input("Idade inválida, digite sua idade novamnte: "))
print("Idade válida ", idade)

"""Faça um programa que solicite ao usuário que informe a matrícula e as três notas de um conjunto de alunos. O programa deverá exibir a mensagem informando se o aluno foi aprovado (média maior ou igual a 70), exame (nota maior ou igual a 60 e menor que 70) ou reprovado (nota inferior a 60). O programa irá terminar quando o usuário informar uma matrícula negativa. """
matricula = float(input("Digite sua matrícula "))
while (matricula > 0):
    n1 = float(input("digite a primeira nota "))
    n2 = float(input("digite a segunda nota "))
    n3 = float(input("digite a terceira nota "))
    media = (n1 + n2 + n3) / 3
    if (media >= 70):
        print("Aprovado")
    elif (media >= 60 and media < 70):
        print("Exame")
    elif (media < 60):
        print("Reprovado")
    matricula = float(input("Digite sua matrícula "))       
print("Fim do Programa")

"""Leia a idade de um número indeterminado de pessoas. Imprima:
- Quantas pessoas possuem idade acima de 50 anos
- A média de idade das pessoas
- O percentual de pessoas com idade abaixo de 40 anos
A leitura será encerrada quando o usuário informar uma idade negativa."""
idade = int(input("Digite a idade: "))
contId40 = 0
contId50 = 0
somaIdade = 0
contIdade = 0
while (idade > 0):
  contIdade = contIdade + 1
  somaIdade = somaIdade + idade
  if (idade < 40):
    contId40 = contId40 + 1 
  elif (idade > 50):
    contId50 = contId50 + 1
  idade = int(input("Digite a idade: "))
print("Pessoas acima de 50:", contId50)
print("Pessoas abaixo de 40:", contId40)
if (contIdade > 0):
  mediaIdade = somaIdade/contIdade
  percId40 = (contId40/contIdade)* 100
else:
  mediaIdade = 0
  percId40 = 0
print("Média das idades: %.2f" %(mediaIdade))
print("Percentual de pessoas abaixo de 40 anos: %.2f %%" %(percId40))

"""A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes, coletando dados sobre o salário e o número de filhos. A prefeitura deseja saber: 
a ) A média do salário da população; 
b ) A média do número de filhos. 
O final da leitura de dados dar-se-á com a entrada de salários negativos. """
qntSalario = 0
qntFilho = 0
somaFilho = 0
somaSalario = 0
salario = float(input("Digite seu salário: "))
filho = int(input("Digite a quantidade de filhos que você possui: "))
while(salario >= 0):
    qntSalario = qntSalario + 1
    somaSalario = somaSalario + salario
    qntFilho = qntFilho + 1
    somaFilho = somaFilho + filho
    salario = float(input("Digite seu salário: "))
    if(salario > 0):
        filho = int(input("Digite a quantidade de filhos que você possui: "))
mediaSalario = somaSalario / qntSalario
print("A media dos salarios é igual a: %.2f" %mediaSalario)
mediaFilho = somaFilho / qntFilho
print("A média dos filho é igual a: ",mediaFilho)

#Faça um programa que faça a leitura de 5 valores, e para cada valor, mostre o seu dobro na tela. 
for valor in range(5):
    numero = float(input("Digite um valor "))
    dobro = print("Dobro : ",numero * 2)

#Faça um programa que leia um número e que imprima os números ímpares de 1 até o número informado.
numero = int(input("Digite um numero "))
for numeroImpar in range(1, numero+1, 2):
    print(numeroImpar)

#Leia um número e imprima a tabuada de multiplicar deste número. Por exemplo, para o número 5:
numero = int(input("Digite um numero "))
for tabuada in range(1, 11):
    print(numero, "*" , tabuada, "=", numero*tabuada)

"""Faça um programa que leia dois números inteiros e que imprima todos os números inteiros existentes entre o menor e o maior número informados."""
n1 = int(input("Digite o primeiro valor "))
n2 = int(input("Digite o segundo valor "))
if(n1>n2):
    for i in range (n2, n1+1):
        print(i)
if(n2>n1):
    for i in range (n2, n1+1):
        print(i)        
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
menor_numero = min(numero1, numero2)
maior_numero = max(numero1, numero2)
print("Números inteiros entre", menor_numero, "e", maior_numero, ":")
for numero in range(menor_numero, maior_numero + 1):
    print(numero)

#Faça um programa que leia um número que calcule a soma dos números inteiros entre 1 e o número informado.
numero = int (input("Informe um número inteiro para obter sua soma de 1 até o número informado: "))
sum = 0
for i in range(1, numero+1):
  sum = sum + i
  print("Soma + %d" %(i))
  print("Subtotal %d" %(sum))
#print(sum)