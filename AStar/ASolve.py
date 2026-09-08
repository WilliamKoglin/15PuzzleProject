from AInput import inputBoard
from ASolvable import solvable
from ANode import Node
from AStarAlgo import AStarSolve


def main():
    testNode = Node((1,2,3,4,5,6,7,8,9,10,11,12,0,13,14,15))
    sol = ((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0))
    if (solvable(testNode.board)):
        print(f'Solution: {AStarSolve(testNode,sol)}')
    else:
        print("Board Not Solvable")

if __name__ == "__main__":
    main()
