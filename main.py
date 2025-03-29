# print("...rock...")
# print("...paper...")
# print("...scissors...")
# player1_choice = input("(enter Player 1's choice): ").lower()
# player2_choice = input("(enter Player 2's choice): ").lower()
# player1 = "Player 1"
# player2 = "Player 2"
# winner = None
#
# if player1_choice == "rock" and player2_choice == "scissors":
#     winner = player1
# elif player1_choice == "paper" and player2_choice == "rock":
#     winner = player1
# elif player1_choice == "scissors" and player2_choice == "paper":
#     winner = player1
# else:
#     winner = player2
#
# print(f"{winner} wins!")

from random import randint

player = input("Player 1, make your move: ").lower()
rand_num = randint(0,2)

if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"Computer picks {computer}.")

if player == computer:
    print("It's a tie!")
elif player == "rock":
    if computer == "scissors":
        print("Player wins!")
    elif computer == "paper":
        print("Computer wins!")
elif player == "paper":
    if computer == "rock":
        print("Player wins!")
    elif computer == "scissors":
        print("Computer wins!")
elif player == "scissors":
    if computer == "paper":
        print("Player wins!")
    elif computer == "rock":
        print("Computer wins!")
else:
    print("Something went wrong!")