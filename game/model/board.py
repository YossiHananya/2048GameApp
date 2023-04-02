from .enums import Move

class Board:
  def __init__(self, size):
    self._size = size
    self._board = [[0] * size for i in range(size)]

  @property
  def table(self):
    return self._board
  
  @property
  def size(self):
    return self._size
    
  def get_empty_tiles(self):
    empty_tiles = list()

    for i in range(self._size):
      for j in range(self._size):
        if self.is_tile_empty(row=i, col=j):
          empty_tiles.append((i,j))

    return empty_tiles
    
  def is_tile_empty(self, row: int, col: int):
    return self._board[row][col] == 0

  def update_tile(self, row:int, col:int, value:int):
    self._board[row][col] = value
  
  def get_tile_value(self, row:int, col:int):
    return self._board[row][col]

  def can_move(self, move):
    for i in range(self._size):
      for j in range(self._size):
        if self.can_tile_move(row=i, col=j, move=move):
          return True

    return False
    
  def can_tile_move(self, row, col, move, merged_tiles = {}):
    if self.is_tile_empty(row=row, col=col):
      return False

    if move == Move.Up:
      limit_check = row > 0
      neighbor = (row - 1, col)
    elif move == Move.Down:
      limit_check = row < (self._size - 1)
      neighbor = (row + 1, col)
    elif move == Move.Left:
      limit_check = col > 0
      neighbor = (row, col - 1)
    elif move == Move.Right:
      limit_check = col < (self._size - 1)
      neighbor = (row, col + 1)

    if not limit_check:
      return False
    
    if neighbor in merged_tiles:
      return False
    
    if self.is_tile_empty(row=neighbor[0], col=neighbor[1]):
      return True
    
    return self.get_tile_value(row=row, col=col) == self.get_tile_value(row=neighbor[0], col=neighbor[1])


  def move_tile(self, row, col, move, merged_tiles):

    if not self.can_tile_move(row, col, move, merged_tiles):
      return
      
    if move == Move.Up:
      neighbor = (row - 1, col)
      new_value = self._board[row][col] + self.get_tile_value(row=row - 1, col=col) 
    elif move == Move.Down:
      neighbor = (row + 1, col)
      new_value = self._board[row][col] + self.get_tile_value(row=row + 1, col=col)
    elif move == Move.Left:
      neighbor = (row, col - 1)
      new_value = self._board[row][col] + self.get_tile_value(row=row, col=col - 1)
    elif move == Move.Right:
      neighbor = (row, col + 1)
      new_value = self._board[row][col] + self.get_tile_value(row=row, col=col + 1)

    if not self.is_tile_empty(row=neighbor[0], col=neighbor[1]):
      merged_tiles.add(neighbor)

    self.update_tile(
      row = neighbor[0], 
      col = neighbor[1], 
      value = self._board[row][col] + self.get_tile_value(row=neighbor[0], col=neighbor[1])
    )
    
    self.update_tile(row = row, col = col, value = 0)
    
    self.move_tile(
      row = neighbor[0], 
      col = neighbor[1], 
      move=move,
      merged_tiles=merged_tiles
    )

  def move(self, move):
    merged_tiles = set()

    order = list(range(self.size))

    if move in [Move.Down, Move.Right]:
      order = list(reversed(order))
      
    if move in [Move.Up, Move.Down]:
      for col in range(self._size):
        for row in order:
          self.move_tile(row=row, col=col, move=move, merged_tiles=merged_tiles)

    if move in [Move.Left, Move.Right]:
      for row in range(self._size):
        for col in order:
          self.move_tile(row=row,col=col, move=move, merged_tiles=merged_tiles)
