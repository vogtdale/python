# create bord
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]


current_player = "X"

game_still_going = True

winner = None
    
def disply_board():
    print("")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("- + - + -")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("- + - + -")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("")


def play_game():
    disply_board()

    while game_still_going:

        #Handle a single player
        handle_turn(current_player)

        #check if gameOver
        check_if_game_over()

        # flip players turn 
        flip_turn()

    if winner == "X" or wiiner == "O":
        print(winner + " won this match")
    elif winner == None:
        print("Tie.")


def handle_turn(player):
    print(player + 's turn to play')

    position = input("Choose a position from 1-9: ")

    valide = False

    while not valide:

        while position not in ["1","2","3","4","5","6","7","8","9"]:

            position = input("Choose a position from 1-9: ")
            
        position = int(position) - 1

        if board[position] == "-":
            valide = True
        else:
            print("You cant move there")
    
    board[position] = player

    disply_board()


def flip_turn():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return
    

def check_if_game_over():
    check_if_tie()
    check_for_winner()


def check_if_tie():
    global game_still_going

    if "-" not in board:
        game_still_going = False
    return

def check_for_winner():
    global winner

    # check rows
    row_winner = check_rows()

    #check for column winner
    column_winner = check_columns()

    # check for diagonals winner 
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        #nobody won
        winner = None
    return


def check_rows():
    global game_still_going

     # check if all the rows have all the same value and is not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

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

play_game()