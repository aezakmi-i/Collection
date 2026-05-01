def celsius(temperature):
    return (temperature * 9 / 5) + 32

def fahrenheit(temperature):
    return (temperature - 32) * 5/9

print("==========> TEMPERATURE CONVERTER <==========")
while True:
    try:
        print("\nType 'C' for Celsius to Fahrenheit\nType 'F' for Fahrenheit to Celsius\nType 'E' to Exit")
        print("What Temperature value you want to convert to?")
        choice = input("Your choice: ")
        print()

        match choice:
            case "C" | "c":
                celTemperature = int(input("Enter your Temperature in Celsius: "))
                #celsius(celTemperature)
                print("Your Temperature in Fahrenheit is: ", celsius(celTemperature))
            case "F" | "f":
                fahTemperature = int(input("Enter your Temperature in Fahrenheit: "))
                print(f"Your Temperature in Fahrenheit is: {fahrenheit(fahTemperature):.2f}", )
            case "E" | "e":
                print("Thank you, Goodbye!")
                exit()
            case _:
                print("Invalid choice")
                continue

        again = input("\nConvert another temperature? (Y/N): ")

        match again:
            case "Y" | "y":
                continue
            case "N" | "n":
                print("\nThank you, Goodbye!")
                exit()
            case _:
                print("\nInvalid choice")
                continue

    except ValueError:
        print("\nInvalid Input")
