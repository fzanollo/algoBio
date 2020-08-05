from pprint import pprint

def score(vi, wi):
    sigma = 2
    mu = 1
    score = 0

    if vi=='-' or wi=='-':
        score = -sigma
    elif vi==wi:
        score = 1
    else:
        score = -mu

    return score

def alineamientoLocal(v,w):
    n = len(v)
    m = len(w)

    camino = [ [ None for i in range(m) ] for j in range(n) ]
    s = [ [ None for i in range(m) ] for j in range(n) ]

    s[0][0] = 0
    for i in range(1,n):
        s[i][0] = 0
        camino[i][0] = (i-1, 0)
    for j in range(1,m):
        s[0][j] = 0
        camino[0][j] = (0, j-1)

    maxGlobalValor = 0
    maxGlobalPosicion = (0,0)

    for i in range(1,n):
        for j in range(1,m):

            maxLocal = sorted([
                (0,(0,0)),
                (s[i-1][j] + score(v[i], '-'), (i-1,j)), # Arriba
                (s[i][j-1] + score('-', w[j]), (i, j-1)), # Izq
                (s[i-1][j-1] + score(v[i], w[j]), (i-1,j-1)) # Diagonal
                ], reverse=True)[0]

            s[i][j] = maxLocal[0]
            camino[i][j] = maxLocal[1]

            if s[i][j] > maxGlobalValor:
                print('max valor viejo', maxGlobalValor, 'nuevo', s[i][j])
                print('max valor pos vieja', maxGlobalPosicion, 'nueva', (i,j))
                maxGlobalValor = s[i][j]
                maxGlobalPosicion = (i,j)

            # if s[i][j] == s[i-1][j-1] + score(v[i], w[j]) and v[i] == w[j]:
            #     camino[i][j] = (i-1,j-1) # Diagonal
            # elif s[i][j] == s[i-1][j] + score(v[i], '-'):
            #     camino[i][j] = (i-1,j) # Arriba
            # elif s[i][j] == s[i][j-1] + score('-', w[j]):
            #     camino[i][j] = (i, j-1) # Izq
            # elif s[i][j] == 0:
            #     camino[i][j] = (0,0)

    pprint(s)

    camino[0][0] = (-1,-1)
    camino[n-1][m-1] = maxGlobalPosicion

    return camino 

def alinear(camino, v, w):
    caminoSeguido = []
    vAlineado = wAlineado = ''
    i = len(v)-1
    j = len(w)-1

    while i>=0 or j>=0:
        direccion = camino[i][j]

        if direccion == (i-1,j-1): # Diagonal
            caminoSeguido.append('Diag'+ str((i,j)))
            vAlineado = v[i] + vAlineado
            wAlineado = w[j] + wAlineado
        
        elif direccion == (i-1,j): # Arriba
            caminoSeguido.append('Abajo'+ str((i,j)))
            vAlineado = v[i] + vAlineado
            wAlineado = '-' + wAlineado

        elif direccion == (i, j-1): # Izq
            caminoSeguido.append('Der'+ str((i,j)))
            vAlineado = '-' + vAlineado
            wAlineado = w[j] + wAlineado

        else:
            caminoSeguido.append('Salto desde '+ str(direccion)+' a '+str((i,j)))
            vAlineado = '-'*(i-direccion[0]) + vAlineado
            wAlineado = '-'*(j-direccion[1]) + wAlineado

        i, j = direccion

    return vAlineado, wAlineado, caminoSeguido[::-1]

v = "YAFDLGYTCMFPVLLGGGELHIVQKETYTAPDEIAHYIKEHGITYIKLTPSLFHTIVNTASFAFDANFESLRLIVLGGEKIIPIDVIAFRKMYGHTEFINHYGPTEATIGA"
w = "AFDVSAGDFARALLTGGQLIVCPNEVKMDPASLYAIIKKYDITIFEATPALVIPLMEYIYEQKLDISQLQILIVGSDSCSMEDFKTLVSRFGSTIRIVNSYGVTEACIDS"

v = "ATGTTATA"
w = "ATCGTCC"

alocal = alineamientoLocal(v,w)
pprint(alocal)

vAlineado, wAlineado, caminoSeguido = alinear(alocal, v, w)
print(vAlineado)
print(wAlineado)
print(caminoSeguido)
