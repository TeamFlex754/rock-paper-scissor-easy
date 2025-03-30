from random import randint

print("....rock.....")
print("....paper.....")
print("....scissors....\n")

while True:

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
            print("Player wins!\n")
        elif computer == "paper":
            print("Computer wins!\n")
    elif player == "paper":
        if computer == "rock":
            print("Player wins!\n")
        elif computer == "scissors":
            print("Computer wins!\n")
    elif player == "scissors":
        if computer == "paper":
            print("Player wins!\n")
        elif computer == "rock":
            print("Computer wins!\n")
    else:
        print("Something went wrong!")

    continue_game = input("Play again? (y/n): ").lower()
    if continue_game != "y":
        print("Thanks for playing!")
        break

