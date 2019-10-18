class cell:

  def __init__(self):
    self.given = False
    self.defAnswer = 0
    self.prov = 0
    self.possible = []
    for i in range(1, 10): self.possible.append(i)

c = cell()
