import numpy as np
import matplotlib.pyplot as plt
import random


class Plot:
    def __init__(self, day1, day2, day3, day4, weights):
        x1 = np.empty((16, 1))
        y1 = np.empty((16, 1))
        x2 = np.empty((16, 1))
        y2 = np.empty((16, 1))
        x3 = np.empty((16, 1))
        y3 = np.empty((16, 1))
        x4 = np.empty((16, 1))
        y4 = np.empty((16, 1))

        for i in range(0, 16):
            x1[i] = day1[i][0]
            y1[i] = day1[i][1]
            x2[i] = day2[i][0]
            y2[i] = day2[i][1]
            x3[i] = day3[i][0]
            y3[i] = day3[i][1]
            x4[i] = day4[i][0]
            y4[i] = day4[i][1]

        x = np.linspace(5, 20, 100)
        if len(weights) == 2:
            y = (weights[0] * x) + weights[1]
            plt.title("Perceptron a")
        if len(weights) == 3:
            y = (weights[0] * x * x) + (weights[1] * x) + weights[2]
            plt.title("Perceptron b")
        if len(weights) == 4:
            y = (weights[0] * x * x * x) + (weights[1] * x * x) + (weights[2] * x) + weights[3]
            plt.title("Perceptron c")

        plt.plot(x, y, 'r--')
        plt.plot(x1, y1, 'ro', x2, y2, 'bo', x3, y3, 'yo')  # training data
        plt.plot(x4, y4, 'go')  # testing data
        plt.ylim(0, 10)
        plt.xlim(5, 20)
        plt.ylabel('kiloWatts')
        plt.xlabel('hours')
        plt.show()


class DataCollector:
    def __init__(self):
        day1 = open("./Project3_data/train_data_1.txt")
        day2 = open("./Project3_data/train_data_2.txt")
        day3 = open("./Project3_data/train_data_3.txt")
        day4 = open("./Project3_data/test_data_4.txt")
        self.data1 = self.populate_array(day1)
        self.data2 = self.populate_array(day2)
        self.data3 = self.populate_array(day3)
        self.data4 = self.populate_array(day4)
        self.trainging_data = self.data1 + self.data2 + self.data3

    def populate_array(self, data):
        day = []
        for i in range(0, 16):
            data_line = data.readline().strip("\n").split(", ")
            data_tuple = data_line.pop(0), data_line.pop(0)
            day.append(data_tuple)
        return day


class Perceptron:
    def __init__(self, learn_speed, num_weights):
        self.speed = learn_speed
        self.weights = []
        for x in range(0, num_weights):
            self.weights.append(random.random())  # randomly assigns the weights
        print(self.weights)

    def feed_forward(self, inputs):
        sum = 0
        if len(self.weights) == 2:
            sum = (self.weights[0] * inputs[0]) \
                  + (self.weights[1] * inputs[1])
        if len(self.weights) == 3:
            sum = (self.weights[0] * inputs[0] * inputs[0]) \
                  + (self.weights[1] * inputs[0]) \
                  + (self.weights[2] * inputs[1])
        if len(self.weights) == 4:
            sum = (self.weights[0] * inputs[0] * inputs[0] * inputs[0]) \
                  + (self.weights[1] * inputs[0] * inputs[0]) \
                  + (self.weights[2] * inputs[0]) \
                  + (self.weights[3] * inputs[1])

        # for i in range(0, len(inputs)):
        #     sum += self.weights[i] * inputs[i]
        return self.activate(sum)  # return the value activation

    def activate(self, num):
        # linear activation f(x) = x
        return num

    def train(self, inputs, desired_output):
        guess = self.feed_forward(inputs)
        error = desired_output - guess

        if len(self.weights) == 2:
            self.weights[0] += error * inputs[0] * self.speed
            self.weights[1] += error * inputs[1] * self.speed
        if len(self.weights) == 3:
            self.weights[0] += error * inputs[0] * self.speed
            self.weights[1] += error * inputs[0] * self.speed
            self.weights[2] += error * inputs[1] * self.speed
        if len(self.weights) == 4:
            self.weights[0] += error * inputs[0] * self.speed
            self.weights[1] += error * inputs[0] * self.speed
            self.weights[2] += error * inputs[0] * self.speed
            self.weights[3] += error * inputs[1] * self.speed
        # for x in range(0, len(self.weights)):
        #     self.weights[x] += error * inputs[x] * self.speed
        # print(self.weights)


class Trainer:
    def __init__(self, learning_rate, weights):
        self.perceptron = Perceptron(learning_rate, weights)

    def train(self, iterations, training_data):
        for j in range(0, iterations):  # trains the perceptron on the entire data set for the number of iterations
            for i in range(0, len(training_data)):  # goes through the training data and trains the perceptron
                y_coord = float(training_data[i][1])  # y coordinate is consumption in kiloWatts
                x_coord = float(training_data[i][0])  # x coordinate is time in hours from 5am to 8pm
                self.perceptron.train([x_coord, 1], y_coord)
        return self.perceptron  # return our trained perceptron


data = DataCollector()

# trainer_1 = Trainer(0.001, 2)  # creates a trainer with a learning rate of 0.01 and 2 weights
# perceptron_1 = trainer_1.train(500, data.trainging_data)
# print(perceptron_1.weights)
# Plot(data.data1, data.data2, data.data3, data.data4, perceptron_1.weights)
#
# trainer_2 = Trainer(0.0001, 3)  # creates a trainer with a learning rate of 0.01 and 3 weights
# perceptron_2 = trainer_2.train(10000, data.trainging_data)
# print(perceptron_2.weights)
# Plot(data.data1, data.data2, data.data3, data.data4, perceptron_2.weights)

trainer_3 = Trainer(0.00001, 4)  # creates a trainer with a learning rate of 0.01 and 3 weights
perceptron_3 = trainer_3.train(50000, data.trainging_data)
print(perceptron_3.weights)
Plot(data.data1, data.data2, data.data3, data.data4, perceptron_3.weights)

# print("Training Data")
# print(data.trainging_data)
# print("Day 1")
# print(data.data1)
# print("Day 2")
# print(data.data2)
# print("Day 3")
# print(data.data3)
# print("Test Day")
# print(data.data4)


