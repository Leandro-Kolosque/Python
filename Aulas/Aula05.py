"""Solicite ao usuário que digite uma data no formato DD/MM/AAAA e imprima a data por extenso. Por exemplo:
27/05/2023 – 27 de maio de 2023
(dica: crie uma lista contendo o nome de cada mês do ano)"""
# input de uma data no formato DD/MM/AAAA e imprimir data por extenso
# capturar entrada do usuário
entry1 = (input("Digite uma data (formato DD/MM/AAAA): "))
splited = entry1.split("/") # o for é pra gera o numero em formato INT 
data = []
for i in splited:
    data.append(int(i))
# especificação de dia/mes/ano
# um item está vazio pois a identação python começa em 0
lista_ano = ["", "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
dia = data[0]
mes = lista_ano[data[1]]
ano = data[2]
print(f"a data {entry1} por extenso ficaria: {dia} de {mes} de {ano}")
