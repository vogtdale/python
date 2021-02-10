# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), 
# compare them, print out a message of congratulations to the winner, 
# and ask if the players want to start a new game)
# Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

print("="*50)
print("=             Rock, Paper, Scissors Game         =")
print("="*50)

while True:
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_one = str(input("payer one choose "))
    player_two = str(input("player two choose "))

    a = game_dict.get(player_one)
    b = game_dict.get(player_two)

    dif = a - b # returns a value between [1 & 2 or -1, -2]

    #check if dif is present in a list 

    if dif in [-1, 2]:
        print("player one wins")
        if str(input("Do you wish to play another game, yes or no?\n")) == "yes":
            continue
        else: 
            print("Game Over")
            break
    elif dif in [-2, 1]:
        print("player two wins")
        if str(input("Do you wish to play another game, yes or no?\n")) == "yes":
            continue
        else: 
            print("Game Over")
            break
    else:
        print("Draw please continue")
        print("")
    
    


    