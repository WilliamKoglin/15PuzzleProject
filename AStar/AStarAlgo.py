from heapq import heappop,heappush
from ANode import Node
    
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

#Returns list of tuples containing board and moved tile
def getNeighbors(board):
    blank = findBlank(board)
    if(blank%4==0):
        moves=[blank+1,blank-4,blank+4]
    elif(blank%4==3):
        moves=[blank-1,blank-4,blank+4]
    else:
        moves=[blank-1,blank+1,blank-4,blank+4]
    boards=[]
    for move in moves:
        if move>-1 and move<16:
            boards.append((newBoard(board,board[move]),board[move]))
    return boards

#Monolithic Function
def AStarSolve(init,sol):
    priorityHeap=[(init.fCost,init)]
    exp = {init.board}
    count = 0
    while priorityHeap:
        count +=1
        curr = heappop(priorityHeap)[1]
        if curr.board == sol:
            return traceBack(curr)
        else:
            for item in getNeighbors(curr.board):
                if item[0] not in exp:
                   newNode = Node(item[0],curr,item[1])
                   heappush(priorityHeap,(newNode.fCost,newNode))
                   exp.add(item[0])

def traceBack(node):
    moves = []
    while node.parent:
        moves.append(node.prev)
        node = node.parent
    return moves[::-1]

# IDA*
def IDASolve(init,sol):
    #set flimit to initial node's fcost
    flimit = init.fCost
    #while true
    while True:
    # set var to IDFS(node, flimit)
        var = IDFS(init,flimit)
        if type(var) == list:
            return var
        else:
            flimit = var
            
    # if ver returns a board, return board
    # else, set flimit to var

def IDFS(node, threshold):
    #initialize thresh_candidate as max f-value of a 15 puzzle + 1
    thresh_candidate = 1000 #reasonable max f-cost
    #if node == sol, call traceback with node, return list
    if node.board == (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0):
        return traceBack(node)
    #else cycle through getneighbors(node.board), we will call each node item
    else:
        for item in IDNeighbors(node):
            if item.fCost <= threshold:
                tval = IDFS(item,threshold)
                if type(tval) == list:
                    return tval
                if tval < thresh_candidate:
                    thresh_candidate = tval
            else:
                if thresh_candidate > item.fCost:
                    thresh_candidate = item.fCost
        return thresh_candidate
    #if item.fcost < threshold, check if < thresh_candidate idfs(item,threshold), if so, set thresh_candidate to that val
    #if item.fcost > threshold, check thresh_candidate against item.fcost
    #return thresh_candidate
    
def IDNeighbors(node):
    #return list of Nodes with boards one move away from away from node excluding pervious move.
    nodelist = []
    for item in (getNeighbors(node.board)):
        if item[1] == node.prev:
            continue
        else:
            nodelist.append(Node(item[0],node,item[1]))
    return nodelist
