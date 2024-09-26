from random import randint, choice
import os


rock = "🪨"
paper = "📄"
scissors = "✂️"

def start_game():
    print("\n\nWelcome to Rock, Paper, Scissors!")
    name = input("\nEnter your name:  ")
    rounds = int(input("Enter the number of rounds that you would like to play: "))
    return name, rounds

def get_player_choice(name):
    play = input(f"\n{name}, enter your choice (rock,paper,scissors):  ")
    if play == "rock":
        return rock
    elif play == "paper":
        return paper
    elif play == "scissors":
        return scissors
    else:
        return get_player_choice(name)
    
def get_computer_choice():
    return choice([rock,paper,scissors])
        
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        print(f"\n{name} vs. Computer \n  {player_choice}         {computer_choice}")
        return "t"
    elif (player_choice == rock and computer_choice == scissors) or (player_choice == paper and computer_choice == rock) or (player_choice == scissors and computer_choice == paper):
        print(f"\n{name} vs. Computer \n  {player_choice}         {computer_choice}")
        return "p"
    else: 
        print(f"\n{name} vs. Computer \n  {player_choice}         {computer_choice}")
        return "c"

def update_score(result, player, computer):
    if result == "p":
        player += 1
    elif result =="c":
        computer += 1
    return player, computer

name, rounds = start_game()
os.system('clear')
count = 0
player = 0
computer = 0
while count < rounds:
    player_choice = get_player_choice(name)
    os.system('clear')
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    player,computer = update_score(result, player, computer)
    
    print(f"\nSCORE:\n{name}: {player}\nComputer: {computer}")
    
