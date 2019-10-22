import readFile
from cell import cell
import sys

def createBoard(ary, index):
  board = []
  for i in range(9): board.append([])
  for i in range(index + 1, index + 10):
    for x in range(9):
      if ary[i][x] == "_": board[i - index - 1].append(cell())
      else: board[i - index - 1].append(cell(True, int(ary[i][x])))
  return board

def toString2d(board):
  string = ""
  for i in range(len(board)):
    for x in range(9):
      print(board[i][x])
      if board[i][x].defAnswer == 0: s = "_"
      else: s = str(board[i][x].defAnswer)
      string += s + ","
    string = string[:-1] + "\n"
  string = string[:-1]
  return string

def toString1d(board):
  string = ""
  for i in range(len(board)): string += board[i].toString() + ","
  return string[:-1]

def boardsToString():
  string = ""
  for board in boards:
    string += toString1d(board)
    string += "\n\n"
  return string

def convertBoard1D(board):
  output = []
  for i in range(9):
    for x in range(9):
      output.append(board[i][x])
  return output

def returnIncorrectBoxes(board):
  outputs = []
  for i in range(9): bools.append(False)
  for i in range(9):
    has = []
    for i in range(9) has.append(False)
    print("bools: " + str(bools))
    for x in range(9):
      #print(board[cliquesBox[i][x]].defAnswer)
      has[board[cliquesBox[i][x]].defAnswer - 1] = True
    print(has)
    for z in range(9):
      if has[z] == False:
        outputs.append(i)
        break
  return outputs

cliquesBox = [[0,1,2,9,10,11,18,19,20],\
[3,4,5,12,13,14,21,22,23],\
[6,7,8,15,16,17,24,25,26],\
[27,28,29,36,37,38,45,46,47],\
[30,31,32,39,40,41,48,49,50],\
[33,34,35,42,43,44,51,52,53],\
[54,55,56,63,64,65,72,73,74],\
[57,58,59,66,67,68,75,76,77],\
[60,61,62,69,70,71,78,79,80]]

file = open(sys.argv[1], "r")
ary = file.readlines()
boards = []
for i in range(len(ary)):
  ary[i] = ary[i].replace("\n", "")
  ary[i] = ary[i].split(",")
i = 0
while i < len(ary):
  if len(ary[i]) == 3:
    boards.append(convertBoard1D(createBoard(ary, i)))
    i += 10
  else: i += 1
print(returnIncorrectBoxes(boards[1]))
