from AInput import inputBoard
from ASolvable import solvable
from ANode import Node
from AStarAlgo import AStarSolve

testNode = Node(inputBoard())
sol = ((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0))
if (solvable(testNode.board)):
    print(f'Solution: {AStarSolve(testNode,sol)}')