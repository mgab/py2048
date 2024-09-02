from pytest import fixture

from py2048.models.board import (
    CellBoard,
    _substitute_value,
    compact_row,
    move_down,
    move_left,
    move_right,
    move_up,
    reverse_row,
    transpose,
)


def test_compact_row() -> None:
    assert compact_row([0, 0, 0, 0]) == [0, 0, 0, 0]
    assert compact_row([1, 0, 0, 0]) == [1, 0, 0, 0]
    assert compact_row([0, 1, 0, 0]) == [1, 0, 0, 0]
    assert compact_row([1, 0, 2, 1]) == [1, 2, 1, 0]
    assert compact_row([1, 3, 2, 1]) == [1, 3, 2, 1]


def test_compact_row_merge() -> None:
    assert compact_row([1, 1, 0, 0]) == [2, 0, 0, 0]
    assert compact_row([2, 0, 2, 0]) == [3, 0, 0, 0]
    assert compact_row([1, 0, 1, 1]) == [2, 1, 0, 0]
    assert compact_row([1, 1, 1, 1]) == [2, 2, 0, 0]
    assert compact_row([1, 2, 2, 1]) == [1, 3, 1, 0]


def test_reverse_row() -> None:
    assert reverse_row([0, 1, 0, 3]) == [3, 0, 1, 0]


def test_transpose() -> None:
    assert transpose(
        [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    ) == [[0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15]]


@fixture
def sample_board() -> CellBoard:
    return [[0, 1, 0, 1], [0, 1, 0, 2], [2, 1, 3, 0], [0, 0, 1, 0]]


def test_move_up(sample_board: CellBoard) -> None:
    assert move_up(sample_board) == [
        [2, 2, 3, 1],
        [0, 1, 1, 2],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]


def test_move_down(sample_board: CellBoard) -> None:
    assert move_down(sample_board) == [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 3, 1],
        [2, 2, 1, 2],
    ]


def test_move_left(sample_board: CellBoard) -> None:
    assert move_left(sample_board) == [
        [2, 0, 0, 0],
        [1, 2, 0, 0],
        [2, 1, 3, 0],
        [1, 0, 0, 0],
    ]


def test_move_right(sample_board: CellBoard) -> None:
    assert move_right(sample_board) == [
        [0, 0, 0, 2],
        [0, 0, 1, 2],
        [0, 2, 1, 3],
        [0, 0, 0, 1],
    ]


def test_add_value(sample_board: CellBoard) -> None:
    assert _substitute_value(sample_board, (1, 2), -1) == [
        [0, 1, 0, 1],
        [0, 1, -1, 2],
        [2, 1, 3, 0],
        [0, 0, 1, 0],
    ]
