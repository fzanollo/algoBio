from pprint import pprint

class HMM(object):
    def __init__(self, emissionM, transitionM):
        self.emissionM = emissionM
        self.transitionM = transitionM

    def hpp(self, seqEstados):
        res = 1/2
        for anterior, actual in zip(seqEstados[:-1], seqEstados[1:]):
            res *= transitionM[anterior][actual]
        return res

    def outcomeProbGivenHPP(self, seqEmisiones, seqEstados):
        res = 1
        for i in range(len(seqEstados)):
            estado = seqEstados[i]
            emision = seqEmisiones[i]
            res *= emissionM[estado][emision]
        return res

# TODO ponele
    """
    resolver con dinamica el problema de encontrar la mejor seq de estados 
    para una seq de emisiones
    """



transitionM = {'F':{'F':0.9, 'B':0.1}, 'B':{'F':0.1, 'B':0.9}}
emissionM = {'F':{'H':0.5, 'T':0.5}, 'B':{'H':0.75, 'T':0.25}}

hmm = HMM(emissionM, transitionM)
# print(hmm.hpp('FFFBBBBBFFF'))
# print(hmm.outcomeProbGivenHPP('THTHHHTHTTH', 'FFFBBBBBFFF'))
# print(hmm.outcomeProbGivenHPP('THTHHHTHTTH', 'FBFBBBFBFFB'))

seqEmisiones = 'THTHHHTHTTH'

        