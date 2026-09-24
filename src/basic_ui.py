import sys
import time
import fishing_events
import trade_crates

def get_int(prompt):
    # Repeatedly prompt until the user enters a valid non-negative integer
    while True:
        user_choice = input(prompt)
        if user_choice.isdigit():
            return int(user_choice)
        print()
        print("Invalid input. Please enter a valid number.")
        print()

# Exits the program
def exit_program():
    print("Exiting the program. Goodbye!")
    time.sleep(3)
    sys.exit()

# Returns to the main menu
def return_to_menu():
    user_choice = get_int("Return to the main menu? (1: Yes/2: No): ")
    print()
        
    match user_choice:
        case 1:
            menu()
        case 2:
            exit_program()
        case _:
            print("Invalid input. Please enter '1' or '2'.")
            print()
            return_to_menu()

# Displays the main menu and handles user input
def menu():
    program_running = True
    
    # Main Menu Loop
    while program_running == True:
        print("Select an option:")
        print("1. Fishing Events")
        print("2. Trade Crates")
        print("3. Exit")
        print()
        
        user_choice = get_int("Enter your choice (1-3): ")
        print()
        match user_choice:
            case 1:
                print("Fishing Events selected.")
                bountiful = get_int("Enter the number of Bountiful Clams: ")
                mystical = get_int("Enter the number of Mystical Clams: ")
                precious = get_int("Enter the number of Precious Clams: ")
                print()
                
                # Call the clams function from fishing_events.py with user input
                fishing_events.clams(bountiful, mystical, precious)
                return_to_menu()
            case 2:
                print("Trade Crates selected.")
                steel = get_int("Enter the number of Steel Ingot Crates: ")
                bronze = get_int("Enter the number of Bronze Ingot Crates: ")
                snowfield = get_int("Enter the number of Snowfield Jade Boxes: ")
                calpheon = get_int("Enter the number of Calpheon Timber Crates: ")
                serendia = get_int("Enter the number of Serendia Timber Crates: ")
                thorn = get_int("Enter the number of Thorn Timber Crates: ")
                palm = get_int("Enter the number of Palm Timber Crates: ")
                print()
                
                # Call the valencia_to_nampo function from trade_crates.py with user input
                trade_crates.valencia_to_nampo(steel, bronze, snowfield, calpheon, serendia, thorn, palm)
                return_to_menu()
            case 3:
                exit_program()
            case _:
                print("Invalid choice. Please select a valid option (1-3).")
                print()