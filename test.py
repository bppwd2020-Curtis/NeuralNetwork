from Neuron import *
from NeuralNetMath import *
from NeuralNetLayer import *
from NeuralNetwork import *
n1 = Neuron("Length")
n2 = Neuron("Width")

neurons = [n1,n2]
inputLayer = NeuralNetLayer(neurons)
nn = NeuralNetwork([inputLayer],5000,0.1)

mystery = [4.5, 1]

data = [[3,   1.5, 1],
        [2,   1,   0],
        [4,   1.5, 1],
        [3,   1,   0],
        [3.5, .5,  1],
        [2,   .5,  0],
        [5.5,  1,  1],
        [1,    1,  0]]

nn.train_all(data)

if(sigmoid(nn.neuralNetLayers[0].getPrediction([4.5,1])) < 0.5):
	print("Blue")
else:
	print("Red")