import re


def validate_piece_input(user_input, allowed_pieces):
    pattern = f"^({'|'.join(allowed_pieces)}) [a-h][1-8]$"
    if not re.match(pattern, user_input):
        return False
    return True


def position_to_coordinates(position):
    column = ord(position[0]) - ord("a")
    row = 8 - int(position[1])
    return row, column


def print_board(board):
    print("\n   a b c d e f g h")
    for i, row in enumerate(board):
        print(f"{8 - i} " + "".join(row) + f" {8 - i}")
    print("   a b c d e f g h\n")


def create_empty_board():
    board = []
    for row in range(8):
        board_row = []
        for col in range(8):
            if (row + col) % 2 == 0:
                board_row.append("⬜")
            else:
                board_row.append("⬛")
        board.append(board_row)
    return board


def place_piece(board, position, symbol):
    row, col = position_to_coordinates(position)
    board[row][col] = symbol


def get_capturable_pieces(white_piece, white_pos, black_pieces):
    white_row, white_col = position_to_coordinates(white_pos)
    capturable = []
    if white_piece == "rook":
        for row in range(white_row - 1, -1, -1):
            pos = (row, white_col)
            for piece, black_pos in black_pieces.items():
                black_row, black_col = position_to_coordinates(black_pos)
                if (black_row, black_col) == pos:
                    capturable.append(f"{piece} at {black_pos}")
                    break

        for row in range(white_row + 1, 8):
            pos = (row, white_col)
            for piece, black_pos in black_pieces.items():
                black_row, black_col = position_to_coordinates(black_pos)
                if (black_row, black_col) == pos:
                    capturable.append(f"{piece} at {black_pos}")
                    break

        for col in range(white_col - 1, -1, -1):
            pos = (white_row, col)
            for piece, black_pos in black_pieces.items():
                black_row, black_col = position_to_coordinates(black_pos)
                if (black_row, black_col) == pos:
                    capturable.append(f"{piece} at {black_pos}")
                    break

        for col in range(white_col + 1, 8):
            pos = (white_row, col)
            for piece, black_pos in black_pieces.items():
                black_row, black_col = position_to_coordinates(black_pos)
                if (black_row, black_col) == pos:
                    capturable.append(f"{piece} at {black_pos}")
                    break

    elif white_piece == "pawn":
        potential_captures = [
            (white_row - 1, white_col - 1),
            (white_row - 1, white_col + 1),
        ]

        for piece, pos in black_pieces.items():
            black_row, black_col = position_to_coordinates(pos)
            if (black_row, black_col) == potential_captures[0]:
                capturable.append(f"{piece} at {pos}")
                continue
            if (black_row, black_col) == potential_captures[1]:
                capturable.append(f"{piece} at {pos}")

    return capturable


def main():
    allowed_white_pieces = {"pawn": "♙ ", "rook": "♖ "}

    allowed_black_pieces = {
        "pawn": "♟ ",
        "rook": "♜ ",
        "bishop": "♝ ",
        "knight": "♞ ",
        "queen": "♛ ",
        "king": "♚ ",
    }

    piece_limits = {
        "king": 1,
        "queen": 1,
        "rook": 2,
        "bishop": 2,
        "knight": 2,
        "pawn": 8,
    }

    piece_count = {
        "king": 0,
        "queen": 0,
        "rook": 0,
        "bishop": 0,
        "knight": 0,
        "pawn": 0,
    }

    board = create_empty_board()

    occupied_positions = set()

    print("Initial chessboard:")
    print_board(board)

    print("Choose your white piece (pawn or rook) and its position on the board.")
    print("Position is a coordinate of a piece (e.g., rook a5 or pawn b2).")

    while True:
        white_input = input("Enter the white piece and position: ").lower()
        if validate_piece_input(white_input, allowed_white_pieces):
            white_piece, white_pos = white_input.split()
            if white_pos not in occupied_positions:
                print(f"White piece '{white_piece}' at {white_pos} added successfully.")
                place_piece(board, white_pos, allowed_white_pieces[white_piece])
                occupied_positions.add(white_pos)
                print_board(board)
                break
            else:
                print(
                    f"Position {white_pos} is already occupied. Please choose a different position."
                )
        else:
            print(
                "Invalid input. Please enter a valid piece and position (e.g., rook a5 or pawn b2)."
            )

    black_pieces = {}
    print("\nNow, enter the black pieces and their positions on the board.")
    print(
        "You can add up to 16 black pieces, based on Chess game rules (1 King/Queen, 2 Rooks/Bishops/Knights, 8 Pawns)."
    )
    print("Type 'done' when finished.")

    while len(black_pieces) < 16:
        black_input = input(
            "Enter a black piece and position (or type 'done' to finish): "
        ).lower()
        if black_input == "done":
            if len(black_pieces) == 0:
                print("You must add at least one black piece before finishing.")
            else:
                break
        elif validate_piece_input(black_input, allowed_black_pieces):
            piece, pos = black_input.split()

            if piece_count[piece] >= piece_limits[piece]:
                print(f"You cannot add more than {piece_limits[piece]} {piece}(s).")
            elif pos not in occupied_positions:
                black_pieces[piece] = pos
                piece_count[piece] += 1
                print(f"Black piece '{piece}' at {pos} added successfully.")
                place_piece(board, pos, allowed_black_pieces[piece])
                occupied_positions.add(pos)
                print_board(board)
                if len(black_pieces) == 16:
                    print("You already added 16 black pieces.")
                    break
            else:
                print(
                    f"Position {pos} is already occupied. Please choose a different position."
                )
        else:
            print(
                "Invalid input. Please enter a valid black piece and position (e.g., rook a5 or pawn b2)."
            )

    capturable_pieces = get_capturable_pieces(white_piece, white_pos, black_pieces)

    print("\nResults:")
    if capturable_pieces:
        print(f"The white piece can take {len(capturable_pieces)} black piece(s):")
        for piece in capturable_pieces:
            print(piece)
    else:
        print("The white piece cannot take any black pieces.")


if __name__ == "__main__":
    main()
