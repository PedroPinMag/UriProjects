notas = [100, 50, 20, 10, 5, 2, 1]

valor = int(input())

print(valor)

for nota in notas:
    qtd = valor // nota
    valor = valor % nota
    print("%d nota(s) de R$ %d,00" % (qtd, nota))
