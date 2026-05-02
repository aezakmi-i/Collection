print("==========> User Input Multiplication Table <==========")

while True:
    try:
        multiplied = int(input("\nEnter a number to be multiplied: "))
        multiplier = int(input("Enter the maximum multiplier: "))

        print("\nResult:\n")
        for i in range(1, multiplier + 1 ):
            print(f"{multiplied} x {i} = {multiplied * i}")
            print("-" * 30)

    except ValueError:
        print("\nInvalid Input: Must be a number.")

    again = input("\nWould you like to continue? (Y/N): ")
    match again:
        case "Y" | "y":
            continue
        case "N" | "n":
            print("\nThank you, Goodbye!")
            break
        case _:
            print(f"\n'{again}' is not a valid input.\nClosing program...")
            break
