import random
from typing import Iterable

CellBoard = list[list[int]]


def _increase(val: int) -> int:
    return val + 1


def compact_row(row: list[int]) -> list[int]:
    def _inner(
        row: list[int],
        acc: list[int] = [],
        last_merged: bool = False,
        tailing_zeroes: int = 0,
    ) -> list[int]:
        if len(row) == 0:
            return acc + [0] * tailing_zeroes
        head, *tail = row
        if head == 0:
            return _inner(tail, acc, last_merged, tailing_zeroes + 1)
        elif acc and head == acc[-1] and not last_merged:
            return _inner(tail, acc[:-1] + [_increase(head)], True, tailing_zeroes + 1)
        else:
            return _inner(tail, acc + [head], False, tailing_zeroes)

    return _inner(row)


def new_empty_board(n: int = 4) -> CellBoard:
    return [[0] * n for _ in range(n)]


def reverse_row(row: list[int]) -> list[int]:
    return row[::-1]


def transpose(board: CellBoard) -> CellBoard:
    return [list(col) for col in zip(*board)]


def move_left(board: CellBoard) -> CellBoard:
    return [compact_row(col) for col in board]


def move_right(board: CellBoard) -> CellBoard:
    return [reverse_row(compact_row(reverse_row(col))) for col in board]


def move_up(board: CellBoard) -> CellBoard:
    return transpose(move_left(transpose(board)))


def move_down(board: CellBoard) -> CellBoard:
    return transpose(move_right(transpose(board)))


def draw(board: CellBoard) -> None:
    print("\n".join([str([2**c if c != 0 else 0 for c in row]) for row in board]))


def _substitute_value(
    board: CellBoard, position: tuple[int, int], value: int
) -> CellBoard:
    i_row, i_col = position
    return [
        (
            [value if j == i_col else cell for j, cell in enumerate(row)]
            if i == i_row
            else row
        )
        for i, row in enumerate(board)
    ]


def _get_empty_cells(board: CellBoard) -> Iterable[tuple[int, int]]:
    return (
        (i, j) for i, row in enumerate(board) for j, cell in enumerate(row) if cell == 0
    )


def _any_adjacent_repeated_number_in_row(row: list[int]) -> bool:
    return any(row[i] == row[i + 1] for i in range(len(row) - 1))


def _any_adjacent_repeated_number(board: CellBoard) -> bool:
    return any(_any_adjacent_repeated_number_in_row(row) for row in board) or any(
        _any_adjacent_repeated_number_in_row(row) for row in transpose(board)
    )


def spawn_number(board: CellBoard) -> CellBoard:
    empties = _get_empty_cells(board)
    position = random.choice(list(empties))
    new_number = 1 if random.random() < 0.9 else _increase(1)
    return _substitute_value(board, position, new_number)


def is_game_over(board: CellBoard) -> bool:
    return not any(_get_empty_cells(board)) and not _any_adjacent_repeated_number(board)
