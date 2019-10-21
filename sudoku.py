import readFile

board = readFile.setupAry(["testFile.txt", "answer.txt", "A1-1,Easy-NYTimes,unsolved"])
print(readFile.toString(board))

def ruleOut(r, c):
  for i in range(9):
    if board[r][i].defAnswer != 0 and i != c: board[r][c].possible.remove(board[r][i].defAnswer)
    if board[i][c].defAnswer != 0 and i != r: board[r][c].possible.remove(board[i][c].defAnswer)

def remove(list, value):
  for i in range(len(list)):
    if list[i] == value:
      del a[i]
      return

def ruleOutAll():
  for i in range(9):
    for x in range(9):
      ruleOut(i, x)

def printPossibilities():
  ruleOutAll()
  for i in range(9):
    for x in range(9):
      print(board[i][x].possible)

printPossibilities()
