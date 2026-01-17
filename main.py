# AuthGuardX - Main Menu
# Beginner-friendly CLI version

from modules.dictionary_generator import run_dictionary_generator
from modules.strength_analyzer import run_strength_analyzer
from modules.brute_force_simulator import run_brute_force_simulator
from modules.hash_identifier import run_hash_identifier
from modules.report_generator import run_report_generator

def show_menu():
    print("\n" + "=" * 40)
    print("        AuthGuardX Toolkit")
    print("=" * 40)
    print("1. Dictionary Generator")
    print("2. Password Strength Analyzer")
    print("3. Brute Force Simulator")
    print("4. Hash Type Identifier")
    print("5. Generate Security Report")
    print("6. Exit")
    print("=" * 40)

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            run_dictionary_generator()

        elif choice == "2":
            run_strength_analyzer()

        elif choice == "3":
            run_brute_force_simulator()

        elif choice == "4":
            run_hash_identifier()

        elif choice == "5":
            run_report_generator()

        elif choice == "6":
            print("\nExiting AuthGuardX. Stay secure! 🔐")
            break

        else:
            print("\nInvalid option. Please choose between 1 and 6.")

if __name__ == "__main__":
    main()
