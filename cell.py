class cell:

  def __init__(self, gave = False, value = 0):
    self.given = gave
    self.defAnswer = value
    self.prov = 0
    self.possible = []
    for i in range(1, 10): self.possible.append(i)

  def toString(self):
    return self.value

c = cell()
