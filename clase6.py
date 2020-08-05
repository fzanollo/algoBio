from pprint import pprint

def suffixArrayConstruction(text):
    suffixes = sorted([(text[i:],i) for i in range(len(text))])
    return [s[1] for s in suffixes]

def patternMatchingWithSuffixArray(text, pattern, suffixArray):
    minIndex = 0
    maxIndex = len(text)
    while minIndex < maxIndex:
        midIndex = (minIndex + maxIndex)//2
        if pattern > text[suffixArray[midIndex]:]:
            minIndex = midIndex + 1
        else:
            maxIndex = midIndex
    first = minIndex
    maxIndex = len(text)
    while minIndex < maxIndex:
        midIndex = (minIndex + maxIndex)//2
        if pattern < text[suffixArray[midIndex]:suffixArray[midIndex]+len(pattern)]:
            maxIndex = midIndex
        else:
            minIndex = midIndex + 1
    last = maxIndex-1
    if first > last:
        return "nop"
    else:
        return (first, last)

def burrowsWheelerTransform(text):
    rotaciones = sorted([text[i:]+text[:i] for i in range(len(text))])
    return [r[-1] for r in rotaciones]

def inverseBurrowsWheelerTransform(code):
    text = ''
    code = [(code[i], code[:i].count(code[i])) for i in range(len(code))]
    ordered = sorted(code)

    print(code)
    print(ordered)

    letra = ordered[0]
    for v in range(len(code)):
        letra = ordered[code.index(letra)]
        text += letra[0]

    return text

def lastToFirst(i, code):
    code = [(code[i], code[:i].count(code[i])) for i in range(len(code))]
    ordered = sorted(code)
    
    return ordered.index(code[i])

def bwMatching(lastColumn, pattern):
    top = 0
    bottom = len(lastColumn)-1

    while top <= bottom:
        if len(pattern) >0:
            symbol = pattern[-1]
            pattern = pattern[:-1]

            if symbol in lastColumn[top:bottom]:
                topIndex = lastColumn[top:bottom].index(symbol)
                # bottomIndex = str(lastColumn[top:bottom]).rindex(symbol) #TODO terminar
                bottomIndex = len(lastColumn) - 1 - lastColumn[::-1].index(symbol)
                print(str(lastColumn[top:bottom]), bottomIndex, symbol)

                top = lastToFirst(topIndex, lastColumn)
                bottom = lastToFirst(bottomIndex, lastColumn)
            else:
                return 0
        else:
            return bottom - top +1

def betterBWMatching():
    pass
    # tema 8


text = "panamabananas$"
suffixArray = suffixArrayConstruction(text)
pattern = "ana"
# print(patternMatchingWithSuffixArray(text, pattern, suffixArray))

# text = 'abracadabra$'
code = burrowsWheelerTransform(text)
# print(inverseBurrowsWheelerTransform(code))
# print(lastToFirst(2,code))
print(bwMatching(code, pattern))
