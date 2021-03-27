from node import Node
import random
import copy
from queue import LifoQueue
import copy
from depthFirst import depthFirstAlgorithm
from iterativeDeepening import iterativeDeepeningAlgorithm


def randomGen():
    f = open("20.txt", "w")
    for x in range(20):
        list = random.sample(range(1, 10), 9)
        f.write(str(list))
        f.write("\n")
    f.close


randomGen()

initial_state = [1, 2, 7, 4, 5, 6, 3, 8, 9]

my_file = open("20.txt", "r")
content_list = my_file.readlines()

# depthFirstAlgorithm(content_list)
# iterativeDeepeningAlgorithm(content_list)

depthFirstAlgorithm(initial_state)
# iterativeDeepeningAlgorithm(initial_state)
