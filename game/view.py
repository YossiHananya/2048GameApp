

class View:
  
  @staticmethod
  def show_game_board(board):
    print(f"{'#' * 5} Game Table {'#' * 5}")
    for row in board.table:
      for cell in row:
        print(f" {cell} ", end='')
      print()

    print(f"{'#' * 25}")

  @staticmethod
  def get_next_move_from_user(valid_moves):
    
    while True:
      user_input = input(f"Please choose your next move from the following valid moves: {valid_moves}")

      if user_input in valid_moves:
        return user_input
      print(f"Invalid input: {user_input}")

  @staticmethod
  def show_game_results(results):
    print("Game end with status: {}")
  