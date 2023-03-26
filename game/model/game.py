import random
from .board import Board
from .enums import Move, GameStatus

class GameModel:
  
  def __init__(self):
    self._status = GameStatus.Initialize
    self._board = Board(size=4)
    for i in range(2):
      self._fill_empty_tile_randomally()
    self._valid_moves = [move for move in Move]
    self._status = GameStatus.Running
  
  @property
  def is_done(self) -> bool:
    return self._status in [GameStatus.Win, GameStatus.Lose]
    
  @property
  def board(self):
    return self._board

  @property
  def results(self):
    return dict(status=self._status)

  @property
  def valid_moves(self) -> bool:
    return self._valid_moves
    
  def move(self, move: Move):
    self._board.move(move=move)
    self._fill_empty_tile_randomally()
    self._update_valid_moves()
    self._update_status()    

  def _fill_empty_tile_randomally(self):
    empty_tiles = self._board.get_empty_tiles()

    if not empty_tiles:
      return
      
    chosen_empty_tile = random.choice(empty_tiles)
    row, col = chosen_empty_tile
    
    self._board.update_tile(
      row=row,
      col=col,
      value=random.choice([2 , 4]) 
    )
  
  def _update_valid_moves(self):
    self._valid_moves = [move for move in Move if self._board.can_move(move=move)]

  def _update_status(self):
    if len(self.valid_moves) != 0:
      self._status = GameStatus.Lose

    for i in range(self._board.size):
      for j in range(self._board.size):
        if self._board.get_tile_value(row=i, col=j) == 2048:
          self._status = GameStatus.Win
          return

    self._status = GameStatus.Running
          
          