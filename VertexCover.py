# Programa Python3 para imprimir o Vertex Cover
# de um dado grafo não direcionado
from collections import defaultdict

# Esta classe representa um grafo direcionado
# usando uma representação de lista de adjacência
class Graph:

    def __init__(self, vertices):
        
        # Número de vértices
        self.V = vertices
        
        # Dicionário padrão para armazenar o grafo
        self.graph = defaultdict(list)

    # Função para adicionar uma aresta ao grafo
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Função para imprimir o Vertex Cover
    def printVertexCover(self):
        
        # Inicializa todos os vértices como não visitados.
        visited = [False] * (self.V)
        
        # Considere todas as arestas uma por uma
        for u in range(self.V):
            
            # Uma aresta só é escolhida quando
            # visited[u] e visited[v]
            # são falsos
            if not visited[u]:
                
                # Percorre todos os adjacentes de u e
                # escolhe o primeiro vértice ainda não visitado
                # (Basicamente estamos escolhendo
                # uma aresta (u, v) entre as arestas restantes.
                for v in self.graph[u]:
                    if not visited[v]:
                        
                        # Adiciona os vértices (u, v) ao
                        # conjunto de resultados. Fazemos o vértice
                        # u e v visitado para que todas as
                        # arestas entre eles sejam ignoradas
                        visited[v] = True
                        visited[u] = True
                        break

        # Imprime o vertex cover
        for j in range(self.V):
            if visited[j]:
                print(j, end=' ')
                
        print()

# Código do programa

# Cria um grafo conforme
# o diagrama acima
g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(5, 6)

g.printVertexCover()