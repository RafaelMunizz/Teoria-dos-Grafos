from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from meu_grafo_matriz_adjacencia_dir import MeuGrafo
from copy import copy

############################ TESTES grafo_test ################################

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

####################### ENGENHARIA DE COMPUTAÇÃO #######################

grafoEngComp = MeuGrafo(['11', '12', '13', '14', '15', '16', '17',
                              '21', '22', '23', '24', '25', '26', '27',
                              '31', '32', '33', '34', '35', '36',
                              '41', '42', '43', '44', '45',
                              '51', '52', '53', '54', '55',
                              '61', '62', '63', '64', '65',
                              '71', '72', '73', '74', '75',
                              '81', '82', '83', '84', '85',
                              '91', '92', '93', '94',
                              '101', '102', '103'])

grafoEngComp.adicionaAresta('a1', '11', '21')
grafoEngComp.adicionaAresta('a2', '14', '24')
grafoEngComp.adicionaAresta('a3', '14', '25')
grafoEngComp.adicionaAresta('a4', '14', '34')
grafoEngComp.adicionaAresta('a5', '14', '35')
grafoEngComp.adicionaAresta('a6', '15', '24')
grafoEngComp.adicionaAresta('a7', '15', '25')
grafoEngComp.adicionaAresta('a8', '15', '34')
grafoEngComp.adicionaAresta('a9', '15', '35')
grafoEngComp.adicionaAresta('a10', '16', '26')
grafoEngComp.adicionaAresta('a11', '21', '31')
grafoEngComp.adicionaAresta('a12', '21', '41')
grafoEngComp.adicionaAresta('a13', '24', '33')
grafoEngComp.adicionaAresta('a14', '24', '43')
grafoEngComp.adicionaAresta('a15', '24', '44')
grafoEngComp.adicionaAresta('a16', '24', '53')
grafoEngComp.adicionaAresta('a17', '24', '54')
grafoEngComp.adicionaAresta('a18', '24', '72')
grafoEngComp.adicionaAresta('a19', '26', '36')
grafoEngComp.adicionaAresta('a20', '31', '51')
grafoEngComp.adicionaAresta('a21', '31', '52')
grafoEngComp.adicionaAresta('a22', '31', '64')
grafoEngComp.adicionaAresta('a23', '34', '63')
grafoEngComp.adicionaAresta('a24', '34', '81')
grafoEngComp.adicionaAresta('a25', '35', '63')
grafoEngComp.adicionaAresta('a26', '35', '81')
grafoEngComp.adicionaAresta('a27', '36', '44')
grafoEngComp.adicionaAresta('a28', '36', '45')
grafoEngComp.adicionaAresta('a29', '36', '55')
grafoEngComp.adicionaAresta('a30', '43', '62')
grafoEngComp.adicionaAresta('a31', '44', '55')
grafoEngComp.adicionaAresta('a32', '44', '93')
grafoEngComp.adicionaAresta('a33', '45', '93')
grafoEngComp.adicionaAresta('a34', '51', '61')
grafoEngComp.adicionaAresta('a35', '52', '75')
grafoEngComp.adicionaAresta('a36', '54', '81')
grafoEngComp.adicionaAresta('a37', '55', '65')
grafoEngComp.adicionaAresta('a38', '61', '84')
grafoEngComp.adicionaAresta('a39', '61', '94')
grafoEngComp.adicionaAresta('a40', '63', '73')
grafoEngComp.adicionaAresta('a41', '64', '75')
grafoEngComp.adicionaAresta('a42', '64', '84')
grafoEngComp.adicionaAresta('a43', '73', '82')
grafoEngComp.adicionaAresta('a44', '74', '83')
grafoEngComp.adicionaAresta('a45', '75', '85')
grafoEngComp.adicionaAresta('a46', '75', '94')
grafoEngComp.adicionaAresta('a47', '83', '92')
grafoEngComp.adicionaAresta('a48', '92', '103')

########################### CONSTRUÇÃO DE EDIFÍCIOS ###########################

grafoConstEdif = MeuGrafo(['11', '12', '13', '14', '15', '16', '17', '18',
                                '21', '22', '23', '24', '25', '26', '27',
                                '31', '32', '33', '34', '35', '36', '37', '38',
                                '41', '42', '43', '44', '45', '46', '47',
                                '51', '52', '53', '54', '55', '56', '57', '58',
                                '61', '62', '63', '64', '65', '66', '67', '68',
                                '71', '72', '73'])

grafoConstEdif.adicionaAresta('a1', '15', '21')
grafoConstEdif.adicionaAresta('a2', '14', '23')
grafoConstEdif.adicionaAresta('a3', '11', '24')
grafoConstEdif.adicionaAresta('a4', '17', '24')
grafoConstEdif.adicionaAresta('a5', '15', '25')
grafoConstEdif.adicionaAresta('a6', '17', '26')
grafoConstEdif.adicionaAresta('a7', '17', '27')
grafoConstEdif.adicionaAresta('a8', '15', '32')
grafoConstEdif.adicionaAresta('a9', '21', '32')
grafoConstEdif.adicionaAresta('a10', '21', '33')
grafoConstEdif.adicionaAresta('a11', '25', '33')
grafoConstEdif.adicionaAresta('a12', '15', '34')
grafoConstEdif.adicionaAresta('a13', '11', '35')
grafoConstEdif.adicionaAresta('a14', '27', '35')
grafoConstEdif.adicionaAresta('a15', '26', '36')
grafoConstEdif.adicionaAresta('a16', '23', '37')
grafoConstEdif.adicionaAresta('a17', '24', '38')
grafoConstEdif.adicionaAresta('a18', '17', '41')
grafoConstEdif.adicionaAresta('a19', '21', '41')
grafoConstEdif.adicionaAresta('a20', '17', '42')
grafoConstEdif.adicionaAresta('a21', '21', '42')
grafoConstEdif.adicionaAresta('a22', '23', '43')
grafoConstEdif.adicionaAresta('a23', '24', '44')
grafoConstEdif.adicionaAresta('a24', '36', '45')
grafoConstEdif.adicionaAresta('a25', '37', '45')
grafoConstEdif.adicionaAresta('a26', '17', '46')
grafoConstEdif.adicionaAresta('a27', '32', '46')
grafoConstEdif.adicionaAresta('a28', '11', '47')
grafoConstEdif.adicionaAresta('a29', '37', '47')
grafoConstEdif.adicionaAresta('a30', '37', '51')
grafoConstEdif.adicionaAresta('a31', '43', '51')
grafoConstEdif.adicionaAresta('a32', '45', '51')
grafoConstEdif.adicionaAresta('a33', '46', '51')
grafoConstEdif.adicionaAresta('a34', '41', '52')
grafoConstEdif.adicionaAresta('a35', '42', '52')
grafoConstEdif.adicionaAresta('a36', '45', '52')
grafoConstEdif.adicionaAresta('a37', '46', '52')
grafoConstEdif.adicionaAresta('a38', '17', '53')
grafoConstEdif.adicionaAresta('a39', '32', '53')
grafoConstEdif.adicionaAresta('a40', '47', '54')
grafoConstEdif.adicionaAresta('a41', '17', '55')
grafoConstEdif.adicionaAresta('a42', '32', '55')
grafoConstEdif.adicionaAresta('a43', '46', '56')
grafoConstEdif.adicionaAresta('a44', '43', '57')
grafoConstEdif.adicionaAresta('a45', '31', '62')
grafoConstEdif.adicionaAresta('a46', '44', '62')
grafoConstEdif.adicionaAresta('a47', '22', '64')
grafoConstEdif.adicionaAresta('a48', '27', '64')
grafoConstEdif.adicionaAresta('a49', '33', '64')
grafoConstEdif.adicionaAresta('a50', '36', '64')
grafoConstEdif.adicionaAresta('a51', '47', '65')
grafoConstEdif.adicionaAresta('a52', '22', '66')
grafoConstEdif.adicionaAresta('a53', '31', '67')

############################## LIC. EM FÍSICA ##############################

grafoFisica = MeuGrafo(['11', '12', '13', '14', '15', '16', '17',
                             '21', '22', '23', '24', '25', '26', '27',
                             '31', '32', '33', '34', '35', '36', '37',
                             '41', '42', '43', '44', '45', '46',
                             '51', '52', '53', '54', '55', '56', '57',
                             '61', '62', '63', '64', '65', '66', '67',
                             '71', '72', '73', '74', '75', '76',
                             '81', '82', '83', '84', '85', '86', '87'])

grafoFisica.adicionaAresta('a1', '11', '21')
grafoFisica.adicionaAresta('a2', '12', '21')
grafoFisica.adicionaAresta('a3', '11', '22')
grafoFisica.adicionaAresta('a4', '12', '22')
grafoFisica.adicionaAresta('a5', '12', '23')
grafoFisica.adicionaAresta('a6', '12', '24')
grafoFisica.adicionaAresta('a7', '14', '24')
grafoFisica.adicionaAresta('a8', '15', '25')
grafoFisica.adicionaAresta('a9', '21', '31')
grafoFisica.adicionaAresta('a10', '23', '31')
grafoFisica.adicionaAresta('a11', '21', '32')
grafoFisica.adicionaAresta('a12', '22', '32')
grafoFisica.adicionaAresta('a13', '23', '33')
grafoFisica.adicionaAresta('a14', '31', '41')
grafoFisica.adicionaAresta('a15', '31', '42')
grafoFisica.adicionaAresta('a16', '32', '42')
grafoFisica.adicionaAresta('a17', '33', '45')
grafoFisica.adicionaAresta('a18', '31', '46')
grafoFisica.adicionaAresta('a19', '41', '51')
grafoFisica.adicionaAresta('a20', '45', '51')
grafoFisica.adicionaAresta('a21', '41', '52')
grafoFisica.adicionaAresta('a22', '42', '52')
grafoFisica.adicionaAresta('a23', '45', '53')
grafoFisica.adicionaAresta('a24', '31', '54')
grafoFisica.adicionaAresta('a25', '43', '55')
grafoFisica.adicionaAresta('a26', '51', '61')
grafoFisica.adicionaAresta('a27', '51', '62')
grafoFisica.adicionaAresta('a28', '52', '62')
grafoFisica.adicionaAresta('a29', '21', '63')
grafoFisica.adicionaAresta('a30', '53', '63')
grafoFisica.adicionaAresta('a31', '51', '64')
grafoFisica.adicionaAresta('a32', '56', '66')
grafoFisica.adicionaAresta('a33', '61', '71')
grafoFisica.adicionaAresta('a34', '41', '72')
grafoFisica.adicionaAresta('a35', '45', '72')
grafoFisica.adicionaAresta('a36', '66', '73')
grafoFisica.adicionaAresta('a37', '31', '74')
grafoFisica.adicionaAresta('a38', '43', '74')
grafoFisica.adicionaAresta('a39', '65', '81')
grafoFisica.adicionaAresta('a40', '74', '82')
grafoFisica.adicionaAresta('a41', '73', '83')
grafoFisica.adicionaAresta('a42', '54', '84')
grafoFisica.adicionaAresta('a43', '71', '84')
grafoFisica.adicionaAresta('a44', '16', '85')
grafoFisica.adicionaAresta('a45', '25', '85')
grafoFisica.adicionaAresta('a46', '21', '57')
grafoFisica.adicionaAresta('a47', '43', '57')
grafoFisica.adicionaAresta('a48', '31', '67')
grafoFisica.adicionaAresta('a49', '57', '67')
grafoFisica.adicionaAresta('a50', '41', '76')
grafoFisica.adicionaAresta('a51', '67', '76')
grafoFisica.adicionaAresta('a52', '51', '86')
grafoFisica.adicionaAresta('a53', '76', '86')

########################### LIC. EM MATEMÁTICA ###########################

grafoMatematica = MeuGrafo(['11', '12', '13', '14', '15', '16', '17',
                                 '21', '22', '23', '24', '25', '26', '27',
                                 '31', '32', '33', '34', '35', '36',
                                 '41', '42', '43', '44', '45', '46',
                                 '51', '52', '53', '54', '55', '56', '57',
                                 '61', '62', '63', '64', '65', '66', '67',
                                 '71', '72', '73', '74', '75', '76', '77',
                                 '81', '82', '83', '84', '85', '86', '87'])

grafoMatematica.adicionaAresta('a1', '11', '21')
grafoMatematica.adicionaAresta('a2', '11', '22')
grafoMatematica.adicionaAresta('a3', '13', '22')
grafoMatematica.adicionaAresta('a4', '16', '26')
grafoMatematica.adicionaAresta('a5', '21', '31')
grafoMatematica.adicionaAresta('a6', '22', '32')
grafoMatematica.adicionaAresta('a7', '12', '33')
grafoMatematica.adicionaAresta('a8', '12', '34')
grafoMatematica.adicionaAresta('a9', '21', '41')
grafoMatematica.adicionaAresta('a10', '23', '41')
grafoMatematica.adicionaAresta('a11', '23', '42')
grafoMatematica.adicionaAresta('a12', '32', '42')
grafoMatematica.adicionaAresta('a13', '36', '43')
grafoMatematica.adicionaAresta('a14', '34', '44')
grafoMatematica.adicionaAresta('a15', '27', '45')
grafoMatematica.adicionaAresta('a16', '33', '51')
grafoMatematica.adicionaAresta('a17', '12', '52')
grafoMatematica.adicionaAresta('a18', '32', '53')
grafoMatematica.adicionaAresta('a19', '44', '54')
grafoMatematica.adicionaAresta('a20', '44', '55')
grafoMatematica.adicionaAresta('a21', '44', '57')
grafoMatematica.adicionaAresta('a22', '51', '61')
grafoMatematica.adicionaAresta('a23', '52', '62')
grafoMatematica.adicionaAresta('a24', '32', '63')
grafoMatematica.adicionaAresta('a25', '54', '64')
grafoMatematica.adicionaAresta('a26', '46', '65')
grafoMatematica.adicionaAresta('a27', '57', '67')
grafoMatematica.adicionaAresta('a28', '42', '71')
grafoMatematica.adicionaAresta('a29', '22', '72')
grafoMatematica.adicionaAresta('a30', '41', '73')
grafoMatematica.adicionaAresta('a31', '42', '73')
grafoMatematica.adicionaAresta('a32', '64', '74')
grafoMatematica.adicionaAresta('a33', '65', '75')
grafoMatematica.adicionaAresta('a34', '67', '77')
grafoMatematica.adicionaAresta('a35', '62', '81')
grafoMatematica.adicionaAresta('a36', '75', '82')
grafoMatematica.adicionaAresta('a37', '32', '83')
grafoMatematica.adicionaAresta('a38', '74', '84')
grafoMatematica.adicionaAresta('a39', '77', '87')

############################### TELEMÁTICA ###############################

grafoTelematica = MeuGrafo(['11', '12', '13', '14', '15', '16', '17',
                                 '21', '22', '23', '24', '25', '26', '27',
                                 '31', '32', '33', '34', '35', '36', '37',
                                 '41', '42', '43', '44', '45', '46', '47',
                                 '51', '52', '53', '54', '55', '56', '57',
                                 '61', '62', '63', '64', '65', '66'])

grafoTelematica.adicionaAresta('a1', '11', '21')
grafoTelematica.adicionaAresta('a2', '12', '22')
grafoTelematica.adicionaAresta('a3', '16', '22')
grafoTelematica.adicionaAresta('a4', '12', '23')
grafoTelematica.adicionaAresta('a5', '16', '23')
grafoTelematica.adicionaAresta('a6', '13', '24')
grafoTelematica.adicionaAresta('a7', '16', '26')
grafoTelematica.adicionaAresta('a8', '21', '31')
grafoTelematica.adicionaAresta('a9', '26', '32')
grafoTelematica.adicionaAresta('a10', '22', '33')
grafoTelematica.adicionaAresta('a11', '23', '33')
grafoTelematica.adicionaAresta('a12', '26', '33')
grafoTelematica.adicionaAresta('a13', '14', '34')
grafoTelematica.adicionaAresta('a14', '25', '35')
grafoTelematica.adicionaAresta('a15', '21', '36')
grafoTelematica.adicionaAresta('a16', '24', '36')
grafoTelematica.adicionaAresta('a17', '31', '41')
grafoTelematica.adicionaAresta('a18', '31', '42')
grafoTelematica.adicionaAresta('a19', '32', '43')
grafoTelematica.adicionaAresta('a20', '32', '44')
grafoTelematica.adicionaAresta('a21', '33', '44')
grafoTelematica.adicionaAresta('a22', '33', '45')
grafoTelematica.adicionaAresta('a23', '21', '46')
grafoTelematica.adicionaAresta('a24', '34', '46')
grafoTelematica.adicionaAresta('a25', '41', '51')
grafoTelematica.adicionaAresta('a26', '41', '52')
grafoTelematica.adicionaAresta('a27', '44', '53')
grafoTelematica.adicionaAresta('a28', '44', '54')
grafoTelematica.adicionaAresta('a29', '37', '55')
grafoTelematica.adicionaAresta('a30', '41', '55')
grafoTelematica.adicionaAresta('a31', '44', '55')
grafoTelematica.adicionaAresta('a32', '42', '61')
grafoTelematica.adicionaAresta('a33', '51', '61')
grafoTelematica.adicionaAresta('a34', '53', '62')

grafoArvore = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
grafoArvore.adicionaAresta('a1', 'A', 'B')
grafoArvore.adicionaAresta('a2', 'A', 'C')
grafoArvore.adicionaAresta('a3', 'B', 'D')
grafoArvore.adicionaAresta('a4', 'B', 'E')
grafoArvore.adicionaAresta('a5', 'C', 'F')
grafoArvore.adicionaAresta('a6', 'C', 'G')

grafoTM = MeuGrafo(['0','1','2','3','4','5','6','7'])
grafoTM.adicionaAresta('a1', '0', '1')
grafoTM.adicionaAresta('a2', '0', '2')
grafoTM.adicionaAresta('a3', '0', '3')
grafoTM.adicionaAresta('a4', '1', '2')
grafoTM.adicionaAresta('a5', '1', '6')
grafoTM.adicionaAresta('a6', '1', '5')
grafoTM.adicionaAresta('a7', '2', '5')
grafoTM.adicionaAresta('a8', '2', '6')
grafoTM.adicionaAresta('a9', '3', '5')
grafoTM.adicionaAresta('a10', '4', '6')
grafoTM.adicionaAresta('a11', '4', '7')

grafoAula = MeuGrafo(['7','3','5','11','8','2','9','10'])
grafoAula.adicionaAresta('a1', '7', '11')
grafoAula.adicionaAresta('a2', '7', '8')
grafoAula.adicionaAresta('a3', '3', '11')
grafoAula.adicionaAresta('a4', '5', '8')
grafoAula.adicionaAresta('a5', '5', '10')
grafoAula.adicionaAresta('a6', '11', '2')
grafoAula.adicionaAresta('a7', '11', '9')
grafoAula.adicionaAresta('a8', '11', '10')
grafoAula.adicionaAresta('a9', '8', '9')

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
'''
# PESO DO ARCO
print(grafoGigante.M[0][2]["a2"].getPeso())
'''
'''
y = "grafoComArestasParalelas2"
x = grafoComArestasParalelas2

print("\nself.assertEqual(self.{}.warshall(), {})".format(y, x.warshall()))
'''

print(grafoEngComp.kahnAlgoritmo())
print(grafoConstEdif.kahnAlgoritmo())
print(grafoFisica.kahnAlgoritmo())
print(grafoMatematica.kahnAlgoritmo())
print(grafoTelematica.kahnAlgoritmo())





