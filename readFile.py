import sys
from cell import cell

board = []

def setupAry():
  file = open(sys.argv[1], "r")
  ary = file.readlines()
  idx = 0
  for i in range(len(ary)):
    if ary[i] == sys.argv[3]: idx = i
  nums = []
  for i in range(idx + 1, idx + 10): nums.append(ary[i].split(","))
  for i in range(len(nums)):
    for x in range(9):
      print(x)
      if (nums[i][x].isdigit()): board.append(cell(True, int(nums[i][x])))
      else: board.append(cell())

def genOutput(generated = True):
  if not generated: setupAry()
  string = ""
  for i in range(len(board)):
    if board[i].defAnswer == 0: s = "_"
    else: s = str(board[i].defAnswer)
    if i % 9 == 1: string += s + "\n"
    else: string += s + ","
  string = string[:-1]
  return string


print(genOutput(False))
