import numpy
class Neuron:
	def __init__(self, name):
		self.weight = numpy.random.randn()
		self.name = name
	def getPred(self,value):
		return self.weight * value