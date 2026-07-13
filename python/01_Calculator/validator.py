def get_number(message):
    
    while True:

        try:
            return float(input(message))

        except ValueError:
            print("Invalid Number. Try Again.")