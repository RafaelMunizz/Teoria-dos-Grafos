import unittest
from meu_grafo_matriz_adjacencia_dir import *
from bibgrafo.grafo_exceptions import *

class TestGrafo(unittest.TestCase):

    def setUp(self):

        #################### GRAFOS ATIVIDADES ####################

        self.g_Roteiro2 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'])
        self.g_Roteiro2.adicionaAresta('a1', 'A', 'B', 2)
        self.g_Roteiro2.adicionaAresta('a2', 'A', 'G', 3)
        self.g_Roteiro2.adicionaAresta('a3', 'A', 'J', 6)
        self.g_Roteiro2.adicionaAresta('a4', 'K', 'G', 4)
        self.g_Roteiro2.adicionaAresta('a5', 'K', 'J', 8)
        self.g_Roteiro2.adicionaAresta('a6', 'J', 'G', 6)
        self.g_Roteiro2.adicionaAresta('a7', 'J', 'I', 4)
        self.g_Roteiro2.adicionaAresta('a8', 'G', 'I', 1)
        self.g_Roteiro2.adicionaAresta('a9', 'G', 'H', 5)
        self.g_Roteiro2.adicionaAresta('a10', 'H', 'F', 3)
        self.g_Roteiro2.adicionaAresta('a11', 'F', 'B', 2)
        self.g_Roteiro2.adicionaAresta('a12', 'B', 'G', 7)
        self.g_Roteiro2.adicionaAresta('a13', 'B', 'C', 5)
        self.g_Roteiro2.adicionaAresta('a14', 'C', 'D', 3)
        self.g_Roteiro2.adicionaAresta('a15', 'D', 'E', 4)
        self.g_Roteiro2.adicionaAresta('a16', 'D', 'B', 6)
        self.g_Roteiro2.adicionaAresta('a17', 'B', 'E', 3)

        self.grafoEuleriano2 = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.grafoEuleriano2.adicionaAresta('a1', 'A', 'B', 2)
        self.grafoEuleriano2.adicionaAresta('a2', 'B', 'C', 3)
        self.grafoEuleriano2.adicionaAresta('a3', 'C', 'A', 4)
        self.grafoEuleriano2.adicionaAresta('a4', 'A', 'G', 7)
        self.grafoEuleriano2.adicionaAresta('a5', 'G', 'C', 5)
        self.grafoEuleriano2.adicionaAresta('a6', 'C', 'D', 4)
        self.grafoEuleriano2.adicionaAresta('a7', 'D', 'G', 3)
        self.grafoEuleriano2.adicionaAresta('a8', 'G', 'F', 6)
        self.grafoEuleriano2.adicionaAresta('a9', 'F', 'D', 4)
        self.grafoEuleriano2.adicionaAresta('a10', 'D', 'E', 1)
        self.grafoEuleriano2.adicionaAresta('a11', 'E', 'F', 2)
        self.grafoEuleriano2.adicionaAresta('a12', 'F', 'A', 3)

        # Criado para testes com algoritmo de Dijkstra
        self.grafoGigante = MeuGrafo(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T'])
        self.grafoGigante.adicionaAresta('a1', 'A', 'B', 3)
        self.grafoGigante.adicionaAresta('a2', 'A', 'C', 4)
        self.grafoGigante.adicionaAresta('a3', 'A', 'D', 5)
        self.grafoGigante.adicionaAresta('a4', 'B', 'G', 5)
        self.grafoGigante.adicionaAresta('a5', 'B', 'F', 6)
        self.grafoGigante.adicionaAresta('a6', 'C', 'F', 3)
        self.grafoGigante.adicionaAresta('a7', 'C', 'E', 6)
        self.grafoGigante.adicionaAresta('a8', 'C', 'D', 3)
        self.grafoGigante.adicionaAresta('a9', 'D', 'E', 3)
        self.grafoGigante.adicionaAresta('a10', 'G', 'I', 2)
        self.grafoGigante.adicionaAresta('a11', 'F', 'I', 3)
        self.grafoGigante.adicionaAresta('a12', 'F', 'H', 4)
        self.grafoGigante.adicionaAresta('a13', 'E', 'H', 2)
        self.grafoGigante.adicionaAresta('a14', 'E', 'K', 6)
        self.grafoGigante.adicionaAresta('a15', 'E', 'J', 3)
        self.grafoGigante.adicionaAresta('a16', 'I', 'L', 5)
        self.grafoGigante.adicionaAresta('a17', 'H', 'L', 10)
        self.grafoGigante.adicionaAresta('a18', 'K', 'L', 3)
        self.grafoGigante.adicionaAresta('a19', 'K', 'O', 5)
        self.grafoGigante.adicionaAresta('a20', 'K', 'N', 2)
        self.grafoGigante.adicionaAresta('a21', 'J', 'N', 4)
        self.grafoGigante.adicionaAresta('a22', 'L', 'M', 6)
        self.grafoGigante.adicionaAresta('a23', 'O', 'M', 4)
        self.grafoGigante.adicionaAresta('a24', 'O', 'P', 4)
        self.grafoGigante.adicionaAresta('a25', 'N', 'P', 6)
        self.grafoGigante.adicionaAresta('a26', 'M', 'R', 5)
        self.grafoGigante.adicionaAresta('a27', 'M', 'Q', 9)
        self.grafoGigante.adicionaAresta('a28', 'Q', 'R', 3)
        self.grafoGigante.adicionaAresta('a29', 'Q', 'S', 2)
        self.grafoGigante.adicionaAresta('a30', 'Q', 'P', 3)
        self.grafoGigante.adicionaAresta('a31', 'P', 'T', 9)
        self.grafoGigante.adicionaAresta('a32', 'T', 'S', 1)

        ################################# GRAFOS CURSOS IFPB #################################

        ####################### ENGENHARIA DE COMPUTAÇÃO #######################

        self.grafoEngComp = MeuGrafo(['11', '12', '13', '14', '15', '16', '17',
                                      '21', '22', '23', '24', '25', '26', '27',
                                      '31', '32', '33', '34', '35', '36',
                                      '41', '42', '43', '44', '45',
                                      '51', '52', '53', '54', '55',
                                      '61', '62', '63', '64', '65',
                                      '71', '72', '73', '74', '75',
                                      '81', '82', '83', '84', '85',
                                      '91', '92', '93', '94',
                                      '101', '102', '103'])

        self.grafoEngComp.adicionaAresta('a1', '11', '21')
        self.grafoEngComp.adicionaAresta('a2', '14', '24')
        self.grafoEngComp.adicionaAresta('a3', '14', '25')
        self.grafoEngComp.adicionaAresta('a4', '14', '34')
        self.grafoEngComp.adicionaAresta('a5', '14', '35')
        self.grafoEngComp.adicionaAresta('a6', '15', '24')
        self.grafoEngComp.adicionaAresta('a7', '15', '25')
        self.grafoEngComp.adicionaAresta('a8', '15', '34')
        self.grafoEngComp.adicionaAresta('a9', '15', '35')
        self.grafoEngComp.adicionaAresta('a10', '16', '26')
        self.grafoEngComp.adicionaAresta('a11', '21', '31')
        self.grafoEngComp.adicionaAresta('a12', '21', '41')
        self.grafoEngComp.adicionaAresta('a13', '24', '33')
        self.grafoEngComp.adicionaAresta('a14', '24', '43')
        self.grafoEngComp.adicionaAresta('a15', '24', '44')
        self.grafoEngComp.adicionaAresta('a16', '24', '53')
        self.grafoEngComp.adicionaAresta('a17', '24', '54')
        self.grafoEngComp.adicionaAresta('a18', '24', '72')
        self.grafoEngComp.adicionaAresta('a19', '26', '36')
        self.grafoEngComp.adicionaAresta('a20', '31', '51')
        self.grafoEngComp.adicionaAresta('a21', '31', '52')
        self.grafoEngComp.adicionaAresta('a22', '31', '64')
        self.grafoEngComp.adicionaAresta('a23', '34', '63')
        self.grafoEngComp.adicionaAresta('a24', '34', '81')
        self.grafoEngComp.adicionaAresta('a25', '35', '63')
        self.grafoEngComp.adicionaAresta('a26', '35', '81')
        self.grafoEngComp.adicionaAresta('a27', '36', '44')
        self.grafoEngComp.adicionaAresta('a28', '36', '45')
        self.grafoEngComp.adicionaAresta('a29', '36', '55')
        self.grafoEngComp.adicionaAresta('a30', '43', '62')
        self.grafoEngComp.adicionaAresta('a31', '44', '55')
        self.grafoEngComp.adicionaAresta('a32', '44', '93')
        self.grafoEngComp.adicionaAresta('a33', '45', '93')
        self.grafoEngComp.adicionaAresta('a34', '51', '61')
        self.grafoEngComp.adicionaAresta('a35', '52', '75')
        self.grafoEngComp.adicionaAresta('a36', '54', '81')
        self.grafoEngComp.adicionaAresta('a37', '55', '65')
        self.grafoEngComp.adicionaAresta('a38', '61', '84')
        self.grafoEngComp.adicionaAresta('a39', '61', '94')
        self.grafoEngComp.adicionaAresta('a40', '63', '73')
        self.grafoEngComp.adicionaAresta('a41', '64', '75')
        self.grafoEngComp.adicionaAresta('a42', '64', '84')
        self.grafoEngComp.adicionaAresta('a43', '73', '82')
        self.grafoEngComp.adicionaAresta('a44', '74', '83')
        self.grafoEngComp.adicionaAresta('a45', '75', '85')
        self.grafoEngComp.adicionaAresta('a46', '75', '94')
        self.grafoEngComp.adicionaAresta('a47', '83', '92')
        self.grafoEngComp.adicionaAresta('a48', '92', '103')

        ########################### CONSTRUÇÃO DE EDIFÍCIOS ###########################

        self.grafoConstEdif = MeuGrafo(['11', '12', '13', '14', '15', '16', '17', '18',
                                        '21', '22', '23', '24', '25', '26', '27',
                                        '31', '32', '33', '34', '35', '36', '37', '38',
                                        '41', '42', '43', '44', '45', '46', '47',
                                        '51', '52', '53', '54', '55', '56', '57', '58',
                                        '61', '62', '63', '64', '65', '66', '67', '68',
                                        '71', '72', '73'])

        self.grafoConstEdif.adicionaAresta('a1', '15', '21')
        self.grafoConstEdif.adicionaAresta('a2', '14', '23')
        self.grafoConstEdif.adicionaAresta('a3', '11', '24')
        self.grafoConstEdif.adicionaAresta('a4', '17', '24')
        self.grafoConstEdif.adicionaAresta('a5', '15', '25')
        self.grafoConstEdif.adicionaAresta('a6', '17', '26')
        self.grafoConstEdif.adicionaAresta('a7', '17', '27')
        self.grafoConstEdif.adicionaAresta('a8', '15', '32')
        self.grafoConstEdif.adicionaAresta('a9', '21', '32')
        self.grafoConstEdif.adicionaAresta('a10', '21', '33')
        self.grafoConstEdif.adicionaAresta('a11', '25', '33')
        self.grafoConstEdif.adicionaAresta('a12', '15', '34')
        self.grafoConstEdif.adicionaAresta('a13', '11', '35')
        self.grafoConstEdif.adicionaAresta('a14', '27', '35')
        self.grafoConstEdif.adicionaAresta('a15', '26', '36')
        self.grafoConstEdif.adicionaAresta('a16', '23', '37')
        self.grafoConstEdif.adicionaAresta('a17', '24', '38')
        self.grafoConstEdif.adicionaAresta('a18', '17', '41')
        self.grafoConstEdif.adicionaAresta('a19', '21', '41')
        self.grafoConstEdif.adicionaAresta('a20', '17', '42')
        self.grafoConstEdif.adicionaAresta('a21', '21', '42')
        self.grafoConstEdif.adicionaAresta('a22', '23', '43')
        self.grafoConstEdif.adicionaAresta('a23', '24', '44')
        self.grafoConstEdif.adicionaAresta('a24', '36', '45')
        self.grafoConstEdif.adicionaAresta('a25', '37', '45')
        self.grafoConstEdif.adicionaAresta('a26', '17', '46')
        self.grafoConstEdif.adicionaAresta('a27', '32', '46')
        self.grafoConstEdif.adicionaAresta('a28', '11', '47')
        self.grafoConstEdif.adicionaAresta('a29', '37', '47')
        self.grafoConstEdif.adicionaAresta('a30', '37', '51')
        self.grafoConstEdif.adicionaAresta('a31', '43', '51')
        self.grafoConstEdif.adicionaAresta('a32', '45', '51')
        self.grafoConstEdif.adicionaAresta('a33', '46', '51')
        self.grafoConstEdif.adicionaAresta('a34', '41', '52')
        self.grafoConstEdif.adicionaAresta('a35', '42', '52')
        self.grafoConstEdif.adicionaAresta('a36', '45', '52')
        self.grafoConstEdif.adicionaAresta('a37', '46', '52')
        self.grafoConstEdif.adicionaAresta('a38', '17', '53')
        self.grafoConstEdif.adicionaAresta('a39', '32', '53')
        self.grafoConstEdif.adicionaAresta('a40', '47', '54')
        self.grafoConstEdif.adicionaAresta('a41', '17', '55')
        self.grafoConstEdif.adicionaAresta('a42', '32', '55')
        self.grafoConstEdif.adicionaAresta('a43', '46', '56')
        self.grafoConstEdif.adicionaAresta('a44', '43', '57')
        self.grafoConstEdif.adicionaAresta('a45', '31', '62')
        self.grafoConstEdif.adicionaAresta('a46', '44', '62')
        self.grafoConstEdif.adicionaAresta('a47', '22', '64')
        self.grafoConstEdif.adicionaAresta('a48', '27', '64')
        self.grafoConstEdif.adicionaAresta('a49', '33', '64')
        self.grafoConstEdif.adicionaAresta('a50', '36', '64')
        self.grafoConstEdif.adicionaAresta('a51', '47', '65')
        self.grafoConstEdif.adicionaAresta('a52', '22', '66')
        self.grafoConstEdif.adicionaAresta('a53', '31', '67')

        ############################## LIC. EM FÍSICA ##############################

        self.grafoFisica = MeuGrafo(['11', '12', '13', '14', '15', '16', '17',
                                     '21', '22', '23', '24', '25', '26', '27',
                                     '31', '32', '33', '34', '35', '36', '37',
                                     '41', '42', '43', '44', '45', '46',
                                     '51', '52', '53', '54', '55', '56', '57',
                                     '61', '62', '63', '64', '65', '66', '67',
                                     '71', '72', '73', '74', '75', '76',
                                     '81', '82', '83', '84', '85', '86', '87'])

        self.grafoFisica.adicionaAresta('a1', '11', '21')
        self.grafoFisica.adicionaAresta('a2', '12', '21')
        self.grafoFisica.adicionaAresta('a3', '11', '22')
        self.grafoFisica.adicionaAresta('a4', '12', '22')
        self.grafoFisica.adicionaAresta('a5', '12', '23')
        self.grafoFisica.adicionaAresta('a6', '12', '24')
        self.grafoFisica.adicionaAresta('a7', '14', '24')
        self.grafoFisica.adicionaAresta('a8', '15', '25')
        self.grafoFisica.adicionaAresta('a9', '21', '31')
        self.grafoFisica.adicionaAresta('a10', '23', '31')
        self.grafoFisica.adicionaAresta('a11', '21', '32')
        self.grafoFisica.adicionaAresta('a12', '22', '32')
        self.grafoFisica.adicionaAresta('a13', '23', '33')
        self.grafoFisica.adicionaAresta('a14', '31', '41')
        self.grafoFisica.adicionaAresta('a15', '31', '42')
        self.grafoFisica.adicionaAresta('a16', '32', '42')
        self.grafoFisica.adicionaAresta('a17', '33', '45')
        self.grafoFisica.adicionaAresta('a18', '31', '46')
        self.grafoFisica.adicionaAresta('a19', '41', '51')
        self.grafoFisica.adicionaAresta('a20', '45', '51')
        self.grafoFisica.adicionaAresta('a21', '41', '52')
        self.grafoFisica.adicionaAresta('a22', '42', '52')
        self.grafoFisica.adicionaAresta('a23', '45', '53')
        self.grafoFisica.adicionaAresta('a24', '31', '54')
        self.grafoFisica.adicionaAresta('a25', '43', '55')
        self.grafoFisica.adicionaAresta('a26', '51', '61')
        self.grafoFisica.adicionaAresta('a27', '51', '62')
        self.grafoFisica.adicionaAresta('a28', '52', '62')
        self.grafoFisica.adicionaAresta('a29', '21', '63')
        self.grafoFisica.adicionaAresta('a30', '53', '63')
        self.grafoFisica.adicionaAresta('a31', '51', '64')
        self.grafoFisica.adicionaAresta('a32', '56', '66')
        self.grafoFisica.adicionaAresta('a33', '61', '71')
        self.grafoFisica.adicionaAresta('a34', '41', '72')
        self.grafoFisica.adicionaAresta('a35', '45', '72')
        self.grafoFisica.adicionaAresta('a36', '66', '73')
        self.grafoFisica.adicionaAresta('a37', '31', '74')
        self.grafoFisica.adicionaAresta('a38', '43', '74')
        self.grafoFisica.adicionaAresta('a39', '65', '81')
        self.grafoFisica.adicionaAresta('a40', '74', '82')
        self.grafoFisica.adicionaAresta('a41', '73', '83')
        self.grafoFisica.adicionaAresta('a42', '54', '84')
        self.grafoFisica.adicionaAresta('a43', '71', '84')
        self.grafoFisica.adicionaAresta('a44', '16', '85')
        self.grafoFisica.adicionaAresta('a45', '25', '85')
        self.grafoFisica.adicionaAresta('a46', '21', '57')
        self.grafoFisica.adicionaAresta('a47', '43', '57')
        self.grafoFisica.adicionaAresta('a48', '31', '67')
        self.grafoFisica.adicionaAresta('a49', '57', '67')
        self.grafoFisica.adicionaAresta('a50', '41', '76')
        self.grafoFisica.adicionaAresta('a51', '67', '76')
        self.grafoFisica.adicionaAresta('a52', '51', '86')
        self.grafoFisica.adicionaAresta('a53', '76', '86')

        ########################### LIC. EM MATEMÁTICA ###########################

        self.grafoMatematica = MeuGrafo(['11', '12', '13', '14', '15', '16', '17',
                                         '21', '22', '23', '24', '25', '26', '27',
                                         '31', '32', '33', '34', '35', '36',
                                         '41', '42', '43', '44', '45', '46',
                                         '51', '52', '53', '54', '55', '56', '57',
                                         '61', '62', '63', '64', '65', '66', '67',
                                         '71', '72', '73', '74', '75', '76', '77',
                                         '81', '82', '83', '84', '85', '86', '87'])

        self.grafoMatematica.adicionaAresta('a1', '11', '21')
        self.grafoMatematica.adicionaAresta('a2', '11', '22')
        self.grafoMatematica.adicionaAresta('a3', '13', '22')
        self.grafoMatematica.adicionaAresta('a4', '16', '26')
        self.grafoMatematica.adicionaAresta('a5', '21', '31')
        self.grafoMatematica.adicionaAresta('a6', '22', '32')
        self.grafoMatematica.adicionaAresta('a7', '12', '33')
        self.grafoMatematica.adicionaAresta('a8', '12', '34')
        self.grafoMatematica.adicionaAresta('a9', '21', '41')
        self.grafoMatematica.adicionaAresta('a10', '23', '41')
        self.grafoMatematica.adicionaAresta('a11', '23', '42')
        self.grafoMatematica.adicionaAresta('a12', '32', '42')
        self.grafoMatematica.adicionaAresta('a13', '36', '43')
        self.grafoMatematica.adicionaAresta('a14', '34', '44')
        self.grafoMatematica.adicionaAresta('a15', '27', '45')
        self.grafoMatematica.adicionaAresta('a16', '33', '51')
        self.grafoMatematica.adicionaAresta('a17', '12', '52')
        self.grafoMatematica.adicionaAresta('a18', '32', '53')
        self.grafoMatematica.adicionaAresta('a19', '44', '54')
        self.grafoMatematica.adicionaAresta('a20', '44', '55')
        self.grafoMatematica.adicionaAresta('a21', '44', '57')
        self.grafoMatematica.adicionaAresta('a22', '51', '61')
        self.grafoMatematica.adicionaAresta('a23', '52', '62')
        self.grafoMatematica.adicionaAresta('a24', '32', '63')
        self.grafoMatematica.adicionaAresta('a25', '54', '64')
        self.grafoMatematica.adicionaAresta('a26', '46', '65')
        self.grafoMatematica.adicionaAresta('a27', '57', '67')
        self.grafoMatematica.adicionaAresta('a28', '42', '71')
        self.grafoMatematica.adicionaAresta('a29', '22', '72')
        self.grafoMatematica.adicionaAresta('a30', '41', '73')
        self.grafoMatematica.adicionaAresta('a31', '42', '73')
        self.grafoMatematica.adicionaAresta('a32', '64', '74')
        self.grafoMatematica.adicionaAresta('a33', '65', '75')
        self.grafoMatematica.adicionaAresta('a34', '67', '77')
        self.grafoMatematica.adicionaAresta('a35', '62', '81')
        self.grafoMatematica.adicionaAresta('a36', '75', '82')
        self.grafoMatematica.adicionaAresta('a37', '32', '83')
        self.grafoMatematica.adicionaAresta('a38', '74', '84')
        self.grafoMatematica.adicionaAresta('a39', '77', '87')

        ############################### TELEMÁTICA ###############################

        self.grafoTelematica = MeuGrafo(['11', '12', '13', '14', '15', '16', '17',
                                         '21', '22', '23', '24', '25', '26', '27',
                                         '31', '32', '33', '34', '35', '36', '37',
                                         '41', '42', '43', '44', '45', '46', '47',
                                         '51', '52', '53', '54', '55', '56', '57',
                                         '61', '62', '63', '64', '65', '66'])

        self.grafoTelematica.adicionaAresta('a1', '11', '21')
        self.grafoTelematica.adicionaAresta('a2', '12', '22')
        self.grafoTelematica.adicionaAresta('a3', '16', '22')
        self.grafoTelematica.adicionaAresta('a4', '12', '23')
        self.grafoTelematica.adicionaAresta('a5', '16', '23')
        self.grafoTelematica.adicionaAresta('a6', '13', '24')
        self.grafoTelematica.adicionaAresta('a7', '16', '26')
        self.grafoTelematica.adicionaAresta('a8', '21', '31')
        self.grafoTelematica.adicionaAresta('a9', '26', '32')
        self.grafoTelematica.adicionaAresta('a10', '22', '33')
        self.grafoTelematica.adicionaAresta('a11', '23', '33')
        self.grafoTelematica.adicionaAresta('a12', '26', '33')
        self.grafoTelematica.adicionaAresta('a13', '14', '34')
        self.grafoTelematica.adicionaAresta('a14', '25', '35')
        self.grafoTelematica.adicionaAresta('a15', '21', '36')
        self.grafoTelematica.adicionaAresta('a16', '24', '36')
        self.grafoTelematica.adicionaAresta('a17', '31', '41')
        self.grafoTelematica.adicionaAresta('a18', '31', '42')
        self.grafoTelematica.adicionaAresta('a19', '32', '43')
        self.grafoTelematica.adicionaAresta('a20', '32', '44')
        self.grafoTelematica.adicionaAresta('a21', '33', '44')
        self.grafoTelematica.adicionaAresta('a22', '33', '45')
        self.grafoTelematica.adicionaAresta('a23', '21', '46')
        self.grafoTelematica.adicionaAresta('a24', '34', '46')
        self.grafoTelematica.adicionaAresta('a25', '41', '51')
        self.grafoTelematica.adicionaAresta('a26', '41', '52')
        self.grafoTelematica.adicionaAresta('a27', '44', '53')
        self.grafoTelematica.adicionaAresta('a28', '44', '54')
        self.grafoTelematica.adicionaAresta('a29', '37', '55')
        self.grafoTelematica.adicionaAresta('a30', '41', '55')
        self.grafoTelematica.adicionaAresta('a31', '44', '55')
        self.grafoTelematica.adicionaAresta('a32', '42', '61')
        self.grafoTelematica.adicionaAresta('a33', '51', '61')
        self.grafoTelematica.adicionaAresta('a34', '53', '62')

    '''
    def test_dijkstra(self):
        self.assertEqual(self.grafoGigante.dijkstra('A', 'S'), ['A','a3','D','a9','E','a15','J','a21','N','a25','P','a31','T','a32','S'])
        self.assertEqual(self.grafoGigante.dijkstra('C', 'F'), ['C', 'a6', 'F'])
        self.assertEqual(self.grafoGigante.dijkstra('E', 'M'), ['E', 'a14', 'K', 'a18', 'L', 'a22', 'M'])
        self.assertEqual(self.grafoGigante.dijkstra('D', 'H'), ['D', 'a9', 'E', 'a13', 'H'])
        self.assertEqual(self.grafoGigante.dijkstra('C', 'O'), ['C', 'a7', 'E', 'a14', 'K', 'a19', 'O'])
        self.assertEqual(self.grafoGigante.dijkstra('D', 'N'), ['D', 'a9', 'E', 'a15', 'J', 'a21', 'N'])
        self.assertEqual(self.g_Roteiro2.dijkstra('A', 'G'), ['A', 'a2', 'G'])
        self.assertEqual(self.g_Roteiro2.dijkstra('C', 'F'), ['C', 'a14', 'D', 'a16', 'B', 'a12', 'G', 'a9', 'H', 'a10', 'F'])
        self.assertEqual(self.g_Roteiro2.dijkstra('E', 'A'), False)
        self.assertEqual(self.g_Roteiro2.dijkstra('A', 'F'), ['A', 'a2', 'G', 'a9', 'H', 'a10', 'F'])
        self.assertEqual(self.g_Roteiro2.dijkstra('B', 'E'), ['B', 'a17', 'E'])
        self.assertEqual(self.grafoEuleriano2.dijkstra('A', 'H'), False)
        self.assertEqual(self.grafoEuleriano2.dijkstra('C', 'G'), ['C', 'a6', 'D', 'a7', 'G'])
        self.assertEqual(self.grafoEuleriano2.dijkstra('B', 'F'), ['B', 'a2', 'C', 'a6', 'D', 'a10', 'E', 'a11', 'F'])
        '''

    def test_Kahn(self):
        self.assertEqual(self.grafoEngComp.kahnAlgoritmo(), ['102', '101', '91', '74', '83', '92', '103', '71', '42', '32', '27', '23', '22', '17', '16', '26', '36', '45',
         '15', '14', '35', '34', '63', '73', '82', '25', '24', '72', '54', '81', '53', '44', '93', '55', '65', '43',
         '62', '33', '13', '12', '11', '21', '41', '31', '64', '52', '75', '85', '51', '61', '94', '84'])
        self.assertEqual(self.grafoConstEdif.kahnAlgoritmo(), ['73', '72', '71', '68', '63', '61', '58', '31', '67', '22', '66', '18', '17', '27', '26', '36', '16', '15',
         '34', '25', '21', '42', '41', '33', '64', '32', '55', '53', '46', '56', '14', '23', '43', '57', '37', '45',
         '52', '51', '13', '12', '11', '47', '65', '54', '35', '24', '44', '62', '38'])
        self.assertEqual(self.grafoFisica.kahnAlgoritmo(), ['87', '75', '65', '81', '56', '66', '73', '83', '44', '43', '55', '37', '36', '35', '34', '27', '26', '17',
         '16', '15', '25', '85', '14', '13', '12', '24', '23', '33', '45', '53', '11', '22', '21', '57', '63', '32',
         '31', '67', '74', '82', '54', '46', '42', '41', '76', '72', '52', '51', '86', '64', '62', '61', '71', '84'])
        self.assertEqual(self.grafoMatematica.kahnAlgoritmo(), ['86', '85', '76', '66', '56', '46', '65', '75', '82', '36', '43', '35', '27', '45', '25', '24', '23', '17',
         '16', '26', '15', '14', '13', '12', '52', '62', '81', '34', '44', '57', '67', '77', '87', '55', '54', '64',
         '74', '84', '33', '51', '61', '11', '22', '72', '32', '83', '63', '53', '42', '71', '21', '41', '73', '31'])
        self.assertEqual(self.grafoTelematica.kahnAlgoritmo(), ['66', '65', '64', '63', '57', '56', '47', '37', '27', '25', '35', '17', '16', '26', '32', '43', '15', '14',
         '34', '13', '24', '12', '23', '22', '33', '45', '44', '54', '53', '62', '11', '21', '46', '36', '31', '42',
         '41', '55', '52', '51', '61'])

