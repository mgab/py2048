from .models.board import (
    draw,
    is_game_over,
    move_down,
    move_left,
    move_right,
    move_up,
    new_empty_board,
    spawn_number,
)

KEY_UP = "w"
KEY_DOWN = "s"
KEY_LEFT = "a"
KEY_RIGHT = "d"
KEY_QUIT = "q"


def app() -> None:
    print("hello")
    keep_loop = True
    board = new_empty_board()
    board = spawn_number(spawn_number(board))
    draw(board)
    while keep_loop:
        event_key = input(
            f"your move: {KEY_UP}/{KEY_DOWN}/{KEY_LEFT}/{KEY_RIGHT}/{KEY_QUIT}\n"
        )
        if event_key == KEY_QUIT:
            keep_loop = False
            print("bye!")
            break
        if event_key == KEY_UP:
            print("move up")
            new_board = move_up(board)
        elif event_key == KEY_DOWN:
            print("move down")
            new_board = move_down(board)
        elif event_key == KEY_LEFT:
            print("move left")
            new_board = move_left(board)
        elif event_key == KEY_RIGHT:
            print("move right")
            new_board = move_right(board)
        else:
            continue

        if new_board != board:
            board = spawn_number(new_board)
        draw(board)
        if is_game_over(board):
            print("GAME OVER!")
            break
