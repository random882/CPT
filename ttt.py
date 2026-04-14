import random
import time

"""
Implement a game of TIC TAC TOE

A human will compete against the computer
The human will go first by choosing a cell to place an X
The computer will go next.  You can decide on any strategy, random is fine.
    (sidequest: For a more advanced strategy, look into the minimax algorithm)
Neither the human nor the computer can choose a cell that is already taken or outside the boundaries of the game.

    A   B   C
  +---+---+---+
1 | . | . | X | 1
  +---+---+---+
2 | O | X | . | 2
  +---+---+---+
3 | O | . | . | 3
  +---+---+---+
    A   B   C
"""


def player_one(board, marker):
    print("List your coordinates by Row then Column (example: R1 C2)")
    player_request = input(f"Where do you want to place {marker}?")
    row, col = parse_input(player_request)
    setmark(board, col, row, marker)


def player_two(board, marker):
    print("Thinking. . . . ")

    DIFFICULTY = 3  # change according to the bots difficulty
    delay = random.uniform(0, 1.5)
    time.sleep(delay)

    opponent = "X" if marker == "O" else "O"

    def get_available_moves(b):
        moves = []
        for r in range(len(b)):
            for c in range(len(b[0])):
                if b[r][c] == ".":
                    moves.append((r, c))
        return moves

    def minimax(b, is_maximizing, depth):
        winner = check_winner(b)
        if winner == marker:
            return 10 - depth
        if winner == opponent:
            return depth - 10

        moves = get_available_moves(b)
        if not moves or depth >= 4:
            return 0

        if is_maximizing:
            best_score = float("-inf")
            for r, c in moves:
                b[r][c] = marker
                score = minimax(b, False, depth + 1)
                b[r][c] = "."
                best_score = max(best_score, score)
            return best_score
        else:
            best_score = float("inf")
            for r, c in moves:
                b[r][c] = opponent
                score = minimax(b, True, depth + 1)
                b[r][c] = "."
                best_score = min(best_score, score)
            return best_score

    available_moves = get_available_moves(board)
    best_score = float("-inf")
    best_move = None

    for r, c in available_moves:
        board[r][c] = marker
        score = minimax(board, False, 0)
        board[r][c] = "."
        if score > best_score:
            best_score = score
            best_move = (r, c)

    if DIFFICULTY == 3:
        move = best_move
    elif DIFFICULTY == 2:
        move = best_move if random.random() < 0.5 else random.choice(available_moves)
    else:
        move = best_move if random.random() < 0.1 else random.choice(available_moves)

    if move:
        row, col = move
        setmark(board, col, row, marker)


def parse_input(player_request):
    player_request = player_request.lower().strip().split()
    if len(player_request) != 2:
        return (
            "Please enter both row and column (e.g., R1 C2)"
        )

    row = player_request[0]
    col = player_request[1]

    if row[0] != "r":
        return "Not a valid row"

    if col[0] != "c":
        return "Not valid column"

    if len(row) < 2:
        return "Row needs a number (e.g., R1)"

    if len(col) < 2:
        return "Column needs a number (e.g., C1)"

    row_digit = row[1]
    col_digit = col[1]

    if not row_digit.isnumeric():
        return "Not a numeric value for row."
    if not col_digit.isnumeric():
        return "Not a valid numeric value for column."

    row_digit = int(row_digit) - 1
    col_digit = int(col_digit) - 1

    return (row_digit, col_digit)


def display_board(board):
    for indx, row in enumerate(board):
        row_display = " | ".join(row)
        print(row_display)
        if indx < len(board) - 1:
            print("-" * len(row_display))


def main():
    board = [
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."],
    ]
    turn_count = 0
    markers = ["X", "O"]
    player_turns = {
        "X": player_one,
        "O": player_two,
    }
    display_board(board)
    while True:
        marker = markers[turn_count]
        player_turn = player_turns[marker]
        player_turn(board, marker)

        turn_count = turn_count + 1
        if turn_count > 1:
            turn_count = 0
        winner_token = check_winner(board)
        if winner_token:
            print(f"{winner_token} has won the match!")
            break


def check_winner(board):
    w = len(board)
    col0 = []
    col1 = []
    col2 = []
    col3 = []
    diag0 = []
    diag1 = []
    for i in range(w):
        col0.append(board[i][0])
        col1.append(board[i][1])
        col2.append(board[i][2])
        col3.append(board[i][3])
        diag0.append(board[i][i])
        diag1.append(board[i][-(i + 1)])

    sequences = [col0, col1, col2, col3, diag0, diag1, board[0], board[1], board[2], board[3]]
    markers = ["X", "O"]
    for marker in markers:
        for sequence in sequences:
            if is_winning_sequence(sequence, marker):
                return marker


def setmark(board, column, row, marker):
    currentvalue = board[row][column]
    if currentvalue != ".":
        print("Invalid move")
        return False
    board[row][column] = marker
    display_board(board)
    return True


def is_winning_sequence(seq: list[str], marker) -> bool:
    for i in seq:
        if i != marker:
            return False
    return True


if __name__ == "__main__":
    main()