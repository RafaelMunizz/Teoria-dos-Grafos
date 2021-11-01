import unittest
from meu_grafo_matriz_adjacencia_dir import *
from bibgrafo.grafo_exceptions import *

class TestGrafo(unittest.TestCase):

    def setUp(self):

        #################### GRAFOS ATIVIDADES ####################

        # Grafo da Paraíba direcionado (Roteiro 1)
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C')
        self.g_p.adicionaAresta('a2', 'C', 'E')
        self.g_p.adicionaAresta('a3', 'E', 'C')
        self.g_p.adicionaAresta('a4', 'C', 'P')
        self.g_p.adicionaAresta('a5', 'P', 'C')
        self.g_p.adicionaAresta('a6', 'C', 'T')
        self.g_p.adicionaAresta('a7', 'C', 'M')
        self.g_p.adicionaAresta('a8', 'M', 'T')
        self.g_p.adicionaAresta('a9', 'T', 'Z')

        # Grafo (Roteiro 2)
        self.g_Roteiro2 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
        self.g_Roteiro2.adicionaAresta('a1', 'A', 'B')
        self.g_Roteiro2.adicionaAresta('a2', 'A', 'G')
        self.g_Roteiro2.adicionaAresta('a3', 'A', 'J')
        self.g_Roteiro2.adicionaAresta('a4', 'K', 'G')
        self.g_Roteiro2.adicionaAresta('a5', 'K', 'J')
        self.g_Roteiro2.adicionaAresta('a6', 'J', 'G')
        self.g_Roteiro2.adicionaAresta('a7', 'J', 'I')
        self.g_Roteiro2.adicionaAresta('a8', 'G', 'I')
        self.g_Roteiro2.adicionaAresta('a9', 'G', 'H')
        self.g_Roteiro2.adicionaAresta('a10', 'H', 'F')
        self.g_Roteiro2.adicionaAresta('a11', 'F', 'B')
        self.g_Roteiro2.adicionaAresta('a12', 'B', 'G')
        self.g_Roteiro2.adicionaAresta('a13', 'B', 'C')
        self.g_Roteiro2.adicionaAresta('a14', 'C', 'D')
        self.g_Roteiro2.adicionaAresta('a15', 'D', 'E')
        self.g_Roteiro2.adicionaAresta('a16', 'D', 'B')
        self.g_Roteiro2.adicionaAresta('a17', 'B', 'E')

        #################### GRAFOS SIMPLES ####################

        self.grafoSimples1 = MeuGrafo(['A', 'B', 'C', 'D', 'E'])
        self.grafoSimples1.adicionaAresta('a1', 'A', 'B')
        self.grafoSimples1.adicionaAresta('a2', 'B', 'D')
        self.grafoSimples1.adicionaAresta('a3', 'B', 'C')
        self.grafoSimples1.adicionaAresta('a4', 'C', 'D')
        self.grafoSimples1.adicionaAresta('a5', 'D', 'E')
        self.grafoSimples1.adicionaAresta('a6', 'C', 'E')

        self.grafoSimples2 = MeuGrafo(['M', 'N', 'O', 'P', 'Q'])
        self.grafoSimples2.adicionaAresta('a1', 'M', 'O')
        self.grafoSimples2.adicionaAresta('a2', 'M', 'P')
        self.grafoSimples2.adicionaAresta('a3', 'O', 'N')
        self.grafoSimples2.adicionaAresta('a4', 'N', 'P')
        self.grafoSimples2.adicionaAresta('a5', 'P', 'Q')

        self.grafoSimples3 = MeuGrafo(['1', '2', '3', '4', '5', '6'])
        self.grafoSimples3.adicionaAresta('a1', '1', '2')
        self.grafoSimples3.adicionaAresta('a2', '1', '3')
        self.grafoSimples3.adicionaAresta('a3', '1', '4')
        self.grafoSimples3.adicionaAresta('a4', '1', '6')
        self.grafoSimples3.adicionaAresta('a5', '3', '4')
        self.grafoSimples3.adicionaAresta('a6', '3', '5')
        self.grafoSimples3.adicionaAresta('a7', '4', '5')
        self.grafoSimples3.adicionaAresta('a8', '2', '3')
        self.grafoSimples3.adicionaAresta('a9', '2', '5')
        self.grafoSimples3.adicionaAresta('a10', '5', '6')
        self.grafoSimples3.adicionaAresta('a11', '4', '6')
        self.grafoSimples3.adicionaAresta('a12', '2', '6')

        #################### GRAFOS COM ARESTAS PARALELAS ####################

        self.grafoComArestasParalelas1 = MeuGrafo(['A', 'B', 'C', 'D', 'E'])
        self.grafoComArestasParalelas1.adicionaAresta('a1', 'A', 'B')
        self.grafoComArestasParalelas1.adicionaAresta('a2', 'B', 'A')
        self.grafoComArestasParalelas1.adicionaAresta('a3', 'A', 'E')
        self.grafoComArestasParalelas1.adicionaAresta('a4', 'E', 'C')
        self.grafoComArestasParalelas1.adicionaAresta('a5', 'B', 'D')
        self.grafoComArestasParalelas1.adicionaAresta('a6', 'D', 'C')

        self.grafoComArestasParalelas2 = MeuGrafo(['1', '2', '3', '4'])
        self.grafoComArestasParalelas2.adicionaAresta('a1', '1', '2')
        self.grafoComArestasParalelas2.adicionaAresta('a2', '2', '3')
        self.grafoComArestasParalelas2.adicionaAresta('a3', '3', '2')
        self.grafoComArestasParalelas2.adicionaAresta('a4', '3', '4')

        #################### GRAFOS SEM ARESTAS PARALELAS ####################

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')


        #################### GRAFOS COMPLETOS ####################

        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1', 'J', 'C')
        self.g_c.adicionaAresta('a2', 'J', 'E')
        self.g_c.adicionaAresta('a3', 'J', 'P')
        self.g_c.adicionaAresta('a4', 'E', 'C')
        self.g_c.adicionaAresta('a5', 'P', 'C')
        self.g_c.adicionaAresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo(['N', 'M'])
        self.g_c2.adicionaAresta('a1', 'N', 'M')

        self.g_c3 = MeuGrafo(['J'])

        self.grafoCompleto1 = MeuGrafo(['P', 'Q', 'R', 'S', 'T'])
        self.grafoCompleto1.adicionaAresta('a1', 'P', 'T')
        self.grafoCompleto1.adicionaAresta('a2', 'P', 'S')
        self.grafoCompleto1.adicionaAresta('a3', 'P', 'R')
        self.grafoCompleto1.adicionaAresta('a4', 'P', 'Q')
        self.grafoCompleto1.adicionaAresta('a5', 'Q', 'T')
        self.grafoCompleto1.adicionaAresta('a6', 'R', 'T')
        self.grafoCompleto1.adicionaAresta('a7', 'Q', 'S')
        self.grafoCompleto1.adicionaAresta('a8', 'Q', 'R')
        self.grafoCompleto1.adicionaAresta('a9', 'R', 'S')
        self.grafoCompleto1.adicionaAresta('a10', 'S', 'T')

        #################### GRAFOS COM LAÇOS ####################

        self.g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('a1', 'A', 'A')
        self.g_l1.adicionaAresta('a2', 'A', 'B')
        self.g_l1.adicionaAresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('a1', 'A', 'B')
        self.g_l2.adicionaAresta('a2', 'B', 'B')
        self.g_l2.adicionaAresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('a1', 'C', 'A')
        self.g_l3.adicionaAresta('a2', 'C', 'C')
        self.g_l3.adicionaAresta('a3', 'D', 'D')
        self.g_l3.adicionaAresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo(['D'])
        self.g_l4.adicionaAresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo(['C', 'D'])
        self.g_l5.adicionaAresta('a1', 'D', 'C')
        self.g_l5.adicionaAresta('a2', 'C', 'C')

        #################### GRAFOS DESCONEXOS ####################

        self.g_d = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_d.adicionaAresta('asd', 'A', 'B')

        # Grafo Paraíba desconexo
        self.g_p_desconexo = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_desconexo.adicionaAresta('a2', 'C', 'E')
        self.g_p_desconexo.adicionaAresta('a3', 'C', 'E')
        self.g_p_desconexo.adicionaAresta('a4', 'P', 'C')
        self.g_p_desconexo.adicionaAresta('a5', 'P', 'C')
        self.g_p_desconexo.adicionaAresta('a6', 'T', 'C')
        self.g_p_desconexo.adicionaAresta('a7', 'M', 'C')
        self.g_p_desconexo.adicionaAresta('a8', 'M', 'T')
        self.g_p_desconexo.adicionaAresta('a9', 'T', 'Z')

        self.grafoDesconexo1 = MeuGrafo(['A', 'B', 'C', 'D', 'E'])
        self.grafoDesconexo1.adicionaAresta('a1', 'A', 'E')
        self.grafoDesconexo1.adicionaAresta('a2', 'E', 'B')
        self.grafoDesconexo1.adicionaAresta('a3', 'E', 'C')
        self.grafoDesconexo1.adicionaAresta('a4', 'C', 'A')

        #################### GRAFOS TESTE DFS ####################

        # Grafo Paraiba DFS partindo de J
        self.g_p_DFS_J = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_DFS_J.adicionaAresta('a1', 'J', 'C')
        self.g_p_DFS_J.adicionaAresta('a2', 'C', 'E')
        self.g_p_DFS_J.adicionaAresta('a4', 'P', 'C')
        self.g_p_DFS_J.adicionaAresta('a6', 'T', 'C')
        self.g_p_DFS_J.adicionaAresta('a8', 'M', 'T')
        self.g_p_DFS_J.adicionaAresta('a9', 'T', 'Z')

        # Grafo Roteiro2 DFS partindo de K
        self.g_Roteiro2_DFS_K = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
        self.g_Roteiro2_DFS_K.adicionaAresta('a4', 'K', 'G')
        self.g_Roteiro2_DFS_K.adicionaAresta('a2', 'A', 'G')
        self.g_Roteiro2_DFS_K.adicionaAresta('a1', 'A', 'B')
        self.g_Roteiro2_DFS_K.adicionaAresta('a11', 'F', 'B')
        self.g_Roteiro2_DFS_K.adicionaAresta('a10', 'H', 'F')
        self.g_Roteiro2_DFS_K.adicionaAresta('a13', 'B', 'C')
        self.g_Roteiro2_DFS_K.adicionaAresta('a14', 'C', 'D')
        self.g_Roteiro2_DFS_K.adicionaAresta('a15', 'D', 'E')
        self.g_Roteiro2_DFS_K.adicionaAresta('a3', 'A', 'J')
        self.g_Roteiro2_DFS_K.adicionaAresta('a7', 'J', 'I')

        #################### GRAFOS TESTE BFS ####################

        # Grafo da Paraíba BFS partindo de C
        self.g_p_BFS_C = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_BFS_C.adicionaAresta('a1', 'J', 'C')
        self.g_p_BFS_C.adicionaAresta('a2', 'C', 'E')
        self.g_p_BFS_C.adicionaAresta('a4', 'P', 'C')
        self.g_p_BFS_C.adicionaAresta('a6', 'T', 'C')
        self.g_p_BFS_C.adicionaAresta('a7', 'M', 'C')
        self.g_p_BFS_C.adicionaAresta('a9', 'T', 'Z')

        # Grafo Roteiro2 BFS partindo de F
        self.g_Roteiro2_BFS_F = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
        self.g_Roteiro2_BFS_F.adicionaAresta('a10', 'H', 'F')
        self.g_Roteiro2_BFS_F.adicionaAresta('a11', 'F', 'B')
        self.g_Roteiro2_BFS_F.adicionaAresta('a9', 'G', 'H')
        self.g_Roteiro2_BFS_F.adicionaAresta('a2', 'A', 'G')
        self.g_Roteiro2_BFS_F.adicionaAresta('a4', 'K', 'G')
        self.g_Roteiro2_BFS_F.adicionaAresta('a6', 'J', 'G')
        self.g_Roteiro2_BFS_F.adicionaAresta('a8', 'G', 'I')
        self.g_Roteiro2_BFS_F.adicionaAresta('a13', 'B', 'C')
        self.g_Roteiro2_BFS_F.adicionaAresta('a16', 'D', 'B')
        self.g_Roteiro2_BFS_F.adicionaAresta('a17', 'B', 'E')

        #################### GRAFOS ACÍCLICOS ####################

        self.grafoAciclico1 = MeuGrafo(['1', '2', '3', '4', '5', '6'])
        self.grafoAciclico1.adicionaAresta('a1', '1', '4')
        self.grafoAciclico1.adicionaAresta('a2', '2', '4')
        self.grafoAciclico1.adicionaAresta('a3', '3', '4')
        self.grafoAciclico1.adicionaAresta('a4', '4', '5')
        self.grafoAciclico1.adicionaAresta('a5', '5', '6')

        self.grafoAciclico2 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])
        self.grafoAciclico2.adicionaAresta('a1', 'A', 'C')
        self.grafoAciclico2.adicionaAresta('a2', 'C', 'E')
        self.grafoAciclico2.adicionaAresta('a3', 'E', 'B')
        self.grafoAciclico2.adicionaAresta('a4', 'E', 'F')
        self.grafoAciclico2.adicionaAresta('a5', 'F', 'D')

        self.grafoAciclico3 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.grafoAciclico3.adicionaAresta('a1', 'A', 'B')
        self.grafoAciclico3.adicionaAresta('a2', 'B', 'D')
        self.grafoAciclico3.adicionaAresta('a3', 'B', 'F')
        self.grafoAciclico3.adicionaAresta('a4', 'A', 'C')
        self.grafoAciclico3.adicionaAresta('a5', 'C', 'G')
        self.grafoAciclico3.adicionaAresta('a6', 'A', 'E')

        #################### GRAFOS BIPARTIDOS ####################

        self.grafoBipartido1 = MeuGrafo(['1', '2', '3', '4', '5', '6'])
        self.grafoBipartido1.adicionaAresta('a1', '1', '4')
        self.grafoBipartido1.adicionaAresta('a2', '1', '5')
        self.grafoBipartido1.adicionaAresta('a3', '1', '6')
        self.grafoBipartido1.adicionaAresta('a4', '2', '4')
        self.grafoBipartido1.adicionaAresta('a5', '2', '5')
        self.grafoBipartido1.adicionaAresta('a6', '2', '6')
        self.grafoBipartido1.adicionaAresta('a7', '3', '4')
        self.grafoBipartido1.adicionaAresta('a8', '3', '5')
        self.grafoBipartido1.adicionaAresta('a9', '3', '6')

        ##################### TESTES CAMINHO EULERIANO ###################

        self.grafoEuleriano1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.grafoEuleriano1.adicionaAresta('a1', 'A', 'B')
        self.grafoEuleriano1.adicionaAresta('a2', 'B', 'C')
        self.grafoEuleriano1.adicionaAresta('a3', 'C', 'D')
        self.grafoEuleriano1.adicionaAresta('a4', 'D', 'A')

        self.grafoEuleriano2 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.grafoEuleriano2.adicionaAresta('a1', 'A', 'B')
        self.grafoEuleriano2.adicionaAresta('a2', 'B', 'C')
        self.grafoEuleriano2.adicionaAresta('a3', 'C', 'A')
        self.grafoEuleriano2.adicionaAresta('a4', 'A', 'G')
        self.grafoEuleriano2.adicionaAresta('a5', 'G', 'C')
        self.grafoEuleriano2.adicionaAresta('a6', 'C', 'D')
        self.grafoEuleriano2.adicionaAresta('a7', 'D', 'G')
        self.grafoEuleriano2.adicionaAresta('a8', 'G', 'F')
        self.grafoEuleriano2.adicionaAresta('a9', 'F', 'D')
        self.grafoEuleriano2.adicionaAresta('a10', 'D', 'E')
        self.grafoEuleriano2.adicionaAresta('a11', 'E', 'F')
        self.grafoEuleriano2.adicionaAresta('a12', 'F', 'A')

        self.grafoEuleriano3 = MeuGrafo(['A', 'B', 'C', 'D', 'E'])
        self.grafoEuleriano3.adicionaAresta('a1', 'A', 'B')
        self.grafoEuleriano3.adicionaAresta('a2', 'B', 'C')
        self.grafoEuleriano3.adicionaAresta('a3', 'C', 'A')
        self.grafoEuleriano3.adicionaAresta('a4', 'A', 'D')
        self.grafoEuleriano3.adicionaAresta('a5', 'D', 'C')
        self.grafoEuleriano3.adicionaAresta('a6', 'C', 'E')
        self.grafoEuleriano3.adicionaAresta('a7', 'E', 'D')

        self.grafoEuleriano4 = MeuGrafo(['A', 'B', 'C'])
        self.grafoEuleriano4.adicionaAresta('a1', 'A', 'B')
        self.grafoEuleriano4.adicionaAresta('a2', 'A', 'C')

        self.grafoEuleriano5 = MeuGrafo(['A', 'B', 'C', 'D', 'E'])
        self.grafoEuleriano5.adicionaAresta('a1', 'A', 'B')
        self.grafoEuleriano5.adicionaAresta('a2', 'B', 'C')
        self.grafoEuleriano5.adicionaAresta('a3', 'C', 'A')
        self.grafoEuleriano5.adicionaAresta('a4', 'A', 'D')
        self.grafoEuleriano5.adicionaAresta('a5', 'D', 'E')
        self.grafoEuleriano5.adicionaAresta('a6', 'E', 'A')

        #################### TESTE WARSHALL ####################

        self.grafoWarshall1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.grafoWarshall1.adicionaAresta('a1', 'A', 'C')
        self.grafoWarshall1.adicionaAresta('a2', 'A', 'B')
        self.grafoWarshall1.adicionaAresta('a3', 'B', 'C')
        self.grafoWarshall1.adicionaAresta('a4', 'C', 'A')
        self.grafoWarshall1.adicionaAresta('a5', 'C', 'D')

        self.grafoWarshall2 = MeuGrafo(['0', '1', '2', '3', '4'])
        self.grafoWarshall2.adicionaAresta('a1', '0', '1')
        self.grafoWarshall2.adicionaAresta('a2', '1', '2')
        self.grafoWarshall2.adicionaAresta('a3', '1', '3')
        self.grafoWarshall2.adicionaAresta('a4', '2', '3')
        self.grafoWarshall2.adicionaAresta('a5', '3', '4')
        self.grafoWarshall2.adicionaAresta('a6', '2', '4')
        self.grafoWarshall2.adicionaAresta('a7', '3', '0')

        self.grafoWarshall3 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.grafoWarshall3.adicionaAresta('a1', 'A', 'A')
        self.grafoWarshall3.adicionaAresta('a2', 'A', 'D')
        self.grafoWarshall3.adicionaAresta('a3', 'B', 'D')
        self.grafoWarshall3.adicionaAresta('a4', 'C', 'A')
        self.grafoWarshall3.adicionaAresta('a5', 'D', 'B')

    def test_warshall(self):
        self.assertEqual(self.grafoWarshall1.warshall(), [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]])
        self.assertEqual(self.grafoWarshall2.warshall(), [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]])
        self.assertEqual(self.grafoWarshall3.warshall(), [[1, 1, 0, 1], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]])
        self.assertEqual(self.grafoEuleriano1.warshall(), [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
        self.assertEqual(self.grafoEuleriano2.warshall(), [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]])
        self.assertEqual(self.grafoSimples1.warshall(), [[0, 1, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]])
        self.assertEqual(self.grafoSimples2.warshall(), [[0, 1, 1, 1, 1], [0, 0, 0, 1, 1], [0, 1, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]])
        self.assertEqual(self.grafoSimples3.warshall(), [[0, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]])
        self.assertEqual(self.grafoAciclico1.warshall(), [[0, 0, 0, 1, 1, 1], [0, 0, 0, 1, 1, 1], [0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]])
        self.assertEqual(self.grafoAciclico2.warshall(), [[0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1], [0, 0, 0, 1, 0, 0]])
        self.assertEqual(self.grafoAciclico3.warshall(), [[0, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])
        self.assertEqual(self.grafoComArestasParalelas1.warshall(), [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]])
        self.assertEqual(self.grafoComArestasParalelas2.warshall(), [[0, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1], [0, 0, 0, 0]])
        self.assertEqual(self.g_p.warshall(), [[0, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0]])




