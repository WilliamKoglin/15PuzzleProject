from AStarAlgo import traceBack, getNeighbors
from ANode import Node
# IDA*
def IDASolve(init,sol):
    #set flimit to initial node's fcost
    flimit = init.fCost
    #while true
    while True:
    # set var to IDFS(node, flimit)
        var = IDFS(init,flimit,sol)
        if type(var) == list:
            return var
        else:
            flimit = var
            
    # if ver returns a board, return board
    # else, set flimit to var

def IDFS(node, threshold, sol):
    #initialize thresh_candidate as max f-value of a 15 puzzle + 1
    thresh_candidate = 1000 #reasonable max f-cost
    #if node == sol, call traceback with node, return list
    if node.board == sol:
        return traceBack(node)
    #else cycle through getneighbors(node.board), we will call each node item
    else:
        for item in IDNeighbors(node):
            if item.fCost <= threshold:
                tval = IDFS(item,threshold,sol)
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
