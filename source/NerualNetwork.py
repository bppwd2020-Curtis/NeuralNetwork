import numpy
data = [[3,   1.5, 1],
        [2,   1,   0],
        [4,   1.5, 1],
        [3,   1,   0],
        [3.5, .5,  1],
        [2,   .5,  0],
        [5.5,  1,  1],
        [1,    1,  0]]

mystery_flower = [4.5, 1]

w1 = numpy.random.randn()
w2 = numpy.random.randn()
bias = numpy.random.randn()

def sigmoid(x):
    return 1/(1+numpy.exp(-x))

def sigmoid_p(x):
    return sigmoid(x) * (1-sigmoid(x))

epoch = 5000
learning_rate = 0.1

for i in range(epoch):
	random_index = numpy.random.randint(len(data))
	point = data[random_index]

	z = point[0]*w1 + point[1]*w2 + bias

	target = point[2]

	prediction = sigmoid(z)

	cost = numpy.square(prediction - target)

	dcost_dpred = 2 * (prediction - target)
	dpred_dz = sigmoid_p(z)

	dz_dw1 = point[0]
	dz_dw2 = point[1]
	dz_db = 1

	dcost_dz = dcost_dpred * dpred_dz
	dcost_dw1 = dcost_dz * dz_dw1
	dcost_dw2 = dcost_dz * dz_dw2
	dcost_db = dcost_dz * dz_db
	w1 = w1 - learning_rate * dcost_dw1
	w2 = w2 - learning_rate * dcost_dw2
	bias = bias - learning_rate * dcost_db

def predicition(v1,v2):
	pred = v1 * w1 + v2 * w2 + bias
	return sigmoid(pred)


print(predicition(0,0))