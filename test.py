from Neuron import *
from NeuralNetMath import *
from NeuralNetLayer import *
from NeuralNetwork import *
n1 = Neuron("Red")
n2 = Neuron("Green")
n3 = Neuron("Blue")

neurons = [n1,n2,n3]
inputLayer = NeuralNetLayer(neurons)
nn = NeuralNetwork([inputLayer],90000,0.001)

mystery = [2.55,2.55,2.55]

data = [
		#Colors That Look Good in Black
		[2.55,2.55,0,1],#yellow
		[0,2.55,0,1],#lime
		[2.55,2.55,2.55,1],#white
		[0,2.55,2.55,1],#cyan
		#Colors That Look good on White
		[1.28,0,0,0],#maroon
		[0,0,0,0],#black
		[1.28,1.28,1.28,0],#gray
		[0,0,1.28,0]#Navy
		]

nn.train_all(data, reLu)

if(reLu(nn.neuralNetLayers[0].getPrediction(mystery)) <= 0):
	print("White")
else:
	print("Black")