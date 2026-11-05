#1
vetor = [-1, 2, -3, 4, -5]

maior_soma = vetor[0]
melhor_subarray = []

for i in range(len(vetor)):
    soma = 0

    for j in range(i, len(vetor)):
        soma += vetor[j]

        if soma > maior_soma:
            maior_soma = soma
            melhor_subarray = vetor[i:j + 1]

print("Maior subarray:", melhor_subarray)
print("Maior soma:", maior_soma)

#2

from itertools import combinations

numeros = [2, 4, 7, 10, 15]
S = 17

encontrado = False

for tamanho in range(1, len(numeros) + 1):
    for grupo in combinations(numeros, tamanho):
        if sum(grupo) == S:
            print("Subconjunto encontrado:", grupo)
            encontrado = True
            break

    if encontrado:
        break

if not encontrado:
    print("Subconjunto não encontrado.")

#3

senha_correta = "5732"
tentativas = 0

for numero in range(10000):
    senha = str(numero).zfill(4)
    tentativas += 1

    if senha == senha_correta:
        print("Senha encontrada:", senha)
        print("Tentativas:", tentativas)
        break

#4

dna = "ACGTACGTTACGGAATCG"
procurada = "TACG"

encontrado = False

for i in range(len(dna) - len(procurada) + 1):
    trecho = dna[i:i + len(procurada)]

    if trecho == procurada:
        print("Sequência encontrada na posição", i + 1)
        encontrado = True
        break

if not encontrado:
    print("Sequência não encontrada.")
