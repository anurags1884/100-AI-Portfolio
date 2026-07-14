from scientific import (
    square_root,
    cube_root,
    percentage,
    factorial,
    absolute,
    logarithm,
    natural_log,
    sine,
    cosine,
    tangent,
    degree_to_radian,
    radian_to_degree
)

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

    choice = input("Enter your choice (0-21): ").strip()

    # Exit
    if choice == "0":
        print("\nThank you for using the calculator.")
        break

    # View History
    elif choice == "8":
        show_history()
        input("\nPress Enter to continue...")
        continue

    # Clear History
    elif choice == "9":
        clear_history()
        input("\nPress Enter to continue...")
        continue

    # Cube Root
    elif choice == "11":

        try:
            number = get_number("\nEnter Number : ")

            result = cube_root(number)

            print("\n" + "=" * 40)
            print(f"∛{number} = {result}")
            print("=" * 40)

            save_history(
                "Cube Root",
                f"∛{number}",
                result
            )

        except Exception as e:
            print("\nError :", e)

        input("\nPress Enter to continue...")
        continue

    # Percentage
    elif choice == "12":

        try:
            print("\nPercentage Calculator")
            value = get_number("Enter Value : ")
            total = get_number("Enter Total : ")

            result = percentage(value, total)

            print("\n" + "=" * 40)
            print(f"{value} is {result:.2f}% of {total}")
            print("=" * 40)

            save_history(
                "Percentage",
                f"{value}/{total} × 100",
                f"{result:.2f}%"
            )

        except Exception as e:
            print("\nError :", e)

        input("\nPress Enter to continue...")
        continue

    # Factorial
    elif choice == "13":

        try:
            number = get_number("\nEnter Whole Number : ")

            result = factorial(number)

            print("\n" + "=" * 40)
            print(f"{int(number)}! = {result}")
            print("=" * 40)

            save_history(
                "Factorial",
                f"{int(number)}!",
                result
            )

        except Exception as e:
            print("\nError :", e)

        input("\nPress Enter to continue...")
        continue

    # Absolute Value
    elif choice == "14":

        try:
            number = get_number("\nEnter Number : ")

            result = absolute(number)

            print("\n" + "=" * 40)
            print(f"|{number}| = {result}")
            print("=" * 40)

            save_history(
                "Absolute",
                f"|{number}|",
                result
            )

        except Exception as e:
            print("\nError :", e)

        input("\nPress Enter to continue...")
        continue

    # Logarithm (Base 10)
    elif choice == "15":

        try:
            number = get_number("\nEnter Positive Number : ")

            result = logarithm(number)

            print("\n" + "=" * 40)
            print(f"log₁₀({number}) = {result:.6f}")
            print("=" * 40)

            save_history(
                "Logarithm",
                f"log10({number})",
                round(result, 6)
            )
        except Exception as e:
            print("\nError :", e)

        input("\nPress Enter to continue...")
        continue

    # Natural Log
    elif choice == "16":

        try:
            number = get_number("\nEnter Positive Number : ")

            result = natural_log(number)

            print("\n" + "=" * 40)
            print(f"ln({number}) = {result:.6f}")
            print("=" * 40)

            save_history(
                "Natural Log",
                f"ln({number})",
                round(result, 6)
            )

        except Exception as e:
            print("\nError :", e)

        input("\nPress Enter to continue...")
        continue

    # Sine
    elif choice == "17":

        try:
            angle = get_number("\nEnter Angle (Degrees) : ")

            result = sine(angle)

            print("\n" + "=" * 40)
            print(f"sin({angle}°) = {result:.6f}")
            print("=" * 40)

            save_history(
                "Sine",
                f"sin({angle})",
                round(result, 6)
            )

        except Exception as e:
            print("\nError :", e)

        input("\nPress Enter to continue...")
        continue

    # Cosine
    elif choice == "18":

        try:
            angle = get_number("\nEnter Angle (Degrees) : ")

            result = cosine(angle)

            print("\n" + "=" * 40)
            print(f"cos({angle}°) = {result:.6f}")
            print("=" * 40)

            save_history(
                "Cosine",
                f"cos({angle})",
                round(result, 6)
            )

        except Exception as e:
            print("\nError :", e)

        input("\nPress Enter to continue...")
        continue

    # Tangent
    elif choice == "19":

        try:
            angle = get_number("\nEnter Angle (Degrees) : ")

            result = tangent(angle)

            print("\n" + "=" * 40)
            print(f"tan({angle}°) = {result:.6f}")
            print("=" * 40)

            save_history(
                "Tangent",
                f"tan({angle})",
                round(result, 6)
            )

        except Exception as e:
            print("\nError :", e)

        input("\nPress Enter to continue...")
        continue
    
        # Degree to Radian
    elif choice == "20":

        try:
            angle = get_number("\nEnter Degrees : ")

            result = degree_to_radian(angle)

            print("\n" + "=" * 40)
            print(f"{angle}° = {result:.6f} rad")
            print("=" * 40)

            save_history(
                "Degree to Radian",
                f"{angle}°",
                round(result, 6)
            )

        except Exception as e:
            print("\nError :", e)

        input("\nPress Enter to continue...")
        continue
    
        # Radian to Degree
    elif choice == "21":

        try:
            angle = get_number("\nEnter Radians : ")

            result = radian_to_degree(angle)

            print("\n" + "=" * 40)
            print(f"{angle} rad = {result:.6f}°")
            print("=" * 40)

            save_history(
                "Radian to Degree",
                f"{angle} rad",
                round(result, 6)
            )

        except Exception as e:
            print("\nError :", e)

        input("\nPress Enter to continue...")
        continue
    
    

    # Square Root
    elif choice == "10":

        try:
            number = get_number("\nEnter Number : ")

            result = square_root(number)

            print("\n" + "=" * 40)
            print(f"√{number} = {result}")
            print("=" * 40)

            save_history(
                "Square Root",
                f"√{number}",
                result
            )

        except Exception as e:
            print("\nError :", e)

        input("\nPress Enter to continue...")
        continue

    # Invalid Choice
    elif choice not in [
        "1", "2", "3", "4", "5", "6", "7",
        "8", "9",
        "10", "11", "12", "13", "14",
        "15", "16", "17", "18", "19",
        "20", "21"
    ]:

        print("\n❌ Invalid Choice")
        input("\nPress Enter to continue...")
        continue

    # Basic Calculator
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

        save_history(
            symbol,
            expression,
            result
        )

    except Exception as e:
        print("\nError :", e)

    input("\nPress Enter to continue...")