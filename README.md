# 3.2 Rock, Paper, Scissors

**Objective**:
In this assignment, you will design and implement a simple text-based "Rock, Paper, Scissors" game using Python functions. The goal is to practice writing functions that take parameters and return values, as well as functions that call other helper functions. The player will play against the computer, and the game will track the score across multiple rounds.

---

### Game Description:
In this game, the player and the computer will simultaneously choose one of the following: rock, paper, or scissors. The rules for winning are:
- Rock beats scissors.
- Scissors beat paper.
- Paper beats rock.

The game will consist of multiple rounds, and after each round, the score will be updated based on whether the player or computer wins. The game ends when the player chooses to stop playing.

#### Additional Features:
1. Players will be able to choose how many rounds they want to play, or they can play until they choose to stop.
2. The game will keep track of the score (wins, losses, and ties).
3. After each round, the player will be asked whether they want to play another round.

---

### Instructions:

1. **Setup the Game**:
   Write a function to set up the game. This function will start the game, display the instructions, and prompt the player to choose how many rounds they would like to play.

2. **Get Player's Choice**:
   Write a function that prompts the player to choose either rock, paper, or scissors. This function should validate the input to make sure it’s one of the three options.

3. **Get Computer's Choice**:
   Write a function that randomly selects either rock, paper, or scissors for the computer. Use Python's `random` module to generate the computer's choice.

   The *randint(min_value, max_value)* method returns an integer number selected element from the specified range.

   ```python
   num = randint(1,3)
   ```

4. **Determine the Winner**:
   Write a function that compares the player's choice to the computer's choice and determines the winner of the round. The function should return whether the player won, lost, or if it was a tie.

5. **Update and Display Score**:
   Write a function to update and display the score after each round. The score should include how many rounds the player has won, lost, or tied.

6. **Play Again**:
   After each round, ask the player if they want to play another round. If they choose yes, the game will continue. If they choose no, the game will end and display the final score.

---

### Requirements:
You must create and use **at least five functions** in your game. Below are the functions you must implement:

1. **start_game()**:
   - This function will start the game, display the instructions, and set up the number of rounds the player wants to play.

2. **get_player_choice()**:
   - This function prompts the player to input their choice (rock, paper, or scissors) and validates the input.

3. **get_computer_choice()**:
   - This function randomly selects the computer's choice using the `random.choice()` method.

4. **determine_winner(player_choice, computer_choice)**:
   - This function compares the player's choice and the computer's choice and returns a string indicating whether the player won, lost, or if it was a tie.

5. **update_score(winner, score)**:
   - This function updates the score based on the outcome of the round and prints the current score.



---

### Example Gameplay:

```
Welcome to Rock, Paper, Scissors!
How many rounds would you like to play? 3

Round 1:
Enter your choice (rock, paper, or scissors): rock
Computer chose: scissors
You won this round!
Score - Wins: 1, Losses: 0, Ties: 0

Round 2:
Enter your choice (rock, paper, or scissors): paper
Computer chose: 🪨
You won this round!
Score - Wins: 2, Losses: 0, Ties: 0

Round 3:
Enter your choice (rock, paper, or scissors): scissors
Computer chose: scissors
This round was a tie!
Score - Wins: 2, Losses: 0, Ties: 1

Game over! Final Score - Wins: 2, Losses: 0, Ties: 1
```

### Grading Criteria:

1. **Correctness**: The game works as described, and the player can successfully play multiple rounds.
2. **Use of Functions**: You have used at least five functions in your game, with clear separation of tasks.
3. **User Interaction**: The game provides clear feedback to the player after each round and correctly handles the player's inputs.
4. **Code Readability**: Your code is well-organized, with proper indentation, comments, and meaningful variable/function names.

