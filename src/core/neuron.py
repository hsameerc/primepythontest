import math
import os
import random

from src.lib.CharVal import main_test_predicted_output
from src.lib.NeuralPath import NeuralPath


def tan_h(x):
    return (math.e ** x - math.e ** (-x)) / (math.e ** x + math.e ** (-x))


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


def softmax(x):
    e_x = [math.exp(i) for i in x]
    sum_e_x = sum(e_x)
    return [i / sum_e_x for i in e_x]


class Neuron:
    def __init__(self, input_size, output_size, name='neuron'):
        self.name = name
        self.weights = [[random.random() for _ in range(input_size)] for _ in range(output_size)]
        self.bias = [random.random() for _ in range(output_size)]

        self.__wp = NeuralPath().get_wb(self.name, True)
        self.__bp = NeuralPath().get_wb(self.name, False)

        # print('loading ' + self.name + ' neuron..')
        # print('loading ' + self.__wp + ' neuron..')
        # print('loading ' + self.__bp + ' neuron..')

        hidden_size = input_size
        self.first_hidden_weights = [[random.random() for _ in range(input_size)] for _ in range(hidden_size)]
        self.first_hidden_bias = [random.random() for _ in range(hidden_size)]

        self.second_hidden_weights = [[random.random() for _ in range(hidden_size)] for _ in range(hidden_size)]
        self.second_hidden_bias = [random.random() for _ in range(hidden_size)]

        self.third_hidden_weights = [[random.random() for _ in range(hidden_size)] for _ in range(output_size)]
        self.third_hidden_bias = [random.random() for _ in range(output_size)]

        self.hidden_first_weighted_sums = None
        self.hidden_first_activation_results = None
        self.hidden_second_activation_results = None
        self.hidden_second_weighted_sums = None
        self.hidden_output_weighted_sums = None
        self.hidden_output_activation_results = None

    def activate(self, inputs):
        weighted_sums = [sum(x * w for x, w in zip(inputs, weights)) + b for weights, b in zip(self.weights, self.bias)]
        activation_results = [sigmoid(ws) for ws in weighted_sums]
        return activation_results

    def forward(self, inputs):
        self.hidden_first_weighted_sums = [sum(x * w for x, w in zip(inputs, weights)) + b for weights, b in
                                           zip(self.first_hidden_weights, self.first_hidden_bias)]
        self.hidden_first_activation_results = [sigmoid(ws) for ws in self.hidden_first_weighted_sums]

        self.hidden_second_weighted_sums = [
            sum(x * w for x, w in zip(self.hidden_first_activation_results, weights)) + b for
            weights, b in zip(self.second_hidden_weights, self.second_hidden_bias)]
        self.hidden_second_activation_results = [sigmoid(ws) for ws in self.hidden_second_weighted_sums]

        self.hidden_output_weighted_sums = [
            sum(x * w for x, w in zip(self.hidden_second_activation_results, weights)) + b for
            weights, b in zip(self.third_hidden_weights, self.third_hidden_bias)]
        self.hidden_output_activation_results = [sigmoid(ws) for ws in self.hidden_output_weighted_sums]
        return self.hidden_output_activation_results

    def backward(self, X, y, learning_rate):
        error = y - self.hidden_output_activation_results
        d_output = error * sigmoid_derivative(self.hidden_output_activation_results)
        error_hidden = d_output.dot(self.third_hidden_weights.T)
        d_hidden = error_hidden * sigmoid_derivative(self.hidden_second_activation_results)
        self.third_hidden_weights += self.hidden_output_activation_results.T.dot(d_output) * learning_rate
        self.third_hidden_bias += np.sum(d_output, axis=0, keepdims=True) * learning_rate
        self.weights += X.T.dot(d_hidden) * learning_rate
        self.bias += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate

    def learn(self, X, y, learning_rate, epochs):
        for epoch in range(epochs):
            self.forward(X)
            self.backward(X, y, learning_rate)

    def train(self, inputs, target_output, learning_rate=0.1):
        predicted_outputs = self.activate(inputs)
        errors = [target - predicted for target, predicted in zip(target_output, predicted_outputs)]
        # print("errors:", errors)
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                self.weights[i][j] += learning_rate * errors[i] * inputs[j]
            self.bias[i] += learning_rate * errors[i]

    def write(self):
        weights = self.weights
        bias = self.bias
        np.savez(self.__wp, *weights)
        np.savez(self.__bp, *bias)
        print('\033[32m' + "Write Complete..." + '\033[0m')

    def load(self):
        if os.path.exists(self.__wp) & os.path.exists(self.__bp):
            pass
            # print('\033[34m' + "loading network - " + self.name + '\033[0m')
        if os.path.exists(self.__wp):
            # print('loading ' + self.__wp + ' weights..')
            loaded_weights = np.load(self.__wp)
            loaded__weights_arrays = [loaded_weights[key] for key in loaded_weights.files]
            self.weights = loaded__weights_arrays
        if os.path.exists(self.__bp):
            # print('loading ' + self.__bp + ' bias..')
            loaded_bias = np.load(self.__bp)
            loaded__bias_arrays = [loaded_bias[key] for key in loaded_bias.files]
            self.bias = loaded__bias_arrays


def network_creator(input_data, output_data, learning_rate, epoch, train_type="XYZ"):
    if len(input_data) == len(output_data):
        for i, val in enumerate(input_data):
            ntw = Neuron(len(val), len(output_data[i]),
                         "neuron_" + str(len(val)) + train_type + str(len(output_data[i])))
            ntw.load()
            # print(output_data[i])
            # print(len(val), len(val),
            #       len(output_data[i]),
            #       "neuron_" + str(len(val)) + train_type + str(len(output_data[i])))
            for x in range(epoch):
                ntw.train(val, output_data[i], learning_rate)
            ntw.write()
            activation = ntw.activate(val)
            status = max(range(len(output_data[i])),
                         key=lambda j: output_data[i][j]) == max(
                range(len(activation)),
                key=lambda k:
                activation[k])
            if status:
                print('\033[31m' + "REAL = PREDICTED POSITION INDEX", status, "" + '\033[0m')
            else:
                print('\033[31m' + "REAL = PREDICTED POSITION ODT", output_data[i], "" + '\033[0m')
                print('\033[31m' + "REAL = PREDICTED POSITION ACT", activation, "" + '\033[0m')


def neuron_tester(test_input=[0.5100001, 0.47, 0.51]):
    input_size = 3
    output_size = 10
    neuron = Neuron(input_size, output_size)
    class_labels = ["Class1", "Class2", "Class3", "Class4", "Class5",
                    "Class6", "Class7", "Class8", "Class9", "Class10"]
    training_data = [
        {"inputs": [0.7, 0.8, 0.6], "target": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], "label": "Class1"},
        {"inputs": [0.2, 0.5, 0.3], "target": [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], "label": "Class2"},
        {"inputs": [0.1, 0.1, 0.1], "target": [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], "label": "Class3"},
        {"inputs": [0.9, 0.8, 0.7], "target": [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], "label": "Class4"},
        {"inputs": [0.3, 0.6, 0.4], "target": [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], "label": "Class5"},
        {"inputs": [0.4, 0.4, 0.4], "target": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], "label": "Class6"},
        {"inputs": [0.6, 0.9, 0.5], "target": [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], "label": "Class7"},
        {"inputs": [0.1, 0.7, 0.2], "target": [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], "label": "Class8"},
        {"inputs": [0.7, 0.7, 0.8], "target": [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], "label": "Class9"},
        {"inputs": [0.5, 0.5, 0.5], "target": [0, 0, 0, 0, 0, 0, 0, 0, 0, 1], "label": "Class10"},
    ]
    epochs = 1000
    learning_rate = 0.1
    for epoch in range(epochs):
        for data in training_data:
            neuron.train(data["inputs"], data["target"], learning_rate)

    print('\033[34m' + "INPUT_DATA" + '\033[0m', test_input)
    predicted_outputs = neuron.activate(test_input)
    output_class = main_test_predicted_output(softmax(predicted_outputs), class_labels)
    print('\033[34m' + "OUTPUT_DATA" + '\033[0m', softmax(predicted_outputs))
    print('\033[34m' + "INPUT_DATA" + '\033[0m',
          max(range(len(softmax(predicted_outputs))), key=lambda i: softmax(predicted_outputs)[i]))
    print('\033[34m' + "OUTPUT CLASS" + '\033[0m',
          output_class)
    if output_class == "Class10":
        print('\033[92m' + "Test PASSED." + '\033[0m')
    else:
        print('\033[91m' + "Test Failed." + '\033[0m')


def neuron_tester_variable_size(test_input):
    max_input_size = 5
    output_size = 10
    neuron = Neuron(max_input_size, output_size)

    def pad_or_truncate(input_data, size):
        if len(input_data) < size:
            return input_data + [0] * (size - len(input_data))
        else:
            return input_data[:size]

    class_labels = ["Class1", "Class2", "Class3", "Class4", "Class5",
                    "Class6", "Class7", "Class8", "Class9", "Class10"]
    training_data = [
        {"inputs": [0.7, 0.8, 0.6], "target": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], "label": "Class1"},
        {"inputs": [0.2, 0.5, 0.3, 0.4], "target": [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], "label": "Class2"},
        {"inputs": [0.1], "target": [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], "label": "Class3"},
        {"inputs": [0.9, 0.8, 0.7, 0.6, 0.5], "target": [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], "label": "Class4"},
        {"inputs": [0.3, 0.6, 0.4], "target": [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], "label": "Class5"},
        {"inputs": [0.4, 0.4, 0.4], "target": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], "label": "Class6"},
        {"inputs": [0.6, 0.9, 0.5], "target": [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], "label": "Class7"},
        {"inputs": [0.1, 0.7, 0.2], "target": [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], "label": "Class8"},
        {"inputs": [0.7, 0.7, 0.8], "target": [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], "label": "Class9"},
        {"inputs": [0.5, 0.5, 0.5], "target": [0, 0, 0, 0, 0, 0, 0, 0, 0, 1], "label": "Class10"},
    ]

    for data in training_data:
        data["inputs"] = pad_or_truncate(data["inputs"], max_input_size)

    epochs = 1000
    learning_rate = 0.1
    for epoch in range(epochs):
        for data in training_data:
            neuron.train(data["inputs"], data["target"], learning_rate)

    test_input = pad_or_truncate(test_input, max_input_size)
    print('\033[34m' + "INPUT_DATA" + '\033[0m', test_input)
    predicted_outputs = neuron.activate(test_input)
    output_class = main_test_predicted_output(softmax(predicted_outputs), class_labels)
    print('\033[34m' + "OUTPUT_DATA" + '\033[0m', softmax(predicted_outputs))
    print('\033[34m' + "INPUT_DATA" + '\033[0m',
          max(range(len(softmax(predicted_outputs))), key=lambda i: softmax(predicted_outputs)[i]))
    print('\033[34m' + "OUTPUT CLASS" + '\033[0m',
          output_class)
    if output_class == "Class2":
        print('\033[92m' + "Test PASSED." + '\033[0m')
    else:
        print('\033[91m' + "Test Failed." + '\033[0m')


if __name__ == '__main__':
    test_input = [0.2, 0.5, 0.3, 0.4]
    neuron_tester()
    neuron_tester_variable_size(test_input)
