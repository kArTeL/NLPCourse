import numpy as np

sentences = [[0,2,3,4,5,1],[0,4,5,7,8,1]]
V = 12


#print(inputs)
for sentence in sentences: 
    n = len(sentence)
    inputs = np.zeros((n-1, V))
    targets = np.zeros((n-1, V))
    inputs[np.arange(n-1),sentence[:n-1]] = 1
    targets[np.arange(n-1),sentence[1:]] = 1
