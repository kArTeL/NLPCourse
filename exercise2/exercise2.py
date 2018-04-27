from __future__ import print_function, division
from future.utils import iteritems
from builtins import range, input
import numpy as np
from brown import get_sentences_with_word2idx
import numpy as np

import sys
import os
sys.path.append(os.path.abspath('../exercise1'))

from exercise1 import get_bigram_probs
if __name__ == '__main__':
    
    sentences, word2idx = get_sentences_with_word2idx()
    V = len(word2idx)
    start_id = word2idx['START']
    end_id = word2idx['END']
    lr = 1e-1
    #print(inputs)
   # for sentence in sentences: 
    sentence = sentences[0]
    n = len(sentence)
    inputs = np.zeros((n-1, V))
    targets = np.zeros((n-1, V))
    inputs[np.arange(n-1),sentence[:n-1]] = 1
    targets[np.arange(n-1),sentence[1:]] = 1
    print(inputs)
    print(inputs.T)