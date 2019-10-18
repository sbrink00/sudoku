import sys

board = []

def getAry():
  file = open(sys.argv[1], "r")
  ary = file.readlines()
  for i in range(ary):
    if ary[i] == sys.argv[3]: idx = i
  nums = []
  for i in range(idx + 1, idx + 10): nums.append(ary[idx].split(","))
  for i in range(len(nums)):
    for x in range(9):
      board[9*i + x]
