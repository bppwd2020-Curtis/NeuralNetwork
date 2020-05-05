from Neuron import *
from NeuralNetMath import *
from NeuralNetLayer import *
from NeuralNetwork import *
n1 = Neuron("Red")
n2 = Neuron("Green")
n3 = Neuron("Blue")

neurons = [n1,n2,n3]
inputLayer = NeuralNetLayer(neurons)
nn = NeuralNetwork([inputLayer],20000,0.001)

mystery = [255,255,255]

data = [
		#Colors That Look Good in Black
		[255,255,0,1],#yellow
		[0,0,255,1],#blue
		[255,0,0,1],#red
		[0,255,0,1],#green
		[128,0,128,1],#purple
		[218,165,32,1],#golden
		[255,255,255,1],#white
		[0,255,255,1],#cyan
		[255,0,255,1],#magenta
		[192,192,192,1],#silver
		#Colors That Look good on White
		[128,0,0,0],#maroon
		[0,128,0,0],#green
		[0,0,0,0],#black
		[128,128,128,0],#gray
		[0,128,128,0],#teal
		[0,0,128,0]#Navy
		]

nn.train_all(data, reLu)

if(sigmoid(nn.neuralNetLayers[0].getPrediction(mystery)) < 0):
	print("White")
elif(sigmoid(nn.neuralNetLayers[0].getPrediction(mystery)) >= 0):
	print("Black")