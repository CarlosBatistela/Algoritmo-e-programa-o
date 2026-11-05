#1
v = [1, 3, 5, 10, 15, 19, 89]
alvo = 19
v2 = [1 ,3 ,5 ,10, 15, 19, 89]
alvo2 = 7
def procurar(v, alvo):
    inicio = 0
    fim = len(v) - 1
    posicao = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if v[meio] == alvo:
            posicao = meio + 1
            break
        elif v[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    print(posicao)
procurar(v, alvo)
procurar(v2, alvo2)

# 2 - Quick Sort

def ordenar(numeros):
    if len(numeros) <= 1:
        return numeros

    referencia = numeros[len(numeros) // 2]

    menores = [item for item in numeros if item < referencia]
    iguais = [item for item in numeros if item == referencia]
    maiores = [item for item in numeros if item > referencia]

    return ordenar(menores) + iguais + ordenar(maiores)

lista1 = [1, 3, 5, 10, 15, 19, 89]
lista2 = [8, 7, 9, -1, 19]

print(ordenar(lista1))
print(ordenar(lista2))


# 3 - Divisão do Terreno

def dividir_terreno(largura, altura):
    while altura != 0:
        resto = largura % altura
        largura = altura
        altura = resto

    print(largura)

dividir_terreno(168, 64)
dividir_terreno(24, 16)


# 4 - Moeda Falsa

lista_moedas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
falsa_definida = 7
lista_moedas2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Moeda_falsa2: 3

def pesar(lado_a, lado_b):
    peso_a = sum(0.5 if moeda == falsa_definida else 1 for moeda in lado_a)
    peso_b = sum(0.5 if moeda == falsa_definida else 1 for moeda in lado_b)

    if peso_a < peso_b:
        return 1
    elif peso_b < peso_a:
        return 2
    else:
        return 0

def encontrar_moeda(moedas):
    grupo_a = moedas[:3]
    grupo_b = moedas[3:6]
    grupo_c = moedas[6:]

    comparacao = pesar(grupo_a, grupo_b)

    if comparacao == 1:
        suspeitas = grupo_a
    elif comparacao == 2:
        suspeitas = grupo_b
    else:
        suspeitas = grupo_c

    comparacao = pesar([suspeitas[0]], [suspeitas[1]])

    if comparacao == 1:
        moeda_encontrada = suspeitas[0]
    elif comparacao == 2:
        moeda_encontrada = suspeitas[1]
    else:
        moeda_encontrada = suspeitas[2]

    print("Moeda falsa:", moeda_encontrada)
    print("Número de pesagens:", 2)

encontrar_moeda(lista_moedas)
encontrar_moeda(lista_moedas2)
