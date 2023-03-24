valores = input().split()

maiorab = (int(valores[0]) + int(valores[1]) + abs(int(valores[0]) - int(valores[1]))) / 2
maiorabc = (maiorab + int(valores[2]) + abs(maiorab - int(valores[2]))) / 2

print("%d eh o maior" % maiorabc)
