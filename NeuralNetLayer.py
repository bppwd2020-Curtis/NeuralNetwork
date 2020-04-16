class NeuralNetLayer:
	def __init__(self,neurons):
		self.neurons = neurons

	def getPrediction(self, data):
		sum = 0
		for i in range(len(self.neurons)):
			sum += self.neurons[i].getPrediction(data[i])