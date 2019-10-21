import readFile
import sys

file = open(sys.argv[1], "r")
ary = file.readlines()
boards = []
i = 0
while i < len(ary):
  ary[i] = ary[i].split(",")
  if len(ary[i]) == 3:
    a = 4

def createBoard(ary, index):
  board = []
  for i in range(9): board[i].append([])
  for i in range(index + 1, index + 10):
    for x in range(9):
      board[i].append(cell(True, int())
