#A simple data structure for a tic-tac toe game

#create the list to hold the different states
theboard = {
    "top-L": " ", "top-M": " ", "top-R": " ",
    "mid-L": " ", "mid-M": " ", "mid-R": " ",
    "low-L": " ", "low-M": " ", "low-R": " "}


#function to print the board
def printboard(board):
    print(board["top-L"] + " | " + board["top-M"] + " | " + board["top-R"])
    print("---------")
    print(board["mid-L"] + " | " + board["mid-M"] + " | " + board["mid-R"])
    print("---------")
    print(board["low-L"] + " | " + board["low-M"] + " | " + board["low-R"])

theboard["top-L"] = "X" 
theboard["top-M"] = "O"
theboard["top-R"] = "X"

theboard["mid-L"] = "O" 
theboard["mid-M"] = "O"
theboard["mid-R"] = "X"

theboard["low-L"] = "X" 
theboard["low-M"] = "X"
theboard["low-R"] = "O"

printboard(theboard)