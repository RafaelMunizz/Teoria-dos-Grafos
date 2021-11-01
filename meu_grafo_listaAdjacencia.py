from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from copy import deepcopy

class MeuGrafo(GrafoListaAdjacencia):

    def grafoEmMatriz(self):
        """
        Grafo construido em formato de matriz. Ex: [['a1','J','C'],['a2',...
        :return: Grafo em matriz. Ex: [['a1','J','C'],['a2',...
        """
        grafoMatriz = []
        for i in self.A:
                grafoMatriz.append([i, self.A[i].getV1(), self.A[i].getV2()])

        return grafoMatriz

    def paresVertices(self):
        '''
        Provê uma lista de todas as combinacoes existentes no grafo.
        :return: Uma lista com os pares de vértices adjacentes
        '''
        # Lista com os pares de vértices ligados por arestas existentes
        combinacoesExistentes = []
        for i in self.A:
            combinacoesExistentes.append(self.A[i].getV1() + "-" + self.A[i].getV2())

        return combinacoesExistentes

    def pegarRotulo(self, verticeA, verticeB):
        '''
        Descobre o rotulo de determinado par de vertices.
        :return: Rotulo de um par de vertices
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        if verticeA not in self.N or verticeB not in self.N: raise VerticeInvalidoException("Vertice nao existe")

        for i in self.A:
            if verticeA == self.A[i].getV1() and verticeB == self.A[i].getV2() or \
                verticeB == self.A[i].getV1() and verticeA == self.A[i].getV2():
                return self.getAresta(i).getRotulo()

        return "Erro: Combinacao inexistente"

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''

        combinacoesExistentes = self.paresVertices()

        # Lista com todas as combinações possíveis de pares de vértices ligados por arestas
        combinacoesPossiveis = []
        for j in self.N:
            for k in self.N:
                if j != k: # Impedindo laços
                    if (k + '-' + j) not in combinacoesPossiveis and (k + '-' + j) not in combinacoesExistentes: # Impedindo vértices iguais inversamente
                        combinacoesPossiveis.append(j + '-' + k)

        # Lista com vértices não adjacentes
        verticesNaoAdjacentes = []
        for l in combinacoesPossiveis:
            if l not in combinacoesExistentes:
                verticesNaoAdjacentes.append(l)

        return verticesNaoAdjacentes

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in self.A:
            if self.A[i].getV1() == self.A[i].getV2():
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V in self.N:
            combinacoesExistentes = self.paresVertices()
            grau = 0
            for i in combinacoesExistentes:
                if i[0] == V: grau += 1
                if i[2] == V: grau += 1

            return grau
        raise VerticeInvalidoException("Vertice nao existe")

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        combinacoesExistentes = self.paresVertices()

        for i in range(len(combinacoesExistentes)):
            for j in range(len(combinacoesExistentes)):

                if i != j :
                    if combinacoesExistentes[i] == combinacoesExistentes[j]:
                        return True
        return False

    def possuiArestasParalelas(self, verticeA, verticeB, retornarLista = False):
        '''
        Descobre se a combinação de vértices possui arestas paralelas sobre eles.
        :param V: Os vértices que podem ou não ter arestas paralelas.
        retornarLista == False -> Retornará um valor booleano informando se há ou não arestas paralelas.
        retornarLista == True -> Retornará uma lista com as arestas que são paralelas nos vértices passados.
        :return: Valor booleano ou lista.
        :raises: VerticeInvalidoException se algum dos vértices não existir no grafo.
        '''

        if verticeA not in self.N or verticeB not in self.N: raise VerticeInvalidoException("Vertice nao existe")

        arestasParalelas = []
        for i in self.A:
            if verticeA == self.A[i].getV1() and verticeB == self.A[i].getV2() or \
                verticeB == self.A[i].getV1() and verticeA == self.A[i].getV2():
                arestasParalelas.append(self.getAresta(i).getRotulo())

        if retornarLista == False:
            if len(arestasParalelas) > 1: return True
            return False

        if retornarLista == True:
            return arestasParalelas

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        if V in self.N:
            listaArestasNoVertice = []
            for a in self.A:
                if self.getAresta(a).getV1() == V or self.getAresta(a).getV2() == V:
                    listaArestasNoVertice.append(self.getAresta(a).getRotulo())

            return listaArestasNoVertice
        raise VerticeInvalidoException("Vertice nao existe")

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        combinacoesExistentes = self.paresVertices()

        # Se o grafo não for simples, automaticamente não será completo.
        if self.ha_laco() or self.ha_paralelas(): return False

        # Lista com todas as combinações possíveis de pares de vértices ligados por arestas, exceto laços
        combinacoesPossiveis = []
        for j in self.N:
            for k in self.N:
                if j != k:
                    combinacoesPossiveis.append(j + '-' + k)

        soma = 0
        for l in combinacoesExistentes:
            for m in combinacoesPossiveis:
                if l == m:
                    soma += 1

        if soma == len(combinacoesPossiveis) / 2: return True
        return False

    def verticesAdjacentes(self, V=''):
        '''
        Provê uma lista de todas os vertices adjacentes a determinado vertice.
        :return: Uma lista com os vértices adjacentes possiveis.
        '''
        if V not in self.N: raise VerticeInvalidoException("Vertice nao existe")

        combinacoesExistentes = self.paresVertices()
        verticesAdjacentes = []  # Vertices que sao adjacentes

        for i in combinacoesExistentes:
            # Adicionando a lista vertices que podem servir de destino a partir do vertice que esta sendo analisado
            if i[0] == V and i[2] not in verticesAdjacentes: verticesAdjacentes.append(i[2])  # Evitando duplicidade de destino no caso de aresta paralela
            if i[2] == V and i[0] not in verticesAdjacentes: verticesAdjacentes.append(i[0])  # Evitando duplicidade de destino no caso de aresta paralela
        return verticesAdjacentes

    def dfs(self, V=''):
        '''
        Provê um grafo que contém as arestas do DFS
        :param V: O vértice onde se inicia o caminho
        :return: Um grafo do tipo árvore DFS
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        if V not in self.N: raise VerticeInvalidoException("Vertice nao existe")

        listaVertices = [] # Lista que armazenara os vertices analisados
        arvoreDFS = MeuGrafo(deepcopy(self.N)) # Novo grafo que sera retornado

        # Funcao recursiva para analisar o grafo passado
        def dfsRecursiva(V=''):

            for i in range(len(self.paresVertices())):

                if V in self.paresVertices()[i]: # Se o vertice passado pertence a lista de determinado par de vertices do grafo
                    aresta = self.paresVertices()[i] # Lista que eh um par de vertice do grafo

                    if ((aresta[0] not in listaVertices) or (aresta[2] not in listaVertices) \
                            and self.paresVertices()[i][0] != self.paresVertices()[i][2]):

                        # Adicionando arestas ao novo grafo (Rotulo por meio da funcao "pegarRotulo")
                        arvoreDFS.adicionaAresta(self.pegarRotulo(aresta[0], aresta[2]), aresta[0], aresta[2])

                        listaVertices.append(aresta[0])
                        listaVertices.append(aresta[2])
                        #Chamada recursiva
                        dfsRecursiva(aresta[2] if aresta[2]!= V else aresta[0])

        dfsRecursiva(V)
        return arvoreDFS

    def bfs(self, V='', **kwargs):
        '''
        Provê um grafo que contém as arestas do BFS
        :param V: O vértice onde se inicia o caminho
        :return: Um grafo do tipo árvore BFS
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        if V not in self.N: raise VerticeInvalidoException

        try:
            self.key = kwargs["bfs"]
        except:
            self.arvoreBFS = MeuGrafo(deepcopy(self.N))
            self.verticesAnalisados = []
            self.arestasIncidentes = []
            self.key = False

        for aresta in self.grafoEmMatriz():
            if (aresta[0] in self.arestas_sobre_vertice(V)) and ((aresta[1] not in self.verticesAnalisados) or \
                (aresta[2] not in self.verticesAnalisados)) and (aresta[1] != aresta[2]):

                self.arvoreBFS.adicionaAresta(aresta[0], aresta[1], aresta[2])
                self.verticesAnalisados.append(aresta[1])
                self.verticesAnalisados.append(aresta[2])

        def verificar():

            vertices = []
            for i in self.arvoreBFS.grafoEmMatriz():

                if (i[1] in vertices) == False: vertices.append(i[1])
                if (i[2] in vertices) == False: vertices.append(i[2])

            if len(vertices) == len(self.arvoreBFS.N): return True
            return False

        for aresta in self.grafoEmMatriz():
            if (aresta[0] in self.arestas_sobre_vertice(V)) and (verificar() == False) and aresta[0] not in self.arestasIncidentes:

                self.arestasIncidentes.append(aresta[0])
                self.bfs(aresta[2] if aresta[2] != V else aresta[1], **{"bfs": False})

        return self.arvoreBFS

    def modificandoGrafoUtil(self):
        '''Transformando grafo em dicionário'''
        listaDicionario = []

        for i in self.N:
            listaAux = []
            listaAux.append(i)
            listaAux.append(self.verticesAdjacentes(i))
            listaDicionario.append(listaAux)

        return dict(listaDicionario)  # Criacão dicionário

    def ha_ciclo(self):
        '''
        Verifica se há ciclo no grafo.
        :return: Um valor booleano que indica se o grafo é conexo.
        '''

        combinacoes = self.todosCaminhosPossiveis(True)
        ciclos = [] # Todos os ciclos do grafo

        for i in combinacoes:
            if i[-1] in self.verticesAdjacentes(i[0]) and (self.possuiArestasParalelas(i[0], i[1]) or len(i) > 2):
                ciclos.append(i)

        try:
            cicloFinal = ciclos[0]
        except: # Caso não haja ciclos no grafo

            # Se houver um laço, basta pegar os vértices iguais e retornar a lista com o laço
            if self.ha_laco():
                for i in self.A:
                    if self.A[i].getV1() == self.A[i].getV2():
                        # return [vertice1, aresta, vertice2]
                        return [self.A[i].getV1(), self.pegarRotulo(self.A[i].getV1(), self.A[i].getV2()), self.A[i].getV2()]

            return False

        cicloFinal.append(cicloFinal[0]) # Colocando a conexão do último vértice ao inicial
        cicloFinal = self.colocarArestas(cicloFinal) # Colocando as arestas correspondentes de cada par

        return cicloFinal

    def caminho(self, n):
        '''
        Provê uma lista com um caminho de tamanho passado por parâmetro.
        :param V: O tamanho do caminho a ser buscado.
        :return: Uma lista com o caminho. Ex: ['A', 'a3', 'J', 'a5', 'K', 'a4', 'G', 'a9', 'H']
        '''
        if n == 0 : return False

        '''Como o código utiliza o parametro para entender a quantidade de vértices, é necessário
        adicionar 1 para ele colocar um vértice a mais e o caminho ficar correto.'''
        n = n + 1
        novoGrafo = self.modificandoGrafoUtil()

        # Função recursiva que criará o caminho como uma lista apenas de vértices
        def recursaoCaminho(novoGrafo, verticeA, verticeB, caminho=[]):

            caminho = caminho + [verticeA]

            if verticeA == verticeB: return [caminho]
            if not verticeA in novoGrafo: return False

            caminhos = []

            for no in novoGrafo[verticeA]:
                if no not in caminho:
                    novosCaminhos = recursaoCaminho(novoGrafo, no, verticeB, caminho)
                    for novoCaminho in novosCaminhos:
                        if len(novoCaminho) == n:
                            caminhos.append(novoCaminho)

            return caminhos # Lista com caminhos possíveis de um único par

        listaCaminhosVertices = [] # TODOS os caminhos possiveis dentro do grafo com o tamanho passado
        for i in self.N:
            for j in self.N:
                # Dois laços para criar uma lista com todos os caminhos de todos os pares de vértices
                caminhos = recursaoCaminho(novoGrafo, i, j)

                if caminhos and len(caminhos[0]) == n:
                    listaCaminhosVertices.append(caminhos[0])

        try:
            listaFinal = listaCaminhosVertices[0] # Pegando apenas um dos caminho do tamanho pedido
        except:
            return False

        listaFinal = self.colocarArestas(listaFinal) # Colocando as arestas do caminho

        return listaFinal

    def conexo(self):
        '''
        Verifica se o grafo é conexo.
        :return: Um valor booleano que indica se o grafo é conexo.
        '''

        grafoAux = self.dfs(self.N[0]) # Criando um novo grafo a partir de uma DFS no primeiro vertice disponivel
        vertices = deepcopy(self.N) # Lista de vertices do grafo passado por parametro
        listaVertices = [] # Lista de vertices que o novo grafo possui

        for i in grafoAux.grafoEmMatriz():
            for j in range(1, 3):
                if i[j] not in listaVertices:
                    listaVertices.append(i[j])

        # Organizando os vertices que os grafos possuem
        listaVertices.sort()
        vertices.sort()

        if vertices == listaVertices: # Comparacao dos vertices dos grafos
            return True
        return False

    def colocarArestas(self, listaVertices):
        '''
        Provê uma lista com as arestas adicionadas a uma lista anteriormente com vértices apenas.
        :param V: Uma lista com vértices. Ex: ['A', 'J', 'K', 'G', 'H']
        :return: Uma lista com vértices e arestas. Ex: ['A', 'a3', 'J', 'a5', 'K', 'a4', 'G', 'a9', 'H']
        '''
        pares = [] # Formando pares com a lista de vértices passados
        for i in range(1, len(listaVertices)):
            pares.append(listaVertices[i-1] + '-' + listaVertices[i])

        rotulos = [] # Lista com os rótulos dos pares
        if self.possuiArestasParalelas(pares[0][0], pares[0][2]) and len(pares) == 2:
            # Caso os vértices possuam arestas paralelas, a função retornará para a variável rotulos as duas arestas
            rotulos = self.possuiArestasParalelas(pares[0][0], pares[0][2], True)

        else: # Se não for paralelas, a função pegará os rótulos dos pares
            for j in pares:
                rotulos.append(self.pegarRotulo(j[0], j[2]))

        listaFinal = [] # Lista com vértices e arestas (Um por índice)
        for k in range(len(listaVertices)): # Colocando um vértice e uma aresta por vez
                listaFinal.append(listaVertices[k])
                if len(listaVertices)-1 != k:
                    listaFinal.append(rotulos[k])

        return listaFinal

    def todosCaminhosPossiveis(self, todos = False, verticeA = '', verticeB = ''):
        '''
        Provê uma matriz com todos os caminhos possíveis de um vértice a outro
        :param V: Os vértices onde se iniciam e terminam o caminho. Ex: para C e T temos: [['C', 'T'], ['C', 'M', 'T']]
        todos == False -> Retornará uma lista com caminho de um vértice a outro.
        todos == True -> Retornará todos os caminhos de todos os vértices.
        :return: Uma matriz
        '''
        # Qualquer vértice serve caso a escolha seja para retornar todos
        if todos == True:
            verticeA = self.N[0]
            verticeB = self.N[1]

        novoGrafo = self.modificandoGrafoUtil()

        def recursaoCaminhosPossiveis(novoGrafo, verticeA, verticeB, caminho=[]):

            caminho = caminho + [verticeA]

            if verticeA == verticeB: return [caminho]
            if not verticeA in novoGrafo: return []

            caminhos = [] # Caminhos do grafo

            for no in novoGrafo[verticeA]:
                if no not in caminho:
                    novosCaminhos = recursaoCaminhosPossiveis(novoGrafo, no, verticeB, caminho)
                    for novoCaminho in novosCaminhos:
                        caminhos.append(novoCaminho)

            return caminhos

        if todos == False:
            # TODOS os caminhos possíveis para os dois vértices
            return recursaoCaminhosPossiveis(novoGrafo, verticeA, verticeB)

        listaCaminhosVertices = []  # TODOS os caminhos possiveis dentro do grafo com o tamanho passado
        for i in self.N:
            for j in self.N:
                # Dois laços para criar uma lista com todos os caminhos de todos os pares de vértices
                caminhos = recursaoCaminhosPossiveis(novoGrafo, i, j)

                try:
                    if len(caminhos[0]) > 1:
                        listaCaminhosVertices.append(caminhos[0])
                except: # Caso exista um vértice sem caminhos no caso de grafos desconexos
                    continue

        if todos == True:
            return listaCaminhosVertices

    def possuiCaminhoEuleriano(self):
        '''
        Verifica se o grafo possui caminho euleriano.
        :return: Um valor booleano.
        '''

        if not self.conexo(): return False

        graus = []

        for i in self.N:
            graus.append(self.grau(i))

        grauImpar = 0

        for j in graus:
            if j % 2 != 0: grauImpar += 1

        if grauImpar == 0 or grauImpar == 2: return True

        return False

    def pesoAresta(self, V1, V2):
        '''
        :param: Vértices 1 e 2.
        :return: Peso do arco formado por V1-V2, caso ele exista.
        '''
        try:
            return self.getAresta(self.pegarRotulo(V1, V2)).getPeso()
        except:
            return False

    def posicaoVertice(self, V):
        '''
        :param: Vértice.
        :return: Posição do vértice na lista de vértices (self.N).
        '''

        for i in range(len(self.N)):
            if self.N[i] == V:
                return i

        return False


