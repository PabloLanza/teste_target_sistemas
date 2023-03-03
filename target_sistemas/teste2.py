#Tarefa 2

from fibonacci import fibonacci


def num_presente(a):
    tamanho = a*2
    sequencia = fibonacci(length=tamanho)
    if a in sequencia:
        print(f'{a} está presente na sequência de fibonacci.')
    else:
        print(f'{a} não está presente na sequência de fibonacci.')

num = int(input("Informe um número:"))
num_presente(num)