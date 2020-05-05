import numpy
def sigmoid(x):
    return 1/(1+numpy.exp(-x))

def actFunct_p(x):
    return x * (1-x)

def reLu(x):
	if(x >= 0):
		return x
	else:
		return 0