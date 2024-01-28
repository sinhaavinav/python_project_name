import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        
        self.current_player = "X"
        self.board = [""] * 9

        self.buttons = [tk.Button(root, text="", font=("Helvetica", 24), width=5, height=2, command=lambda i=i: self.click(i)) for i in range(9)]

        for i in range(3):
            for j in range(3):
                self.buttons[i * 3 + j].grid(row=i, column=j)

    def click(self, position):
        if self.board[position] == "" and not self.check_winner():
            self.board[position] = self.current_player
            self.buttons[position].config(text=self.current_player, state="disabled")
            
            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
            elif "" not in self.board:
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            else:
                self.switch_player()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True

        return False

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
