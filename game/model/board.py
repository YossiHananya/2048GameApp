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
    
  def can_tile_move(self, row, col, move):
    if move == Move.Up:
      return row > 0 and self._board[row - 1][col] in [0, self._board[row][col]]
    elif move == Move.Down:
      return row < (self._size - 1) and self._board[row + 1][col] in [0, self._board[row][col]] 

    elif move == Move.Left:
      return col > 0 and self._board[row][col - 1] in [0, self._board[row][col]]

    elif move == Move.Right:
      return col < (self._size - 1)  and self._board[row][col + 1] in [0, self._board[row][col]]

  def move_tile(self, row, col, move):
    if not self.can_tile_move(row, col, move):
      return
      
    if move == Move.Up:
      new_location_row = row - 1
      new_location_col = col
      new_value = self._board[row][col] + self.get_tile_value(row=row - 1, col=col) 
    elif move == Move.Down:
      new_location_row = row + 1
      new_location_col = col
      new_value = self._board[row][col] + self.get_tile_value(row=row + 1, col=col)
    elif move == Move.Left:
      new_location_row = row
      new_location_col = col - 1
      new_value = self._board[row][col] + self.get_tile_value(row=row, col=col - 1)
    elif move == Move.Right:
      new_location_row = row
      new_location_col = col + 1
      new_value = self._board[row][col] + self.get_tile_value(row=row, col=col + 1)

    self.update_tile(
      row = new_location_row, 
      col = new_location_col, 
      value = new_value
    )
    
    self.update_tile(row = row, col = col, value = 0)
    
    self.move_tile(
      row = new_location_row, 
      col = new_location_col, 
      move=move
    )

  def move(self, move):
    order = list(range(self.size))

    if move in [Move.Down, Move.Right]:
      order = list(reversed(order))
      
    if move in [Move.Up, Move.Down]:
      for col in range(self._size):
        for i in order:
          self.move_tile(row=i,col=col, move=move)
      
    if move in [Move.Left, Move.Right]:
      for row in range(self._size):
        for i in order:
          self.move_tile(row=row,col=i, move=move)