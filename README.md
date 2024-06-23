### Puzzle Game README

## Introduction

This Puzzle Game is a sliding puzzle game implemented using Python and the Tkinter library for the graphical user interface (GUI). The objective of the game is to arrange the tiles in numerical order by moving the empty slot.

## How to Play

1. **Starting the Game:**
   - When the game starts, a 2x2 puzzle board is displayed with numbers from 1 to \(n^2 - 1\) randomly shuffled, with one slot left empty.

2. **Moving Tiles:**
   - Use the directional buttons (UP, DOWN, LEFT, RIGHT) provided below the puzzle to move the empty slot and rearrange the tiles.
   - Alternatively, you can use the arrow keys on your keyboard to move the empty slot.

3. **Winning the Game:**
   - Arrange the tiles in numerical order with the empty slot at the bottom-right corner.
   - Once solved, a congratulatory message will be displayed, and you will be prompted to either continue with a larger puzzle or end the game.

## Game Features

### Puzzle Generation
- **Solvable Puzzle Generation:** The game generates a random puzzle board that is guaranteed to be solvable.
  - The puzzle is created by shuffling numbers and ensuring the inversion count is even, which is a requirement for the puzzle to be solvable.

### Puzzle Mechanics
- **Tile Movement:** Players can move tiles in four directions (up, down, left, right) by moving the empty slot.
  - The game handles the tile swapping and updates the board accordingly.
  
### Game Logic
- **Solvable Check:** The game checks if the generated puzzle is solvable by counting inversions.
  - Inversions are pairs of tiles where a larger number precedes a smaller number in the linear representation of the puzzle.
  - A puzzle is solvable if the inversion count is even.
  
- **Winning Condition:** The game continuously checks if the current board state matches the solved state (numerical order with the empty slot at the end).

### User Interface
- **Dynamic UI:** The game board is dynamically created based on the puzzle size.
  - The window size adjusts according to the puzzle size.
  
- **Direction Buttons:** Buttons for moving the empty slot are provided below the puzzle grid.
  - The buttons are color-coded and labeled for better user experience.
  
- **Message Display:** Informational messages are displayed using Tkinter's `messagebox` to guide the player and celebrate the win.
  
- **Game Continuation:** Upon solving the puzzle, the player is asked if they want to continue to a larger puzzle.
  - If the player chooses to continue, the puzzle size increases, and a new game is started.

## Code Overview

### Main Classes and Functions

1. **`PuzzleGame` Class:**
   - **`__init__(self, size)`:** Initializes the game with a given puzzle size and generates a solvable puzzle.
   - **`generate_solvable_puzzle(self)`:** Generates a random, solvable puzzle.
   - **`is_puzzle_solvable(self, puzzle)`:** Checks if the generated puzzle is solvable.
   - **`sort_numbers(self)`:** Checks if the current board is in the solved state.
   - **`move_empty_slot(self, direction)`:** Moves the empty slot in the specified direction and updates the board.
   - **`find_empty_slot(self, puzzle)`:** Finds the position of the empty slot on the board.
   - **`increase_size(self)`:** Increases the size of the puzzle and generates a new solvable puzzle.

2. **`PuzzleGameUI` Class:**
   - **`__init__(self, root, game)`:** Initializes the game UI with the Tkinter root and the puzzle game instance.
   - **`create_direction_buttons(self)`:** Creates directional buttons for moving the empty slot.
   - **`move_empty(self, row, col)`:** Moves the empty slot based on row and column and updates the board.
   - **`move_empty_with_direction(self, direction)`:** Moves the empty slot based on the specified direction and updates the board.
   - **`determine_direction(self, row, col)`:** Determines the direction to move the empty slot based on its current position.
   - **`update_board(self)`:** Updates the UI to reflect the current state of the board.
   - **`display_message(self, message)`:** Displays informational messages to the player.
   - **`ask_to_continue(self)`:** Asks the player if they want to continue with a larger puzzle.
   - **`create_new_game_ui(self)`:** Creates a new game UI for a larger puzzle.

### Running the Game

To run the game, execute the script:
```bash
python puzzle_game.py
```

This will start the game with a 2x2 puzzle. Enjoy solving the puzzles and challenge yourself with larger grids as you progress!
