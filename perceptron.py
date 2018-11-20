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

        # plt.plot(x, y, 'g--')

        plt.ylim(0, 10)
        plt.xlim(5, 20)
        plt.ylabel('kiloWatts')
        plt.xlabel('hours')
        plt.plot(x1, y1, 'ro', x2, y2, 'bo', x3, y3, 'yo', x4, y4, 'go')
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

    def populate_array(self, data):
        day = []
        for i in range(0, 16):
            data_line = data.readline().strip("\n").split(",")
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
print("Day 1")
print(data.data1)

print("\nDay 2")
print(data.data2)

print("\nDay 3")
print(data.data3)

print("\nTest Day")
print(data.data4)

Plot(data.data1, data.data2, data.data3, data.data4, 0)

