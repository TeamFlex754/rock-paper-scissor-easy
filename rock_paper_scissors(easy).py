print("...rock...")
print("...paper...")
print("...scissors...")
player1_choice = input("(enter Player 1's choice): ").lower()
player2_choice = input("(enter Player 2's choice): ").lower()
player1 = "Player 1"
player2 = "Player 2"
winner = None

if player1_choice == "rock" and player2_choice == "scissors":
    winner = player1
elif player1_choice == "paper" and player2_choice == "rock":
    winner = player1
elif player1_choice == "scissors" and player2_choice == "paper":
    winner = player1
else:
    winner = player2

print(f"{winner} wins!")