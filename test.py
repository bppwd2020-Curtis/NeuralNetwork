from Neuron import *
from NeuralNetMath import *
n1 = Neuron("Length")
n2 = Neuron("Width")

neurons = [n1,n2]


value = 1

sum = 0
for n in neurons:
	sum += n.getPred(value)
	value+=1

print(sigmoid(sum))