import random

print("==========> Number Guessing Game <==========\n")
guessNum = random.randint(1, 50)

while True:
    stringNum = str(guessNum)
    replaced = stringNum.replace(stringNum, "#" * len(stringNum))
    print("                    " + "?" * 6 + "\n                    > " + replaced + " <\n" + "                    " + "?" * 6)
    #print(guessNum)
    #print(type(guessNum))
    #print(type(stringNum))
    try:
        guess = int(input("\nGuess a number between 1 and 50: "))
        if guess > guessNum:
            print("> Lower!")
        elif guess < guessNum:
            print("> Higher!")
        else:
            print("> Correct! You guessed the number!\n")
            again = input("Do you want to play again? (Y/N): ")

            if again == "Y" or again == "y":
                guessNum = random.randint(1, 50)
                continue
            elif again == "N" or again == "n":
                break
            else:
                print("\nError: Invalid input.\nExiting...")
                break

    except ValueError:
        print("> Error: Please enter a number.\n")



