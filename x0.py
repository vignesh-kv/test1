import random
from tkinter import Tk, Button, Label

def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and not check_winner():
        buttons[row][column]['text'] = player

        if check_winner():
            label.config(text=f"{player} wins!")
        elif check_winner() == "tie":
            label.config(text="Tie!")
        else:
            player = players[1] if player == players[0] else players[0]
            label.config(text=f"{player}'s turn")

def check_winner():
    # Check rows
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    
    # Check columns
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    # Check diagonals
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    
    # Check tie
    if not empty_spaces():
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "tie"

    return False

def empty_spaces():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                return True
    return False

def new_game():
    global player
    player = random.choice(players)
    label.config(text=f"{player}'s turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

# Set up the window
window = Tk()
window.title("Tic-Tac-Toe")

players = ["X", "O"]
player = random.choice(players)

label = Label(window, text=f"{player}'s turn", font=('consolas', 40))
label.pack(side="top")

reset_button = Button(window, text="Restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

frame = Tk.Frame(window)
frame.pack()

# Create buttons for the board
buttons = [[0, 0, 0] for _ in range(3)]  # Initialize the board with 0s
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
