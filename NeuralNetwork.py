import numpy
from NeuralNetMath import *
class NeuralNetwork:
	def __init__(self, neuralNetLayers, epochs, learning_rate):
		self.neuralNetLayers = neuralNetLayers
		self.epochs = epochs
		self.learning_rate = learning_rate

	def train(self, training_data, actFun):
		random_index = numpy.random.randint(len(training_data))
		point = training_data[random_index]

		target = point[len(point)-2]

		point = point[:-1]

		
		#using index 0 for test while studying deep learning
		
		z = self.neuralNetLayers[0].getPrediction(point)
		prediction = actFun(z)

		cost = numpy.square(prediction - target)

		dcost_dpred = 2 * (prediction - target)
		dpred_dz = actFunct_p(actFun(z))

		dz_w = point

		dz_b = 1

		dcost_dz = dcost_dpred * dpred_dz

		dcost_dw = []

		for i in range(len(point)):
			dcost_dw.append(point[i] * dcost_dz)

		dcost_db = dcost_dz * dz_b

		for c in range(len(self.neuralNetLayers[0].neurons)):
			self.neuralNetLayers[0].neurons[c].weight -= self.learning_rate * dcost_dw[c]

		self.neuralNetLayers[0].bias -= self.learning_rate * dcost_db

	def train_all(self, training_data,actFun):
		for i in range(self.epochs):
			self.train(training_data,actFun)