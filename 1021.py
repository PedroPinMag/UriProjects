notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

valor = float(input())

print("NOTAS:")
for nota in notas:
    qtd = valor // nota
    valor = valor % nota
    print("%d nota(s) de R$ %d.00" % (qtd, nota))

print("MOEDAS:")
for moeda in moedas:
    qtd = valor // moeda
    valor = valor % moeda
    print("%d moeda(s) de R$ %.2f" % (qtd, moeda))
