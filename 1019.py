duracao = int(input())

horas = duracao // 3600
duracao = duracao % 3600

minutos = duracao // 60
duracao = duracao % 60

segundos = duracao

print('{}:{}:{}'.format(horas, minutos, segundos))
