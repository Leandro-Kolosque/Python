from math import *

# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a primeira nota: "))
nota3 = int(input("Digite a primeira nota: "))
nota4 = int(input("Digite a primeira nota: "))
media = (nota1+nota2+nota3+nota4)/4
print("Sua média foi igual a: ", media)"""

# Faça um Programa que converta metros para centímetros.
"""metros = float(input("Digite a quantidade de metros para a conversão "))
print(metros * 100, "centímetros")"""

# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""raio = float(input("Digite o valor do raio do círculo: "))
print("A área do círculo será: ", 3.14 * raio**2)"""

# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""lado = float(input("Digite o valor de um dos lados do quadrado: "))
area = lado * lado
print("O dobro da área do quadrado será: ", area * 2)"""

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
# salHora = float(input("Digite o seu salário por hora: R$",))
"""horasMes = float(input("Digite quantas horas você trabalha por mês: "))
print("Seu salário no mês será igual a: R$", salHora * horasMes)"""

# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.C = 5 * ((F-32) / 9).
"""tempF = float(input("Digite a temperatura em Fahrenheit "))
tempC = 5 * ((tempF-32) / 9)
print("A temperatura em graus Celcius será igual a: {:.2f} °" .format(tempC))"""

# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""tempC = float(input("Digite a temperatura em graus Celsius "))
tempF = (tempC * 9/5) + 32
print("A temperatura em Farenheit será igaul a: {:.2f} °" .format(tempF))"""

"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e 
mostre: 
a) o produto do dobro do primeiro com metade do segundo . 
b) a soma do triplo do primeiro com o terceiro. 
c) o terceiro elevado ao cubo"""
"""n1 = int(input("Digite o primeiro número inteiro "))
n2 = int(input("Digite o segundo número inteiro "))
n3 = float(input("Digite um número real: "))
print((n1 * 2) * (n2 / 2))
print((3*n1) + n3)
print(n3**3)"""

#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""altura = float(input("Digite sua altura "))
print("Seu peso ideal é igual a: ", (72.7*altura) -58)"""

#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
"""a) Para homens: (72.7*h) - 58
b)Para mulheres: (62.1*h) - 44.7"""
"""altura = float(input("Digite sua altura: "))
pesoIdealH = (72.7*altura) - 58
pesoIdealM = (62.1*altura) - 44.7
print("Seu peso ideal caso seja homem é igual a: {:.2f} e caso seja mulher é igual a: {:.2f}" .format(pesoIdealH, pesoIdealM))"""

"""João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas."""
"""peso = float(input("Digite o peso do peixe: "))
excesso = peso - 50
if (excesso > 1):
    multa = 4 * excesso
    print("O valor da multa será R$",multa)
elif (excesso <= 0):
    print("Você não pagará multa, portanto você irá pagar apenas o valor do peixe, R$")"""

"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:salário bruto.quanto pagou ao INSS.quanto pagou ao sindicato.o salário líquido.calcule os descontos e o salário líquido, conforme a tabela abaixo:+ Salário Bruto : R$ a- IR (11%) : R$ b- INSS (8%) : R$ c- Sindicato ( 5%) : R$ d= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido."""
"""salHora = float(input("Digite o valor que você recebe por hora, R$ "))
horaMes= float(input("Digite a quantidade de horas que você trabaha por mês, Horas: "))
salBruto = salHora * horaMes
print(salBruto)
impostoRenda = salBruto * 0.11
print("Você irá pagar R$", impostoRenda)
inss = salBruto * 0.08
print("Você irá pagar R$", inss)
sindicato = salBruto * 0.05
print("Você irá pagar R$", sindicato)
print("Seu sálario líquido será R$", salBruto - impostoRenda - inss - sindicato)"""

"""Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;A mensagem "Reprovado", se a média for menor do que sete;A mensagem "Aprovado com Distinção", se a média for igual a dez."""
"""nota1 = float(input("Digite sua primeira nota "))
nota2 = float(input("Digite sua segunda nota "))
media = (nota1 + nota2) /2
if(media >= 7):
    print("Aprovado")
elif(media == 10):
    print("Aprovado com Distinção")
elif(media < 7):
    print("Reprovado")"""

"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:salários até R$ 280,00 (incluindo) : aumento de 20%salários entre R$ 280,00 e R$ 700,00 : aumento de 15%salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:o salário antes do reajuste;o percentual de aumento aplicado;o valor do aumento;o novo salário, após o aumento."""
"""salColaborador = float(input("Digite seu salário atual R$"))
if(salColaborador < 280):
    print("Seu antigo salário era R$", salColaborador, "Seu novo salário será R$", (salColaborador * 0.20) + salColaborador, "Portanto seu aumento foi de R$", salColaborador * 0.20 )
elif(salColaborador >= 280 and salColaborador < 700):
    print("Seu antigo salário era R$", salColaborador, "Seu novo salário será R$", (salColaborador * 0.15) + salColaborador, "Portanto seu aumento foi de R$", salColaborador * 0.15 )
elif(salColaborador >= 700 and salColaborador < 1500):
    print("Seu antigo salário era R$", salColaborador, "Seu novo salário será R$", (salColaborador * 0.10) + salColaborador, "Portanto seu aumento foi de R$", salColaborador * 0.10 )
elif(salColaborador >= 1500):
    print("Seu antigo salário era R$", salColaborador, "Seu novo salário será R$", (salColaborador * 0.05) + salColaborador, "Portanto seu aumento foi de R$", salColaborador * 0.05 )"""

"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo: Média de Aproveitamento Conceito Entre 9.0 e 10.0 A Entre 7.5 e 9.0 B Entre 6.0 e 7.5 C Entre 4.0 e 6.0 D Entre 4.0 e zero EO algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E."""
"""nota1 = float(input("Digite sua primeira nota "))
nota2 = float(input("Digite sua segunda nota "))
media = (nota1 + nota2) /2
if(media >=9 and media <= 10):
    print("Conceito A, Aprovado")
elif(media >= 7.5 and media < 9):
    print("Conceito B, Aprovado")
elif(media >= 6 and media < 7.5):
    print("Conceito C, Aprovado")
elif(media >= 4 and media < 6):
    print("Conceito D, Reprovado")
elif(media > 4):
    print("Conceito E, Reprovado")"""

"""Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.Dicas:Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;Triângulo Equilátero: três lados iguais;Triângulo Isósceles: quaisquer dois lados iguais;Triângulo Escaleno: três lados diferentes;"""
"""n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 == n2 == n3:
    print('Os segmentos acima formam um triângulo equilátero.')
elif n1 == n2 or n1 == n3 or n2 == n3:
    print('Os segmentos acima formam um triângulo isósceles.')
else:
    print('Os segmentos acima formam um triângulo escaleno.')"""

"""Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido."""
"""nota = int(input("Digite sua nota "))
while(nota < 0 and nota > 10 ):
    nota = int(input("nota inválida, digite uma nota novamnte: "))
print("Nota válida ", nota)"""

"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:Tabuada de 5: 5 X 1 = 5 5 X 2 = 10 ... 5 X 10 = 50"""
"""numero = int(input("Digite um numero "))
for tabuada in range(1, 11):
    print(numero, "*" , tabuada, "=", numero*tabuada)"""

"""O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:Preço do pão: R$ 0.18 Panificadora Pão de Ontem - Tabela de preços 1 - R$ 0.18 2 - R$ 0.36 ... 50 - R$ 9.00"""
"""precoPao = float(input("Preço do pão: R$ "))
print("Panificadora Pão de Ontem - Tabela de preços")
for quantidade in range(1, 51):
    valorTotal = quantidade * precoPao
    print(f"{quantidade} - R$ {valorTotal:.2f}")"""

"""O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:Lojas Tabajara Produto 1: R$ 2.20 Produto 2: R$ 5.80 Produto 3: R$ 0 Total: R$ 9.00 Dinheiro: R$ 20.00 Troco: R$ 11.00"""
"""precoMercadoria = float(input("Digite o valor da mercadoria: R$ "))
while precoMercadoria != 0:    
    qntdMercadorias = float(input("Digite quantas mercadorias foram compradas: "))
    print("O valor da mercadoria será igual a: R$", precoMercadoria, "*", qntdMercadorias, "=", qntdMercadorias * precoMercadoria)
    valorPago = float(input("Digite o valor pago: R$ "))
    print("Seu troco será igual a: R$", valorPago - (precoMercadoria * qntdMercadorias))
    precoMercadoria = float(input("Digite o valor da mercadoria: R$ "))"""

"""Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes"""
"""codigoGordo = 0
codigoMagro = 0
codigoAlto = 0
codigoBaixo = 0
pesoGordo = 0
pesoMagro = 1000
alturaAlto = 0
alturaBaixo = 500
somaPesos = 0
somaAlturas = 0
qntdClientes = 0
while True:
    codigo = input("Digite o codigo do cliente: ")
    if codigo == "0":
        break
    qntdClientes += 1
    altura = int(input("Digite a altura do cliente (em centímetros): "))
    peso = float(input("Digite o peso do cliente (em kg): "))
    somaPesos += peso
    somaAlturas += altura
    if altura > alturaAlto:
        alturaAlto = altura
        codigoAlto = codigo
    if altura < alturaBaixo:
        alturaBaixo = altura
        codigoBaixo = codigo
    if peso > pesoGordo:
        pesoGordo = peso
        codigoGordo = codigo
    if peso < pesoMagro:
        pesoMagro = peso
        codigoMagro = codigo
mediaAlturas = somaAlturas / qntdClientes
mediaPesos = somaPesos / qntdClientes
print(
    f"O cliente mais alto é o que tem o código {codigoAlto}"
    f" e ele possui {alturaAlto}cm de altura\n"
    f"O cliente mais baixo é o que tem o código {codigoBaixo}"
    f" e ele possui {alturaBaixo}cm de altura\n"
    f"O cliente mais gordo é o que tem o código {codigoGordo}"
    f" e ele pesa {pesoGordo:.2f}kg\n"
    f"O cliente mais magro é o que tem o código {codigoMagro}"
    f" e ele pesa {pesoMagro:.2f}kg\n"
    f"A média de altura dos clientes é de {mediaAlturas:.2f}cm\n"
    f"A média de peso dos clientes é de {mediaPesos:.2f}kg")"""

"""Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:1 , 2, 3, 4 - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - Jose/ 2- João/etc) 5 - Voto Nulo 6 - Voto em Branco"""
"""Faça um programa que calcule e mostre:O total de votos para cada candidato;O total de votos nulos;O total de votos em branco;A percentagem de votos nulos sobre o total de votos;A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero."""
print("Candidatos: \n1 - José\n2 - João\n3 - Maria\n4 - Clara")
print("Digite 0 para sair, 5 para votar nulo ou 6 para votar em branco.")
votos = 0
candidato01 = 0
candidato02 = 0
candidato03 = 0
candidato04 = 0
nulos = 0
brancos = 0
while True:
    voto = int(input(f"Digite o voto numero {votos + 1}: "))
    if voto == 0:
        break
    votos += 1
    if voto == 1:
        candidato01 += 1
    elif voto == 2:
        candidato02 += 1
    elif voto == 3:
        candidato03 += 1
    elif voto == 4:
        candidato04 += 1
    elif voto == 5:
        nulos += 1
    elif voto == 6:
        brancos += 1
    else:
        print("Voto inválido!")
        votos -= 1
print(
     "\nResultado da eleição:"
    f"\nJosé teve {candidato01} votos"
    f"\nJoão teve {candidato02} votos"
    f"\nMaria teve {candidato03} votos"
    f"\nClara teve {candidato04} votos"
    f"\n{nulos} votos foram anulados, um total de {100 * nulos / votos:.2f}%"
    f"\n{brancos} votos foram em branco, "
    f"um total de {100 * brancos / votos:.2f}%"
)