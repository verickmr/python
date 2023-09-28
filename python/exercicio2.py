# 1-questao
num = int(input("digite um número:"))

if num < 10:
    print("Menor")
elif num > 10:
    print("Maior")
else:
    print("Igual")

# 2-questão
num = int(input("digite um número:"))

if num >= 0:
    print("Positivo")
else:
    print("Negativo")

# 3-questão 
apple = int(input ("Quanas maçãs?:"))

if apple < 12:
    custo = apple * 1.30
elif apple >= 12:
    custo = apple 
    
print("Custou:R${:.2f}".format(custo))

# 4-questão
nota1 =  float(input("Qual a nota:"))
nota2 =  float(input("Qual a nota:"))
media = (nota1 + nota2)

if media >=6:
    print("Aprovado")
else:
    print("Reprovado")
    
print(media)

# 5-quetão 
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if valor1 > valor2:
    maior = valor1
else:
    maior = valor2

print("O maior valor é: {}".format(maior))

# 6-questão
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if valor1 > valor2:
    maior = valor1
    menor = valor2
else:
    maior = valor2
    menor = valor1

print(maior,menor)

# 7-questão
conta = int(input("Qual o número da conta:"))
saldo =  float(input("Qual o saldo:"))
debito =  float(input("Qual o débito:"))
credito =  float(input("Qual o crédito:"))
saldoAtual = saldo - (debito + credito)

if saldoAtual >= 0: 
    print("Saldo positivo")
else:
    print("Saldo negativo")

# 8-questão
atual = int(input("Quantidade atual em estoque: "))
maxima = int(input("Quantidade máxima em estoque: "))
minima = int(input("Quantidade mínima em estoque: "))
media = (maxima + minima) / 2

if atual >= media:
    print("Não efetuar compra")
else:
    print("Efetuar compra")

# 9-questão
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if 9.0 <= media <= 10.0:
    conceito = "A"
elif 7.5 <= media < 9.0:
    conceito = "B"
elif 6.0 <= media < 7.5:
    conceito = "C"
elif 4.0 <= media < 6.0:
    conceito = "D"
elif 0 <= media < 4:
    conceito = "E"

if conceito in ["A", "B", "C"]:
    situacao = "APROVADO"
else:
    situacao = "REPROVADO"

print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Média: {media:.2f}")
print(f"Conceito: {conceito}")
print(f"Situação: {situacao}")
