from constants import APP_NAME, VERSION, MENU
from operations import (
    add,
    subtract,
    multiply,
    divide,
    modulus,
    power,
    floor_division
)
from validator import get_number
from history import save_history, show_history, clear_history

print("=" * 60)
print(APP_NAME.center(60))
print(f"Version {VERSION}".center(60))
print("=" * 60)

while True:

    print(MENU)

    choice = input("Enter your choice (0-9): ").strip()

    if choice == "0":
        print("\nThank you for using the calculator.")
        break

    elif choice == "8":
        show_history()
        input("\nPress Enter to continue...")
        continue

    elif choice == "9":
        clear_history()
        input("\nPress Enter to continue...")
        continue

    elif choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("\n❌ Invalid Choice")
        input("\nPress Enter to continue...")
        continue

    num1 = get_number("\nEnter First Number : ")
    num2 = get_number("Enter Second Number : ")

    try:

        if choice == "1":
            result = add(num1, num2)
            symbol = "+"

        elif choice == "2":
            result = subtract(num1, num2)
            symbol = "-"

        elif choice == "3":
            result = multiply(num1, num2)
            symbol = "*"

        elif choice == "4":
            result = divide(num1, num2)
            symbol = "/"

        elif choice == "5":
            result = modulus(num1, num2)
            symbol = "%"

        elif choice == "6":
            result = power(num1, num2)
            symbol = "^"

        elif choice == "7":
            result = floor_division(num1, num2)
            symbol = "//"

        expression = f"{num1} {symbol} {num2}"

        print("\n" + "=" * 40)
        print(f"Result : {expression} = {result}")
        print("=" * 40)

        save_history(symbol, expression, result)

    except Exception as e:
        print("\nError :", e)

    input("\nPress Enter to continue...")