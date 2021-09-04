import random

# Function to check whether you win the game or computer
def gameWin(you, computer):
    if you == computer:
        return None

    elif computer == "r":
        if you == "p":
            return True
        elif you == "s":
            return False

    elif computer == "p":
        if you == "s":
            return True
        elif you == "r":
            return False

    elif computer == "s":
        if you == "r":
            return True
        elif you == "p":
            return False


print("Computer's turn: Rock(r) Paper(p) or Scissor(s)?")
randNo = random.randint(1, 3)
if randNo == 1:
    computer = "r"
elif randNo == 2:
    computer = "p"
elif randNo == 3:
    computer = "s"


you = input("Your turn: Rock(r) Paper(p) or Scissor(s)?: ")
print("\n")


result = gameWin(you, computer)


print(f"Computer chose {computer}")
print(f"You chose {you}")
print("\n")


if result == None:
    print("It's a tie!")
elif result:
    print("You Won!")
else:
    print("You Lose!")
