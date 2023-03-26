from enum import Enum


class GameStatus(Enum):
  Initialize = 1
  Running = 2
  Lose = 3
  Win = 4


class Move(Enum):
  Up = 1
  Down = 2
  Left = 3
  Right = 4