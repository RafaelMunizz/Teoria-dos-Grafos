from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_exceptions import *
from copy import deepcopy

class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''

        lista = []
        for i in range(len(self.M)):
            for j in range(len(self.M)):

                if self.M[i][j] != '-':
                    if not self.M[i][j] and i != j:

                        lista.append(self.N[i] + '-' + self.N[j])

        return lista

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

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in range(len(self.M)):
            if self.M[i][i]:
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N: raise VerticeInvalidoException("Vértice não existe")

        indiceVertice = self.N.index(V)
        grau = 0

        for i in range(len(self.N)):
            if self.M[indiceVertice][i] and self.M[i][indiceVertice]:

                if len(self.M[indiceVertice][i]) > 0 and self.M[indiceVertice][i] != '-': # LINHA
                    grau += len(self.M[indiceVertice][i])
                if len(self.M[i][indiceVertice]) > 0 and self.M[i][indiceVertice] != '-': # COLUNA
                    grau += len(self.M[i][indiceVertice])

        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in range(len(self.M)):
            for j in range(len(self.M[i])):

                if len(self.M[i][j]) > 1:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        if V not in self.N: raise VerticeInvalidoException("Vértice não existe")

        indiceVertice = self.N.index(V)

        matrizArestas = []
        for i in range(len(self.N)):
            if self.M[indiceVertice][i] and self.M[i][indiceVertice]:

                if self.M[indiceVertice][i] != '-':  # LINHA
                    matrizArestas.append(list(self.M[indiceVertice][i].keys()))
                if self.M[i][indiceVertice] != '-':  # COLUNA
                    matrizArestas.append(list(self.M[i][indiceVertice].keys()))

        arestasVertice = []
        for arestas in matrizArestas:
            for aresta in arestas:
                arestasVertice.append(aresta)

        return arestasVertice

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''

        for i in self.N:
            if len(self.arestas_sobre_vertice(i)) != (len(self.N) - 1):
                return False
        return True

    def conexo(self):
        '''
        Verifica se o grafo é conexo
        :return: Bool representando se o grafo é conexo
        '''

        listadfs = list()
        dfs = self.dfs(self.N[0])
        l = list()
        for linha in self.M:
            for coluna in linha:
                if coluna != "-" and coluna != {}:
                    for aresta in coluna:
                        l.append(coluna[aresta].getV1())
                        l.append(coluna[aresta].getV2())
        listadfs.append(l)
        for dfs in listadfs:
            for vertice in self.N:
                if not (vertice in dfs):
                    return False
        return True

    def ponte(self, N):
        '''
        Verifica se determinado vertice é uma ponte dentro do grafo.
        :return: bool representando se é ponte
        '''
        l = list()
        for linha in self._matriz:
            for coluna in linha:
                if coluna != "-" and coluna != {}:
                    l.append(coluna[1])
                    l.append(coluna[2])
        for vertice in N:
            if not (vertice in l):
                return True
        return False

    def listaRotulos(self):
        '''
        Prove uma lista com as arestas do grafo.
        Lista do tipo [A0,A1,...,An]
        :return: lista.
        '''
        la = list()
        for lin in range(len(self.M)):
            for col in range(len(self.M)):
                if self.M[lin][col] != "-" and self.M[lin][col] != {}:
                    for aresta in self.M[lin][col]:
                        la.append(aresta)
        return la

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

    ############### DFS ###############

    def dfs(self, V='', **kwargs):
        '''
        Provê uma árvore (um grafo) que contém apenas as arestas do dfs
        :param V: O vértice a de onde se inicia o caminho
        :return: Um grafo do tipo árvore
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N:
            raise VerticeInvalidoException

        try:
            self.acdfs = kwargs["dfs"]
        except:
            self.acdfs = True

        if self.acdfs == True:
            self._arvoredfs = MeuGrafo(self.N)
            self.arestas_dfs = []
            self.acdfs = False

        for coluna in self.M[self.N.index(V)]:
            if coluna != "-" and coluna != {}:
                for aresta in coluna:
                    if ((coluna[aresta].getV1() not in self.arestas_dfs) or (
                            coluna[aresta].getV2() not in self.arestas_dfs)) \
                            and (coluna[aresta].getV1() != coluna[aresta].getV2()):
                        self._arvoredfs.adicionaAresta(aresta, coluna[aresta].getV1(), coluna[aresta].getV2())
                        self.arestas_dfs.append(coluna[aresta].getV1())
                        self.arestas_dfs.append(coluna[aresta].getV2())
                        self.dfs(coluna[aresta].getV2() if coluna[aresta].getV2() != V else coluna[aresta].getV1(),
                                 **{"dfs": False})

        return self._arvoredfs

    ############### CAMINHO EULERIANO ###############

    def caminhoEuleriano(self):
        '''
        Verifica se o grafo possui um caminho euleriano.
        Caso possua, prove uma lista do tipo [V0,A0 .. Vn,An].
        :return: False ou lista com caminho.
        '''
        impar, lvi = self.ehEuleriano()
        if (not impar) or (not self.conexo()):
            return False

        self._caminho = list()
        self._matriz = self.matrizArestas()
        self._arestas = self.listaRotulos()

        # Escolhe o vertice de inicio do caminho
        if lvi != []:
            Vi = lvi[0]
        elif lvi == []:
            Vi = 0
        self._caminho.append(self.N[Vi])
        Eh_caminho = self.buscarCaminho(Vi)

        return self._caminho

    def ehEuleriano(self):
        '''
        Verifica se cada vertice é de grau impar e a quantidade
        de vertices impares no grafo
        :return: True, lista de vertices impar se verdadeiro
                 False, None se falso
        '''
        total = 0
        i = 0
        lvi = list()
        while (total <= 2) and (i <= len(self.N) - 1):
            grau = 0
            grau += self.grau(self.N[i])
            if grau % 2 == 1:
                total += 1
                lvi.append(i)
            i += 1
        if total == 0 or total == 2:
            return True, lvi
        else:
            return False, None

    def buscarCaminho(self, v):
        '''
        Gera o caminho eureliano.
        :return: bool referente a existencia do caminho.
        '''
        grau = self.grauMatriz(self.N[v], self._matriz)
        if grau == 0:
            return True
        elif grau == 1:
            for c in range(len(self.M[v])):
                if v < c:
                    linha, coluna = v, c
                else:
                    linha, coluna = c, v
                if self._arestas != [] and self._matriz[linha][coluna] != "-" and self._matriz[linha][coluna] != {}:
                    aresta = self._matriz[linha][coluna]
                    self._arestas.remove(aresta[0])
                    self._caminho.append(aresta[0])
                    self._caminho.append(aresta[1] if aresta[1] != self.N[v] else aresta[2])
                    self._matriz[linha][coluna] = "-"
                    self.buscarCaminho(self.N.index(aresta[1] if aresta[1] != self.N[v] else aresta[2]))
        else:
            __N = self.N.copy()
            for c in range(len(self.M[v])):
                if v < c:
                    linha, coluna = v, c
                else:
                    linha, coluna = c, v
                if self._arestas != [] and self._matriz[linha][coluna] != "-" and self._matriz[linha][coluna] != {}:
                    aresta = self._matriz[linha][coluna]
                    self._matriz[linha][coluna] = "-"
                    if self.grauMatriz(self.N[v], self._matriz) == 0: __N.remove(self.N[v])
                    if not self.ponte(__N):
                        self._arestas.remove(aresta[0])
                        self._caminho.append(aresta[0])
                        self._caminho.append(aresta[1] if aresta[1] != self.N[v] else aresta[2])
                        self.buscarCaminho(self.N.index(aresta[1] if aresta[1] != self.N[v] else aresta[2]))
                    elif self.grauMatriz(aresta[1] if aresta[1] != self.N[v] else aresta[2], self._matriz) != 0:
                        self._arestas.remove(aresta[0])
                        self._caminho.append(aresta[0])
                        self._caminho.append(aresta[1] if aresta[1] != self.N[v] else aresta[2])
                        self.buscarCaminho(self.N.index(aresta[1] if aresta[1] != self.N[v] else aresta[2]))

                    else:
                        self._matriz[linha][coluna] = aresta
                        self._arestas.append(aresta[0])
                        __N.append(self.N[v])
        return False

    def grauMatriz(self, V, M):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :param M: Matriz a analisada a partir de V
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N:
            raise VerticeInvalidoException
        cont = 0
        for l in range(len(M)):
            for c in range(len(M)):
                if M[l][c] != "-" and V in M[l][c]:
                    cont += 1
        return cont

    def matrizArestas(self):
        '''
        Prove uma matriz com as arestas do grafo.
        :return: Matriz com as arestas do grafo
        '''
        matriz = []
        for l in range(len(self.M)):
            matriz.append([])
            for c in range(len(self.M)):
                if self.M[l][c] != "-" and self.M[l][c] != {}:
                    for aresta in self.M[l][c]:
                        matriz[l].append([aresta, self.M[l][c][aresta].getV1(), self.M[l][c][aresta].getV2()])
                else:
                    matriz[l].append("-")
        return matriz

    ############### MAIS FUNÇÕES ÚTEIS ###############
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

    def arcoNaPosicao(self, pos1, pos2):
        '''Retorna o arco da matriz na posição
        passada por parâmetro'''

        arco = []

        for i in range(len(self.N)):
            if i == pos1:
                arco.append(self.N[i])

        for j in range(len(self.N)):
            if j == pos2:
                arco.append(self.N[j])

        if len(arco) != 2: return False

        return arco

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

                    if '-' not in (list((self.M[i][j]))[0]):

                        if len(list((self.M[i][j]).keys())) == 1:
                            rotulo = list((self.M[i][j]).keys())[0] # Extraindo rótulo da posição matriz[i][j]
                            rotulos.append(rotulo) # Rótulo
                            pesos.append(self.M[i][j][rotulo].getPeso()) # Peso do rótulo
                            v1.append(self.N[i]) # Vértice 1
                            v2.append(self.N[j]) # Vértice 2
                        else:

                            for k in (list((self.M[i][j]).keys())):

                                rotulo = k  # Extraindo rótulo da posição matriz[i][j]
                                rotulos.append(rotulo)  # Rótulo
                                pesos.append(self.M[i][j][rotulo].getPeso())  # Peso do rótulo
                                v1.append(self.N[i])  # Vértice 1
                                v2.append(self.N[j])  # Vértice 2


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

        grafo = self.matrizAdjacenciaBinaria()
        novaMatriz = []

        for i in range(len(grafo)):
            aux = []
            for j in range(len(grafo[0])):

                if grafo[i][j] != 0:
                    arco = self.arcoNaPosicao(i, j)
                    aux.append(self.pesoArco(arco[0], arco[1]))
                else:
                    aux.append(0)

            novaMatriz.append(aux)

        return novaMatriz

    def matrizAdjacenciaBinaria(self):
        '''
        Modifica o grafo para que ele se transforme em uma matriz composta apenas de 1 e 0.
        :param grafo: Uma cópia do grafo que será transformado.
        :return: Uma matriz. Ex: [[1, 0, 0, 1], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]]
        '''

        matriz = deepcopy(self.M)

        for i in range(len(self.M)):
            for j in range(len(self.M[0])):

                if self.M[i][j] != 'o' and self.M[i][j] != '-' and self.M[i][j]:
                    matriz[i][j] = 1
                else:
                    matriz[i][j] = 0


        return matriz

    ############### ALGORITMO DE PRIM ###############

    def menorPeso(self, pesos, visitados, quantVertices):
        '''Menor peso entre vértices'''
        minimo = 9**9

        for v in range(quantVertices):
            if pesos[v] < minimo and visitados[v] == False:
                minimo = pesos[v]
                menorIndice = v

        return menorIndice

    def primAlgoritmo(self):
        '''
        Utiliza o algoritmo de Prim para criar uma matriz formada
        pelo arco mais o peso do arco. Ex: [['A-B', 3], ['A-C', 4], ...
        :param : O grafo.
        :return: Uma nova matriz gerada a partir do algoritmo de Prim.
        '''

        vertices = deepcopy(self.N)
        grafo = self.matrizAdjacenciaComPesos()
        quantVertices = len(grafo)

        pesos = [9**9] * quantVertices # Menores peso do arco
        noPais = [None] * quantVertices # Guardar Minimum Spanning Tree
        pesos[0] = 0 # Distancia até nó raiz é 0
        visitados = [False] * quantVertices
        noPais[0] = -1

        for n in range(quantVertices):

            # Escolha o vértice de distância mínima ainda não processado.
            vMenorDist = self.menorPeso(pesos, visitados, quantVertices)
            visitados[vMenorDist] = True

            for v in range(quantVertices):

                if grafo[vMenorDist][v] > 0 and visitados[v] == False and pesos[v] > grafo[vMenorDist][v]:
                    pesos[v] = grafo[vMenorDist][v]
                    noPais[v] = vMenorDist

        caminhoPrim = []
        for i in range(1, quantVertices):
            aux = []
            aux.append(vertices[noPais[i]] + '-' + vertices[i])
            aux.append(self.pesoArco(vertices[noPais[i]], vertices[i]))
            caminhoPrim.append(aux)

        return caminhoPrim

    ############### ALGORITMO DE KRUSKAL ###############

    def posicaoDoVertice(self, V):
        '''Retorna a posição do vértice(V) em self.N'''
        for i in range(len(self.N)):
            if self.N[i] == V:
                return i

    def utilKruskal(self):
        grafo = self.matrizModificada()
        novaLista = []
        for j in range(len(grafo)):
            aux = []
            for k in range(1, 3):
                aux.append(self.posicaoDoVertice(grafo[j][k]))
            aux.append(grafo[j][3])
            novaLista.append(aux)

        return novaLista

    def buscaKruskal(self, pai, i):
        '''Função de utilidade para encontrar o conjunto de um elemento i'''
        if pai[i] == i:
            return i
        return self.buscaKruskal(pai, pai[i])

    def kruskalAlgoritmo(self):
        '''
        Utiliza o algoritmo de Kruskal para criar uma matriz formada
        pelo arco mais o peso do arco. Ex: [['A-B', 3], ['A-C', 4], ...
        :param : O grafo.
        :return: Uma nova matriz gerada a partir do algoritmo de Kruskal.
        '''
        grafo = self.utilKruskal()
        V = len(self.N)
        i = soma = 0
        # Ordendando listas por ordem de peso
        graph = sorted(grafo, key=lambda item: item[2])
        pai, rank, resultado = [], [], []

        for node in range(V):
            pai.append(node)
            rank.append(0)

        while soma < V - 1:

            v1, v2, peso = graph[i]
            i += 1
            aux1 = self.buscaKruskal(pai, v1)
            aux2 = self.buscaKruskal(pai, v2)

            # Se incluir esta borda não  causar um ciclo inclua no resultado
            # E incrementa o índice do resultado para a próxima borda

            if aux1 != aux2:
                soma += 1
                resultado.append([v1, v2, peso])

                # União de dois conjuntos de aux1 e aux2
                xRaiz = self.buscaKruskal(pai, aux1)
                yRaiz = self.buscaKruskal(pai, aux2)

                if rank[xRaiz] < rank[yRaiz]: pai[xRaiz] = yRaiz
                elif rank[xRaiz] > rank[yRaiz]: pai[yRaiz] = xRaiz
                else:
                    pai[yRaiz] = xRaiz
                    rank[xRaiz] += 1

        resultadoFinal = []
        for i in range(len(resultado)):
            aux = []
            aux.append(self.N[resultado[i][0]] + '-' + self.N[resultado[i][1]])
            aux.append(resultado[i][2])
            resultadoFinal.append(aux)

        return resultadoFinal

