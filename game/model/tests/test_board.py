import pytest
from game.model.enums import Move
from game.model.board import Board


@pytest.mark.parametrize(
    ("table", "move", "expected"),
    [
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
        ),
        
        
        (
            [
                [8, 4, 4 , 0],
                [0, 0, 0 , 0],
                [0, 0, 0 , 0],
                [0, 0, 0 , 0],
            ], 
            Move.Left,
            [
                [8, 8, 0 , 0],
                [0, 0, 0 , 0],
                [0, 0, 0 , 0],
                [0, 0, 0 , 0],
            ],
        ),
    ]   
)
def test_movement(table, move, expected):
    board = Board(size=4)
    board._table = table
    board.move(move=move)
    assert board._table == expected
    # assert True
