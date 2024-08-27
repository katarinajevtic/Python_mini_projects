import datetime
import os

DIARY_FILE = "diary.txt"



def write_entry(entry):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(DIARY_FILE, "a") as f:
        f.write(f"{timestamp}\n{entry}\n\n")
        print("Entry successful added!")


def read_entry():
    try:
        with open(DIARY_FILE, "r") as f:
            entries = f.read()
            if entries:
                print(entries)
            else:
                print("No entries found")
    except FileNotFoundError:
        print("No entries found in the diary")


def main():
    print("---Welcome to your personal diary!---")
    if not os.path.exists(DIARY_FILE):
        with open(DIARY_FILE, "w"):
            pass

    while True:
        print("\n Menu:")
        print("1. Write a new entry")
        print("2. Read all entries")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            entry = input("Write your entry: ")
            if entry.strip():
                write_entry(entry)
            else:
                print("Entry can't be empty")
        elif choice == "2":
            read_entry()
        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select valid option.")


if __name__ == "__main__":
    main()
