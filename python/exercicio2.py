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
nota1 =  int(input("Qual a nota:"))
nota2 =  int(input("Qual a nota:"))
media = (nota1 + nota2)
if media >=6:
    print("Aprovado")
else:
    print("Reprovado")

# 5-quetão 
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
if valor1 > valor2:
    maior = valor1
else:
    maior = valor2

print("O maior valor é: {}".format(maior))
