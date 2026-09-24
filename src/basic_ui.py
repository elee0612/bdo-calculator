import sys
import time
import fishing_events
import trade_crates

def exit_program():
    print("Exiting the program. Goodbye!")
    time.sleep(3)
    sys.exit()

def return_to_menu():
    user_choice = input("Return to the main menu? (1: Yes/2: No): ")
        
    match user_choice:
        case "1":
            menu()
        case "2":
            exit_program()
        case _:
            print("Invalid input. Please enter '1' or '2'.")

def menu():
    program_running = True
    
    while program_running == True:
        print("Select an option:")
        print("1. Fishing Events")
        print("2. Trade Crates")
        print("3. Exit")
        
        user_choice = input("Enter your choice (1-3): ")
        match user_choice:
            case "1":
                print("Fishing Events selected.")
                bountiful = int(input("Enter the number of Bountiful Clams: "))
                mystical = int(input("Enter the number of Mystical Clams: "))
                precious = int(input("Enter the number of Precious Clams: "))
                print()
                
                fishing_events.clams(precious, mystical, bountiful)
                return_to_menu()
            case "2":
                print("Trade Crates selected.")
                steel = int(input("Enter the number of Steel Ingot Crates: "))
                bronze = int(input("Enter the number of Bronze Ingot Crates: "))
                snowfield = int(input("Enter the number of Snowfield Jade Boxes: "))
                calpheon = int(input("Enter the number of Calpheon Timber Crates: "))
                serendia = int(input("Enter the number of Serendia Timber Crates: "))
                thorn = int(input("Enter the number of Thorn Timber Crates: "))
                palm = int(input("Enter the number of Palm Timber Crates: "))
                print()
                
                trade_crates.valencia_to_nampo(steel, bronze, snowfield, calpheon, serendia, thorn, palm)
                return_to_menu()
            case "3":
                exit_program()
            case _:
                print("Invalid choice. Please select a valid option (1-3).")