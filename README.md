# Rock, Paper, Scissors 

**Objective**: In this assignment, you will write a series of Python functions to create a Rock, Paper, Scissors game. You will handle user input, computer choices, score tracking, and determine the winner of the game.

---

### Part 1: Setup Instructions

Before writing your functions, here's an outline of how the game will work:

1. Briefly explain how "Rock, Paper, Scissors" is played.
2. Ask the player for their name and the number of rounds they wish to play.
3. Game Loop: For each round, the player and computer will choose either rock, paper, or scissors. A winner will be determined for each round, and the scores will be tracked.

At the end of the game, the final winner is declared based on the total scores of the player and the computer.

---

### Part 2: Function Descriptions

You need to implement the following functions. Each function has a clear, well-defined purpose and will be called repeatedly during the game.

---

1. **`get_player_choice(name)`**:
   - **Purpose**: This function prompts the player to choose either "rock," "paper," or "scissors."
   - **Input**: Takes the player's `name` as an argument to customize the prompt (e.g., "David, enter your choice:").
   - **Output**: Returns the corresponding emoji for the player's choice:
     - 🪨 for rock
     - 📄 for paper
     - ✂️ for scissors
   - If the player enters an invalid choice, prompt them again until a valid one is entered.

   Example emojis:
   ```python
   rock = "🪨"
   paper = "📄"
   scissors = "✂️"
   ```

---

2. **`get_computer_choice()`**:
   - **Purpose**: Randomly selects "rock," "paper," or "scissors" as the computer's choice.
   - **Input**: None
   - **Output**: Returns the emoji representing the computer's choice.
   - **Hint**: Use random.randint(1, 3) to generate a random number.
      - If the number is 1, return "🪨" (rock).
      - If the number is 2, return "📄" (paper).
      - If the number is 3, return "✂️" (scissors).

---

3. **`determine_winner_and_score(player_choice, computer_choice, player_score, computer_score)`**:
   - **Purpose**: This function does **two** things:
     1. Determines who wins the round by comparing the player's choice and the computer's choice.
     2. Updates the scores based on the result of the round.
   - **Input**:
     - `player_choice`: The player's selected emoji.
     - `computer_choice`: The computer's selected emoji.
     - `player_score`: The player's current score.
     - `computer_score`: The computer's current score.
   - **Output**: Returns the updated scores for both the player and the computer. It should print the result of the round (who won or if it was a tie).
   - **Hint**: Implement the rules of Rock, Paper, Scissors:
     - Rock beats scissors.
     - Scissors beat paper.
     - Paper beats rock.
     - If both players choose the same option, it’s a tie.

---

### Part 3: Game Logic Overview

Once you've written the above functions, the game will proceed as follows:

1. **Setup**: The player inputs their name and the number of rounds they want to play.
2. **Game Loop**:
   - For each round:
     - The player selects rock, paper, or scissors.
     - The computer randomly selects rock, paper, or scissors.
     - The winner of the round is determined, and the scores are updated.
     - After each round, display the current scores.
3. **End of Game**: After all rounds, compare the final scores and declare the winner (or a tie).

---

### Hints:

- **Random Choices**: Use `random.choice()` for the computer's selection.
- **Input Validation**: Ensure the player's choice is valid (i.e., rock, paper, or scissors).
- **Game Flow**: Write each function to handle a specific part of the game and ensure the main loop calls these functions in sequence for each round.
