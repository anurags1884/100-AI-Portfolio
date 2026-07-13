from constants import APP_NAME, VERSION, MENU
from operations import add
from validator import get_number

print("=" * 60)
print(APP_NAME.center(60))
print(f"Version {VERSION}".center(60))
print("=" * 60)

print(MENU)

choice = input("Enter your choice (0-7): ")

if choice == "1":
    print("\n------ Addition ------")

    num1 = get_number("Enter First Number : ")
    num2 = get_number("Enter Second Number: ")

    result = add(num1, num2)

    print("-" * 40)
    print(f"Result = {result}")
    print("-" * 40)

elif choice == "0":
    print("\nThank you for using the calculator.")

else:
    print("\nFeature coming in next step...")