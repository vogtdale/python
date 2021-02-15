# create the Board using a list
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

# If game is still going
game_still_going = True 

# Who won? Or tie?
winner = None

current_player = "X"

# ------------------------------- #
#           Functions             #
# ------------------------------- #

# draw the board
def display_board():
    print("")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("- + - + -")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("- + - + -")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("")

# handle whose turn it is 
def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False

    while not valid:

        while position not in ["1","2","3","4","5","6","7","8","9"]:

            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You cant move there, try again")
            
    board[position] = player

    display_board()

# change player
def flip_player():
    global current_player

     # if the current player was X, then change it to O
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    global winner
    #check rows 
    row_winner = check_rows()

    #check columns
    column_winner = check_columns()

    #check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        # nobobdy won
        winner = None
    return


def check_rows():
    global game_still_going

    # check if all the rows have all the same value and is not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    
    #return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[2]
    elif row_3:
        return board[3]
    return


def check_columns():
    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # If any column does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():

    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    # If any diagonal does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return the winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


# funtion will call all the other functions 
# and acts as the main function for running the app
def play_game():
    display_board()

    while game_still_going:

        # Handle a single turn of an arbitrary player
        handle_turn(current_player)

        # check if games is over
        check_if_game_over()

        # Flip to the other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won this match.")
    elif winner == None:
        print("Tie.")

play_game()