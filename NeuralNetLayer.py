import numpy
class NeuralNetLayer:
	def __init__(self,neurons):
		self.neurons = neurons
		self.bias = numpy.random.randn()

	def getPrediction(self, data):
		sum = 0
		for i in range(len(self.neurons)):
			sum += self.neurons[i].getPred(data[i])
		return sum + self.bias