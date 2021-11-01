from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from meu_grafo_listaAdjacencia import MeuGrafo

############################ TESTES grafo_test ################################

#################### GRAFOS ATIVIDADES ####################

# Grafo da Paraíba (Roteiro 1)
g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
g_p.adicionaAresta('a1', 'J', 'C')
g_p.adicionaAresta('a2', 'C', 'E')
g_p.adicionaAresta('a3', 'C', 'E')
g_p.adicionaAresta('a4', 'P', 'C')
g_p.adicionaAresta('a5', 'P', 'C')
g_p.adicionaAresta('a6', 'T', 'C')
g_p.adicionaAresta('a7', 'M', 'C')
g_p.adicionaAresta('a8', 'M', 'T')
g_p.adicionaAresta('a9', 'T', 'Z')

# Grafo (Roteiro 2)
g_Roteiro2 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
g_Roteiro2.adicionaAresta('a1', 'A', 'B')
g_Roteiro2.adicionaAresta('a2', 'A', 'G')
g_Roteiro2.adicionaAresta('a3', 'A', 'J')
g_Roteiro2.adicionaAresta('a4', 'K', 'G')
g_Roteiro2.adicionaAresta('a5', 'K', 'J')
g_Roteiro2.adicionaAresta('a6', 'J', 'G')
g_Roteiro2.adicionaAresta('a7', 'J', 'I')
g_Roteiro2.adicionaAresta('a8', 'G', 'I')
g_Roteiro2.adicionaAresta('a9', 'G', 'H')
g_Roteiro2.adicionaAresta('a10', 'H', 'F')
g_Roteiro2.adicionaAresta('a11', 'F', 'B')
g_Roteiro2.adicionaAresta('a12', 'B', 'G')
g_Roteiro2.adicionaAresta('a13', 'B', 'C')
g_Roteiro2.adicionaAresta('a14', 'C', 'D')
g_Roteiro2.adicionaAresta('a15', 'D', 'E')
g_Roteiro2.adicionaAresta('a16', 'D', 'B')
g_Roteiro2.adicionaAresta('a17', 'B', 'E')

#################### GRAFOS SIMPLES ####################

grafoSimples1 = MeuGrafo(['A', 'B', 'C', 'D', 'E'])
grafoSimples1.adicionaAresta('a1', 'A', 'B')
grafoSimples1.adicionaAresta('a2', 'B', 'D')
grafoSimples1.adicionaAresta('a3', 'B', 'C')
grafoSimples1.adicionaAresta('a4', 'C', 'D')
grafoSimples1.adicionaAresta('a5', 'D', 'E')
grafoSimples1.adicionaAresta('a6', 'C', 'E')

grafoSimples2 = MeuGrafo(['M', 'N', 'O', 'P', 'Q'])
grafoSimples2.adicionaAresta('a1', 'M', 'O')
grafoSimples2.adicionaAresta('a2', 'M', 'P')
grafoSimples2.adicionaAresta('a3', 'O', 'N')
grafoSimples2.adicionaAresta('a4', 'N', 'P')
grafoSimples2.adicionaAresta('a5', 'P', 'Q')

grafoSimples3 = MeuGrafo(['1', '2', '3', '4', '5', '6'])
grafoSimples3.adicionaAresta('a1', '1', '2')
grafoSimples3.adicionaAresta('a2', '1', '3')
grafoSimples3.adicionaAresta('a3', '1', '4')
grafoSimples3.adicionaAresta('a4', '1', '6')
grafoSimples3.adicionaAresta('a5', '3', '4')
grafoSimples3.adicionaAresta('a6', '3', '5')
grafoSimples3.adicionaAresta('a7', '4', '5')
grafoSimples3.adicionaAresta('a8', '2', '3')
grafoSimples3.adicionaAresta('a9', '2', '5')
grafoSimples3.adicionaAresta('a10', '5', '6')
grafoSimples3.adicionaAresta('a11', '4', '6')
grafoSimples3.adicionaAresta('a12', '2', '6')

#################### GRAFOS COM ARESTAS PARALELAS ####################

grafoComArestasParalelas1 = MeuGrafo(['A', 'B', 'C', 'D', 'E'])
grafoComArestasParalelas1.adicionaAresta('a1', 'A', 'B')
grafoComArestasParalelas1.adicionaAresta('a2', 'A', 'B')
grafoComArestasParalelas1.adicionaAresta('a3', 'A', 'E')
grafoComArestasParalelas1.adicionaAresta('a4', 'E', 'C')
grafoComArestasParalelas1.adicionaAresta('a5', 'B', 'D')
grafoComArestasParalelas1.adicionaAresta('a6', 'D', 'C')

grafoComArestasParalelas2 = MeuGrafo(['1', '2', '3', '4'])
grafoComArestasParalelas2.adicionaAresta('a1', '1', '2')
grafoComArestasParalelas2.adicionaAresta('a2', '2', '3')
grafoComArestasParalelas2.adicionaAresta('a3', '2', '3')
grafoComArestasParalelas2.adicionaAresta('a4', '3', '4')

#################### GRAFOS SEM ARESTAS PARALELAS ####################

# Grafo da Paraíba sem arestas paralelas
g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')

#################### GRAFOS COMPLETOS ####################

g_c = MeuGrafo(['J', 'C', 'E', 'P'])
g_c.adicionaAresta('a1', 'J', 'C')
g_c.adicionaAresta('a2', 'J', 'E')
g_c.adicionaAresta('a3', 'J', 'P')
g_c.adicionaAresta('a4', 'E', 'C')
g_c.adicionaAresta('a5', 'P', 'C')
g_c.adicionaAresta('a6', 'P', 'E')

g_c2 = MeuGrafo(['Nina', 'Maria'])
g_c2.adicionaAresta('amiga', 'Nina', 'Maria')

g_c3 = MeuGrafo(['J'])

grafoCompleto1 = MeuGrafo(['P', 'Q', 'R', 'S', 'T'])
grafoCompleto1.adicionaAresta('a1', 'P', 'T')
grafoCompleto1.adicionaAresta('a2', 'P', 'S')
grafoCompleto1.adicionaAresta('a3', 'P', 'R')
grafoCompleto1.adicionaAresta('a4', 'P', 'Q')
grafoCompleto1.adicionaAresta('a5', 'Q', 'T')
grafoCompleto1.adicionaAresta('a6', 'R', 'T')
grafoCompleto1.adicionaAresta('a7', 'Q', 'S')
grafoCompleto1.adicionaAresta('a8', 'Q', 'R')
grafoCompleto1.adicionaAresta('a9', 'R', 'S')
grafoCompleto1.adicionaAresta('a10', 'S', 'T')

#################### GRAFOS COM LAÇOS ####################

g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
g_l1.adicionaAresta('a1', 'A', 'A')
g_l1.adicionaAresta('a2', 'A', 'B')
g_l1.adicionaAresta('a3', 'A', 'A')

g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
g_l2.adicionaAresta('a1', 'A', 'B')
g_l2.adicionaAresta('a2', 'B', 'B')
g_l2.adicionaAresta('a3', 'B', 'A')

g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
g_l3.adicionaAresta('a1', 'C', 'A')
g_l3.adicionaAresta('a2', 'C', 'C')
g_l3.adicionaAresta('a3', 'D', 'D')
g_l3.adicionaAresta('a4', 'D', 'D')

g_l4 = MeuGrafo(['D'])
g_l4.adicionaAresta('a1', 'D', 'D')

g_l5 = MeuGrafo(['C', 'D'])
g_l5.adicionaAresta('a1', 'D', 'C')
g_l5.adicionaAresta('a2', 'C', 'C')

#################### GRAFOS DESCONEXOS ####################

g_d = MeuGrafo(['A', 'B', 'C', 'D'])
g_d.adicionaAresta('asd', 'A', 'B')

# Grafo Paraíba desconexo
g_p_desconexo = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
g_p_desconexo.adicionaAresta('a2', 'C', 'E')
g_p_desconexo.adicionaAresta('a3', 'C', 'E')
g_p_desconexo.adicionaAresta('a4', 'P', 'C')
g_p_desconexo.adicionaAresta('a5', 'P', 'C')
g_p_desconexo.adicionaAresta('a6', 'T', 'C')
g_p_desconexo.adicionaAresta('a7', 'M', 'C')
g_p_desconexo.adicionaAresta('a8', 'M', 'T')
g_p_desconexo.adicionaAresta('a9', 'T', 'Z')

grafoDesconexo1 = MeuGrafo(['A', 'B', 'C', 'D', 'E'])
grafoDesconexo1.adicionaAresta('a1', 'A', 'E')
grafoDesconexo1.adicionaAresta('a2', 'E', 'B')
grafoDesconexo1.adicionaAresta('a3', 'E', 'C')
grafoDesconexo1.adicionaAresta('a4', 'C', 'A')

#################### GRAFOS TESTE DFS ####################

# Grafo Paraiba DFS partindo de J
g_p_DFS_J = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
g_p_DFS_J.adicionaAresta('a1', 'J', 'C')
g_p_DFS_J.adicionaAresta('a2', 'C', 'E')
g_p_DFS_J.adicionaAresta('a4', 'P', 'C')
g_p_DFS_J.adicionaAresta('a6', 'T', 'C')
g_p_DFS_J.adicionaAresta('a8', 'M', 'T')
g_p_DFS_J.adicionaAresta('a9', 'T', 'Z')

# Grafo Roteiro2 DFS partindo de K
g_Roteiro2_DFS_K = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
g_Roteiro2_DFS_K.adicionaAresta('a4', 'K', 'G')
g_Roteiro2_DFS_K.adicionaAresta('a2', 'A', 'G')
g_Roteiro2_DFS_K.adicionaAresta('a1', 'A', 'B')
g_Roteiro2_DFS_K.adicionaAresta('a11', 'F', 'B')
g_Roteiro2_DFS_K.adicionaAresta('a10', 'H', 'F')
g_Roteiro2_DFS_K.adicionaAresta('a13', 'B', 'C')
g_Roteiro2_DFS_K.adicionaAresta('a14', 'C', 'D')
g_Roteiro2_DFS_K.adicionaAresta('a15', 'D', 'E')
g_Roteiro2_DFS_K.adicionaAresta('a3', 'A', 'J')
g_Roteiro2_DFS_K.adicionaAresta('a7', 'J', 'I')

#################### GRAFOS TESTE BFS ####################

# Grafo da Paraíba BFS partindo de C
g_p_BFS_C = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
g_p_BFS_C.adicionaAresta('a1', 'J', 'C')
g_p_BFS_C.adicionaAresta('a2', 'C', 'E')
g_p_BFS_C.adicionaAresta('a4', 'P', 'C')
g_p_BFS_C.adicionaAresta('a6', 'T', 'C')
g_p_BFS_C.adicionaAresta('a7', 'M', 'C')
g_p_BFS_C.adicionaAresta('a9', 'T', 'Z')

# Grafo Roteiro2 BFS partindo de F
g_Roteiro2_BFS_F = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
g_Roteiro2_BFS_F.adicionaAresta('a10', 'H', 'F')
g_Roteiro2_BFS_F.adicionaAresta('a11', 'F', 'B')
g_Roteiro2_BFS_F.adicionaAresta('a9', 'G', 'H')
g_Roteiro2_BFS_F.adicionaAresta('a2', 'A', 'G')
g_Roteiro2_BFS_F.adicionaAresta('a4', 'K', 'G')
g_Roteiro2_BFS_F.adicionaAresta('a6', 'J', 'G')
g_Roteiro2_BFS_F.adicionaAresta('a8', 'G', 'I')
g_Roteiro2_BFS_F.adicionaAresta('a13', 'B', 'C')
g_Roteiro2_BFS_F.adicionaAresta('a16', 'D', 'B')
g_Roteiro2_BFS_F.adicionaAresta('a17', 'B', 'E')

#################### GRAFOS ACÍCLICOS ####################

grafoAciclico1 = MeuGrafo(['1', '2', '3', '4', '5', '6'])
grafoAciclico1.adicionaAresta('a1', '1', '4')
grafoAciclico1.adicionaAresta('a2', '2', '4')
grafoAciclico1.adicionaAresta('a3', '3', '4')
grafoAciclico1.adicionaAresta('a4', '4', '5')
grafoAciclico1.adicionaAresta('a5', '5', '6')

grafoAciclico2 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])
grafoAciclico2.adicionaAresta('a1', 'A', 'C')
grafoAciclico2.adicionaAresta('a2', 'C', 'E')
grafoAciclico2.adicionaAresta('a3', 'E', 'B')
grafoAciclico2.adicionaAresta('a4', 'E', 'F')
grafoAciclico2.adicionaAresta('a5', 'F', 'D')

grafoAciclico3 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
grafoAciclico3.adicionaAresta('a1', 'A', 'B')
grafoAciclico3.adicionaAresta('a2', 'B', 'D')
grafoAciclico3.adicionaAresta('a3', 'B', 'F')
grafoAciclico3.adicionaAresta('a4', 'A', 'C')
grafoAciclico3.adicionaAresta('a5', 'C', 'G')
grafoAciclico3.adicionaAresta('a6', 'A', 'E')

#################### GRAFOS BIPARTIDO ####################

grafoBipartido1 = MeuGrafo(['1', '2', '3', '4', '5', '6'])
grafoBipartido1.adicionaAresta('a1', '1', '4')
grafoBipartido1.adicionaAresta('a2', '1', '5')
grafoBipartido1.adicionaAresta('a3', '1', '6')
grafoBipartido1.adicionaAresta('a4', '2', '4')
grafoBipartido1.adicionaAresta('a5', '2', '5')
grafoBipartido1.adicionaAresta('a6', '2', '6')
grafoBipartido1.adicionaAresta('a7', '3', '4')
grafoBipartido1.adicionaAresta('a8', '3', '5')
grafoBipartido1.adicionaAresta('a9', '3', '6')

##################### TESTES CAMINHO EULERIANO ###################

grafoEuleriano1 = MeuGrafo(['A', 'B', 'C', 'D'])
grafoEuleriano1.adicionaAresta('a1', 'A', 'B')
grafoEuleriano1.adicionaAresta('a2', 'B', 'C')
grafoEuleriano1.adicionaAresta('a3', 'C', 'D')
grafoEuleriano1.adicionaAresta('a4', 'D', 'A')

grafoEuleriano2 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
grafoEuleriano2.adicionaAresta('a1', 'A', 'B')
grafoEuleriano2.adicionaAresta('a2', 'B', 'C')
grafoEuleriano2.adicionaAresta('a3', 'C', 'A')
grafoEuleriano2.adicionaAresta('a4', 'A', 'G')
grafoEuleriano2.adicionaAresta('a5', 'G', 'C')
grafoEuleriano2.adicionaAresta('a6', 'C', 'D')
grafoEuleriano2.adicionaAresta('a7', 'D', 'G')
grafoEuleriano2.adicionaAresta('a8', 'G', 'F')
grafoEuleriano2.adicionaAresta('a9', 'F', 'D')
grafoEuleriano2.adicionaAresta('a10', 'D', 'E')
grafoEuleriano2.adicionaAresta('a11', 'E', 'F')
grafoEuleriano2.adicionaAresta('a12', 'F', 'A')

grafoEuleriano3 = MeuGrafo(['A', 'B', 'C', 'D', 'E'])
grafoEuleriano3.adicionaAresta('a1', 'A', 'B')
grafoEuleriano3.adicionaAresta('a2', 'B', 'C')
grafoEuleriano3.adicionaAresta('a3', 'C', 'A')
grafoEuleriano3.adicionaAresta('a4', 'A', 'D')
grafoEuleriano3.adicionaAresta('a5', 'D', 'C')
grafoEuleriano3.adicionaAresta('a6', 'C', 'E')
grafoEuleriano3.adicionaAresta('a7', 'E', 'D')

grafoEuleriano4 = MeuGrafo(['A', 'B', 'C'])
grafoEuleriano4.adicionaAresta('a1', 'A', 'B')
grafoEuleriano4.adicionaAresta('a2', 'A', 'C')

grafoEuleriano5 = MeuGrafo(['A', 'B', 'C', 'D', 'E'])
grafoEuleriano5.adicionaAresta('a1', 'A', 'B')
grafoEuleriano5.adicionaAresta('a2', 'B', 'C')
grafoEuleriano5.adicionaAresta('a3', 'C', 'A')
grafoEuleriano5.adicionaAresta('a4', 'A', 'D')
grafoEuleriano5.adicionaAresta('a5', 'D', 'E')
grafoEuleriano5.adicionaAresta('a6', 'E', 'A')

#################### TESTES FUNÇÕES ####################

'''
#### LISTA DE ADJACENCIA ###

# PERCORRER VÉRTICES (NÓS)
for v in teste.N:
    print(v)
'''
'''
# PERCORRER ARESTAS
for a in teste.A:
    print(a)
'''
'''
# PERCORRER VÉRTICES QUE LIGAM ARESTAS
for a in teste.A:
    print(teste.A[a])
'''
'''
# PEGAR ÚNICA ARESTAJ
print(teste.getAresta("a1"))
'''
'''
# INFORMAÇÕES DA ARESTA (teste = self em meu_grafo)
print(teste.getAresta("a1"))
print(teste.getAresta("a1").getRotulo())
print(teste.getAresta("a1").getV1())
print(teste.getAresta("a1").getV2())
print(teste.getAresta("a1").getPeso())
'''

print(g_Roteiro2.dfs("A"))