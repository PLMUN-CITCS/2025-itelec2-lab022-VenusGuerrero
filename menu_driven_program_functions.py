def display_menu():
    print("\nMenu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")

def greet_user():
    print("Hello! Welcome!")

def get_integer_input():
    while True:
        try:
            number = int(input("Enter an integer: "))
            return number
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is an Even number."
    return f"{number} is an Odd number."

def even_odd_checker_action():
    number_final = get_integer_input()
    result = check_even_odd(number_final)
    print(result)

def handle_menu_choice(choice):
    if choice == 1:
        greet_user()
    elif choice == 2:
        even_odd_checker_action()
    elif choice == 3:
        print("Exiting the program. Goodbye!")
        return True
    else:
        print("\nInvalid choice. Please enter a number between 1 and 3.")
    return False


while True:
    display_menu()
    try:
        user_choice = int(input("Enter your choice (1-3): "))
        if handle_menu_choice(user_choice):
            break
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")
