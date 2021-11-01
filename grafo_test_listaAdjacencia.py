import unittest
from meu_grafo_listaAdjacencia import *
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

    def test_dfs(self):

        self.assertEqual(list(self.g_p_sem_paralelas.dfs('J').A), ['a1', 'a2', 'a3', 'a4', 'a6', 'a7'])
        self.assertEqual(list(self.g_p_sem_paralelas.dfs('C').A), ['a1', 'a2', 'a3', 'a4', 'a6', 'a7'])
        self.assertEqual(list(self.g_p_sem_paralelas.dfs('E').A), ['a2', 'a1', 'a3', 'a4', 'a6', 'a7'])
        self.assertEqual(list(self.g_p_sem_paralelas.dfs('P').A), ['a3', 'a1', 'a2', 'a4', 'a6', 'a7'])
        self.assertEqual(list(self.g_p_sem_paralelas.dfs('M').A), ['a5', 'a1', 'a2', 'a3', 'a4', 'a7'])
        self.assertEqual(list(self.g_p_sem_paralelas.dfs('T').A), ['a4', 'a1', 'a2', 'a3', 'a5', 'a7'])
        self.assertEqual(list(self.g_p_sem_paralelas.dfs('Z').A), ['a7', 'a4', 'a1', 'a2', 'a3', 'a5'])
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(list(self.g_p_sem_paralelas.dfs('A').A), [])

        self.assertEqual(self.g_p.dfs("J"), self.g_p_DFS_J)

        self.assertEqual(self.g_Roteiro2.dfs("K"), self.g_Roteiro2_DFS_K)

        self.assertEqual(list(self.g_Roteiro2.dfs('A').A), ['a1', 'a11', 'a10', 'a9', 'a4', 'a5', 'a7', 'a13', 'a14', 'a15'])
        self.assertEqual(list(self.g_Roteiro2.dfs('B').A), ['a1', 'a2', 'a4', 'a5', 'a7', 'a9', 'a10', 'a13', 'a14', 'a15'])
        self.assertEqual(list(self.g_Roteiro2.dfs('C').A), ['a13', 'a1', 'a2', 'a4', 'a5', 'a7', 'a9', 'a10', 'a16', 'a15'])
        self.assertEqual(list(self.g_Roteiro2.dfs('D').A), ['a14', 'a13', 'a1', 'a2', 'a4', 'a5', 'a7', 'a9', 'a10', 'a17'])
        self.assertEqual(list(self.g_Roteiro2.dfs('E').A), ['a15', 'a14', 'a13', 'a1', 'a2', 'a4', 'a5', 'a7', 'a9', 'a10'])
        self.assertEqual(list(self.g_Roteiro2.dfs('F').A), ['a10', 'a9', 'a2', 'a1', 'a13', 'a14', 'a15', 'a3', 'a5', 'a7'])
        self.assertEqual(list(self.g_Roteiro2.dfs('G').A), ['a2', 'a1', 'a11', 'a10', 'a13', 'a14', 'a15', 'a3', 'a5', 'a7'])
        self.assertEqual(list(self.g_Roteiro2.dfs('H').A), ['a9', 'a2', 'a1', 'a11', 'a13', 'a14', 'a15', 'a3', 'a5', 'a7'])
        self.assertEqual(list(self.g_Roteiro2.dfs('I').A), ['a7', 'a3', 'a1', 'a11', 'a10', 'a9', 'a4', 'a13', 'a14', 'a15'])
        self.assertEqual(list(self.g_Roteiro2.dfs('J').A), ['a3', 'a1', 'a11', 'a10', 'a9', 'a4', 'a8', 'a13', 'a14', 'a15'])
        self.assertEqual(list(self.g_Roteiro2.dfs('K').A), ['a4', 'a2', 'a1', 'a11', 'a10', 'a13', 'a14', 'a15', 'a3', 'a7'])
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(list(self.g_Roteiro2.dfs('X').A), [])

    def test_bfs(self):
        self.assertEqual(list(self.g_p.bfs('J').A),['a1', 'a2', 'a4', 'a6', 'a7', 'a9'])
        self.assertEqual(list(self.g_p.bfs('C').A),['a1', 'a2', 'a4', 'a6', 'a7', 'a9'])
        self.assertEqual(list(self.g_p.bfs('E').A),['a2', 'a1', 'a4', 'a6', 'a7', 'a9'])
        self.assertEqual(list(self.g_p.bfs('P').A),['a4', 'a1', 'a2', 'a6', 'a7', 'a9'])
        self.assertEqual(list(self.g_p.bfs('M').A),['a7', 'a8', 'a1', 'a2', 'a4', 'a9'])
        self.assertEqual(list(self.g_p.bfs('T').A),['a6', 'a8', 'a9', 'a1', 'a2', 'a4'])
        self.assertEqual(list(self.g_p.bfs('Z').A),['a9', 'a6', 'a8', 'a1', 'a2', 'a4'])
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(list(self.g_p.dfs('A').A), [])

        self.assertEqual(self.g_p.bfs("C"), self.g_p_BFS_C)

        self.assertEqual(self.g_Roteiro2.bfs("F"), self.g_Roteiro2_BFS_F)

        self.assertEqual(list(self.g_Roteiro2.bfs('A').A),['a1', 'a2', 'a3', 'a11', 'a13', 'a16', 'a17', 'a10', 'a4', 'a8'])
        self.assertEqual(list(self.g_Roteiro2.bfs('B').A),['a1', 'a11', 'a12', 'a13', 'a16', 'a17', 'a3', 'a4', 'a8', 'a9'])
        self.assertEqual(list(self.g_Roteiro2.bfs('C').A),['a13', 'a14', 'a1', 'a11', 'a12', 'a17', 'a3', 'a4', 'a8', 'a9'])
        self.assertEqual(list(self.g_Roteiro2.bfs('D').A),['a14', 'a15', 'a16', 'a1', 'a11', 'a12', 'a3', 'a4', 'a8', 'a9'])
        self.assertEqual(list(self.g_Roteiro2.bfs('E').A),['a15', 'a17', 'a14', 'a1', 'a11', 'a12', 'a3', 'a4', 'a8', 'a9'])
        self.assertEqual(list(self.g_Roteiro2.bfs('F').A),['a10', 'a11', 'a9', 'a2', 'a4', 'a6', 'a8', 'a13', 'a16', 'a17'])
        self.assertEqual(list(self.g_Roteiro2.bfs('G').A),['a2', 'a4', 'a6', 'a8', 'a9', 'a12', 'a11', 'a13', 'a16', 'a17'])
        self.assertEqual(list(self.g_Roteiro2.bfs('H').A),['a9', 'a10', 'a2', 'a4', 'a6', 'a8', 'a12', 'a13', 'a16', 'a17'])
        self.assertEqual(list(self.g_Roteiro2.bfs('I').A),['a7', 'a8', 'a3', 'a5', 'a1', 'a11', 'a13', 'a16', 'a17', 'a10'])
        self.assertEqual(list(self.g_Roteiro2.bfs('J').A),['a3', 'a5', 'a6', 'a7', 'a1', 'a11', 'a13', 'a16', 'a17', 'a10'])
        self.assertEqual(list(self.g_Roteiro2.bfs('K').A),['a4', 'a5', 'a2', 'a8', 'a9', 'a12', 'a11', 'a13', 'a16', 'a17'])
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(list(self.g_Roteiro2.bfs('X').A), [])

    def test_ha_ciclo(self):
        self.assertEqual(self.g_p.ha_ciclo(), ['C', 'a2', 'E', 'a3', 'C']) # Paraiba
        self.assertEqual(self.g_p_sem_paralelas.ha_ciclo(), ['C', 'a4', 'T', 'a6', 'M', 'a5', 'C']) # PB sem paralelas
        self.assertEqual(self.g_c.ha_ciclo(), ['J', 'a1', 'C', 'a4', 'E', 'a2', 'J']) # Completo
        self.assertEqual(self.g_l1.ha_ciclo(), ['A', 'a1', 'A']) # Laços
        self.assertEqual(self.g_l3.ha_ciclo(), ['C', 'a2', 'C']) # Laços
        self.assertEqual(self.grafoDesconexo1.ha_ciclo(), ['A', 'a1', 'E', 'a3', 'C', 'a4', 'A']) # Desconexo
        self.assertFalse(self.grafoAciclico1.ha_ciclo()) # Aciclico
        self.assertFalse(self.grafoAciclico2.ha_ciclo()) # Aciclico
        self.assertFalse(self.grafoAciclico3.ha_ciclo()) # Aciclico
        self.assertEqual(self.grafoSimples1.ha_ciclo(), ['B', 'a2', 'D', 'a4', 'C', 'a3', 'B']) # Simples
        self.assertEqual(self.grafoSimples2.ha_ciclo(), ['M', 'a1', 'O', 'a3', 'N', 'a4', 'P', 'a2', 'M']) # Simples
        self.assertEqual(self.grafoSimples3.ha_ciclo(), ['1', 'a1', '2', 'a8', '3', 'a2', '1']) # Simples

    def test_caminho(self):
        self.assertEqual(self.g_p.caminho(1), ['J', 'a1', 'C'])
        self.assertEqual(self.g_p.caminho(2), ['J', 'a1', 'C', 'a2', 'E'])
        self.assertEqual(self.g_p.caminho(3), ['J', 'a1', 'C', 'a6', 'T', 'a8', 'M'])
        self.assertEqual(self.g_p.caminho(4), ['J', 'a1', 'C', 'a7', 'M', 'a8', 'T', 'a9', 'Z'])
        self.assertFalse(self.g_p.caminho(5))
        self.assertEqual(self.g_Roteiro2.caminho(1), ['A', 'a1', 'B'])
        self.assertEqual(self.g_Roteiro2.caminho(2), ['A', 'a2', 'G', 'a12', 'B'])
        self.assertEqual(self.g_Roteiro2.caminho(3), ['A', 'a3', 'J', 'a6', 'G', 'a12', 'B'])
        self.assertEqual(self.g_Roteiro2.caminho(4), ['A', 'a2', 'G', 'a9', 'H', 'a10', 'F', 'a11', 'B'])
        self.assertEqual(self.g_Roteiro2.caminho(5), ['A', 'a3', 'J', 'a6', 'G', 'a9', 'H', 'a10', 'F', 'a11', 'B'])
        self.assertEqual(self.g_Roteiro2.caminho(6), ['A', 'a3', 'J', 'a5', 'K', 'a4', 'G', 'a9', 'H', 'a10', 'F', 'a11', 'B'])
        self.assertEqual(self.g_Roteiro2.caminho(7), ['A', 'a2', 'G', 'a9', 'H', 'a10', 'F', 'a11', 'B', 'a17', 'E', 'a15', 'D', 'a14', 'C'])
        self.assertEqual(self.g_Roteiro2.caminho(8), ['A', 'a3', 'J', 'a5', 'K', 'a4', 'G', 'a9', 'H', 'a10', 'F', 'a11', 'B', 'a16', 'D', 'a14', 'C'])
        self.assertEqual(self.g_Roteiro2.caminho(9), ['A', 'a3', 'J', 'a5', 'K', 'a4', 'G', 'a9', 'H', 'a10', 'F', 'a11', 'B', 'a17', 'E', 'a15', 'D', 'a14', 'C'])
        self.assertFalse(self.g_Roteiro2.caminho(10))
        self.assertEqual(self.grafoComArestasParalelas1.caminho(1), ['A', 'a1', 'B'])
        self.assertEqual(self.grafoComArestasParalelas1.caminho(2), ['A', 'a3', 'E', 'a4', 'C'])
        self.assertEqual(self.grafoComArestasParalelas1.caminho(3), ['A', 'a1', 'B', 'a5', 'D', 'a6', 'C'])
        self.assertEqual(self.grafoComArestasParalelas1.caminho(4), ['A', 'a3', 'E', 'a4', 'C', 'a6', 'D', 'a5', 'B'])
        self.assertFalse(self.grafoComArestasParalelas1.caminho(5))
        self.assertFalse(self.grafoComArestasParalelas1.caminho(6))
        self.assertEqual(self.grafoSimples3.caminho(1), ['1', 'a1', '2'])
        self.assertEqual(self.grafoSimples3.caminho(2), ['1', 'a2', '3', 'a8', '2'])
        self.assertEqual(self.grafoSimples3.caminho(3), ['1', 'a2', '3', 'a6', '5', 'a9', '2'])
        self.assertEqual(self.grafoSimples3.caminho(4), ['1', 'a2', '3', 'a5', '4', 'a7', '5', 'a9', '2'])
        self.assertEqual(self.grafoSimples3.caminho(5), ['1', 'a2', '3', 'a5', '4', 'a7', '5', 'a10', '6', 'a12', '2'])
        self.assertFalse(self.grafoSimples3.caminho(6))

    def test_conexo(self):
        self.assertTrue(self.g_p.conexo())
        self.assertTrue(self.g_p_sem_paralelas.conexo())
        self.assertTrue(self.g_c.conexo())
        self.assertTrue(self.grafoCompleto1.conexo())
        self.assertFalse(self.g_l1.conexo())
        self.assertFalse(self.g_l2.conexo())
        self.assertFalse(self.g_l3.conexo())
        self.assertFalse(self.g_d.conexo())
        self.assertFalse(self.g_p_desconexo.conexo())
        self.assertFalse(self.grafoDesconexo1.conexo())
        self.assertTrue(self.grafoAciclico1.conexo())
        self.assertTrue(self.grafoAciclico2.conexo())
        self.assertTrue(self.grafoAciclico3.conexo())
        self.assertTrue(self.grafoBipartido1.conexo())

