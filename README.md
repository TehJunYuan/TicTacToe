# Tic Tac Toe Game

This is a simple Tic Tac Toe game implemented in Python. The game can be played in the terminal, where two players take turns to mark the cells in a 3×3 grid with 'X' and 'O'. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game. If all nine cells are filled without any player forming such a row, the game is declared a draw.

## Features

- Two-player game
- Simple terminal-based interface
- Automatic detection of win and draw conditions

## Requirements

- Python 3.x

## How to Run

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/tic-tac-toe.git
    cd tic-tac-toe
    ```

2. **Run the game:**

    ```sh
    python main.py
    ```

## How to Play

1. The game starts by displaying an empty 3x3 grid.
2. Players take turns to input their moves. A move is specified by entering the position in the format `row-col`, where:
   - `row` can be `top`, `mid`, or `bot` (for top, middle, and bottom rows respectively)
   - `col` can be `l`, `c`, or `r` (for left, center, and right columns respectively)
3. For example, to place a mark in the top-left cell, enter `top-l`. To place a mark in the center cell, enter `mid-c`.
4. After each move, the current state of the grid is displayed.
5. The game continues until either player wins or the game is declared a draw.
