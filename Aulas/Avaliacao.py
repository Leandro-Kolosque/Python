#Leandro Wirgert Kolosque#
"""Avaliação de Desempenho - Análise de dados e programação em python
25/11/2023
Professor: Marivaldo Pereira dos Santos"""

from math import *

#Questão 1: Calculadora de Média - Escreva um programa em Python que recebe três notas como entrada do usuário e calcula a média. Em seguida, imprima a média calculada.
def media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3)/3
n1 =float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
n3 = float(input("Digite sua terceira nota: "))
mediaFinal = media(n1, n2, n3)
print("{:.2f} °" .format(mediaFinal))

#Questão 2: Verificador de Número Par ou Ímpar - Crie um programa em Python que solicita um número ao usuário e verifica se o número é par ou ímpar. Imprima o resultado.
def par(numero):
    return (numero % 2 == 0)
n = int(input("Digite um valor "))
if(par(n)):
    print("O número é par")
else:
    print("O número é ímpar")

#Questão 3: Calculadora de Fatorial
"""Desenvolva um programa em Python que calcula o fatorial de um número fornecido pelo usuário. O fatorial de um número é o produto de todos os inteiros positivos até esse número."""
def calcular_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)
numero = int(input("Digite um número inteiro: "))
resultado = calcular_fatorial(numero)
print("O fatorial de", numero, "é:", resultado)

#Questão 4: Verificação de Idade
"""Escreva um programa em Python que solicite ao usuário a entrada da sua idade e, em seguida, determine se a pessoa é maior de idade ou menor de idade. Utilize operadores relacionais para fazer essa verificação."""
idade = int(input("Digite sua idade "))
if (idade < 18):
    print("Você é menor de idade")
else:
    print("Você é maior de idade")

#Questão 5: Calculadora de IMC (Índice de Massa Corporal)
"""Crie um programa em Python que peça ao usuário para fornecer sua altura (em metros) e peso (em quilogramas) e, em seguida, calcule e informe o IMC. Utilize operadores relacionais para classificar o resultado em categorias como "Abaixo do peso", "Peso normal", "Sobrepeso", etc."""
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite sua altura em quilogramas: "))
imc = peso / (altura * altura)
print (imc)
if (imc > 18.5):
    print("Seu IMC = , {:.2f} logo você está Abaixo do peso" .format(imc))
elif (imc >= 18.5  and imc <= 24,9):
    print("Seu IMC = , {:.2f} logo você está com um peso normal" .format(imc))
elif(imc > 24,9):
    print("Seu IMC = , {:.2f} logo você está com sobrepeso" .format(imc))

#Questão 6: Verificação de Números Pares e Múltiplos de 3
"""Escreva um programa em Python que solicite ao usuário que insira um número inteiro. O programa deve então verificar se o número inserido é simultaneamente par e múltiplo de 3. Imprima uma mensagem indicando se a condição é verdadeira ou falsa."""
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0 and numero % 3 == 0:
    print(f'O número {numero} é simultaneamente par e múltiplo de 3.')
else:
    print(f'O número {numero} não atende à condição desejada.')

#Questão 7: Validando Senha Forte
"""Escreva um programa em Python que solicite ao usuário que crie uma senha. A senha deve atender aos seguintes critérios:
• Pelo menos 8 caracteres de comprimento.
• Deve conter pelo menos uma letra maiúscula.
• Deve conter pelo menos um número.
• Deve conter pelo menos um caractere especial, como @, #, ou !.
O programa deve imprimir uma mensagem indicando se a senha atende a todos os critérios ou não."""
import re
print("Cadastre aqui sua senha com os seguintes critérios: \n"

      "         *Ao menos 8 digitos\n"
      "         *Ao menos uma letra MAIÚSCULA\n"
      "         *Ao menos um número\n"
      "         *Ao menos um caractere especial(!@#$%¨&*)\n")
senha = input("Digite sua senha : ")
while not (re.search(r'.{8,}', senha) and   
           re.search(r'[A-Z]', senha) and 
           re.search(r'\d', senha) and   
           re.search(r'[!@#$%¨&*]', senha)):  
    senha = input("Senha inválida, preencha com os critérios informados: ")
print("Senha cadastrada com sucesso!")

#Questão 8: Soma dos Números Pares
"""Escreva um programa em Python que solicita ao usuário inserir um número inteiro positivo, N. O programa deve então calcular e imprimir a soma de todos os números pares de 1 até N, utilizando uma estrutura de repetição."""
def somar_elementos(numero):
    soma = 0 
    for i in range(1, numero + 1):
        soma += i
    return soma
numero = int(input("Digite um número inteiro positivo: "))
resultado = somar_elementos(numero)
print("A soma dos elementos entre 1 e", numero, "é:", resultado)

#Questão 9 Caso: Sistema Simples de Controle de Notas e Faltas
"""Você foi designado para desenvolver um sistema simples de controle de notas e faltas para uma escola. O sistema deve permitir o cadastro de alunos, registro de notas e controle de faltas. Além disso, deve fornecer funcionalidades para calcular a média das notas e verificar se um aluno está aprovado ou reprovado com base em um critério predefinido.
Requisitos do Sistema:
1. Cadastro de Alunos:
◦ O sistema deve permitir o cadastro de alunos, incluindo informações como nome, número de matrícula, e curso.
2. Registro de Notas e Faltas:
◦ Para cada aluno cadastrado, o sistema deve permitir o registro de notas em diferentes disciplinas.
◦ Além disso, o sistema deve permitir o registro de faltas para cada aluno.
3. Cálculo de Média:
◦ O sistema deve calcular a média das notas de cada aluno nas disciplinas registradas.
4. Verificação de Aprovação/Reprovação:
◦ Com base nas médias calculadas, o sistema deve determinar se um aluno está aprovado ou reprovado.
◦ O critério de aprovação/reprovação é uma média mínima de 7.0.
5. Relatório de Desempenho:
◦ O sistema deve gerar um relatório de desempenho, listando os alunos, suas notas, faltas e status de aprovação/reprovação."""
quantidade_alunos = int(input("Digite a quantidade de alunos: "))
alunos = []
for i in range(quantidade_alunos):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    matricula = input(f"Digite a matrícula do aluno {i + 1}: ")
    curso = input(f"Digite o curso do aluno {i + 1}: ")
    quantidade_notas = int(input(f"Digite a quantidade de notas para o aluno {i + 1}: "))
notas = []
for j in range(quantidade_notas):
    nota = float(input(f"Digite a nota {j + 1} para o aluno {i + 1}: "))
    notas.append(nota)
faltas = int(input(f"Digite a quantidade de faltas para o aluno {i + 1}: "))
media = sum(notas) / quantidade_notas
status = "Aprovado" if media >= 7.0 else "Reprovado"
aluno_info = {
            "Nome": nome,
            "Matrícula": matricula,
            "Curso": curso,
            "Notas": notas,
            "Faltas": faltas,
            "Média": media,
            "Status": status
        }
alunos.append(aluno_info)
print("\nRelatório de Desempenho:")
for aluno in alunos:
    print("\nAluno:")
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

#10 - Caso Prático para Análise de Dados com Planilha do Excel:
"""Objetivo: Você é um analista de dados em uma empresa farmacêutica e foi designado para analisar os dados do setor de preços de medicamentos do mês de novembro. A Agência Nacional de Vigilância Sanitária (ANVISA) disponibilizou a tabela CMED (Câmara de Regulação do Mercado de Medicamentos) no site https://simtax.com.br/tabela-cmed-excel-2023/.
Passos:
1. Download da Planilha:
◦ Acesse o site https://simtax.com.br/tabela-cmed-excel-2023/.
◦ Baixe a planilha referente ao mês de novembro de 2023.
2. Análise Inicial:
◦ Abra a planilha no Excel e faça uma análise inicial dos dados. Observe as principais colunas, como "Nome do Produto," "Laboratório," "Preço Máximo de Venda ao Consumidor", verifique os preços sem impostos e com impostos de acordo com ICMS praticado e outras relevantes que você achar interessante.
3. Identificação de Tendências:
◦ Utilize gráficos e fórmulas no Excel para identificar tendências nos preços dos medicamentos. Pode ser interessante comparar os preços médios por categoria terapêutica ou laboratório.
4. Análise por Laboratório:
◦ Agrupe os dados por laboratório e analise a participação de mercado de cada um. Destaque os laboratórios que têm maior representatividade nos preços dos medicamentos.
5. Elaboração de Relatório:
◦ Com base na sua análise, elabore um relatório destacando as principais descobertas e tendências. Inclua gráficos e visualizações que facilitem a compreensão dos dados."""
