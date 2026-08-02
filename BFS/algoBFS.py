from nodeBFS import Node
from collections import deque

#initialize queue and explored
def BFS(init,sol):
    queue = deque([init])
    explored = {init.board}
    while True:
        current = queue.popleft()
        if current.board == sol:
            path = []
            while True:
                if current.prev == None:
                    return path[::-1]
                path.append(current.prev)
                current = current.parent
        neighbors = getNeighbors(current.board)
        for board,prev in neighbors:
            if board not in explored:
                explored.add(board)
                queue.append (Node(board,current,prev))

#Finds index of blank
def findBlank(board):
    for tileIndex in range(len(board)):
        if board[tileIndex] == 0:
            return tileIndex

#Finds tiles and swaps blank and tile
def newBoard(board,move):
    newB = []
    for tile in range(len(board)):
        if(board[tile]==0):
            newB.append(move)
        elif(board[tile]==move):
            newB.append(0)
        else:
            newB.append(board[tile])
    return tuple(newB)


def getNeighbors(board):
    blank = findBlank(board)
    out=[]

    if blank%4==0:
        moves = [blank + 1, blank + 4, blank - 4]
    elif blank%4==3:
        moves = [blank - 1, blank + 4, blank - 4]
    else:
        moves = [blank + 1, blank - 1, blank + 4, blank - 4]
    
    for move in moves:
        if (move>-1 and move < 16):
            out.append(((newBoard(board,board[move])),board[move]))
    return out
