# Recursivo

def dfs_recursivo(no, total):
    if no > total:
        return 0

    esquerda = dfs_recursivo(no * 2, total)
    direita = dfs_recursivo(no * 2 + 1, total)

    return 1 + esquerda + direita

# Iterativo --------------------------------------------


def dfs_iterativo(total):

    lpilha = [1]
    cvisitados = 0

    while lpilha:
        no = lpilha.pop()

        if no > total:
            continue

        cvisitados += 1

        lpilha.append(no * 2 + 1)
        lpilha.append(no * 2)

    return cvisitados
#-------------------------------------------

total = 8

resultado_recursivo = dfs_recursivo(1, total)
resultado_iterativo = dfs_iterativo(total)


print("Quantidade de nós da busca RECURSIVA: ", resultado_recursivo)

print("Quantidade de nós da busca ITERATIVA: ", resultado_iterativo)




