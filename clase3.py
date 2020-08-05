from pprint import pprint

def composition(texto, k):
    partes = [texto[i:i+k] for i in range(len(texto)-k+1)]
    return sorted(partes)

def stringFromPath(lista):
    res = lista[0]
    for e in lista[1:]:
        res += e[-1]
    return res

def sonOverlap(ki, kj):
    return ki[1:] == kj[:-1]

def overlapGraph(kameros):
    res = {}
    for i in range(len(kameros)):
        adjacents = []
        for j in range(len(kameros)):
            if i!=j and sonOverlap(kameros[i], kameros[j]):
                adjacents.append(kameros[j])
        res[str(i)] = (kameros[i], adjacents)

    return res

def deBruijnKMeros(kmeros):
    res = {}
    for arista in kmeros:
        nodo1 = arista[:-1]
        nodo2 = arista[1:]

        if nodo1 not in res:
            res[nodo1] = []

        if nodo2 not in res:
            res[nodo2] = []

        res[nodo1].append(nodo2)

    return res

def find_euler_tour(visited,current,graph):
    queue=[current]
    while queue:
        if graph[current]:
            queue.append(current)
            current=graph[current].pop()
        else:
            visited.append(current)
            current=queue.pop()
    return visited

def caminoDeEulerDesde(grafo, primero):
    visited = []
    current = primero
    lista = find_euler_tour(visited,current,grafo)
    lista.reverse()
    return lista[:-1]

# clase 4
def obtenerInversoAdjacentes(listaDeAdjacentes):
    res = {}
    for nodo, adjacentes in listaDeAdjacentes.items():
        for adj in adjacentes:
            if adj not in res:
                res[adj]=[]
            if nodo not in res:
                res[nodo]=[]
            res[adj].append(nodo)
    return res

def conectarPrimeroYUltimo(listaDeAdjacentes):
    primero = ultimo = None
    
    gradosEntrada = obtenerInversoAdjacentes(listaDeAdjacentes)
    
    for nodo, adjacentes in listaDeAdjacentes.items():
        dout = len(adjacentes)
        din = len(gradosEntrada[nodo])

        if dout < din:
            ultimo = nodo

        if dout > din:
            primero = nodo
        
    # print(primero, ultimo)

    listaDeAdjacentes[ultimo]=[primero]
    return primero, ultimo

def stringReconstructionProblem(kmeros):
    grafo = deBruijnKMeros(kmeros)
    primero, ultimo = conectarPrimeroYUltimo(grafo)

    euler = caminoDeEulerDesde(grafo, primero)

    return stringFromPath(euler)

def pairedComposition(text, k, d):
    kdmeros = []

    for i in range(len(text)-2*k-d+1):
        kd1 = text[i:i+k]
        kd2 = text[i+k+d:i+2*k+d]
        kdmeros.append((kd1, kd2))

    return kdmeros

def stringSpelledByGappedPattern(gappedPatterns, k, d):
    prefixString = stringFromPath([x[0] for x in gappedPatterns])
    suffixString = stringFromPath([x[1] for x in gappedPatterns])

    return prefixString[k+1:] == suffixString[:-k-1]

# def deBruijnKdmeros(kmeros):


# sec = "TATGGGGTGC"
# # partes = composition(sec, 3) #k-meros
# # print(partes)

# path = ['TAA','AAT','ATG','TGC','GCC','CCA','CAT','ATG','TGG','GGG','GGA','GAT','ATG','TGT','GTT']

# print(stringFromPath(path))
# pprint(overlapGraph(sorted(path)))

# cadena = 'TAATGCCATGGGATGTT'
# coso = stringReconstructionProblem(composition(cadena,3))
# pprint(coso)

# pprint(pairedComposition(cadena, 3, 1))
# print()
# pprint(pairedComposition(cadena, 3, 2))
# cadena = 'AGCAGCTGCTGCA'
# k=2
# d=1
# gappedPatterns = pairedComposition(cadena, k, d)
# print(gappedPatterns)
# print(stringSpelledByGappedPattern(gappedPatterns, k, d))

with open('CarsonellaRuddii.txt','r') as infile:
    cadena = ''
    for row in infile:
        cadena += row
    cadena = cadena.replace('\n','')

# coso = stringReconstructionProblem(composition(cadena,151))
print(coso)
print(coso==cadena)