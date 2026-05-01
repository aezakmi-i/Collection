print("==========> Odd and Even Checker <==========")
while True:
    try:
        num = int(input("\nEnter a number: "))

        if num % 2 == 0:
            print("\nAnswer: Even")
        else:
            print("\nAnswer: Odd")
    except ValueError:
        print("\nInvalid Input, It only accept whole numbers.")

    again = input("\nWould you like to try again? (Y/N): ")
    match again:
        case "Y" | "y":
            continue
        case "N" | "n":
            print("\nThank you, Goodbye")
            exit()
        case _:
            print("\nInvalid Input")
            continue
