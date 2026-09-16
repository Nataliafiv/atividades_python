primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def pesquisa_sequencial(primos, item):
    for i, j in enumerate(primos):
        if j == item:
            return i

print(pesquisa_sequencial(primos, 67))
