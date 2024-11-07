from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Self

from py2048.game import MoveAction, apply_action, start_game
from py2048.models.board import CellBoard


class GameCommand(Enum):
    QUIT = auto()
    UNDO = auto()


class InteractiveUserInterface(ABC):
    @abstractmethod
    def _display_start_game(self: Self) -> None: ...

    @abstractmethod
    def _display_board(self: Self, board: CellBoard) -> None: ...

    @abstractmethod
    def _get_user_action(self: Self) -> MoveAction | GameCommand: ...

    @abstractmethod
    def _display_end_game(self: Self, board: CellBoard) -> None: ...

    def run(self: Self) -> None:
        self._display_start_game()
        prev_board = board = start_game()
        self._display_board(board)
        active_game = True
        while active_game:
            action = self._get_user_action()
            match action:
                case GameCommand.QUIT:
                    active_game = False
                case GameCommand.UNDO:
                    if board != prev_board:
                        board = prev_board
                case MoveAction():
                    new_board, v = apply_action(board, action)
                    if v == 0:
                        continue
                    if v == -1:
                        active_game = False
                    prev_board, board = board, new_board
            self._display_board(board)
        self._display_end_game(board)
