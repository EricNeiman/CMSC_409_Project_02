import numpy as np
import matplotlib.pyplot as plt
import random

class Perceptron:

    def __init__(self, learn_speed, num_weights):
        self.speed = learn_speed

        self.weights = []
        for x in range(0, num_weights):
            self.weights.append(random.random() * 2 - 1)

    def feed_forward(self, inputs):
        sum = 0
        # multiply inputs by weights and sum them
        for x in range(0, len(self.weights)):
            sum += self.weights[x] * inputs[x]
        # return the 'activated' sum
        return self.activate(sum)

    def activate(self, num):
        # turn a sum over 0 into 1, and below 0 into -1
        if num > 0:
            return 1
        return -1

    def train(self, inputs, desired_output):
        guess = self.feed_forward(inputs)
        error = desired_output - guess

        for x in range(0, len(self.weights)):
            self.weights[x] += error * inputs[x] * self.speed


class Trainer:

    def __init__(self):
        self.perceptron = Perceptron(0.01, 3)

    def f(self, x):
        return 0.5 * x + 10  # line: f(x) = 0.5x + 10

    def train(self):
        for x in range(0, 1000000):
            x_coord = random.random() * 500 - 250
            y_coord = random.random() * 500 - 250
            line_y = self.f(x_coord)

            if y_coord > line_y:  # above the line
                answer = 1
                self.perceptron.train([x_coord, y_coord, 1], answer)
            else:  # below the line
                answer = -1
                self.perceptron.train([x_coord, y_coord, 1], answer)
        return self.perceptron  # return our trained perceptron



data = open("data.txt")
dataPoints = []
i = 0
while i < 4000:
    dataLine = data.readline().strip("\n").split(",")
    dataTuple = (dataLine.pop(0), dataLine.pop(0), dataLine.pop(0))
    dataPoints.append(dataTuple)
    i += 1

print(len(dataPoints))

# i = 0
# while i < 4000:
#     print(dataPoints[i])
#     i += 1


trainer = Trainer()
p = trainer.train()

print("(-7, 9): " + str(p.feed_forward([-7, 9, 1])))
print("(3, 1): " + str(p.feed_forward([3, 1, 1])))