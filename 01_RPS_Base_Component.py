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

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item in the list (or the first letter of an item), the
        # full name item is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()


# Main routine goes here


# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they've played before
# If 'no', show instructions


# Ask user for # of rounds then loop...
rounds_played = 0


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
    choose = choice_checker(choose_instruction, rps_list, choose_error)

    # end game if exit code is typed
    if choose == "xxx":
        break

    # print out choice for comparison purposes
    print("You chose: {}".format(choose))

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])
    print("Comp Choice: ", comp_choice)

    # compare choices



    # rest of loop / game

    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break

print("Thanks for playing")

# Ask user if they want to see their game history.
# If 'yes', show game history
