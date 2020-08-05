import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv

def composition(texto, k):
    partes = [texto[i:i+k] for i in range(len(texto)-k)]
    return sorted(partes)

def deBruijnKMeros(kmeros):
    res = {}
    # defino el grafo como un multigrafo:
    G = nx.MultiDiGraph()
    # no encontre una manera mas linda (que ande) que hacer un diccionario para los labels de ejes:
    edge_labels = {}

    for arista in kmeros:
        nodo1 = arista[:-1]
        nodo2 = arista[1:]

        # No hace falta agregar los nodos (al agregar ejes se crean si no estan)
        # pero los agrego para poner label (opcion: armar otro dict y pasarlo)
        G.add_node(nodo1, label = nodo1)
        G.add_node(nodo2, label = nodo2)
        # Agrego el eje y guardo su label (con la tupla de nodos como key, osea se pisan los repetidos)
        G.add_edge(nodo1, nodo2, label=arista)
        edge_labels[(nodo1,nodo2)]=arista

        if not nodo1 in res:
            res[nodo1]=[]
        
        res[nodo1].append(nodo2)

    # hay muchos layout, hay que ver cual es mejor, matplot no se lleva bien con los multiples ejes
    # otra opcion es poner un solo eje con peso 
    pos=nx.spring_layout(G)
    # dibujo el grafo
    nx.draw(G, pos, with_labels = True)
    # dibujo los labels de los ejes (obs: usa el mismo "pos")
    nx.draw_networkx_edge_labels(G, pos, edge_labels= edge_labels)
    # plotear
    nx.drawing.nx_agraph.write_dot(G,'coso.dot')
    G=pgv.AGraph("coso.dot")

    progOptions=['neato', 'dot', 'twopi', 'circo', 'fdp', 'nop']
    for progOption in progOptions:
        G.draw('{0}.png'.format(progOption),prog=progOption)

    # plt.draw()
    # # mostrar 
    # plt.show()

    return res

cadena = 'TAATGGGATGCCATGTT'
deBruijnKMeros(composition(cadena, 3))
