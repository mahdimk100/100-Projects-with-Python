import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        # Create the board
        self.board = [[None for j in range(3)] for i in range(3)]

        # Create the buttons
        self.buttons = [[None for j in range(3)] for i in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(master, text="", font=("Arial", 32), width=3, height=1,
                                               command=lambda row=i, col=j: self.button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

        # Create the status label
        self.status_label = tk.Label(master, text="", font=("Arial", 16))
        self.status_label.grid(row=3, columnspan=3)

        # Create the reset button
        self.reset_button = tk.Button(master, text="Reset", font=("Arial", 16), command=self.reset)
        self.reset_button.grid(row=4, columnspan=3)

        # Set the first player
        self.current_player = "X"

    def button_click(self, row, col):
        if self.board[row][col] is not None:
            return
        self.board[row][col] = self.current_player
        self.buttons[row][col].config(text=self.current_player)
        if self.check_win():
            self.status_label.config(text=f"{self.current_player} wins!")
            self.disable_buttons()
        elif self.check_tie():
            self.status_label.config(text="Tie game!")
            self.disable_buttons()
        else:
            self.switch_player()

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] is not None:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] is not None:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] is not None:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] is not None:
            return True
        return False

    def check_tie(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    return False
        return True

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"
        self.status_label.config(text=f"{self.current_player}'s turn")

    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=tk.DISABLED)

    def reset(self):
        self.current_player = "X"
        self.status_label.config(text="")
        for i in range(3):
            for j in range(3):
                self.board[i][j] = None
                self.buttons[i][j].config(text="")
                self.buttons[i][j].config(state=tk.NORMAL)

root = tk.Tk()
tic_tac_toe = TicTacToe(root)
root.mainloop()
