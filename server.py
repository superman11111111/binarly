from flask import Flask
from binarytree import Node
app = Flask(__name__)

@app.route('/')
def hello_world():
  import random
  n = None
  for i in range(10):
    # n = Node(random.randint(0,10), parent=n)
    n = Node(i, parent=n)
  print(n.find_root())
  return str(n)

if __name__ == "__main__":
  app.run(debug=True)
