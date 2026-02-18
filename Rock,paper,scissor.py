import random

def play_game(rounds=0, player_wins=0, computer_wins=0):
    if rounds == 3:
        print(f"\nGame Over! Final Score - You: {player_wins}, Computer: {computer_wins}")
        return
    
    choices = ["rock", "paper", "scissors"]
    player = input("\nEnter rock, paper, or scissors (or 'quit' to exit): ").lower()
    
    if player == "quit":
        print(f"Final Score - You: {player_wins}, Computer: {computer_wins}")
        return
    
    if player not in choices:
        print("Invalid choice! Try again.")
        return play_game(rounds, player_wins, computer_wins)
    
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    
    if player == computer:
        print("It's a tie!")
        return play_game(rounds + 1, player_wins, computer_wins)
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win this round!")
        return play_game(rounds + 1, player_wins + 1, computer_wins)
    else:
        print("Computer wins this round!")
        return play_game(rounds + 1, player_wins, computer_wins + 1)

play_game()