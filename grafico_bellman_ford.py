
import time
import random
import statistics
import matplotlib.pyplot as plt

from bellman_ford import (
    bellman_ford_iterativo as bellman_iterativo,
    bellman_ford_recursivo as bellman_recursivo
)


NUM_EXECUCOES = 10
random.seed(42)  

# 1. GERADOR DE GRAFOS DIRECIONADOS E PONDERADOS
def gerar_grafo(num_vertices):
    grafo = {i: [] for i in range(num_vertices)}

    for i in range(num_vertices - 1):
        peso = random.randint(1, 10)
        grafo[i].append((i + 1, peso))

    return grafo



tamanhos_vertices = [
    10, 50, 100, 500, 1000, 2000,
    3000, 4000, 5000, 10000, 20000
]

tempos_iterativo = []
tempos_recursivo = []

print("Iniciando a coleta de tempos...")
print(f"Cada versão será executada {NUM_EXECUCOES} vezes por tamanho.\n")



for v in tamanhos_vertices:
    grafo_teste = gerar_grafo(v)

   
    resultado_recursivo = bellman_recursivo(grafo_teste, 0)
    resultado_iterativo = bellman_iterativo(grafo_teste, 0)

    assert resultado_recursivo == resultado_iterativo, (
        f"Resultados diferentes para o grafo com {v} vértices!"
    )

    tempos_r = []
    tempos_i = []

   
    for repeticao in range(NUM_EXECUCOES):
        
        if repeticao % 2 == 0:
            inicio = time.perf_counter()
            bellman_recursivo(grafo_teste, 0)
            fim = time.perf_counter()
            tempos_r.append(fim - inicio)

            inicio = time.perf_counter()
            bellman_iterativo(grafo_teste, 0)
            fim = time.perf_counter()
            tempos_i.append(fim - inicio)

        else:
            inicio = time.perf_counter()
            bellman_iterativo(grafo_teste, 0)
            fim = time.perf_counter()
            tempos_i.append(fim - inicio)

            inicio = time.perf_counter()
            bellman_recursivo(grafo_teste, 0)
            fim = time.perf_counter()
            tempos_r.append(fim - inicio)

   
    media_r = statistics.mean(tempos_r)
    media_i = statistics.mean(tempos_i)

    tempos_recursivo.append(media_r)
    tempos_iterativo.append(media_i)

    print(f"Grafo com {v:>6} vértices:")
    print(f"  Recursivo: {media_r:.8f} segundos")
    print(f"  Iterativo: {media_i:.8f} segundos")
    print()


print("Análise concluída! Gerando gráfico...")


plt.figure(figsize=(10, 6))

plt.plot(
    tamanhos_vertices,
    tempos_recursivo,
    marker="o",
    linestyle="-",
    label="Bellman-Ford Recursivo"
)

plt.plot(
    tamanhos_vertices,
    tempos_iterativo,
    marker="s",
    linestyle="--",
    label="Bellman-Ford Iterativo"
)

plt.title(
    "Bellman-Ford: média do tempo de execução",
    fontsize=14,
    fontweight="bold"
)
plt.xlabel("Número de vértices", fontsize=12)
plt.ylabel("Tempo médio (segundos)", fontsize=12)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(fontsize=11)
plt.tight_layout()

plt.show()
