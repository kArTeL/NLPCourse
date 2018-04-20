import nltk
from nltk.corpus import brown
from nltk.probability import FreqDist
from collections import Counter


def bigramProbabilityAddOne(current, previous, corpus):
    # totalPrevios = corpus.words()
    # P(current/previous) = (count(previous current) + 1 )/ (count(previous) + corpus.length)
    #print("loading corpus")
    totalCorpusWords   = corpus.words()
    #totalCorpusWords   = [{"":10,"20":}]
    print("corpus length %d" % len(totalCorpusWords))
    #print("end loading corpus")
    wordsFrecuency     = Counter(totalCorpusWords)
    #print("words frecuency %s" % wordsFrecuency)
    print("starting get unique words")
    totalDiferentWords = len(list(wordsFrecuency))

    print("TOTAL DIFERENT WORDS %d" % totalDiferentWords)
    print("END get unique words")

    previousCount      = wordsFrecuency[previous]
    print("the word %s has %d ocurrencies" % (previous, previousCount))

    return previousCount

def getUniqueWords(allWords) :
    uniqueWords = [] 
    for i in allWords:
        if not i in uniqueWords:
            uniqueWords.append(i)
    return uniqueWords

#print(brown.sents())
print(bigramProbabilityAddOne("hola","Current",brown))