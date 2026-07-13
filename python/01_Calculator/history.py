import json
from datetime import datetime
import os

HISTORY_FILE = "history.json"


def load_history():

    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w") as f:
            json.dump([], f)

    try:
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)

    except:
        return []


def save_history(operation, expression, result):

    history = load_history()

    history.append({
        "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "operation": operation,
        "expression": expression,
        "result": result
    })

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)


def show_history():

    history = load_history()

    if len(history) == 0:
        print("\nNo History Found.")
        return

    print("\n" + "=" * 60)
    print("CALCULATION HISTORY")
    print("=" * 60)

    for i, item in enumerate(history, start=1):

        print(f"\nRecord {i}")
        print(f"Time       : {item['time']}")
        print(f"Expression : {item['expression']}")
        print(f"Result     : {item['result']}")


def clear_history():

    with open(HISTORY_FILE, "w") as file:
        json.dump([], file, indent=4)

    print("\nHistory Cleared Successfully.")