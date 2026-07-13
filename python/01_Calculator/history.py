import json
from datetime import datetime

HISTORY_FILE = "history.json"


def save_history(operation, expression, result):
    record = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "operation": operation,
        "expression": expression,
        "result": result,
    }

    try:
        with open(HISTORY_FILE, "r") as file:
            history = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        history = []

    history.append(record)

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)