import unittest
from meu_grafo_matriz_adjacencia_nao_dir import *
from bibgrafo.grafo_exceptions import *

class TestGrafo(unittest.TestCase):

    def setUp(self):

        #################### GRAFOS ATIVIDADES ####################

        # Grafo da Paraíba (Roteiro 1)
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C')
        self.g_p.adicionaAresta('a2', 'C', 'E')
        self.g_p.adicionaAresta('a3', 'C', 'E')
        self.g_p.adicionaAresta('a4', 'P', 'C')
        self.g_p.adicionaAresta('a5', 'P', 'C')
        self.g_p.adicionaAresta('a6', 'T', 'C')
        self.g_p.adicionaAresta('a7', 'M', 'C')
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
        self.grafoComArestasParalelas1.adicionaAresta('a2', 'A', 'B')
        self.grafoComArestasParalelas1.adicionaAresta('a3', 'A', 'E')
        self.grafoComArestasParalelas1.adicionaAresta('a4', 'E', 'C')
        self.grafoComArestasParalelas1.adicionaAresta('a5', 'B', 'D')
        self.grafoComArestasParalelas1.adicionaAresta('a6', 'D', 'C')

        self.grafoComArestasParalelas2 = MeuGrafo(['1', '2', '3', '4'])
        self.grafoComArestasParalelas2.adicionaAresta('a1', '1', '2')
        self.grafoComArestasParalelas2.adicionaAresta('a2', '2', '3')
        self.grafoComArestasParalelas2.adicionaAresta('a3', '2', '3')
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


    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adicionaAresta('a10', 'J', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', '', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', 'A', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('aa-bb')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('a1', 'J', 'C')

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(), ['J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z', 'M-Z'])
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), [])
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), [])

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), set(['a1']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')), set(['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), set(['a7', 'a8']))
        self.assertEqual(set(self.g_l2.arestas_sobre_vertice('B')), set(['a1', 'a2', 'a3']))
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('C')), set())
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('A')), set(['asd']))
        with self.assertRaises(VerticeInvalidoException):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))

    def test_caminhoEuleriano(self):
        self.assertTrue(self.grafoEuleriano1.caminhoEuleriano(), ['A', 'a1', 'B', 'a2', 'C', 'a3', 'D', 'a4', 'A'])
        self.assertTrue(self.grafoEuleriano2.caminhoEuleriano(), ['A', 'a1', 'B', 'a2', 'C', 'a3', 'A', 'a12', 'F', 'a9', 'D', 'a6', 'C', 'a5', 'G', 'a7', 'D', 'a10', 'E', 'a11', 'F', 'a8', 'G', 'a4', 'A'])
        self.assertTrue(self.grafoEuleriano3.caminhoEuleriano(), ['A', 'a1', 'B', 'a2', 'C', 'a3', 'A', 'a4', 'D', 'a5', 'C', 'a6', 'E', 'a7', 'D'])
        self.assertTrue(self.grafoEuleriano4.caminhoEuleriano(), ['B', 'a1', 'A', 'a2', 'C'])
        self.assertTrue(self.grafoEuleriano5.caminhoEuleriano(), ['A', 'a1', 'B', 'a2', 'C', 'a3', 'A', 'a4', 'D', 'a5', 'E', 'a6', 'A'])
        self.assertTrue(self.grafoSimples2.caminhoEuleriano(), ['P', 'a2', 'M', 'a1', 'O', 'a3', 'N', 'a4', 'P', 'a5', 'Q'])
        self.assertTrue(self.grafoSimples3.caminhoEuleriano(), ['1', 'a1', '2', 'a8', '3', 'a2', '1', 'a3', '4', 'a5', '3', 'a6', '5', 'a9', '2', 'a12', '6', 'a11', '4', 'a7', '5', 'a10', '6', 'a4', '1'])
        self.assertTrue(self.grafoCompleto1.caminhoEuleriano(), ['P', 'a4', 'Q', 'a8', 'R', 'a3', 'P', 'a2', 'S', 'a7', 'Q', 'a5', 'T', 'a6', 'R', 'a9', 'S', 'a10', 'T', 'a1', 'P'])
        self.assertTrue(self.g_Roteiro2.caminhoEuleriano(), ['A', 'a1', 'B', 'a13', 'C', 'a14', 'D', 'a16', 'B', 'a17', 'E', 'a15', 'D', 'a11', 'F', 'a10', 'H', 'a9', 'G', 'a2', 'A', 'a3', 'J', 'a6', 'G', 'a8', 'I', 'a7', 'J', 'a5', 'K', 'a4', 'G', 'a12', 'B'])
        self.assertFalse(self.grafoSimples1.caminhoEuleriano())
        self.assertFalse(self.g_p.caminhoEuleriano())
        self.assertFalse(self.g_c.caminhoEuleriano())
        self.assertFalse(self.g_l2.caminhoEuleriano())
        self.assertFalse(self.g_l3.caminhoEuleriano())