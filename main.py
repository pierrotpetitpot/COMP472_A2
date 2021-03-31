
from depthFirst import depthFirstAlgorithm
from iterativeDeepening import iterativeDeepeningAlgorithm
from aStar import aStarBoth

# initial state of the puzzle
initial_state = [1, 2, 7, 4, 5, 6, 3, 8, 9]

# calls the different algorithm with the specified initial state
depthFirstAlgorithm(initial_state)
iterativeDeepeningAlgorithm(initial_state)
aStarBoth(initial_state)
