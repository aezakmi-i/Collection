def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b

print("==========> Welcome to Lance's Mini Calculator <==========")
print()
while True:
    try:
        fnum = int(input("Enter first number: "))
        operator = input("Choose operator (+,-,*,/): ")
        snum = int(input("Enter second number: "))
        match operator:
            case "+":
                print(addition(fnum, snum))
            case "-":
                print(subtraction(fnum, snum))
            case "*":
                print(multiplication(fnum, snum))
            case "/":
                if snum == 0:
                    print("Cannot divide by zero")
                else:
                    print(division(fnum, snum))
            case _:
                print("Invalid operator")

        print()
        again = input("Do you want to continue? (y/n): ")
        print()
        if again != "y":
            print("Goodbye")
            break

    except ValueError:
        print("Invalid input")













