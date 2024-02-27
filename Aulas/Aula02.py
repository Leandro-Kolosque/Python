x = int(input("Digite um número: "))
if (x < 0):
  print('O número que você digitou é negativo!!')
print('Fim do programa!!')

# Faça um programa que receba dois números e mostre o maior e o menor. Emita uma mensagem, caso os dois sejam iguais.
n1 = int(input("Digite o primeiro número "))
n2 = int(input("Digite o segundo número "))
if (n1 > n2):
    print ("Maior :", n1)
    print ("Menor :", n2)
elif (n1 < n2):
    print ("Menor :", n1)
    print ("Maior :", n2)
else:
    print("Ambos os números são iguais")
print("Fim do Programa!")

"""Faça um programa que receba as duas notas de um aluno, calcule sua média, e que imprima a sua situação: 
>= 7 -> Aprovado
< 7 -> Reprovado"""
nota1 = float(input("Digite sua primeira nota "))
nota2 = float(input("Digite sua segunda nota "))
media = (nota1 + nota2)/2
if (media >= 7):
    print("Aprovado")
else:
    print("Reprovado")

# Faça um programa que receba 3 notas de um aluno, calcule e mostre uma mensagem de acordo com sua média:
nota1 = float(input("Digite sua primeira nota "))
nota2 = float(input("Digite sua segunda nota "))
nota3 = float(input("Digite sua terceira nota "))
media = (nota1 + nota2 + nota3)/3
if (media <3):
    print("Reprovado", media)
elif(media >=3 <7):
    print("Recuperação", media)
else:
    print("Aprovado", media)

"""Dados três valores X,Y,Z, verificar se eles podem ser os comprimentos dos lados de um triângulo. Se eles não formarem um triângulo escrever uma mensagem. Considerar que o comprimento de cada lado de um triângulo é menor que a soma dos outros dois lados"""
ladoX = int(input("Digite o valor do lado X "))
ladoY = int(input("Digite o valor do lado Y "))
ladoZ = int(input("Digite o valor do lado Z "))
if (ladoX < ladoY + ladoZ) and (ladoY < ladoX + ladoZ) and (ladoZ < ladoX + ladoY):
    print("Isso pode ser um trinângulo")
else:
    print("Isso não é um trinângulo")


"""Construa um programa para determinar se o indivíduo está com um peso favorável. Essa situação é determinada através do IMC (Índice de Massa Corpórea), que é definida como sendo a relação entre o peso (PESO – em kg) e o quadrado da Altura (ALTURA – em m) do indivíduo. Ou seja,
IMC= PESO/ALTURA2 """
peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em M: "))
imc = peso / (altura * altura)
print(imc)
if (imc <20):
    print(f"IMC{imc:.2f} Você está abaixo do peso ")
elif(imc >=20 and imc < 25):
    print(f"{imc:.2f} Seu peso está classificado como normal")
elif (imc >= 25 and imc <30):
    print(f"{imc:.2f} Você está em situação de sobre peso ")
elif(imc >=30 and imc < 40):
    print(f"IMC{imc:.2f} Você está obeso")
else:
    print(f"{imc:.2f} Você está em situação de Obseidade Mórbida")

"""Uma empresa decide dar aumento de 30% aos funcionários com salários inferiores a R$1000,00. Faça um programa que receba o salário do funcionário e mostre o valor do salário reajustado ou uma mensagem, caso o funcionário não tenha direito ao aumento."""
salario = float(input("Digite seu salário "))
if (salario < 1000):
    print(salario * 0.30, " Seu salário foi reajustado ")
else:
    print("Seu slário não será reajustado")

#Faça um programa que receba a idade de um nadador e mostre a sua categoria
idade = int(input("Digite sua idade "))
if(idade <= 7):
    print("Categoria : 'Infantil' ")
elif(idade <= 10):
    print("Categoria: 'Juvenil' ")
elif(idade <= 15):
    print("Categoria: 'Adolescente' ")
elif(idade <= 30):
    print("Categoria: 'Adulto' ")
else:
    print("Categoria: 'Senior' ")

#Faça um programa que leia a idade de uma pessoa e informe a sua classe eleitoral: 
idade = int(input("Digite sua idade "))
if (idade < 16):
    print(idade, "Você não é um eleitor válido")
elif(idade >=16 and idade <18 or idade > 65):
    print(idade, "Você é um eleitro facultativo")
else:
    print(idade, "Você é um eleitor obrigatório")

"""Faça um programa que leia um número inteiro entre 1 e 7 e escreva o dia da semana correspondente. Caso o usuário digite um número fora desse intervalo, deverá aparecer uma mensagem informando que não existe dia da semana com esse número."""
diaSemana = int(input("Digite o dia da semana (1-7 sendo 1 = domingo 7 = sabado) "))
if(diaSemana == 1):
    print("Domingo")
elif(diaSemana == 2):
    print("Segunda")
elif(diaSemana == 3):
    print("Terça")
elif(diaSemana == 4):
    print("Quarta")
elif(diaSemana == 5):
    print("Quinta")
elif(diaSemana == 6):
    print("Sexta")
elif(diaSemana == 7):
    print("Sábado")
else:
    print("não existe dia da semana com esse número")

"""Faça um programa que leia um número inteiro entre 1 e 12 e escrever o mês correspondente. Caso o usuário digite um número fora desse intervalo, deverá aparecer uma mensagem informando que não existe mês com este número."""
mesAno = int(input("Digite o mês desejado "))
if(mesAno == 1):
    print("Janeiro")
elif(mesAno == 2):
    print("Fevereiro")
elif(mesAno == 3):
    print("Março")
elif(mesAno == 4):
    print("Abril")
elif(mesAno == 5):
    print("Maio")
elif(mesAno == 6):
    print("Junho")
elif(mesAno == 7):
    print("Julho")
elif(mesAno == 7):
    print("Agosto")
elif(mesAno == 7):
    print("Setembro")
elif(mesAno == 7):
    print("Outubro")
elif(mesAno == 7):
    print("Novembro")    
elif(mesAno == 7):
    print("Dezembro")
else:
    print("não existe um mês com esse número")

"""Faça um programa que solicite ao usuário que informe dois números e que exiba o seguinte menu:
1 – Somar
2 – Subtrair 
3 – Multiplicar
4 – Dividir
Em seguida, leia a opção escolhida e exiba o resultado de acordo com a opção."""
n1 = float(input("Digite o primeiro valor "))
n2 = float(input("Digite o segundo valor "))
operacao = int(input("Digite a opção desejada "))
if(operacao == 1):
    print("Soma: ", n1 + n2)
elif(operacao == 2):
    print("Subtração: ", n1 - n2)
elif(operacao == 3):
    print("Multiplicação: ", n1 * n2)   
elif(operacao == 4):
    print("Divisão: %.2f" %(n1 / n2))