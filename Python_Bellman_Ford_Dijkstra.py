from IPython.display import clear_output
from heapq import heappop, heappush
import matplotlib.pyplot as plt
from colorama import Fore
import networkx as nx
import sys

def base():
    print("                                                   ")
    print(Fore.BLUE + '\t\t\t ALGRITMOS VORACES \t\t\t')
    print(Fore.BLACK + 'Opciones de Ingreso:')
    print('\t 1. Ingrese "1" para Algoritmo de Bellman-Ford.')
    print('\t 2. Ingrese "2" para Algoritmo de Dijkstra.')
    print('\t 3. Ingrese "0" para Salir.')
    opcion_voraz = input("\t  " + "¿Cual es tu opción?: ")
    if opcion_voraz.isdigit() & len(opcion_voraz) != 0:
        clear_output(wait=True)
        tipo_seleccion(int(opcion_voraz))
    else:
        clear_output(wait=True)
        print("                                                                                              ")
        print(Fore.RED + "\t  Opción Erronea - Solo se permiten números enteros positivos.  \t\n" + Fore.BLACK)
        base()

def bellman_ford():
    print("                                                                ")
    print(Fore.BLUE + '\t\t\t ALGORITMO DE BELLMAN-FORD \t\t\t' + Fore.BLACK)
    print("                                                                ")
    print(Fore.BLACK + 'Información del Proceso:')
    print('\t A. Se elige el nodo de incicio.')
    print('\t B. Se elige el nodo final.')
    print('\t C. Se observa la ruta más corta.')
    print('\t D. Escribir los nodos como se encuentran en el grafo.')
    print("                                   ")
    print(Fore.GREEN + '\t\t\t GRAFO A SER ANALIZADO \t\t\t' + Fore.BLACK)
    G = nx.DiGraph()
    edges = [["0", "1"], ["0", "2"], ["1", "2"], ["1", "3"], ["1", "4"], ["3", "2"], ["4", "2"], ["4", "3"]]
    G.add_edges_from(edges)
    ubicacion_nodos = {"0":(0, 1), "1":(1, 2), "2":(1, 0), "3":(2, 2), "4":(2, 0)}
    nx.draw(G, ubicacion_nodos, edge_color = 'black', width = 1, linewidths = 1, node_size = 500, node_color = 'pink', alpha = 0.9, 
            labels = {node : node for node in G.nodes()})
    nx.draw_networkx_edge_labels(G, ubicacion_nodos, edge_labels = {("0", "1"): "-1", ("0", "2"): "4", ("1", "2"): "-3", ("1", "3"): "2", 
                                                                    ("1", "4"): "2", ("3", "2"): "5", ("4", "2"): "1", ("4", "3"): "-3"}, 
                                 label_pos = 0.7, font_color='red')
    plt.axis('on')
    plt.show()
    nodo_inicio = input("\t    " + "Escriba el nombre del nodo de inicio: ")
    nodo_final =  input("\t    " + "Escriba el nombre del nodo de fin: ")
    if len(nodo_inicio) or len(nodo_final):
        print("                                   ")
        def getPath(parent, vertex):
            if vertex < 0:
                return []
            return getPath(parent, parent[vertex]) + [vertex]
        def bellmanFord(edges, source, n):
            distance = [sys.maxsize] * n
            parent = [-1] * n
            distance[source] = 0
            for k in range(n - 1):
                for (u, v, w) in edges:
                    if distance[u] != sys.maxsize and distance[u] + w < distance[v]:
                        distance[v] = distance[u] + w
                        parent[v] = u
            for (u, v, w) in edges:
                if distance[u] != sys.maxsize and distance[u] + w < distance[v]:
                    print("Error:Ciclo de peso negativo encontrado.")
                    return
            for i in range(n):
                if i != source and distance[i] < sys.maxsize:
                    if source == int(nodo_inicio) and i == int(nodo_final):
                        print(Fore.GREEN + "Entre los Nodos: " + str(source) + " —> " + str(i) + "\t\tCosto mínimo = " + str(distance[i]) + "\tRuta = " + str(getPath(parent, i)) + Fore.BLACK)
                    else:
                        print(Fore.BLUE + "Entre los Nodos: " + str(source) + " —> " + str(i) + "\t\tCosto mínimo = " + str(distance[i]) + "\tRuta = " + str(getPath(parent, i)) + Fore.BLACK)
                    
        if __name__ == '__main__':
            edges = [(0, 1, -1), (0, 2, 4), (1, 2, -3), (1, 3, 2), (1, 4, 2), (3, 2, 5), (4, 2, 1), (4, 3, -3)]
            n = 5
            print("                                                                                        ")
            print(Fore.GREEN + '\t\t\t RESULTADOS TRAS APLICAR EL ALGORITMO DE BELLMA-FORD \t\t\t' + Fore.BLACK)
            print("                                                                                        ")
            for source in range(n):
                bellmanFord(edges, source, n)
            print("                                                                                                               ")
            print(Fore.RED + "Si no encuentra su resultado en texto verde en la lista que se imprime se debe a: " + Fore.BLACK)
            print(Fore.RED + "\t 1.- No se encontro conexión entre los nodos ingresados." + Fore.BLACK)
            print(Fore.RED + "\t 2.- Uno o los dos nodos ingresados no se encuentran en el grafo." + Fore.BLACK)
        salir()
    else:
        clear_output(wait=True)
        print("                                                                                         ")
        print(Fore.RED + "\t  Opción Erronea - No se ingreso correctamente los nodos.  \t\n" + Fore.BLACK)
        bellman_ford()

def dijkstra():
    print("                                                            ")
    print(Fore.BLUE + '\t\t\t ALGORITMO DE DIJKSTRA \t\t\t' + Fore.BLACK)
    print("                                                            ")
    print(Fore.BLACK + 'Información del Proceso:')
    print('\t A. Se elige el nodo de incicio.')
    print('\t B. Se elige el nodo final.')
    print('\t C. Se observa la ruta más corta.')
    print('\t D. Escribir los nodos como se encuentran en el grafo.')
    print("                                   ")
    print(Fore.GREEN + '\t\t\t GRAFO A SER ANALIZADO \t\t\t' + Fore.BLACK)
    G = nx.DiGraph()
    # edges = [["0", "1"], ["0", "3"], ["0", "4"], ["1", "2"], ["3", "4"], ["4", "1"], ["4", "5"], ["5", "1"], ["5", "2"]]
    # G.add_edges_from(edges)
    # ubicacion_nodos = {"0":(0, 1), "1":(1, 1), "2":(2, 1), "3":(0, 0), "4":(1, 0), "5":(2, 0)}
    # nx.draw(G, ubicacion_nodos, edge_color = 'black', width = 1, linewidths = 1, node_size = 500, node_color = 'pink', alpha = 0.9, 
    #         labels = {node : node for node in G.nodes()})
    # nx.draw_networkx_edge_labels(G, ubicacion_nodos, edge_labels = {("0", "1"): "16", ("0", "3"): "4", ("0", "4"): "8", ("3", "4"): "3", 
    #                                                                 ("4", "1"): "7", ("4", "5"): "1", ("5", "1"): "5", ("5", "2"): "6", 
    #                                                                 ("1", "2"): "2"}, font_color='red')
    # plt.axis('on')
    edges = [["START", "A"], ["START", "B"], ["START", "C"], ["A", "D"], ["B", "D"], ["A", "E"], ["C", "G"], ["D", "FINISH"], ["C", "FINISH"]]
    G.add_edges_from(edges)
    ubicacion_nodos = {"START":(0, 1), "A":(1, 2), "B":(1, 1), "C":(1, 0), "D":(2, 2), "E":(2, 1), "G":(2, 0), "FINISH":(3, 1)}
    nx.draw(G, ubicacion_nodos, edge_color = 'black', width = 1, linewidths = 1, node_size = 500, node_color = 'pink', alpha = 0.9, labels = {node : node for node in G.nodes()})
    nx.draw_networkx_edge_labels(G, ubicacion_nodos, edge_labels = {("START", "A"): "3", ("START", "B"): "1", ("START", "C"): "2", ("A", "D"): "3", ("B", "D"): "4", ("A", "E"): "5", ("C", "G"): "4", ("D", "FINISH"): "2", ("C", "FINISH"): "8"}, label_pos = 0.7, font_color='red')
    plt.axis('on')
    plt.show()
    nodo_inicio = input("\t    " + "Escriba el nombre del nodo de inicio: ")
    nodo_final =  input("\t    " + "Escriba el nombre del nodo de fin: ")
    if len(nodo_inicio) or len(nodo_final):
        print("                                   ")
        class Node:
            def __init__(string, vertex, weight = 0):
                string.vertex = vertex
                string.weight = weight
            def __lt__(string, other):
                return string.weight < other.weight
        class Graph:
            def __init__(string, edges, n):
                string.adjList = [[] for _ in range(n)]
                for (source, dest, weight) in edges:
                    string.adjList[source].append((dest, weight))
        def get_route(prev, i, route):
            if i >= 0:
                get_route(prev, prev[i], route)
                route.append(i)
        def findShortestPaths(graph, source, n):
            pq = []
            heappush(pq, Node(source))
            dist = [sys.maxsize] * n
            dist[source] = 0
            done = [False] * n
            done[source] = True
            prev = [-1] * n
            while pq:
                node = heappop(pq)
                u = node.vertex
                for (v, weight) in graph.adjList[u]:
                    if not done[v] and (dist[u] + weight) < dist[v]:
                        dist[v] = dist[u] + weight
                        prev[v] = u
                        heappush(pq, Node(v, dist[v]))
                done[u] = True
            route = []
            for i in range(n):
                if i != source and dist[i] != sys.maxsize:
                    get_route(prev, i, route)
                    if source == int(nodo_inicio) and i == int(nodo_final):
                        print(Fore.GREEN + "Entre los Nodos: " + str(source) + " —> " + str(i) + "\t\tCosto mínimo = " + str(dist[i]) + "\tRuta = " + str(route) + Fore.BLACK)
                    else:
                        print(Fore.BLUE + "Entre los Nodos: " + str(source) + " —> " + str(i) + "\t\tCosto mínimo = " + str(dist[i]) + "\tRuta = " + str(route) + Fore.BLACK)
                    route.clear()
        if __name__ == '__main__':
            # edges =  [(0, 1, 16), (0, 3, 4), (0, 4, 8), (1, 2, 2), (3, 4, 3), (4, 1, 7), (4, 5, 1), (5, 1, 5), (5, 2, 6)]
            # n = 6
            edges =  [(0, 1, 3), (0, 2, 1), (0, 3, 2), (1, 4, 3), (2, 4, 4), (1, 5, 5), (3, 6, 4), (4, 7, 2), (3, 7, 8)]
            n = 8
            graph = Graph(edges, n)
            print("                                                                                        ")
            print(Fore.GREEN + '\t\t\t RESULTADOS TRAS APLICAR EL ALGORITMO DE DIJKSTRA \t\t\t' + Fore.BLACK)
            print("                                                                                        ")
            for source in range(n):
                findShortestPaths(graph, source, n)
            print("                                                                                                               ")
            print(Fore.RED + "Si no encuentra su resultado en texto verde en la lista que se imprime se debe a: " + Fore.BLACK)
            print(Fore.RED + "\t 1.- No se encontro conexión entre los nodos ingresados." + Fore.BLACK)
            print(Fore.RED + "\t 2.- Uno o los dos nodos ingresados no se encuentran en el grafo." + Fore.BLACK)
        salir()
    else:
        clear_output(wait=True)
        print("                                                                                         ")
        print(Fore.RED + "\t  Opción Erronea - No se ingreso correctamente los nodos.  \t\n" + Fore.BLACK)
        dijkstra()
    
def default_1():
    clear_output(wait = True)
    print(Fore.RED + "                                                                    ")
    print(Fore.RED + "\t  Opción Erronea - Ingrese una de las opciones establecidas.  \t\n")
    base()

def tipo_seleccion(numero_0):
    return opciones_bellman_ford_dijkstra.get(numero_0, default_1)()

def salir():
    print("                                                     ")
    print(Fore.BLUE + '\t\t\t ADIÓS HASTA LA PRÓXIMA \t\t\t' + Fore.BLACK)
    sys.exit()

opciones_bellman_ford_dijkstra = {
    1: bellman_ford,
    2: dijkstra,
    0: salir
    }

base()