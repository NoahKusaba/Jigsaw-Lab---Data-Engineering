class simpleGame:
  def __init__(self):
    self.state = []
    self.create_board()
    self.turns = 0
    self.valid = True
    #add id? to store
    self.XorO = ["X","O"]


  def startGame(self):
    print(f"Game Starting")

    while self.valid:
      
      for row in self.state:
        print(row)

      print(f"input coordinates in x , y format")
      playerInput = (int(input()),int(input()))
      if self.addBoard(playerInput): # if coordinates are valid 
        
        self.turns +=1
        gameState = self.checkState()
        if gameState and self.turns >=5:
          print(gameState)
          break
      else:
        print("error")

  def create_board(self):
      for i in range(3):
          row = []
          for j in range(3):
              row.append('-')
          self.state.append(row)

  def addBoard(self,input):
    

    if self.state[input[0]][input[1]] == "-":
      self.state[input[0]][input[1]] = self.XorO[0]
      self.XorO.reverse()
      return True
    else:
      return False

  def checkState(self):
  
    def checkWin(x,o):
      if x == 3:
        return "X wins "
      elif o == 3:
        return "O wins"
      else: 
        return 0

    def checkDiagonal(state):
      xCount = 0
      xxCount = 0
      oCount = 0 
      ooCount = 0      
      #check forward diagonal
      for index in range (0,3):
        if state[index][index] == "X":
          xCount +=1 
        elif state[index][index] == "O":
          oCount +=1
      win = checkWin(xCount,oCount)
      if win:
        return win
      #check backward diagonal 210, 012 [0][2], [1][1], [2][0]
      for index in range (2,-1, -1):
        if state[index][index] == "X":
          xxCount +=1 
        elif state[index][index] == "O":
          ooCount +=1
      winB = checkWin(xxCount,ooCount)
      if winB:
        return winB
      return 0

    def checkTie(state):
      count= 0
      for row in state:
        for rowindex in row:
          if rowindex == "X" or  rowindex == "O":
            count +=1
      if count == 9:
        return "Tie no Win "

    def rowWin(state):
      for row in state:
        xCount = 0
        oCount = 0
        for rowindex in row: 
          if rowindex == "X":
            xCount+= 1 
          elif rowindex =="O":
            oCount+=1 
        win = checkWin(xCount,oCount)
        if win:
          return win

    #Vertical Wins: 
    def columnWin(state):
      for column in range(0,3):
        xCount = 0
        oCount = 0 
        for row in state: 
          if row[column] == "X":
            xCount +=1 
          elif row[column] == "O":
            oCount +=1
        win = checkWin(xCount,oCount)
        if win:
          return win

    # Run check win functions
    win = rowWin(self.state)
    if win:
      return win
    win = columnWin(self.state)
    if win:
      return win
    win = checkDiagonal(self.state)
    if win:
      return win
    tie = checkTie(self.state)
    if tie:
      return tie
    return None




