import random
import time

attempts = 0


def playagain():
    global attempts
    answer = input("Do you want to play again? (y/n)")
    if answer == "y" or answer == "Y":
        attempts += 1
        playgame()

def playgame():
    global attempts
    items = ["rock", "paper", "scissors", "rock", "paper", "scissors", "rock", "paper", "scissors", "rock", "paper",
             "scissors", "rock", "paper", "scissors", "rock", "paper", "scissors"]

    ei = items[random.randint(0, 17)]

    time.sleep(0.5)
    print("enemy has chosen.")
    time.sleep(0.5)

    if attempts == 0:
        print("Item guide:\n rock: type the number 1\n paper: type the number 2 \n scissors: type the number 3\n")
        print("\n")
        time.sleep(0.5)

    chosen = input("Choose your numbered item: ")

    # rock
    if chosen == "1":
        if ei == "scissors":
            print("You won!")
            playagain()

        else:
            if ei == "paper":
                print("You lose!")
                playagain()
            else:
                if ei == "rock":
                    print("draw!")
                    attempts += 1
                    playgame()

    # paper
    if chosen == "2":
        if ei == "rock":
            print("You won!")
            playagain()

        else:
            if ei == "scissors":
                print("You lose!")
                playagain()
            else:
                if ei == "paper":
                    print("draw!")
                    attempts += 1
                    playgame()

    # scissors
    if chosen == "3":
        if ei == "paper":
            print("You won!")
            playagain()

        else:
            if ei == "rock":
                print("You lose!")
                playagain()
            else:
                if ei == "scissors":
                    print("draw!")
                    attempts += 1
                    playgame()


playgame()
