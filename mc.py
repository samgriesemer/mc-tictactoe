from node import Node
from board import Board
import random

def UCT(rootstate, maxiters, verbose=False):

  root = Node(board=rootstate)

  for i in range(maxiters):
    node = root
    board = rootstate.copy()
    
    # selection - select best child if parent fully expanded and not terminal
    while node.untried_actions == [] and node.children != []:
      node = node.select()
      board.move(node.action)
      
    # expansion - expand parent to a random untried action
    if node.untried_actions != [] and not board.result():
      a = random.choice(node.untried_actions)
      board.move(a)
      node = node.expand(a, board.copy())

    while board.get_moves() != [] and not board.result():
      board.move(random.choice(board.get_moves()))

    # backpropagation
    while node != None:
      result = board.result()
      if result:
        if node.board.player==board.player:
          result = 1
        else: result = -1
      else: result = 0
      node.update(result)
      node = node.parent
      
  # Output some information about the tree - can be omitted
  if (verbose): print( root.TreeToString(0))
  else: print( root.ChildrenToString())

  s = sorted(root.children, key=lambda c:c.wins/c.visits)
  return {"action":s[-1].action, "children":root.get_children()}