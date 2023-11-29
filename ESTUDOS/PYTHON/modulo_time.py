import time
from collections import counter

#time
data_hoje = time.ctime()
print(data_hoje)

tempo_inicial = time.time()
for i  in range(100000000):
    pass
tempo_final = time.time()
duracao = tempo_final - tempo_inicial
print('O programa levou {} segundos para rodar'.format(duracao) )

#collections counter
vendas = {'notebook' : 2514, 'iphone' : 52447, 'celular samsung' : 5412}
aux = counter(vendas)
print(aux.most_common(3))