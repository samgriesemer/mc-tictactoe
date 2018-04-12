import numpy as np

class Board:
  '''
  class handling state of the board
  '''

  def __init__(self, state=None):
    if state == None:
      self.state = np.zeros([2,3,3])
    else:
      self.state = np.array(state)
    self.player = 0 # current player's turn

  def copy(self):
    '''
    make copy of the board
    '''
    copy = Board()
    copy.player = self.player
    copy.state = np.copy(self.state)
    return copy

  def move(self, move):
    '''
    take move of form [x,y] and play
    the move for the current player
    '''
    if np.any(self.state[:,move[0],move[1]]): return False
    self.state[self.player][move[0],move[1]] = 1
    self.player ^= 1
    return True

  def get_moves(self):
    '''
    return remaining possible board moves
    (ie where there are no O's or X's)
    '''
    if self.result():
        return []
    
    return np.argwhere(self.state[0]+self.state[1]==0).tolist()

  def result(self):
    '''
    check rows, columns, and diagonals
    for sequence of 3 X's or 3 O's
    '''
    board = self.state[self.player^1]
    col_sum = np.any(np.sum(board,axis=0)==3)
    row_sum = np.any(np.sum(board,axis=1)==3)
    d1_sum  = np.any(np.trace(board)==3)
    d2_sum  = np.any(np.trace(np.flip(board,1))==3)
    return col_sum or row_sum or d1_sum or d2_sum