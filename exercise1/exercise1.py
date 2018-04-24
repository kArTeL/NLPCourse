from __future__ import print_function, division
from future.utils import iteritems
from builtins import range, input
import numpy as np
from brown import get_sentences_with_word2idx

def get_bigram_count(star_idx, end_idx,  sentences, V, smoothie=1):
    bigram_count_matrix = np.ones((V,V)) * smoothie
    #print(bigram_count_matrix)

    for sentence in sentences:
        for i in range(len(sentence)):
            # current word.
            word_index = sentence[i]
            
            # if is the first word we need add start -> word.
            if i == 0:
                bigram_count_matrix[star_idx, word_index] += 1
            else: 
                previousWord = sentence[i-1]
                bigram_count_matrix[previousWord, word_index] += 1
            if i == len(sentence) - 1:
                bigram_count_matrix[word_index, end_idx] += 1
    bigram_count_matrix /= bigram_count_matrix.sum(axis=1, keepdims=True)
    return bigram_count_matrix

 # a function to calculate normalized log prob score
  # for a sentence
def get_score(sentence, start_idx, end_idx, bigram_probs):
    score = 0
    for i in range(len(sentence)):
      if i == 0:
        # beginning word
        score += np.log(bigram_probs[start_idx, sentence[i]])
      else:
        # middle word
        score += np.log(bigram_probs[sentence[i-1], sentence[i]])
    # final word
    score += np.log(bigram_probs[sentence[-1], end_idx])

    # normalize the score
    return score / (len(sentence) + 1)

def get_words(sentence, idx_words):
    return ' '.join(idx2word[i] for i in sentence)

if __name__ == '__main__':
    # get indexed sentenses and word indexed set.
    sentences, word2idx = get_sentences_with_word2idx()

    # diferent words length
    V = len(word2idx)

    # start and end index.
    start_idx = word2idx["START"]
    end_idx = word2idx["END"]
    smoothie = 0.1
    print(get_bigram_count(start_idx,end_idx,sentences,V,smoothie))

      # a function to map word indexes back to real words
    idx2word = dict((v, k) for k, v in iteritems(word2idx))
































# def bigramProbabilityAddOne(current, previous, corpus):
#     # totalPrevios = corpus.words()
#     # P(current/previous) = (count(previous current) + 1 )/ (count(previous) + corpus.length)
#     #print("loading corpus")
#     totalCorpusWords   = corpus.words()
#     #totalCorpusWords   = [{"":10,"20":}]
#     print("corpus length %d" % len(totalCorpusWords))
#     #print("end loading corpus")
#     wordsFrecuency     = Counter(totalCorpusWords)
#     #print("words frecuency %s" % wordsFrecuency)
#     print("starting get unique words")
#     totalDiferentWords = len(list(wordsFrecuency))

#     print("TOTAL DIFERENT WORDS %d" % totalDiferentWords)
#     print("END get unique words")

#     previousCount      = wordsFrecuency[previous]
#     print("the word %s has %d ocurrencies" % (previous, previousCount))

#     return previousCount

# def getUniqueWords(allWords) :
#     uniqueWords = [] 
#     for i in allWords:
#         if not i in uniqueWords:
#             uniqueWords.append(i)
#     return uniqueWords

#print(brown.sents())