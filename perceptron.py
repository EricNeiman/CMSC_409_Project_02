import numpy as np
import matplotlib.pyplot as plt
import random


class Plot:
    def __init__(self, male_points, female_points, weights):
        m_heights = np.empty((2000, 1))
        m_weights = np.empty((2000, 1))
        f_heights = np.empty((2000, 1))
        f_weights = np.empty((2000, 1))

        i = 0
        while i < 2000:
            m_tuple = male_points.pop(0)
            m_height = m_tuple[0]
            m_weight = m_tuple[1]
            m_heights[i] = m_height
            m_weights[i] = m_weight
            f_tuple = female_points.pop(0)
            f_height = f_tuple[0]
            f_weight = f_tuple[1]
            f_heights[i] = f_height
            f_weights[i] = f_weight
            i += 1

        x_weight = weights.pop(0)
        y_weight = weights.pop(0)
        bias = weights.pop(0)
        x = np.linspace(0, .3, 50)
        y = ((x_weight * x) + bias) / y_weight

        plt.plot(x, y, 'g--')

        # plt.ylim(0, 1)
        plt.xlim(0, 0.3)
        plt.ylabel('Height (Inches)')
        plt.xlabel('Weight (Pounds)')
        plt.plot(m_weights, m_heights, 'ro', f_weights, f_heights, 'bo')
        plt.show()


class DataCollector:
    def __init__(self):
        data = open("data.txt")
        self.male_points = []
        self.female_points = []
        max_height = 87.
        min_height = 45.
        max_weight = 220.
        min_weight = 153.
        i = 0
        while i < 4000:
            data_line = data.readline().strip("\n").split(",")
            data_tuple = ((float(data_line.pop(0)) - min_height) / max_height, (float(data_line.pop(0)) - min_weight) / max_weight, data_line.pop(0))
            if i < 2000:
                self.male_points.append(data_tuple)
            else:
                self.female_points.append(data_tuple)
            i += 1


class Perceptron:
    def __init__(self, learn_speed, num_weights):
        self.speed = learn_speed
        self.weights = []
        for x in range(0, num_weights):
            self.weights.append(random.random())  # randomly assigns the weights
        print(self.weights)

    def feed_forward(self, inputs):
        sum = (self.weights[0] * inputs[0]) + (self.weights[1] * inputs[1]) + (self.weights[2] * inputs[2])
        return self.activate(sum)  # return the value from the soft/hard activation

    def activate(self, num):
        # # hard activation function
        if num > 0:
            return 1
        return 0
        # # soft activation function (tanh)
        # return np.tanh(num)

    def train(self, inputs, desired_output):
        guess = self.feed_forward(inputs)
        error = desired_output - guess

        for x in range(0, len(self.weights)):
            self.weights[x] += error * inputs[x] * self.speed


class Trainer:
    def __init__(self):
        weights = 3
        learning_rate = 0.01
        self.perceptron = Perceptron(learning_rate, weights)

    def train(self, iterations, male_points, female_points):
        i = 0
        while i < iterations:  # 0 to 1000 or 3000
            if i % 2 == 0:
                current_point = male_points.pop()
            else:
                current_point = female_points.pop()
            y_coord = float(current_point[0])  # y coordinate is height in inches
            x_coord = float(current_point[1])  # x coordinate is weight in pounds
            answer = current_point[2]  # answer = 0 for male and 1 for female
            if answer == 0:  # 0 in data set is male
                answer = 1
            else:  # 1 in the data set is female
                answer = 0
            self.perceptron.train([x_coord, y_coord, 1], answer)
            i += 1
        return self.perceptron  # return our trained perceptron


data = DataCollector()
m_training_points = data.male_points.copy()
f_training_points = data.female_points.copy()
trainer = Trainer()
p = trainer.train(1000, m_training_points, f_training_points)
pweights = p.weights.copy()
xweight = pweights.pop(0)
yweight = pweights.pop(0)
bias = pweights.pop(0)

plot = Plot(data.male_points, data.female_points, p.weights)
print("y = (" + str(xweight) + "x + " + str(bias) + ") / " + str(yweight))
