# Create the Board
board = ["0", "0", "O",
         "0", "0", "O",
         "0", "0", "O"]

# Dispaly the board
def displayBoard():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("- + - + -")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("- + - + -")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def handle_turn():
    
     # get user to to choose positon on the board
     choix = input("Choose a value from 1-9 player :>> ")
     choix = int(choix) - 1

     board[choix] = "X"

     displayBoard()



# The main function which has all the gameplay functionality.
def play_game():

    # Dispaly the inintial board
    displayBoard()

    handle_turn()


play_game()