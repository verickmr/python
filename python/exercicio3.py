#%%
# 1-questão
for num in range(1000,2001):
    if num % 11 == 5:
        print(num)
# %%
# 2-questão
for num in range(1,11):
    for multi in range(1,11):
        soma = num + multi
        print(f"{num} + {multi} = {soma}")
        resultado = num * multi
        print(f"{num} x {multi} = {resultado}")
        sub = num - multi
        print(f"{num} - {multi} = {sub}")
        div = num / multi
        print(f"{num} : {multi} = {div}")

# %%
# 3-questão
amigos = ["Fernando","Victor","Breno","Eduardo","Luis"]
for amigo in amigos:
    print(amigo)

# %%
# 4-questão
num = int(input("digite um número:"))
multi = 1
while multi <= 10:
        soma = num + multi
        print(f"{num} + {multi} = {soma}")
        resultado = num * multi
        print(f"{num} x {multi} = {resultado}")
        sub = num - multi
        print(f"{num} - {multi} = {sub}")
        div = num / multi
        print(f"{num} : {multi} = {div}")
        multi += 1
# %%
# 5-questão
amigos = ["Fernando","Victor","Breno","Eduardo","Luis"]
for amigo in amigos:
    print("Olá como vai você " + amigo)
# %%
# 6-questão
celebs = ["Cristiano Ronaldo", "Lionel Messi","Neymar","Arrascaeta",]
for celeb in celebs:
     print("Está covidado para jantar na minha casa " + celeb)
# %%
