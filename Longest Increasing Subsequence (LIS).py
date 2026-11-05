
def lis(sequencia):
    if not sequencia:
        return 0, []

    dp = [1] * len(sequencia)
    anterior = [-1] * len(sequencia)

    for i in range(len(sequencia)):
        for j in range(i):
            if sequencia[j] < sequencia[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    anterior[i] = j

    maior = max(dp)
    posicao = dp.index(maior)

    resultado = []

    while posicao != -1:
        resultado.append(sequencia[posicao])
        posicao = anterior[posicao]

    resultado.reverse()

    return maior, resultado


sequencia = [10, 22, 9, 33, 21, 50, 41, 60]

tamanho, maior_sequencia = lis(sequencia)

print("Tamanho da maior subsequência:", tamanho)
print("Maior subsequência crescente:", maior_sequencia)
