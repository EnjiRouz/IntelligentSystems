import numpy as np

# входной и выходной слои
input_layer = np.array(([0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]), dtype=float)
output_layer = np.array(([0], [1], [1], [0]), dtype=float)


# логистическая активационная функция (функция активации сигмоиды)
def sigmoid(t):
    return 1 / (1 + np.exp(-t))


# производная активационной функции
def sigmoid_derivative(p):
    return p * (1 - p)


class NeuralNetwork:
    def __init__(self, input_layer, output_layer):
        self.input = input_layer
        self.weights1 = np.random.rand(self.input.shape[1], 4)
        self.weights2 = np.random.rand(4, 1)
        self.y = output_layer
        self.output = np.zeros(output_layer.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.layer2 = sigmoid(np.dot(self.layer1, self.weights2))
        return self.layer2

    def back_propagation(self):
        d_weights2 = np.dot(self.layer1.T, 2 * (self.y - self.output) * sigmoid_derivative(self.output))
        d_weights1 = np.dot(self.input.T, np.dot(2 * (self.y - self.output) * sigmoid_derivative(self.output),
                                                 self.weights2.T) * sigmoid_derivative(self.layer1))

        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def train(self):
        self.output = self.feedforward()
        self.back_propagation()


if __name__ == '__main__':
    NN = NeuralNetwork(input_layer, output_layer)
    for i in range(1501):
        if i % 500 == 0:
            print("For iteration # " + str(i))
            print("Input : \n" + str(input_layer))
            print("Expected Output: \n" + str(output_layer))
            print("Predicted Output: \n" + str(NN.feedforward()))
            print("Loss: " + str(np.mean(np.square(output_layer - NN.feedforward()))))
            print("Weights of the first layer:\n"+str(NN.weights1)+"\nWeights of the second layer:\n"+str(NN.weights2))
            print("\n")

        NN.train()
