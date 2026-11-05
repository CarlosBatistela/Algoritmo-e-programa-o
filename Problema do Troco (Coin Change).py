
c = [1, 3, 4]

def resolver(x):
    if x < 0:
        return float('inf')
    elif x == 0:
        return 0
    else:
        return min( resolver(x - moeda) + 1 for moeda in c)

x = int(input('valor a se formar: '))
print(f'Resultado: resolver(x)')
