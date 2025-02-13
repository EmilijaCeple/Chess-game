![](https://external-preview.redd.it/WdAc0sOzC4bkaejed4ofUnfYaBPhh_xv-EjRMY-dff4.jpg?auto=webp&s=0c46855de8d06d675848ef3043177f5dd00c8f85)

# Chess game

## Overview

This Python program determines which black pieces a white piece can capture based on a given board state. The user enters a white piece and its position, followed by up to 16 black pieces. The program then evaluates and displays which black pieces are within the capturing range of the white piece.

## How It Works

White Piece Selection:
- The user chooses a white chess piece from two available options (e.g., knight and rook)
- The piece and its position are entered in the format: piece position (e.g., knight a5)
  
Black Piece Input:
- The user adds at least one and up to 16 black pieces, following the same format (e.g., pawn d4)
- After adding at least one black piece, the user can type done to finish

## Validation & Feedback:
- The program ensures all inputs follow the correct format (piece position)
- It provides confirmation messages for valid entries and error messages for invalid ones

## Capture Analysis:

Once all pieces are placed, the program evaluates which black pieces the white piece can capture based on chess movement rules. The results are displayed, listing any black pieces that are within the capturing range.

## Contributing

- Contributions are welcome! If you'd like to improve this code, suggest features, or fix issues, feel free to submit a pull request or open an issue.

## Thank you!
