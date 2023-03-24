peca1 = input().split()
peca2 = input().split()

codigo_peca1 = int(peca1[0])
numero_peca1 = int(peca1[1])
valor_peca1 = float(peca1[2])

codigo_peca2 = int(peca2[0])
numero_peca2 = int(peca2[1])
valor_peca2 = float(peca2[2])

valor_total = (numero_peca1 * valor_peca1) + (numero_peca2 * valor_peca2)

print("VALOR A PAGAR: R$ %.2f" % valor_total)
