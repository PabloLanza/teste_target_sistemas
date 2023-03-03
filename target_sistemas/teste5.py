#Tarefa 5

palavra = str(input("Digite uma palavra: "))
lista = list()
for i in range(len(palavra)):
    lista.append(palavra[i])

ultima_letra = len(palavra) - 1
primeira_letra = 0
c = 0
palavra_invertida = list()

while c < len(palavra):
    palavra_invertida.append(lista[ultima_letra])
    ultima_letra = ultima_letra - 1
    c = c + 1

for i in range(len(palavra_invertida)):
    print(palavra_invertida[i], end="", flush=True)