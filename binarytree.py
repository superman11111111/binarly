class Node():
  def __init__(self, v=0, parent=None, children=[]):
    self.v = v
    self.p = parent
    self.c = children
  def claim_children(self, nodes):
    # TODO: Implement better search than Linear Search
    for n in nodes:
      if n.parent == self:
        self.c.append(n)
  def find_parent(self, nodes):
    for n in nodes:
      if parent:
        return f"{self} already has a parent {self.parent}"
      if self in n.children:
        self.p = parent
  def find_root(self):
    c = self
    while c.p: c = c.p
    return c
  def __repr__(self):
    if self.p:
      return f"Node({self.v}, {self.p.v}, {len(self.c)})"
    return f"Node({self.v}, {self.p}, {len(self.c)})"
if __name__ == "__main__":
  import random
  n = None
  for i in range(10):
    # n = Node(random.randint(0,10), parent=n)
    n = Node(i, parent=n)
  print(n.find_root())
