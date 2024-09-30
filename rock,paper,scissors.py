from random import randint, choice
import os

######### Function Definitions #########
def print_instructions():
    print("\n\nWelcome to Rock, Paper, Scissors!\n")
    print("Rock, Paper, Scissors is a simple hand game played between two people. Each player simultaneously chooses one of three options: rock, paper, or scissors.\nThe winner of each round is determined by the following rules:\n\n  - Rock (🪨) beats Scissors (✂️) because rock can crush scissors.\n  - Scissors (✂️) beats Paper (📄) because scissors can cut paper.\n  - Paper (📄) beats Rock (🪨) because paper can wrap around rock.\n\nIf both players choose the same option, the round is a tie. The game is typically played in multiple rounds, and the player with the most wins at the end is the overall winner.\n\n")




######### Main Program #########
rock = "🪨"
paper = "📄"
scissors = "✂️"

print_instructions()