#! /usr/bin/env python

from game.control import GameControl 
from game.model.game import GameModel
from game.view import View 


def main():
  view=View()
  model=GameModel()
  game = GameControl(model=model, view=view)
  game.start()

if __name__ == '__main__':
  main()