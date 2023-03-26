idade_em_dias = int(input())

anos = idade_em_dias // 365
meses = (idade_em_dias % 365) // 30
dias = (idade_em_dias % 365) % 30

print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))
