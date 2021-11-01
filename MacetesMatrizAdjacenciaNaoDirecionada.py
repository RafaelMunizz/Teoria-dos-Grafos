from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from meu_grafo_matriz_adjacencia_nao_dir import MeuGrafo

############################ TESTES grafo_test ################################

# Grafo da Paraíba sem arestas paralelas
g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C', 2)
g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E', 3)
g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C', 4)
g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C', 2)
g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C', 4)
g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T', 5)
g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z', 3)

grafoPrim1 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
grafoPrim1.adicionaAresta('a1', 'A', 'B', 2)
grafoPrim1.adicionaAresta('a2', 'A', 'C', 1)
grafoPrim1.adicionaAresta('a3', 'A', 'E', 3)
grafoPrim1.adicionaAresta('a4', 'A', 'D', 2)
grafoPrim1.adicionaAresta('a5', 'C', 'D', 1)
grafoPrim1.adicionaAresta('a6', 'C', 'D', 3)
grafoPrim1.adicionaAresta('a7', 'D', 'E', 5)
grafoPrim1.adicionaAresta('a8', 'E', 'G', 3)
grafoPrim1.adicionaAresta('a9', 'E', 'F', 5)
grafoPrim1.adicionaAresta('a10', 'F', 'G', 4)

# Grafo (Roteiro 2)
g_Roteiro2 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
g_Roteiro2.adicionaAresta('a1', 'A', 'B', 2)
g_Roteiro2.adicionaAresta('a2', 'A', 'G', 3)
g_Roteiro2.adicionaAresta('a3', 'A', 'J', 6)
g_Roteiro2.adicionaAresta('a4', 'K', 'G', 4)
g_Roteiro2.adicionaAresta('a5', 'K', 'J', 8)
g_Roteiro2.adicionaAresta('a6', 'J', 'G', 6)
g_Roteiro2.adicionaAresta('a7', 'J', 'I', 4)
g_Roteiro2.adicionaAresta('a8', 'G', 'I', 1)
g_Roteiro2.adicionaAresta('a9', 'G', 'H', 5)
g_Roteiro2.adicionaAresta('a10', 'H', 'F', 3)
g_Roteiro2.adicionaAresta('a11', 'F', 'B', 2)
g_Roteiro2.adicionaAresta('a12', 'B', 'G', 7)
g_Roteiro2.adicionaAresta('a13', 'B', 'C', 5)
g_Roteiro2.adicionaAresta('a14', 'C', 'D', 3)
g_Roteiro2.adicionaAresta('a15', 'D', 'E', 4)
g_Roteiro2.adicionaAresta('a16', 'D', 'B', 6)
g_Roteiro2.adicionaAresta('a17', 'B', 'E', 3)

grafoSimples3 = MeuGrafo(['1', '2', '3', '4', '5', '6'])
grafoSimples3.adicionaAresta('a1', '1', '2', 3)
grafoSimples3.adicionaAresta('a2', '1', '3', 4)
grafoSimples3.adicionaAresta('a3', '1', '4', 2)
grafoSimples3.adicionaAresta('a4', '1', '6', 3)
grafoSimples3.adicionaAresta('a5', '3', '4', 1)
grafoSimples3.adicionaAresta('a6', '3', '5', 6)
grafoSimples3.adicionaAresta('a7', '4', '5', 5)
grafoSimples3.adicionaAresta('a8', '2', '3', 2)
grafoSimples3.adicionaAresta('a9', '2', '5', 4)
grafoSimples3.adicionaAresta('a10', '5', '6', 3)
grafoSimples3.adicionaAresta('a11', '4', '6', 4)
grafoSimples3.adicionaAresta('a12', '2', '6', 5)

grafoEuleriano2 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
grafoEuleriano2.adicionaAresta('a1', 'A', 'B', 2)
grafoEuleriano2.adicionaAresta('a2', 'B', 'C', 3)
grafoEuleriano2.adicionaAresta('a3', 'C', 'A', 4)
grafoEuleriano2.adicionaAresta('a4', 'A', 'G', 7)
grafoEuleriano2.adicionaAresta('a5', 'G', 'C', 5)
grafoEuleriano2.adicionaAresta('a6', 'C', 'D', 4)
grafoEuleriano2.adicionaAresta('a7', 'D', 'G', 3)
grafoEuleriano2.adicionaAresta('a8', 'G', 'F', 6)
grafoEuleriano2.adicionaAresta('a9', 'F', 'D', 4)
grafoEuleriano2.adicionaAresta('a10', 'D', 'E', 1)
grafoEuleriano2.adicionaAresta('a11', 'E', 'F', 2)
grafoEuleriano2.adicionaAresta('a12', 'F', 'A', 3)

# Criado para testes com algoritmo de Dijkstra
grafoGigante = MeuGrafo(
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'])
grafoGigante.adicionaAresta('a1', 'A', 'B', 3)
grafoGigante.adicionaAresta('a2', 'A', 'C', 4)
grafoGigante.adicionaAresta('a3', 'A', 'D', 5)
grafoGigante.adicionaAresta('a4', 'B', 'G', 5)
grafoGigante.adicionaAresta('a5', 'B', 'F', 6)
grafoGigante.adicionaAresta('a6', 'C', 'F', 3)
grafoGigante.adicionaAresta('a7', 'C', 'E', 6)
grafoGigante.adicionaAresta('a8', 'C', 'D', 3)
grafoGigante.adicionaAresta('a9', 'D', 'E', 3)
grafoGigante.adicionaAresta('a10', 'G', 'I', 2)
grafoGigante.adicionaAresta('a11', 'F', 'I', 3)
grafoGigante.adicionaAresta('a12', 'F', 'H', 4)
grafoGigante.adicionaAresta('a13', 'E', 'H', 2)
grafoGigante.adicionaAresta('a14', 'E', 'K', 6)
grafoGigante.adicionaAresta('a15', 'E', 'J', 3)
grafoGigante.adicionaAresta('a16', 'I', 'L', 5)
grafoGigante.adicionaAresta('a17', 'H', 'L', 10)
grafoGigante.adicionaAresta('a18', 'K', 'L', 3)
grafoGigante.adicionaAresta('a19', 'K', 'O', 5)
grafoGigante.adicionaAresta('a20', 'K', 'N', 2)
grafoGigante.adicionaAresta('a21', 'J', 'N', 4)
grafoGigante.adicionaAresta('a22', 'L', 'M', 6)
grafoGigante.adicionaAresta('a23', 'O', 'M', 4)
grafoGigante.adicionaAresta('a24', 'O', 'P', 4)
grafoGigante.adicionaAresta('a25', 'N', 'P', 6)
grafoGigante.adicionaAresta('a26', 'M', 'R', 5)
grafoGigante.adicionaAresta('a27', 'M', 'Q', 9)
grafoGigante.adicionaAresta('a28', 'Q', 'R', 3)
grafoGigante.adicionaAresta('a29', 'Q', 'S', 2)
grafoGigante.adicionaAresta('a30', 'Q', 'P', 3)
grafoGigante.adicionaAresta('a31', 'P', 'T', 9)
grafoGigante.adicionaAresta('a32', 'T', 'S', 1)
#################### TESTES FUNÇÕES ####################
'''
# PERCORRER VÉRTICES (NÓS)
for v in g_p.N:
    print(v)
'''
'''
# PERCORRER MATRIZ
for i in range(len(g_p.M)):
     print(g_p.M[i])
'''
'''
# PERCORRER ARESTAS
for linha in range(len(g_p.M)):
    for coluna in range(len(g_p.M[linha])):

        if g_p.M[linha][coluna] != '-' :
            for aresta in g_p.M[linha][coluna]:
                print(aresta)
'''
'''
# INDICE DO VERTICE NA MATRIZ
print(g_p.N.index('C'))
'''


print(g_Roteiro2.dfs('A'))

