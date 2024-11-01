import sys
import time
import random
import glob
import pyfiglet
import csv


def main():
    name = input("Please Enter your name: ")
    mode = menu(name)
    game = game_mode(mode, name)
    game_maker(word_maker(game), name)


def menu(name):
    print(pyfiglet.figlet_format("Welcome to hangman, " + name, font="small"))
    while True:
        print("━" * 45)
        x = input(
            """please choose what you would like to do:
(1) Begin the game
(2) Add custom theme
(3) Exit\n"""
        )
        if x.isdigit():
            if int(x) <= 3:
                return int(x)
        print("\033[1mInvalid option, please choose between 1-4\033[0m")
        time.sleep(0.7)


def game_mode(n, name):
    if n == 3:
        game_exit(name)
    elif n == 2:
        theme_maker()
    else:
        while True:
            print("━" * 45)
            x = input(
                """please choose a Theme:
(1) History
(2) Countries
(3) Elements
(4) Custom
(5) Exit\n"""
            )
            if x.isdigit():
                if int(x) <= 5:
                    if int(x) == 5:
                        game_exit(name)

                    elif int(x) == 4:
                        y = glob.glob("*.csv")
                        z = 0
                        print("━" * 45)
                        for i in y:
                            if i not in ["1.csv", "2.csv", "3.csv"]:
                                if z == 0:
                                    print("Available files:")
                                print(i)
                                z += 1
                        if z == 0:
                            print(
                                "\033[1mNo Custom .csv files were found, please make one first\033[0m"
                            )
                            time.sleep(0.7)
                            continue
                        print("━" * 45)
                        while True:
                            z = 0
                            x = input("Enter the name of an .csv file: ")
                            if x not in y:
                                print("\033[1mPlease enter a valid .csv file\033[0m")
                                time.sleep(0.7)
                                print("━" * 45)
                                for i in y:
                                    if i not in ["1.csv", "2.csv", "3.csv"]:
                                        if z == 0:
                                            print("Available files:")
                                        print(i)
                                        z = 1
                                print("━" * 45)
                            else:
                                return x
                    return x + ".csv"
            print("\033[1mInvalid option, please choose between 1-5\033[0m")
            time.sleep(0.7)


def word_maker(n):
    x = []
    try:
        with open(n, mode="r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                x.append(row[0])

        y = random.choice(x).lower()
    except (FileNotFoundError, IndexError):
        sys.exit("ERROR: It seems the file you provided was empty")
    return y


def game_maker(n, name):
    z = 0
    correct = set()
    wrong = set()
    print(pyfiglet.figlet_format("Good luck, " + name, font="small"))

    while z != 6:
        output = ""
        print("━" * 30)
        print(hangman[z])
        print("━" * 30)
        for i in n:
            if i in correct:
                output += i
            else:
                output += "_ "
        if output == n:
            break
        print("word: ", output, "\n")
        guess = input("Guess: ").lower()

        if len(guess) != 1:
            print("\033[1mPlease enter in a single character.\033[0m")
            time.sleep(0.7)
            continue

        if guess in n:
            if guess not in correct:
                print(pyfiglet.figlet_format("Correct !", font="small"))
                correct.add(guess[0])
            else:
                print("\033[1mYou already guessed this correctly:\033[0m", guess)
                time.sleep(0.7)
        else:
            if guess in wrong:
                print("\033[1mYou already guessed this incorrectly:\033[0m", guess)
                time.sleep(0.7)
                continue
            print(pyfiglet.figlet_format("Incorrect :( ", font="small"))
            z += 1
            if not guess == "":
                wrong.add(guess[0])
    if z == 6:
        print("━" * 30)
        print(hangman[6])
        print("━" * 30)
        print(pyfiglet.figlet_format("Game Over! ", font="big"))
        print(f"You lose {name}, the correct word was: {n}")
        print("━" * 30)
        print("Correct guesses:", len(correct))
        print("Incorrect guesses:", z)
        print("━" * 30)
        return False

    else:
        print(pyfiglet.figlet_format("You Win! ", font="big"))
        print(f"Congratulations {name}! The word was indeed: {n}")
        print("━" * 30)
        print("Correct guesses:", len(correct))
        print("Incorrect guesses:", z)
        print("━" * 30)
        return True


def theme_maker():
    x = input("Please enter the name of your file (exclude .csv): ")
    with open(x + ".csv", mode="w") as file:
        writer = csv.writer(file)
        while True:
            print("━" * 30)
            print("Use /exit to save and exit the file")
            y = input("Word:  ")
            if y == "/exit":
                break
            writer.writerow([y])
        print("file succesfully saved")
        sys.exit()


def game_exit(name):
    sys.exit(pyfiglet.figlet_format(f"Thanks for playing {name}!", font="small"))


hangman = [
    """
  +---+
  |   |
      |
      |
      |
      |
==========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
==========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
==========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
==========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
==========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
==========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
==========""",
]

if __name__ == "__main__":
    main()
