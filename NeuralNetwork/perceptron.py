import numpy as np


class Perceptron(object):
    def __init__(self, number_of_inputs, threshold=100, learning_rate=0.01):
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = np.zeros(number_of_inputs + 1)

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        if summation > 0:
            activation = 1
        else:
            activation = 0
        return activation

    def train(self, training_inputs, outputs):
        for i in range(self.threshold):
            for inputs, output in zip(training_inputs, outputs):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (output - prediction) * inputs
                self.weights[0] += self.learning_rate * (output - prediction)


if __name__ == '__main__':
    training_inputs = [np.array([1, 1]), np.array([1, 0]), np.array([0, 1]), np.array([0, 0])]
    expected_output = np.array([1, 0, 0, 0])

    perceptron = Perceptron(2)
    print("Initial weights: "+str(perceptron.weights))

    perceptron.train(training_inputs, expected_output)
    print("Prediction for [1, 1]: "+str(perceptron.predict(np.array([1, 1]))))
    print("Prediction for [1, 0]: "+str(perceptron.predict(np.array([1, 0]))))
    print("Prediction for [0, 1]: "+str(perceptron.predict(np.array([0, 1]))))
    print("Prediction for [0, 0]: "+str(perceptron.predict(np.array([0, 0]))))

    print("Final weights: "+str(perceptron.weights))

    training_inputs.clear()
