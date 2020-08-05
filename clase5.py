from pprint import pprint

def trieConstruction(patterns):
    trie = {}
    for pattern in patterns:
        currentNode = trie
        for symbol in pattern:
            if not symbol in currentNode:
                currentNode[symbol] = {}
            
            currentNode = currentNode[symbol]
        currentNode['isPattern']=True
    return trie

def prefixTrieMatching(text, trie):
    matches = []
    match = ''
    
    currentNode = trie
    i=0
    while i < len(text):
        symbol = text[i]

        if symbol in currentNode:
            match += symbol
            currentNode = currentNode[symbol]
            if 'isPattern' in currentNode:
                matches.append(match)
        elif currentNode=={}:
            matches.append(match)
        else:
            break

        i+=1
        
    return matches

def trieMatching(text, trie):
    matches = []
    for i in range(len(text)):
        matches += prefixTrieMatching(text[i:], trie)
    return matches

# def prefijoDe(currentNode, subtexto):



# def suffixTree(text):
#     tree = {}
#     for posInicial in range(len(text)):
#         currentNode = tree

#         agregar
#         subtexto = text[posInicial:]
#         hayPrefijo, prefijo, clave = prefijoDe(currentNode, subtexto)

#         if hayPrefijo:

#         else:
#             currentNode[subtexto] = {'posInicial':posInicial}
            
#     return tree 

patterns = ['anana', 'ana','lol']
trie = trieConstruction(patterns)
# print(trie)
# print(prefixTrieMatching('ananabalol', trie))
# print(trieMatching('ananabalol', trie))
print(suffixTree('panamabananas'))

#TODO PROGRAMAR EL SUFFIXTREE
