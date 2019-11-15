#! /usr/bin/python
import sys
import time
import random
class cell:

  def __init__(self, gave = False, value = 0):
    self.given = gave
    self.defAnswer = value
    self.possible = []
    for i in range(1, 10): self.possible.append(i)

  def toString(self):
    if self.defAnswer != 0: return str(self.defAnswer)
    else: return "_"

def toString2d(board):
  string = ""
  for i in range(len(board)):
    cell = board[i]
    string += str(cell.defAnswer)
    if i % 9 == 8: string += "\n"
    else: string += ","
  return string

def equals(b1, b2):
  for i in range(81):
    if b1[i].defAnswer != b2[i].defAnswer: return False
  return True

def boardsToString():
  string = ""
  for board in boards:
    string += toString2d(board)
    string += "\n"
  return string

def createBoard(ary, index):
  board = []
  for i in range(index + 1, index + 10):
    for x in range(9):
      if ary[i][x] == "_": board.append(cell())
      else: board.append(cell(True, int(ary[i][x])))
  return board

def resetTimesUsed():
  global timesUsed
  for i in range(9): timesUsed[i] = 0

def genDictionary():
  dictionary = {}
  for i in range(81):
    tempAry = []
    row,col,box = genRCB(i)
    for x in range(9):
      if Cliques[row][x] != i: tempAry.append(Cliques[row][x])
      if Cliques[col][x] != i: tempAry.append(Cliques[col][x])
      if Cliques[box][x] != i: tempAry.append(Cliques[box][x])
    tempAry = list(set(tempAry))
    dictionary[i] = tempAry
  return dictionary

def randomizePossibilities(board):
  for i in range(len(board)):
    if not board[i].given:
      randomize(board[i].possible)

def randomize(ary):
  for i in range(5):
    idx1 = random.randint(0, len(ary) - 1)
    idx2 = random.randint(0, len(ary) - 1)
    ary[idx1],ary[idx2] = ary[idx2],ary[idx1]

def check(board):
  for i in range(len(Cliques)):
    has = []
    for imstupid in range(9): has.append(False)
    for x in range(9):
      has[board[Cliques[i][x]].defAnswer - 1] = True
    for z in range(9):
      if has[z] == False: return False
  return True

def remove(list, val):
  i = 0
  while i < len(list):
    if (list[i] == val):
      del list[i]
      i -= 1
    i += 1

def genRCB(i):
  row = int(i / 9)
  col = i % 9 + 9
  box = 0
  for x in range(18, 27):
    if i in Cliques[x]: box = x
  return row,col,box

def modifyPossibilities(board):
  global dictionary
  for i in range(len(board)):
    if not board[i].given:
      for x in range(20):
        val = board[dictionary[i][x]].defAnswer
        if val != 0:
          remove(board[i].possible, val)

def addNum(board, num, square):
  global timesUsed
  global dictionary
  if timesUsed[num - 1] == 9: return False
  for i in range(20):
    if board[dictionary[square][i]].defAnswer == num: return False
  board[square].defAnswer = num
  timesUsed[num - 1] += 1
  return True

def removeNum(board, square):
  global timesUsed
  global backtracks
  timesUsed[board[square].defAnswer - 1] -= 1
  board[square].defAnswer = 0
  backtracks += 1

def solve(board):
  modifyPossibilities(board)
  randomizePossibilities(board)
  return solveHelper(board, 0)

def solveHelper(board, square):
  if square == len(board): return True
  if board[square].given:
    if solveHelper(board, square + 1): return True
  else:
    for i in range(len(board[square].possible)):
      if addNum(board, board[square].possible[i], square):
        if solveHelper(board, square + 1): return True
        removeNum(board, square)
  return False

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
timesUsed = []
for i in range(9): timesUsed.append(0)
backtracks = 0
dictionary  = genDictionary()

def something():
  file = open(sys.argv[1], "r")
  ary = file.readlines()
  boards = []
  headings = []
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

def findAndSolve():
  headings,boards = something()
  heading = sys.argv[3]
  for i in range(len(headings)):
    if heading in headings[i][0]:
      return i,headings,boards
  return 0,headings,boards

def solveBoard():
  boardNum,headings,boards = findAndSolve()
  solve(boards[boardNum])
  return boardNum,headings,boards

def writeFile():
  num,headings,boards = solveBoard()
  heading = str(headings[num][0]) + "," + str(headings[num][1]) + "," + "solved\n"
  board = toString2d(boards[num])
  string = board[:-1]
  file = open(sys.argv[2], "w")
  file.write(string)

def writeFile2():
  headings,boards = something()
  file = open(sys.argv[2], "w")
  string = ""
  for i in range(len(boards)):
    string += headings[i][0] + ": Time - "
    startTime = time.time()
    solve(boards[i])
    totalTime = time.time() - startTime
    global backtracks
    string += str(round(totalTime, 2)) + ". Backtracks - " + str(backtracks) + ".\n"
    backtracks = 0
    resetTimesUsed()
  string = string[:-1]
  file.write(string)

def writeFile3():


writeFile2()
#what is n
#one million phrases per second
#10^88 monkeys
#since big bang(13.73 billion)
#what is largest guarenteed phrase
#100 characters possible
