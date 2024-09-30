### Python Assignment: Rock, Paper, Scissors Game (Simplified)

**Objective**: In this assignment, you will write a series of Python functions that will be used to create a Rock, Paper, Scissors game. Your task is to write functions to handle the user input, computer choices, score tracking, and determining the winner of the game.

---

### Part 1: Setup Instructions

Before writing your functions, here's an outline of how the game will work:

1. Provide a brief description of how "Rock, Paper, Scissors" is played.
2. Ask the player for their name
2. Ask for the number of rounds
3. Game Loop: For each round, the player and the computer will select either rock, paper, or scissors. The winner of each round will be determined based on the choices.

At the end of the game, a final winner will be declared based on the total scores of both the player and the computer.

---

### Part 2: Function Descriptions

You need to implement the following functions based on the descriptions provided below. Each function should have a clear, well-defined purpose.

---

1. **`get_player_choice()`**:
   - **Purpose**: This function will ask the player for their choice of either "rock," "paper," or "scissors."
   - **Input**: The function takes the player's name as an argument so that you can customize the prompt (e.g., "David, enter your choice:").
   - **Output**: The function should return the corresponding emoji for the player's choice (🪨 for rock, 📄 for paper, ✂️ for scissors). If the player enters an invalid choice, the function should prompt the player again until a valid choice is entered.

   - Example emojis:
     ```python
     rock = "🪨"
     paper = "📄"
     scissors = "✂️"
     ```

---

2. **`get_computer_choice()`**:
   - **Purpose**: This function randomly selects either "rock," "paper," or "scissors" as the computer's choice.
   - **Input**: None.
   - **Output**: The function should return the emoji that corresponds to the computer's randomly selected choice.
   - **Hint**: Use Python’s `random.choice()` function to randomly pick from a list containing the rock, paper, and scissors emojis.

---

3. **`determine_winner(player_choice, computer_choice)`**:
   - **Purpose**: This function compares the player's choice with the computer's choice to determine who won the round.
   - **Input**: The function takes two arguments:
     - `player_choice`: the player's selected emoji.
     - `computer_choice`: the computer's selected emoji.
   - **Output**: The function should return:
     - `"player"` if the player wins the round.
     - `"computer"` if the computer wins the round.
     - `"tie"` if the round is a tie.
   - **Hint**: Implement the rules of Rock, Paper, Scissors:
     - Rock beats scissors.
     - Scissors beat paper.
     - Paper beats rock.
     - If both players make the same choice, it's a tie.

---

4. **`update_score(result, player_score, computer_score)`**:
   - **Purpose**: This function updates the scores based on the result of the round.
   - **Input**: The function takes three arguments:
     - `result`: `"player"`, `"computer"`, or `"tie"`, depending on who won the round.
     - `player_score`: the current player score.
     - `computer_score`: the current computer score.
   - **Output**: The function should return the updated player and computer scores.



---

### Part 3: Game Logic Overview

Once you have written the above functions, the game will work as follows:

1. **Setup**: The player will input their name and the number of rounds.
2. **Gameplay Loop**:
   - For each round:
     - The player selects either rock, paper, or scissors.
     - The computer randomly selects rock, paper, or scissors.
     - The winner of the round is determined.
     - Scores are updated.
3. **End of Game**: After all rounds are complete, the final scores are compared, and the winner of the game is declared based on who won the most rounds.



---

### Hints:

- **Random Choice**: Use `random.choice()` to select the computer’s move.
- **Input Validation**: Ensure the player's choice is valid by checking for rock, paper, or scissors.
- **Game Flow**: Each function will handle a specific part of the game logic, so keep them organized and clearly defined.
