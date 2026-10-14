
def bellman_ford_iterativo(grafo, origem):
    vertices = list(grafo.keys())

   
    distancias = {v: float("inf") for v in vertices}
    distancias[origem] = 0

   
    for _ in range(len(vertices) - 1):
        houve_atualizacao = False

        for u in vertices:
            for v, peso in grafo[u]:
                if distancias[u] != float("inf"):
                    nova_distancia = distancias[u] + peso

                    if nova_distancia < distancias[v]:
                        distancias[v] = nova_distancia
                        houve_atualizacao = True

        
        if not houve_atualizacao:
            break

   
    for u in vertices:
        for v, peso in grafo[u]:
            if distancias[u] != float("inf"):
                if distancias[u] + peso < distancias[v]:
                    raise ValueError(
                        "O grafo contém um ciclo negativo alcançável."
                    )

    return distancias

def bellman_ford_recursivo(grafo, origem):
    vertices = list(grafo.keys())
    distancias = {v: float("inf") for v in vertices}
    distancias[origem] = 0

    def relaxar_rodada(rodada):
        if rodada >= len(vertices) - 1:
            return

        houve_atualizacao = False

        for u in vertices:
            for v, peso in grafo[u]:
                if distancias[u] != float("inf"):
                    nova_distancia = distancias[u] + peso

                    if nova_distancia < distancias[v]:
                        distancias[v] = nova_distancia
                        houve_atualizacao = True

        if houve_atualizacao:
            relaxar_rodada(rodada + 1)

    relaxar_rodada(0)

   
    for u in vertices:
        for v, peso in grafo[u]:
            if distancias[u] != float("inf"):
                if distancias[u] + peso < distancias[v]:
                    raise ValueError(
                        "O grafo contém um ciclo negativo alcançável."
                    )

    return distancias
