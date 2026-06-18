#key steps: 
"""1)setup the GUI window using tkinker 
2)create the game grid (a 3X3 matrix)
3) handle the user input for the X's and O's 
4)check for wining conditions 
5)reset the game after a win or draw
6)display game status(like who's turn it is)"""

import tkinter as tk #tkinter is an GUI
from tkinter import messagebox #used to show messages when the game ends(like who won).

#creating main window
root= tk.Tk()
root.title("tic-tac-toe")

def create_board_grid(self):
    grid_frame=tk.Frame(master=self)
    grid_frame.pack 
    for row in range(3):
        self.rowconfigure(row, weight=1 , minsize=50)
        self.columnconfigure(row, weight=1 , minsize= 75)
        button=tk.Button(
            master=grid_frame,
            text="",
            font= font.Font(size=36 , weight= "bold"),
            fg= "black",
            width=3,
            height=2,
            highlightbackground="lightblue",
       )
        self._cells[button]= (row, col)
        button.grid(
            row=row,
            column= col,
            padx=5, 
            pady=5,
            sticky= "nsew"
        )

#instalization of board
buttons= [""]
board= [""]*9 #3x3 grid 
turn= "X" #x goes first

#defining button function 
def button_click(i):
    global turn 
    if board[i]== "":
        board[i]= turn 
        buttons[i].config(text=turn)
"""python have different variable scopes , which dictate where and how they can be accesed 
1)local scope: a variable defined inside a function (can be used only within that function)
2)global scope: a variable is defined outside of all functions and can be accessed from anywhere in program 
why do we use global turn:it represnts whose turn it is and needs to be accessible and modifiable by multiple funtions
in the program.
"""
#button[i].config(text=turn) modifies the text of the button at index i to the current value of turn 

def check_winner():
    winning_combinations=[
        (0,1,2), (3,4,5),(6,7,8), #horizontal
        (0,3,6), (1,4,7), (2,5,8), #vertical
        (0,4,8), (2,4,6) #diagonal
        ]
    
    for a , b , c in winning_combinations:
        if board[a]==board[b]==board[c] and board[a]!="":
            return board[a]
        
    return None
    # values a,b,c reprensent the indices of the three cells in the grid that form a winning line(vertical,horizontal,digonal)
    #board[a]==board[b]==board[c] checks if the value in the three cells at indices a,b,c are same 
    #board[a] != "" this ensures that the cells arent empty 

status_label= tk.Label(root , text=f"player X's turn", font=("Arial", 14))

#game reset
def reset_game():
    global board, turn 
    board=[""]*9
    for button in buttons:
        button.config(text="")
        turn = "X"
        status_label.config(text="player X's turn")

#handling the turn:
winner = check_winner
if winner:
    messagebox.showinfo("game over", f"player{winner} wins!")
    reset_game()
elif"" not in board: 
    messagebox.showinfo("game over", "its a draw!")
    reset_game()
else: 
    turn="O" if turn=="X" else "X"
    status_label.config(text= f"player {turn}'s turn")

#creating the 9 buttons for tic-tac-toe 3x3
def create_button(i):
    buttons = tk.Button(root, text="", font=("Arial", 20), height=3 , width=6, command=lambda i=i:button_click(i))
for i, button in enumerate(buttons):
    row, col= divmod(i , 3)
    button.grid(row=row, column=col)

status_label.grid(row=3 , column=0 , columnspan=3)
#label displays whose turn it is 

#GUI loop
root.mainloop()
                       