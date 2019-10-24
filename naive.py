import sys
class cell:

  def __init__(self, gave = False, value = 0):
    self.given = gave
    self.defAnswer = value
    self.prov = 0
    self.possible = []
    for i in range(1, 10): self.possible.append(i)

  def toString(self):
    if self.defAnswer != 0: return str(self.defAnswer)
    else: return "_"

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

def createBoard(ary, index):
  board = []
  for i in range(index + 1, index + 10):
    for x in range(9):
      if ary[i][x] == "_": board.append(cell())
      else: board.append(cell(True, int(ary[i][x])))
  return board

def check(board):
  for i in range(len(Cliques)):
    has = []
    for imstupid in range(9): has.append(False)
    for x in range(9):
      has[board[Cliques[i][x]].defAnswer - 1] = True
    for z in range(9):
      if has[z] == False: return False
  return True

Cliques=[[0,1,2,3,4,5,6,7,8],\
[9,10,11,12,13,14,15,16,17],\
[18,19,20,21,22,23,24,25,26],\
[27,28,29,30,31,32,33,34,35],
[36,37,38,39,40,41,42,43,44],
[45,46,47,48,49,50,51,52,53],\
[54,55,56,57,58,59,60,61,62],\
[63,64,65,66,67,68,69,70,71],\
[72,73,74,75,76,77,78,79,80,],\
[0,9,18,27,36,45,54,63,72],\
[1,10,19,28,37,46,55,64,73],\
[2,11,20,29,38,47,56,65,74],
[3,12,21,30,39,48,57,66,75],\
[4,13,22,31,40,49,58,67,76],\
[5,14,23,32,41,50,59,68,77],\
[6,15,24,33,42,51,60,69,78],\
[7,16,25,34,43,52,61,70,79],\
[8,17,26,35,44,53,62,71,80],\
[0,1,2,9,10,11,18,19,20],\
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
    boards.append(createBoard(ary, i))
    i += 10
  else: i += 1
print(boardsToString())
print(check(boards[1]))
#to get Cliques
#row:
#column: position mod 9
#box:
print(10%9)
