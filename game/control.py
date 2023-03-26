from .model.enums import Move


Arrows_map = {
  Move.Up: ['w', 'W'],
  Move.Down: ['s', 'S'],
  Move.Left: ['a', 'A'],
  Move.Right: ['d', 'D']
}

class GameControl:

  def __init__(self, model, view):
      self.model = model
      self.view = view

  def start(self):
      while not self.model.is_done:
        self.view.show_game_board(board=self.model.board)
        allowed_inputs=[] 
        
        for move in self.model.valid_moves:
          allowed_inputs.extend(Arrows_map[move])
        
        next_move_input = self.view.get_next_move_from_user(
                      valid_moves=allowed_inputs
        )

        selected_move = None
        for move in Move:
          if next_move_input in Arrows_map[move]:
            selected_move = move
            
        results = self.model.move(move=selected_move)
        
      self.view.show_game_results(self.model.results)