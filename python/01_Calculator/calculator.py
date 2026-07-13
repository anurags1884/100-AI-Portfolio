from constants import APP_NAME, VERSION, MENU
from operations import (
    add,
    subtract,
    multiply,
    divide,
    modulus,
    power,
    floor_division,
)
from validator import get_number


print("=" * 60)
print(APP_NAME.center(60))
print(f"Version {VERSION}".center(60))
print("=" * 60)


while True:

    print(MENU)

    choice = input("Enter your choice (0-7): ")

    if choice == "0":
        print("\nThank you for using the calculator.")
        break

    elif choice in ["1", "2", "3", "4", "5", "6", "7"]:

        num1 = get_number("\nEnter First Number : ")
        num2 = get_number("Enter Second Number: ")

        if choice == "1":
            result = add(num1, num2)
            operation = "+"

        elif choice == "2":
            result = subtract(num1, num2)
            operation = "-"

        elif choice == "3":
            result = multiply(num1, num2)
            operation = "*"

        elif choice == "4":
            result = divide(num1, num2)
            operation = "/"

        elif choice == "5":
            result = modulus(num1, num2)
            operation = "%"

        elif choice == "6":
            result = power(num1, num2)
            operation = "^"

        elif choice == "7":
            result = floor_division(num1, num2)
            operation = "//"

        print("\n" + "-" * 40)
        print(f"{num1} {operation} {num2} = {result}")
        print("-" * 40)

    else:
        print("\n❌ Invalid Choice. Please try again.")