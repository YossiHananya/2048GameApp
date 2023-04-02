import pytest
from game.model.enums import Move
from game.model.board import Board


@pytest.mark.parametrize(
        (
            [
                [4, 0, 0 , 0],
                [2, 0, 0 , 0],
                [2, 0, 0 , 0],
                [0, 0, 0 , 0],
            ], 
            Move.Up,
            [
                [4, 0, 0 , 0],
                [4, 0, 0 , 0],
                [0, 0, 0 , 0],
                [0, 0, 0 , 0],
            ],
        )
)
def test_movement(table, move, excpected):
    board = Board(size=4)
    board._table = table
    board.move(move=move)
    assert board._table == excpected

