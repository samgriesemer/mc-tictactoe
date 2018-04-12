from math import *
import random

import numpy as np

class Node:
  '''
  maintains state of nodes in
  the monte carlo search tree
  '''
  def __init__(self, parent=None, action=None, board=None):
    self.parent = parent
    self.board = board
    self.children = []
    self.wins = 0
    self.visits = 0
    self.untried_actions = board.get_moves()
    self.action = action

  def select(self):
    '''
    select child of node with 
    highest UCB1 value
    '''
    s = sorted(self.children, key=lambda c:c.wins/c.visits+0.2*sqrt(2*log(self.visits)/c.visits))
    return s[-1]

  def expand(self, action, board):
    '''
    expand parent node (self) by adding child
    node with given action and state
    '''
    child = Node(parent=self, action=action, board=board)
    self.untried_actions.remove(action)
    self.children.append(child)
    return child

  def update(self, result):
    self.visits += 1
    self.wins += result
    
  ###

  def __repr__(self):
    return "[M:" + str(self.action) + " W/V:" + str(self.wins) + "/" + str(self.visits) + " U:" + str(self.untried_actions) + "]"

  def TreeToString(self, indent):
    s = self.IndentString(indent) + str(self)
    for c in self.children:
      s += c.TreeToString(indent+1)
    return s

  def IndentString(self,indent):
    s = "\n"
    for i in range (1,indent+1):
        s += "| "
    return s

  def ChildrenToString(self):
    s = ""
    for c in self.children:
         s += str(c) + "\n"
    return s