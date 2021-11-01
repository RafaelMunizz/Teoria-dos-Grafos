from bibgrafo.grafo_matriz_adj_dir import GrafoMatrizAdjacenciaDirecionado
from bibgrafo.grafo_exceptions import *
from copy import deepcopy, copy

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def verticesAdjacentes(self, V=''):
        '''
        Provê uma lista de todas os vertices adjacentes a determinado vertice.
        :return: Uma lista com os vértices adjacentes possiveis.
        '''
        matriz = self.matrizModificada()

        verticesAdjacentes = []

        for i in matriz:
            if i[1] == V:
                verticesAdjacentes.append(i[2])

        return verticesAdjacentes

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N: raise VerticeInvalidoException("Vértice não existe")

        indiceVertice = self.posicaoVertice(V)
        grau = 0

        for i in range(len(self.N)):
            if self.M[i][indiceVertice] != {}: grau += 1

        return grau

    def matrizModificada(self):
        '''
        :param: grafo.
        :return: Uma matriz que representa o grafo de outra forma, com rótulo, v1, v2 e peso.
        Ex:
        [['a1', 'A', 'B', 3], ['a2', 'A', 'C', 4], ['a3', 'A', 'D', 5], ['a4', 'B', 'G', 5], ...
        '''

        # Listas que servirão para criação da matriz final.
        rotulos = []
        pesos = []
        v1 = []
        v2 = []
        matrizModificada = [] # Matriz final

        for i in range(len(self.N)):
            for j in range(len(self.N)):

                if self.M[i][j]:

                    rotulo = list(self.M[i][j].keys())[0] # Extraindo rótulo da posição matriz[i][j]

                    rotulos.append(rotulo) # Rótulo
                    pesos.append(self.M[i][j][rotulo].getPeso()) # Peso do rótulo
                    v1.append(self.N[i]) # Vértice 1
                    v2.append(self.N[j]) # Vértice 2

        # Adicionando as informações recolhidas numa só matriz
        for k in range(len(rotulos)):
            aux = []

            # Identificador da ordem da aresta. Será utilizado
            # para organizar os arcos na posição correta, pois eles
            # aparecem em ordens aleatórias. Ex: a1, a2, a13, a15, a7 ...
            aux.append(int(rotulos[k][1:]))

            aux.append(rotulos[k])
            aux.append(v1[k])
            aux.append(v2[k])
            aux.append(pesos[k])
            matrizModificada.append(aux)

        # Colocando arcos na ordem correta com ajuda
        # do primeiro elemento, que é o identificador
        matrizModificada.sort()

        # Removendo o identificador
        for l in matrizModificada:
            del l[0]

        return matrizModificada

    def pesoArco(self, v1, v2):
        '''
        :param: Vértices 1 e 2.
        :return: Peso do arco formado por V1-V2, caso ele exista.
        '''

        matriz = self.matrizModificada()

        # Ex: i = [['a1', 'A', 'B', 1]
        for i in matriz:
            if i[1] == v1 and i[2] == v2:
                return i[3] # Peso

        return False

    def pegarRotulo(self, v1, v2):
        '''
        :param: Vértices 1 e 2.
        :return: Rótulo do arco formado por V1-V2, caso ele exista.
        '''

        matriz = self.matrizModificada()

        # Ex: i = [['a1', 'A', 'B', 1]
        for i in matriz:
            if i[1] == v1 and i[2] == v2:
                return i[0] # Rotulo

        return False

    def matrizAdjacenciaComPesos(self):
        '''
        Modifica o grafo para que ele se transforme em uma matriz composta pelo peso do arco e 0.
        :param grafo: O grafo que será transformado.
        :return: Uma matriz. Ex: [[3, 0, 0, 5], [0, 4, 0, 7], [2, 0, 0, 4], [0, 3, 3, 0]]
        '''

        matriz = []

        for i in range(len(self.M)):
            aux = []
            for j in range(len(self.M[0])):

                if self.M[i][j]:
                    aux.append(self.pesoArco(self.N[i], self.N[j]))
                else:
                    aux.append(0)

            matriz.append(aux)

        return matriz

    def matrizAdjacenciaBinaria(self):
        '''
        Modifica o grafo para que ele se transforme em uma matriz composta apenas de 1 e 0.
        :param grafo: Uma cópia do grafo que será transformado.
        :return: Uma matriz. Ex: [[1, 0, 0, 1], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]]
        '''

        matriz = []

        for i in range(len(self.M)):
            aux = []
            for j in range(len(self.M[0])):

                if self.M[i][j]:
                    aux.append(1)
                else:
                    aux.append(0)

            matriz.append(aux)

        return matriz

    def warshall(self):
        '''
        Utiliza o algoritmo de warshall para criar uma matriz formada de 1 e 0 com base em uma matriz inicial.
        :param : O grafo.
        :return: A matriz alcançabilidade formada por 0 e 1. Ex: [[1, 1, 0, 1], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]]
        '''

        matrizAlcancabilidade = self.matrizAdjacenciaBinaria()

        for i in range(len(self.N)):
            for j in range(len(self.N)):

                if matrizAlcancabilidade[j][i] == 1:

                    for k in range(len(self.N)):

                        matrizAlcancabilidade[j][k] = max(matrizAlcancabilidade[j][k], matrizAlcancabilidade[i][k])

        return matrizAlcancabilidade

    def imprimirMatriz(self, matriz):
        '''
        imprime o grafo de uma forma mais visível para o usuário.
        :param matriz: Uma matriz formada por 0 e 1.
        Ex:
        :entrada: [[1, 1, 0, 1], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]].
        :saída:  |A|B|C|D|
                A|1 1 0 1
                B|0 1 0 1
                C|1 1 0 1
                D|0 1 0 1
        '''

        print(" ",end='|')
        for k in range(len(self.N)):
            print(self.N[k], end='|')
        print()

        for i in range(len(matriz)):
            print(self.N[i], end='|')

            for j in range(len(matriz[0])):
                print(matriz[i][j], end=' ')

            print()

    def posicaoVertice(self, V):
        '''
        :param: Vértice.
        :return: Posição do vértice na lista de vértices (self.N).
        '''

        for i in range(len(self.N)):
            if self.N[i] == V:
                return i

        return False

    def colocarArestas(self, listaVertices):
        '''
        Provê uma lista com as arestas adicionadas a uma lista anteriormente com vértices apenas.
        :param V: Uma lista com vértices. Ex: ['A', 'J', 'K', 'G', 'H']
        :return: Uma lista com vértices e arestas. Ex: ['A', 'a3', 'J', 'a5', 'K', 'a4', 'G', 'a9', 'H']
        '''

        pares = []  # Formando pares com a lista de vértices passados
        for i in range(1, len(listaVertices)):
            pares.append(listaVertices[i - 1] + '-' + listaVertices[i])

        rotulos = []  # Lista com os rótulos dos pares

        for j in pares:
            rotulos.append(self.pegarRotulo(j[0], j[2]))

        listaFinal = []  # Lista com vértices e arestas (Um por índice)
        for k in range(len(listaVertices)):  # Colocando um vértice e uma aresta por vez
            listaFinal.append(listaVertices[k])
            if len(listaVertices) - 1 != k:
                listaFinal.append(rotulos[k])

        return listaFinal

    ############### DIJKSTRA ###############

    def setComPesos(self, lista):
        '''
        Recebe uma lista com vértices e retorna set com valores.
        :param: Lista de vértices adjacentes.
        :return: set() com valores None.
        '''

        dictAux = {}
        for i in lista:
            dictAux[i] = None
        return dictAux

    def modificandoGrafoUtil(self):
        '''
        Modifica o grafo para um dicionário.
        :param: Grafo.
        :return: Grafo como um dicionário.
        '''

        matriz = []
        for i in self.N:
            aux = []
            aux.append(i)
            aux.append(self.setComPesos(self.verticesAdjacentes(i)))
            matriz.append(aux)

        matriz = dict(matriz)

        for j in matriz:
            for k in matriz[j]:
                matriz[j][k] = self.pesoArco(j, k)

        return matriz

    def dijkstra(self, origem, destino):
        '''
        Utiliza o algoritmo de Dijkstra para criar uma lista com o menor caminho.
        :param : O grafo, o vértice de origem e o de destino.
        :return: Uma lista com o menor caminho.
        Ex: De 'A' para 'I': ['A', 'a2', 'C', 'a6', 'F', 'a11', 'I']
        '''

        novoGrafo = self.modificandoGrafoUtil()

        if origem == destino:  # Se o vertice de origem e de destino são iguais
            return [origem + '-' + destino]
        if origem not in novoGrafo:  # Se o vertice de origem não está no grafo
            return False
        if destino not in novoGrafo:  # Se o vertice de destino não está no grafo
            return False

        rotulos = {}  # Criando dicionário de rótulos
        ordem = {}  # registrar se um rotulo foi atualizado

        # Criando dicionário de rótulos
        for i in novoGrafo.keys():

            if i == origem:
                rotulos[i] = 0  # Menor distância de origem para origem é 0
            else:
                rotulos[i] = float("inf")  # Rótulos iniciais são infinitos

        naoVisitado = copy(rotulos)  # Usado no looping

        ## Início do algoritmo
        while len(naoVisitado) > 0:

            # Encontrando a key de menor rótulo
            minNo = min(naoVisitado, key=naoVisitado.get)  # minNo é o nó com o menor rótulo

            # Rótulos conectados ao menor rótulo (minNo)
            for i in novoGrafo[minNo]:

                if rotulos[i] > (rotulos[minNo] + novoGrafo[minNo][i]):
                    rotulos[i] = rotulos[minNo] + novoGrafo[minNo][i]
                    naoVisitado[i] = rotulos[minNo] + novoGrafo[minNo][i]
                    ordem[i] = minNo

            del naoVisitado[minNo]  # Uma vez que um nó é visitado, ele é excluído de naoVisitado

        temp = copy(destino)
        auxCaminho = []
        caminho = []

        while 1:
            auxCaminho.append(temp)
            if temp in ordem:
                temp = ordem[temp]  # Se ordem.has_key(temp): temp = ordem[temp]
            else:
                return False  # Se não houver caminho, retorne False

            if temp == origem:
                auxCaminho.append(temp)
                break

        for j in range(len(auxCaminho) - 1, -1, -1):
            caminho.append(auxCaminho[j])

        # O retorno do caminho é dado pela variável "caminho".
        # Caso queira retornar o peso do menor caminho deve-se retornar "str(rotulos[destino])"
        caminho = str(self.colocarArestas(caminho))

        return caminho

    ############### KANH ###############

    def kahnAlgoritmo(self):
        '''
        Utiliza o algoritmo de Kahn para criar uma lista com a ordenação topológica.
        :param : O grafo.
        :return: Uma lista dos vértices em ordenação topológica.
        Ex: ['5', '3', '7', '8', '11', '10', '9', '2']
        '''

        l = [] # lista que conterá os elementos da ordenação topológica.
        i = [] # Lista que conterá os elementos (vértices) com o grau de incidência.
        s = []  # Conjunto de vértices que não possuem arcos de entrada.

        for n in self.N: # Colocando em i todos os graus dos vértices
            i.append(self.grau(n))

        for m in range(len(i)): # Buscando os vértices fonte (grau 0) e colocando em s
            if i[m] == 0:
                s.append(m)

        while s:
            v = s[-1] # v = último elemento de s

            # Removendo último elemento de s e adicionando ele em l
            s.pop(-1)
            l.append(self.N[v])

            for o in self.verticesAdjacentes(self.N[v]):
                u = self.posicaoVertice(o) # Índice dos vértices adjacentes ao inserido em l
                i[u] -= 1 # Diminuindo o grau dos vértices adjacentes em 1 (já que seu pai foi removido)
                if i[u] == 0:  # Se o grau dos vértices adjacentes se tornar 0, adicione em s
                    s.append(u)

        return l


