import re
import Porter_Stemmer_Python
import ctypes as ctypes

class SentenceProcessor:
    def __init__(self):
        self.sentences = open("sentences.txt", "r", encoding="utf8")  # sets up file to read from
        self.processed = open("processed.txt", "w+", encoding="utf8")  # creates file to hold processed sentences
        self.stop_words = open("stop_words.txt", "r", encoding="utf8")
        self.stop = []
        self.create_stop_words()
        # print(self.stop)

        for i in range(46):
            self.current = " " + self.sentences.readline()  # sets current to a line in sentences.txt
            self.current = self.remove_characters()  # removes numbers and special characters
            self.current = self.current.lower()  # makes all characters lowercase
            self.current = self.remove_stop_words()  # removes stop words from sentences
            self.current = re.sub(' +', ' ', self.current)  # trims excess spaces
            self.current = self.current.split(' ')
            self.current.pop(0)
            self.current.pop(len(self.current) - 1)
            self.current.insert(len(self.current), "\n")
            print(self.current)
            for i in range(len(self.current)):
                if i < len(self.current) - 1:
                    line = self.current[i] + " "
                else:
                    line = self.current[i]
                self.processed.write(line)


    def remove_characters(self):
        line = self.current
        for char in '0123456789`~!@#$%^&*()-_=+[{]};:,<.>/?\'\"\n':
            line = line.replace(char, ' ')
        return line

    def create_stop_words(self):
        for i in range(119):
            word = self.stop_words.readline().replace("\n", "")
            word = " " + word + " "
            self.stop.append(word)

    def remove_stop_words(self):
        line = self.current
        for word in self.stop:
            line = line.replace(word, ' ')
        return line


sp = SentenceProcessor()

# p = Porter_Stemmer_Python.PorterStemmer()
# string = "villains".split('')
# print(p.stem(string, 0, 8))