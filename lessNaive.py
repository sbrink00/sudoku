import sys
import time
#CELL __________________________________________________________________________
class cell:

  def __init__(self, num, given = False, value = 0):
    self.num = num
    self.definite = given
    self.defAnswer = value
    self.possible = []
    for i in range(1, 10): self.possible.append(i)

  def toString(self):
    if self.defAnswer != 0: return str(self.defAnswer)
    else: return "_"

#HEAP __________________________________________________________________________
#if a < b return -1
def comparator(cell1, cell2):
  if len(cell1.possible) == len(cell2.possible): return 0
  if len(cell1.possible) < len(cell2.possible): return -1
  return 1


class Pqueue:

  def __init__(self, comparator):
    self.compFunction = comparator
    self.ary = []
    self.ary.append(None)

  #added a method to clear the pqueue without having to sort it
  def clear(self): self.ary = [None]

  def push(self, thing):
    self.ary.append(thing)
    if (len(self.ary) == 2): return
    idx = len(self.ary) - 1
    while(self.compFunction(self.ary[idx], self.ary[int(idx/2)]) == -1):
      self.ary[idx],self.ary[int(idx/2)] = self.ary[int(idx/2)],self.ary[idx]
      idx = int(idx/2)
      if idx < 2: return

  def pop(self):
    if len(self.ary) == 1: return None
    self.ary[1],self.ary[len(self.ary) - 1] = self.ary[len(self.ary) - 1],self.ary[1]
    output = self.ary[-1]
    self.ary.pop(-1)
    idx = 1
    while True:
      left = idx * 2
      right = idx * 2 + 1
      if left >= len(self.ary): return output
      if right >= len(self.ary) and left < len(self.ary):
        cToLeft = self.compFunction(self.ary[idx], self.ary[left])
        if cToLeft == 1: self.ary[idx],self.ary[left] = self.ary[left],self.ary[idx]
        return output
      lToR = self.compFunction(self.ary[left], self.ary[right])
      if lToR == 1: switchIdx = right
      else: switchIdx = left
      if self.compFunction(self.ary[idx], self.ary[switchIdx]) == 1:
        self.ary[idx],self.ary[switchIdx] = self.ary[switchIdx],self.ary[idx]
        idx = switchIdx
      else: return output

  def getOrderedList(self):
    output = []
    while len(self.ary) > 1:
      output.append(self.pop())
    return output

#METHODS _______________________________________________________________________

def boardsToString():
  string = ""
  for board in boards:
    string += toString2d(board)
    string += "\n"
  return string

def orderedCellsToString(squares):
  string = ""
  for cell in squares:
    string += str(cell.num) + ","
  return string[:-1]

def toString2d(board):
  string = ""
  for i in range(len(board)):
    cell = board[i]
    string += str(cell.defAnswer)
    if i % 9 == 8: string += "\n"
    else: string += ","
  return string

def numEmpty(board):
  sum = 0
  for square in board:
    if square.defAnswer == 0: sum += 1
  return sum

def createBoard(ary, index):
  board = []
  num = 0
  for i in range(index + 1, index + 10):
    for x in range(9):
      if ary[i][x] == "_": board.append(cell(num))
      else: board.append(cell(num, True, int(ary[i][x])))
      num += 1
  return board

def genRCB(i):
  row = int(i / 9)
  col = i % 9 + 9
  box = 0
  for x in range(18, 27):
    if i in Cliques[x]: box = x
  return row,col,box

def remove(list, val):
  i = 0
  while i < len(list):
    if (list[i] == val):
      del list[i]
      i -= 1
    i += 1

def addNum(board, num, square):
  row,col,box = genRCB(square)
  for x in range(9):
    val = board[Cliques[row][x]].defAnswer
    if val == num and Cliques[row][x] != square: return False
    val = board[Cliques[col][x]].defAnswer
    if val == num and Cliques[col][x] != square: return False
    val = board[Cliques[box][x]].defAnswer
    if val == num and Cliques[box][x] != square: return False
  board[square].defAnswer = num
  return True

def modifyPossibilities(board):
  for i in range(len(board)):
    if not board[i].definite:
      row,col,box = genRCB(i)
      for x in range(9):
        val = board[Cliques[row][x]].defAnswer
        if val != 0:
          remove(board[i].possible, val)
        val = board[Cliques[col][x]].defAnswer
        if val != 0:
          remove(board[i].possible, val)
        val = board[Cliques[box][x]].defAnswer
        if val != 0:
          remove(board[i].possible, val)

def addForcedValues(board):
  added = True
  while added:
    added = False
    modifyPossibilities(board)
    for i in range(len(board)):
      if (not board[i].definite and len(board[i].possible) == 1):
        board[i].defAnswer = board[i].possible[0]
        board[i].definite = True
        added = True

def removeNum(board, square):
  board[square].defAnswer = 0

def makeOrderedCells(board):
  cellheap = Pqueue(comparator)
  for i in range(len(board)):
    if not board[i].definite: cellheap.push(boards[0][i])
  orderedCells = cellheap.getOrderedList()
  return orderedCells

def solve(board):
  #addForcedValues(board)
  squares = makeOrderedCells(board)
  print(orderedCellsToString(squares))
  print(toString2d(board))
  return solveHelper(board, 0, squares)

def solveHelper(board, n, squares):
  #print(n)
  if n == len(squares): return True
  for i in range(len(squares[n].possible)):
    if addNum(board, squares[n].possible[i], squares[n].num):
      if solveHelper(board, n + 1, squares): return True
      removeNum(board, squares[n].num)
  return False


def something():
  global headings
  global boards
  file = open(sys.argv[1], "r")
  ary = file.readlines()
  for i in range(len(ary)):
    ary[i] = ary[i].replace("\n", "")
    ary[i] = ary[i].split(",")
  i = 0
  while i < len(ary):
    if len(ary[i]) == 3:
      headings.append(ary[i])
      boards.append(createBoard(ary, i))
      i += 10
    else: i += 1
  return headings,boards

#GLOBALS AND TESTING _______________________________________________________________________
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
headings = []
boards = []
something()

t1 = time.time()
solve(boards[0])
print("Less naive time: " + str(time.time() - t1))
print(toString2d(boards[0]))
