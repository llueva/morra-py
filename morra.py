#RANDOM IMPORT:
from random import randint
#GAME RULES:
game_rules = """
    Welcome to Morra! In this game, you'll decide how many fingers
    to hold up (from one hand) and then the computer will randomly
    do the same. You'll need to guess the total number of fingers
    to win the round, before seeing how many fingers the computer
    has decided to hold up!
"""

print(game_rules)

######NAMEINPUT:

player_name = input("What is your name? ")
print(player_name)

#####ROUNDSINPUT:

number_of_rounds = int(input("How many rounds would you like to play? "))
print(number_of_rounds)

####PLAYERGUESS:

player_guess = input("Guess the total number of fingers: ")
print(player_guess)


#####GAMELOOP:

player_score = 0
computer_score = 0
rounds_tied = 0

################################################################################################################
#GAMELOOPSTART
for i in range(number_of_rounds):


    player_guess = int(input("How many fingers do you want to hold up? Ex: (1-5) "))


    if player_guess not in range(1,6):


        print(f"\n{player_guess} is not a valid guess. Please refresh and try again!\n")
        player_guess = randint(1,6)


    computer_guess = randint(1,6) 
    total_guess = int(input("What is your number guess? "))


    if total_guess > computer_guess:
        print(f"\nThat is correct! {player_name} Wins!\n")
        player_score += 1
        continue


    elif computer_guess > total_guess:
        computer_score += 1
        print("\nThat is incorrect! Computer Wins!\n")
        continue


    else:
        rounds_tied += 1
        print("\nRound Tied!\n")
        continue


print(f"Player Won: {player_score} rounds.\nComputer Won: {computer_score} rounds.\nRounds Tied: {rounds_tied}")