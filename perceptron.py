import numpy as np
import matplotlib.pyplot as plt
import random


class Perceptron:

    def __init__(self, learn_speed, num_weights):
        self.speed = learn_speed

        self.weights = []
        for x in range(0, num_weights):
            self.weights.append(random.random() * 2 - 1)
        # print(self.weights)

    def feed_forward(self, inputs):
        sum = 0.0
        # multiply inputs by weights and sum them
        for x in range(0, len(self.weights)):
            # print(inputs[x])
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
        male_points = []
        female_points = []

        i = 0
        while i < 4000:
            data_line = training_data.readline().strip("\n").split(",")
            data_tuple = (data_line.pop(0), data_line.pop(0), data_line.pop(0))
            if i < 2000:
                male_points.append(data_tuple)
            else:
                female_points.append(data_tuple)
            i += 1
            # print(data_tuple)

        i = 0
        while i < iterations:  # 0 to 1000 or 3000
            if iterations == 1000:
                if i % 2 == 0:
                    current_point = male_points.pop()
                else:
                    current_point = female_points.pop()
            if iterations == 3000:
                if i % 2 == 0:
                    current_point = male_points.pop()
                else:
                    current_point = female_points.pop()

            print(i)
            print(current_point)
            y_coord = float(current_point[0])
            x_coord = float(current_point[1])
            answer = current_point[2]
            if answer == 0:  # 0 in data set is male
                answer = 1
            else:  # 1 in the data set is female
                answer = -1
            self.perceptron.train([x_coord, y_coord, 1], answer)
            i += 1

        return self.perceptron  # return our trained perceptron


trainer = Trainer()
p = trainer.train(3000)

print(p.weights)
print("Female: " + str(p.feed_forward([56.35923863, 172.40367, 1])))
