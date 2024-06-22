import random
import tkinter as tk
from tkinter import messagebox

class PuzzleGame:
    def __init__(self, size):
        self.size = size
        self.board = []  # Initialize an empty board
        self.generate_solvable_puzzle()

    def generate_solvable_puzzle(self):
        while True:
            puzzle = [[0 for _ in range(self.size)] for _ in range(self.size)]
            numbers = [i for i in range(1, self.size**2)]
            random.shuffle(numbers)

            for i in range(self.size):
                for j in range(self.size):
                    if numbers:
                        puzzle[i][j] = numbers.pop(0)

            if self.is_puzzle_solvable(puzzle):
                self.board = puzzle  # Set the generated solvable puzzle to the board
                return

    def is_puzzle_solvable(self, puzzle):
        inversion_count = 0
        flattened_puzzle = [num for row in puzzle for num in row]

        for i in range(len(flattened_puzzle) - 1):
            for j in range(i + 1, len(flattened_puzzle)):
                if flattened_puzzle[i] > flattened_puzzle[j] and flattened_puzzle[i] != 0 and flattened_puzzle[j] != 0:
                    inversion_count += 1

        return inversion_count % 2 == 0

    def sort_numbers(self):
        sorted_numbers = [i for i in range(1, self.size**2)]
        sorted_numbers.append(0)
        flattened_board = [num for row in self.board for num in row]

        return flattened_board == sorted_numbers

    def move_empty_slot(self, direction):
        empty_position = self.find_empty_slot(self.board)

        if direction == "up" and empty_position[0] > 0:
            self.board[empty_position[0]][empty_position[1]], self.board[empty_position[0] - 1][empty_position[1]] = \
                self.board[empty_position[0] - 1][empty_position[1]], self.board[empty_position[0]][empty_position[1]]
        elif direction == "down" and empty_position[0] < self.size - 1:
            self.board[empty_position[0]][empty_position[1]], self.board[empty_position[0] + 1][empty_position[1]] = \
                self.board[empty_position[0] + 1][empty_position[1]], self.board[empty_position[0]][empty_position[1]]
        elif direction == "left" and empty_position[1] > 0:
            self.board[empty_position[0]][empty_position[1]], self.board[empty_position[0]][empty_position[1] - 1] = \
                self.board[empty_position[0]][empty_position[1] - 1], self.board[empty_position[0]][empty_position[1]]
        elif direction == "right" and empty_position[1] < self.size - 1:
            self.board[empty_position[0]][empty_position[1]], self.board[empty_position[0]][empty_position[1] + 1] = \
                self.board[empty_position[0]][empty_position[1] + 1], self.board[empty_position[0]][empty_position[1]]

    def find_empty_slot(self, puzzle):
        for i in range(self.size):
            for j in range(self.size):
                if puzzle[i][j] == 0:
                    return i, j

    def increase_size(self):
        self.size += 1
        self.generate_solvable_puzzle()

class PuzzleGameUI:
    def __init__(self, root, game):
        self.root = root
        self.game = game

        self.root.title(f"Puzzle Game - {self.game.size}x{self.game.size}")

        # Increase the size of the window and center it
        window_width = 100 + self.game.size * 100
        window_height = 100 + self.game.size * 100
        self.root.geometry(f"{window_width}x{window_height}+{root.winfo_screenwidth() // 2 - window_width // 2}+{root.winfo_screenheight() // 2 - window_height // 2}")
        
        self.labels = [[None for _ in range(self.game.size)] for _ in range(self.game.size)]

        for i in range(self.game.size):
            for j in range(self.game.size):
                number = self.game.board[i][j]
                label = tk.Label(root, text=str(number), font=("Arial", 20), width=4, height=2, relief="solid", borderwidth=2)
                label.grid(row=i, column=j, padx=5, pady=5)
                self.labels[i][j] = label

        self.create_direction_buttons()

        self.display_message("Use the buttons or arrow keys to move the empty slot.")

    def create_direction_buttons(self):
        button_size = 10  # Adjust the size as needed

        ##Todo: register arrow keys then pass to Button as args
        
        # Add background color to buttons
        tk.Button(self.root, text="UP", command=lambda: self.move_empty_with_direction("up"), width=button_size, height=2, bg="#4CAF50", fg="white").grid(row=self.game.size, column=self.game.size//2)
        tk.Button(self.root, text="DOWN", command=lambda: self.move_empty_with_direction("down"), width=button_size, height=2, bg="#4CAF50", fg="white").grid(row=self.game.size + 1, column=self.game.size//2)
        tk.Button(self.root, text="LEFT", command=lambda: self.move_empty_with_direction("left"), width=button_size, height=2, bg="#4CAF50", fg="white").grid(row=self.game.size + 1, column=self.game.size//2 - 1)
        tk.Button(self.root, text="RIGHT", command=lambda: self.move_empty_with_direction("right"), width=button_size, height=2, bg="#4CAF50", fg="white").grid(row=self.game.size + 1, column=self.game.size//2 + 1)


    def move_empty(self, row, col):
        direction = self.determine_direction(row, col)
        self.game.move_empty_slot(direction)
        self.update_board()

        if self.game.sort_numbers():
            self.display_message(f"Congratulations! Puzzle of size {self.game.size}x{self.game.size} solved.")
            self.ask_to_continue()

    def move_empty_with_direction(self, direction):
        self.game.move_empty_slot(direction)
        self.update_board()

        if self.game.sort_numbers():
            self.display_message(f"Congratulations! Puzzle of size {self.game.size}x{self.game.size} solved.")
            self.ask_to_continue()

    def determine_direction(self, row, col):
        empty_row, empty_col = self.game.find_empty_slot()

        if row == empty_row - 1 and col == empty_col:
            return "up"
        elif row == empty_row + 1 and col == empty_col:
            return "down"
        elif row == empty_row and col == empty_col - 1:
            return "left"
        elif row == empty_row and col == empty_col + 1:
            return "right"

    def update_board(self):
        for i in range(self.game.size):
            for j in range(self.game.size):
                number = self.game.board[i][j]
                self.labels[i][j].config(text=str(number))
    
    def display_message(self, message):
        messagebox.showinfo("Puzzle Game", message)

    def ask_to_continue(self):
        result = messagebox.askquestion("Continue", "Do you want to continue?")
        if result == 'yes':
            self.game.increase_size()
            self.root.destroy()
            self.create_new_game_ui()
        else:
            self.root.destroy()
            print("Game ended.")

    def create_new_game_ui(self):
        new_root = tk.Tk()
        new_game_ui = PuzzleGameUI(new_root, self.game)

if __name__ == "__main__":
    root = tk.Tk()
    game = PuzzleGame(2)
    game_ui = PuzzleGameUI(root, game)
    root.mainloop()
