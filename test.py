from Neuron import *
from NeuralNetMath import *
from NeuralNetLayer import *
from NeuralNetwork import *
n1 = Neuron("Red")
n2 = Neuron("Green")
n3 = Neuron("Blue")

neurons = [n1,n2,n3]
inputLayer = NeuralNetLayer(neurons)
nn = NeuralNetwork([inputLayer],2000,0.001)

mystery = [12.8,0,0]

data = [
		#Colors That Look Good in Black
		[25.5,25.5,0,1],#yellow
		[0,0,25.5,1],#blue
		[25.5,0,0,1],#red
		[0,25.5,0,1],#green
		[12.8,0,12.8,1],#purple
		[21.8,16.5,3.2,1],#golden
		[25.5,25.5,25.5,1],#white
		[0,25.5,25.5,1],#cyan
		[25.5,0,25.5,1],#magenta
		[19.2,19.2,19.2,1],#silver
		#Colors That Look good on White
		[12.8,0,0,0],#maroon
		[0,12.8,0,0],#green
		[0,0,0,0],#black
		[12.8,12.8,12.8,0],#gray
		[0,12.8,12.8,0],#teal
		[0,0,12.8,0]#Navy
		]

nn.train_all(data, reLu)

if(sigmoid(nn.neuralNetLayers[0].getPrediction(mystery)) < 0):
	print("White")
elif(sigmoid(nn.neuralNetLayers[0].getPrediction(mystery)) >= 0):
	print("Black")