
import time
import random
import statistics
import matplotlib.pyplot as plt

from dfs import dfs_recursivo, dfs_iterativo

# Configurações
NUM_EXECUCOES = 10
random.seed(42)  # Permite reproduzir os mesmos grafos


# 1. GERADOR DE ARVORE BINARIA BALANCEADA
def gerar_arvore(num_vertices):
    return num_vertices



# 2. TAMANHOS DOS GRAFOS
tamanhos_vertices = [
    10, 50, 100, 500, 1000, 2000,
    3000, 4000, 5000, 10000, 20000
]

tempos_iterativo = []
tempos_recursivo = []

print("Iniciando a coleta de tempos...")
print(f"Cada versão será executada {NUM_EXECUCOES} vezes por tamanho.\n")


# 3. COLETA DE TEMPOS
for v in tamanhos_vertices:
    arvore_teste = gerar_arvore(v)

    # Confere se as implementações produzem o mesmo resultado.
    resultado_recursivo = dfs_recursivo(1, v)
    resultado_iterativo = dfs_iterativo(v)

    assert resultado_recursivo == resultado_iterativo, (
        f"Resultados diferentes para a arvore com {v} nos!"
    )

    tempos_r = []
    tempos_i = []

    # Repete as medições usando sempre o mesmo grafo.
    for repeticao in range(NUM_EXECUCOES):

        # Alterna a ordem para reduzir possíveis efeitos da ordem
        # de execução sobre as medições.
        if repeticao % 2 == 0:
            inicio = time.perf_counter()
            dfs_recursivo(1, arvore_teste)
            fim = time.perf_counter()
            tempos_r.append(fim - inicio)

            inicio = time.perf_counter()
            dfs_iterativo(arvore_teste)
            fim = time.perf_counter()
            tempos_i.append(fim - inicio)

        else:
            inicio = time.perf_counter()
            dfs_iterativo(arvore_teste)
            fim = time.perf_counter()
            tempos_i.append(fim - inicio)

            inicio = time.perf_counter()
            dfs_recursivo(1, arvore_teste)
            fim = time.perf_counter()
            tempos_r.append(fim - inicio)

    # Calcula a média dos tempos
    media_r = statistics.mean(tempos_r)
    media_i = statistics.mean(tempos_i)

    tempos_recursivo.append(media_r)
    tempos_iterativo.append(media_i)

    print(f"Arvore com {v:>6} nos:")
    print(f"  Recursivo: {media_r:.8f} segundos")
    print(f"  Iterativo: {media_i:.8f} segundos")
    print()


print("Análise concluída! Gerando gráfico...")


# 4. GRÁFICO COM AS MÉDIAS
plt.figure(figsize=(10, 6))

plt.plot(
    tamanhos_vertices,
    tempos_recursivo,
    marker="o",
    linestyle="-",
    label="DFS Recursivo"
)

plt.plot(
    tamanhos_vertices,
    tempos_iterativo,
    marker="s",
    linestyle="--",
    label="DFS Iterativo"
)

plt.title(
    "DFS: média do tempo de execução",
    fontsize=14,
    fontweight="bold"
)
plt.xlabel("Quantidade de nos", fontsize=12)
plt.ylabel("Tempo médio (segundos)", fontsize=12)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(fontsize=11)
plt.tight_layout()

plt.show()
