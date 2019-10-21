import sys
from cell import cell

board = []
for i in range(9): board.append([])

def setupAry(alist = None):
  if alist == None: alist = ["placeholder"] + sys.argv
  else: alist = ["placeholder"] + alist
  global args
  args = alist
  print(args)
  global name
  name = args[3]
  file = open(args[1], "r")
  ary = file.readlines()
  idx = -1
  for i in range(len(ary)):
    ary[i] = ary[i].replace("\n","")
    if ary[i] == args[3]: idx = i
  if idx < 0: print("ERROR")
  nums = []
  for i in range(idx + 1, idx + 10): nums.append(ary[i].split(","))
  for i in range(len(nums)):
    for x in range(9):
      if (nums[i][x].isdigit()): board[i].append(cell(True, int(nums[i][x])))
      else: board[i].append(cell())
  return board

def writeFile(generated = True):
  if not generated: setupAry()
  string = toString(board)
  file = open(args[2], "w")
  pythonDoesntWork = name.replace("unsolved","solved")
  string = pythonDoesntWork + "\n" + string
  file.write(string)

def toString(bord):
  string = ""
  for i in range(len(bord)):
    for x in range(9):
      if bord[i][x].defAnswer == 0: s = "_"
      else: s = str(bord[i][x].defAnswer)
      string += s + ","
    string = string[:-1] + "\n"
  string = string[:-1]
  return string

#writeFile(False)
#print(toString(board))
