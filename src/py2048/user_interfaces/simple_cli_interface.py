from typing import Self

from py2048.game import MoveAction, get_score
from py2048.models.board import CellBoard, as_list_of_lists

from .interactive_interface_base import GameCommand, InteractiveUserInterface


class RawUserInterface(InteractiveUserInterface):
    KEY_UP = "w"
    KEY_DOWN = "s"
    KEY_LEFT = "a"
    KEY_RIGHT = "d"
    KEY_QUIT = "q"
    KEY_UNDO = "u"

    def init(self: Self) -> None:
        pass

    def _display_start_game(self: Self) -> None:
        print("Welcome to py2048!")

    def _display_board(self: Self, board: CellBoard) -> None:
        print(
            "\n".join(
                [
                    str([2**c if c != 0 else 0 for c in row])
                    for row in as_list_of_lists(board)
                ]
            )
        )

    def _display_end_game(self: Self, board: CellBoard) -> None:
        score = get_score(board)
        print("---------", "Game over!", f"Score: {score}", "---------", sep="\n")

    def _get_user_action(self: Self) -> MoveAction | GameCommand:
        while True:
            key = input(
                f"Move with: {self.KEY_UP} / {self.KEY_DOWN} "
                f"/ {self.KEY_LEFT} / {self.KEY_RIGHT}\n"
                f"Undo / Quit: {self.KEY_UNDO} / {self.KEY_QUIT}\n"
            )
            match key:
                case self.KEY_UP:
                    return MoveAction.MOVE_UP
                case self.KEY_DOWN:
                    return MoveAction.MOVE_DOWN
                case self.KEY_RIGHT:
                    return MoveAction.MOVE_RIGHT
                case self.KEY_LEFT:
                    return MoveAction.MOVE_LEFT
                case self.KEY_QUIT:
                    return GameCommand.QUIT
                case self.KEY_UNDO:
                    return GameCommand.UNDO
                case _:
                    print("Invalid input, try again")
