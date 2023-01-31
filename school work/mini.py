import tkinter as tk
from tkinter import messagebox

# Initialize Tkinter window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry('1010x790')

# Initialize game variables
board = {"1": " ", "2": " ", "3": " ",
         "4": " ", "5": " ", "6": " ",
         "7": " ", "8": " ", "9": " "}
player = "X"

# Function to update the game board
def update_board(button, spot):
    global player
    print(spot)
    if board[spot] == " ":
        board[spot] = player
        button.config(text=player)
        check_winner()
        switch_player()
        root.title("Turn: " + player)

# Function to switch between players
def switch_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"

# Function to check if there is a winner
def check_winner():
    if (board["1"] == board["2"] == board["3"] != " " or
        board["4"] == board["5"] == board["6"] != " " or
        board["7"] == board["8"] == board["9"] != " " or
        board["1"] == board["4"] == board["7"] != " " or
        board["2"] == board["5"] == board["8"] != " " or
        board["3"] == board["6"] == board["9"] != " " or
        board["1"] == board["5"] == board["9"] != " " or
        board["3"] == board["5"] == board["7"] != " "):
            root.after(10, end_game())

# Function to end the game
def end_game():
    global player
    messagebox.showinfo("Game Over", player + " wins!")
    root.destroy()

button1 = tk.Button(root, text="", width=15, height=6,
                    command=lambda: update_board(button1, "1"))
button2 = tk.Button(root, text="", width=15, height=6,
                    command=lambda: update_board(button2, "2"))
button3 = tk.Button(root, text="", width=15, height=6,
                    command=lambda: update_board(button3, "3"))
button4 = tk.Button(root, text="", width=15, height=6,
                    command=lambda: update_board(button4, "4"))
button5 = tk.Button(root, text="", width=15, height=6,
                    command=lambda: update_board(button5, "5"))
button6 = tk.Button(root, text="", width=15, height=6,
                    command=lambda: update_board(button6, "6"))
button7 = tk.Button(root, text="", width=15, height=6,
                    command=lambda: update_board(button7, "7"))
button8 = tk.Button(root, text="", width=15, height=6,
                    command=lambda: update_board(button8, "8"))
button9 = tk.Button(root, text="", width=15, height=6,
                    command=lambda: update_board(button9, "9"))

list_of_buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
count = 0

for i in list_of_buttons:
    count += 1
    i.grid(row = (count - 1) // 3, column = (count - 1) % 3)
    i.config(font=("Courier", 28))

root.mainloop()