import random
from collections.abc import Iterable

CellBoard = list[list[int]]
# TODO: refactor as an object with methods


def _increase(val: int) -> int:
    return val + 1


def _compact_row(row: list[int]) -> list[int]:
    def _inner(
        row: list[int],
        acc: list[int] = [],  # noqa: B006
        *,
        last_merged: bool = False,
        tailing_zeroes: int = 0,
    ) -> list[int]:
        if len(row) == 0:
            return acc + [0] * tailing_zeroes
        head, *tail = row
        if head == 0:
            return _inner(
                tail, acc, last_merged=last_merged, tailing_zeroes=tailing_zeroes + 1
            )
        if acc and head == acc[-1] and not last_merged:
            return _inner(
                tail,
                [*acc[:-1], _increase(head)],
                last_merged=True,
                tailing_zeroes=tailing_zeroes + 1,
            )
        return _inner(
            tail, [*acc, head], last_merged=False, tailing_zeroes=tailing_zeroes
        )

    return _inner(row)


def new_empty_board(size: int = 4) -> CellBoard:
    return [[0] * size for _ in range(size)]


def _reverse_row(row: list[int]) -> list[int]:
    return row[::-1]


def _transpose(board: CellBoard) -> CellBoard:
    return [list(col) for col in zip(*board, strict=True)]


def move_left(board: CellBoard) -> CellBoard:
    return [_compact_row(col) for col in board]


def move_right(board: CellBoard) -> CellBoard:
    return [_reverse_row(_compact_row(_reverse_row(col))) for col in board]


def move_up(board: CellBoard) -> CellBoard:
    return _transpose(move_left(_transpose(board)))


def move_down(board: CellBoard) -> CellBoard:
    return _transpose(move_right(_transpose(board)))


def as_list_of_lists(board: CellBoard) -> list[list[int]]:
    return board


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
        _any_adjacent_repeated_number_in_row(row) for row in _transpose(board)
    )


def spawn_number(board: CellBoard) -> CellBoard:
    empties = _get_empty_cells(board)
    position = random.choice(list(empties))
    prob_base_value = 0.9
    new_number = 1 if random.random() < prob_base_value else _increase(1)
    return _substitute_value(board, position, new_number)


def is_game_over(board: CellBoard) -> bool:
    return not any(_get_empty_cells(board)) and not _any_adjacent_repeated_number(board)


def get_max_value(board: CellBoard) -> int:
    return max(max(row) for row in board)
