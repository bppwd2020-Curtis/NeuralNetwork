def sigmoid(x):
    return 1/(1+numpy.exp(-x))

def sigmoid_p(x):
    return sigmoid(x) * (1-sigmoid(x))