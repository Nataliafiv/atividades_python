pessoas = [
    (3, 'Ana'), (10, 'Bruno'), (15, 'Carlos'), (18, 'Daniela'),
    (19, 'Eduardo'), (23, 'Juliana'), (28, 'Fernanda'), (33, 'Gustavo'),
    (35, 'Helena'), (43, 'Igor'), (48, 'Larissa'), (58, 'Kleber'),
    (83, 'Larissa'), (84, 'Marcos'), (86, 'Natália'), (97, 'Otávio'),
    (104, 'Patrícia'), (106, 'Rafael'), (115, 'Sabrina'), (120, 'Tiago'),
    (122, 'Vanessa'), (127, 'Amanda'), (143, 'Breno'), (147, 'Camila'),
    (149, 'Diego'), (179, 'Gabriela'), (184, 'Henrique'), (187, 'Isabela'),
    (194, 'João'), (199, 'Karen'), (201, 'Leonardo'), (211, 'Mirela'),
    (213, 'Nicolas'), (232, 'Olívia'), (256, 'Simone'), (258, 'Túlio'),
    (261, 'Victor'), (269, 'Wesley'), (273, 'Xênia'), (278, 'Yasmin'),
    (280, 'Zeca'), (288, 'Alana'), (291, 'Caio'), (292, 'Diana'),
    (294, 'Fábio')
]


def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    tentativas = 0

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio][0]
        tentativas += 1

        if chute == item:
            return lista[meio][1], tentativas
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    return None, tentativas


nome, tentativas = pesquisa_binaria(pessoas, 256)

print("Nome:", nome)
print("Tentativas na pesquisa binária:", tentativas)
print("Tentativas na pesquisa sequencial:", pessoas.index((256, 'Simone')) + 1)