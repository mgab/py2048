from enum import Enum, auto, member

from .models.board import (
    CellBoard,
    get_max_value,
    is_game_over,
    move_down,
    move_left,
    move_right,
    move_up,
    new_empty_board,
    spawn_number,
)


class MoveAction(Enum):
    MOVE_UP = member(move_up)
    MOVE_DOWN = member(move_down)
    MOVE_RIGHT = member(move_right)
    MOVE_LEFT = member(move_left)

    def apply_move(self, board: CellBoard) -> CellBoard:
        return self.value(board)


def start_game() -> CellBoard:
    board = new_empty_board()
    return spawn_number(spawn_number(board))


def apply_action(board: CellBoard, action: MoveAction) -> tuple[CellBoard, int]:
    # TODO: use wrapper objects instead of 0, 1, -1
    new_board = action.apply_move(board)
    if new_board == board:
        return new_board, 0  # no changes
    new_board = spawn_number(new_board)
    if is_game_over(new_board):
        return new_board, -1  # game over
    return new_board, 1  # normal move


def get_score(board: CellBoard) -> int:
    return get_max_value(board)


class GameCommand(Enum):
    QUIT = auto()
    UNDO = auto()
