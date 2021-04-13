import random


# Functions go here

def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an integer that is more than 0"
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        response = input(question).lower()

        # iterates through list and if response is an item in the list (or the first letter of an item), the
        # full name item is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()


def yes_no(question):
    valid = False
    while not valid:
        response = input("Would you like to see your stats? ").lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

# Main routine goes here


# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they've played before
# If 'no', show instructions


# Ask user for # of rounds then loop...
game_summary = []

rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # rounds heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)
    choose_instruction = "Please choose rock (r), paper (p), or scissors(s) or 'xxx' to exit "
    choose_error = "Please choose from rock / paper / scissors (or xxx to quit) "

    # Ask user for choice and check its valid
    user_choice = choice_checker(choose_instruction, rps_list, choose_error)

    # end game if exit code is typed
    if user_choice == "xxx":
        break

    # print out choice for comparison purposes
    print("You chose: {}".format(user_choice))

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])
    print("Comp Choice: ", comp_choice)

    # compare choices
    if user_choice == comp_choice:
        result = "tie"
        rounds_drawn += 1
    elif user_choice == "rock" and comp_choice == "scissors":
        result = "won"
    elif user_choice == "paper" and comp_choice == "rock":
        result = "won"
    elif user_choice == "scissors" and comp_choice == "paper":
        result = "won"
    else:
        result = "lost"
        rounds_lost += 1

    if result == "tie":
        feedback = "It's a tie"
    else:

        feedback = "{} vs {} - you {}".format(user_choice, comp_choice, result)

    # output results
    print(feedback)

    round_result = "Round {}: {} vs {}, {}".format(rounds_played + 1, user_choice, comp_choice, result)

    game_summary.append(round_result)

    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break


# Ask user if they want to see their game history.
# If 'yes', show game history

rounds_won = rounds_played - rounds_lost - rounds_drawn

# **** calculate game stats ******
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_tie = rounds_drawn / rounds_played * 100

print()
print("***** Game History *******")
for game in game_summary:
    print(game)

print()

# displays game stats with % values to the nearest whole number
print("******** Game Stats *********")
print("Win: {}, ({:.0f}%)\nLoss: {}, "
      "({:.0f}%)\nTie:{}, ({:.0f}%)".format(rounds_won, percent_win, rounds_lost, percent_lose,
                                            rounds_drawn, percent_tie))

# Show game
# Quick Calculations (stats)
rounds_won = rounds_played - rounds_lost - rounds_drawn

# End of Game Statements
print()
print('***** End Game Summary *****')
print("Won: {} \t|\t Lost: {} \t|\t Draw: {}".format(rounds_won, rounds_lost,
                                                     rounds_drawn))
print("thanks for playing")
