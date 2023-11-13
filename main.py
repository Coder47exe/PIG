import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll


while True:
    players = input("Enter th number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("must be between 2 and 4")
    else:
        print("invalid")
max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:                                               # loop for checking player score
    for player_idx in range(players):                                               # loop for individual player turn
        print("\nPlayers number", player_idx + 1, "turn has just started!\n")
        current_score = 0

        while True:                                                                 # loop for  number of turn for each player
            should_roll = input("would you like to roll (y): ")
            if should_roll.lower()!= "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1!, Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print(f"Your total score is:", player_scores[player_idx])
