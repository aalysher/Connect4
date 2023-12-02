# Connect 4 Console Game

This is a simple two-player console version of the classic Connect 4 game implemented in Python. The game is played on a 6x7 board, and the objective is to connect four discs of the same color in a row, either horizontally, vertically, or diagonally.

## How to Play

1. Run the `main.py` file to start the game.
2. Players take turns entering the column number (0-6) where they want to drop their disc.
3. The game displays the current state of the board after each move.
4. The game automatically checks for a winner or a draw after each move.
5. The first player to connect four discs in a row wins the game.

## Customization

You can customize the size of the game board by providing the number of rows and columns when creating an instance of the `Connect4` class in the `main.py` file.

```python
# Example: Create a 7x7 game board
ConnectFour(rows=7, cols=7).execute()
```

## Running the Game
1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command:
```python
make
```
4. Follow the on-screen instructions to play the game.