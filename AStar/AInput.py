#Basic input checks to see if the user inputs a number
def getInput():
    while True:
        num = input("Enter a Number: ")
        try:
            out = int(num)
        except:
            print("Please input a valid number.")
        else:
            break
    return(out)

#Function for getting input for a slot on the grid. Checks for valid input
def inputGrid(grid,curRow,curNum):
    while (True):
        if(any(curNum in row for row in grid) or curNum in curRow):
            print("No duplicates allowed, please try again")
            curNum=getInput()
        elif(curNum<0 or curNum>15):
            print("Please make sure number is in valid range (0-15)")
            curNum=getInput()
        else:
            break
    return(curNum)

#Tupalizes a board if possible
def tupalize (inputedBoard):
    listIn=[]
    for row in inputedBoard:
        for val in row:
            listIn.append(val)
    board = tuple(listIn)
    return(board)


#Initiallizes the input of a board
def inputBoard():
    grid=[]
    for x in range(4):
        row=[]
        for y in range(4):
            row.append(inputGrid(grid,row,getInput()))
        grid.append(row)
    return (tupalize(grid))
