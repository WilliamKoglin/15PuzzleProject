import sys
from inputBFS import inputBoard
from solvableBFS import solvable
from algoBFS import BFS
from nodeBFS import Node

solution = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0)
initial = inputBoard()
if not solvable(initial):
    sys.exit("Board is not solvable")
else:

    print(BFS(Node(initial),solution))
