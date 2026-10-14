# Rock, Paper, Scissors - the very first project from the course.
# It's a tiny game, but it sneaks in a LOT of Python basics:
# variables, functions, dictionaries, input, lists, if/elif/else and f-strings.

import random  # a "library" - Python's built-in toolbox for random stuff


# Variables are just names that hold values.
# Writing them in CAPS is a habit people use for things that never change.
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"


def get_choices():
    # input() pauses and waits for the player to type something
    player_choice = input("Enter a choice (rock, paper, scissors): ").lower()

    # A list holds several items in order. random.choice picks one of them.
    options = [ROCK, PAPER, SCISSORS]
    computer_choice = random.choice(options)

    # A dictionary stores pairs: a key and its value.
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    # f-strings let us drop variables right into text using {}
    print(f"You chose {player}, computer chose {computer}")

    # if / elif / else - Python checks each one top to bottom
    if player == computer:
        return "It's a tie!"
    elif player == ROCK:
        # a "nested if" - an if inside another if
        if computer == SCISSORS:
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    elif player == PAPER:
        if computer == ROCK:
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
    elif player == SCISSORS:
        if computer == PAPER:
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."
    else:
        return "Hmm, that's not a valid choice."


# Calling the functions - this is where the game actually runs
choices = get_choices()

# Grabbing values out of the dictionary with their keys
result = check_win(choices["player"], choices["computer"])
print(result)
