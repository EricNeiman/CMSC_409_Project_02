import numpy as np
import matplotlib.pyplot as plt
import random

class Perceptron:

    def __init__(self, learn_speed, num_weights):
        self.speed = learn_speed

        self.weights = []
        for x in range(0, num_weights):
            self.weights.append(random.random() * 2 - 1)

        print(self.weights)

    def feed_forward(self, inputs):
        sum = 0.0
        # multiply inputs by weights and sum them
        for x in range(0, len(self.weights)):
            print(inputs[x])
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
        self.perceptron = Perceptron(0.1, 3)

    def train(self, iterations):
        training_data = open("data.txt")
        training_points = []

        i = 0
        while i < 4000:
            data_line = training_data.readline().strip("\n").split(",")
            data_tuple = (data_line.pop(0), data_line.pop(0), data_line.pop(0))
            training_points.append(data_tuple)
            if iterations == 1000 & i == 499:
                i += 1501  # jumps to the start of females
            else:
                if iterations == 3000 & i == 1499:
                    i += 501 # jumps to the start of females
                else:
                    i += 1

        for x in range(0, iterations): # 0 to 1000 or 3000
            current_point = training_points.pop()
            print(current_point)
            y_coord = float(current_point[0])
            x_coord = float(current_point[1])
            answer = current_point[2]

            if answer == 0: # 0 in data set is male
                answer = 1
            else:
                answer = -1

            self.perceptron.train([x_coord, y_coord, 1], answer)

        return self.perceptron  # return our trained perceptron


trainer = Trainer()
p = trainer.train(3000)

print("Female: " + str(p.feed_forward([56.35923863, 172.40367, 1])))
