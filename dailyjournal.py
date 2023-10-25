# Initialize an empty journal
journal = {}

def add_journal_entry():
    date = input("Enter the date (YYYY-MM-DD): ")
    entry = input("Write your journal entry: ")
    journal[date] = entry
    print("Journal entry added for", date)

def get_journal_entry():
    date = input("Enter the date (YYYY-MM-DD) to retrieve the journal entry: ")
    entry = journal.get(date, "No entry found for this date.")
    print(entry)

def main():
    print("Welcome to the Daily Journal Bot!")
    
    while True:
        print("\nOptions:")
        print("1. Add a journal entry")
        print("2. Get a journal entry")
        print("3. Exit")
        
        choice = input("Select an option (1/2/3): ")
        
        if choice == '1':
            add_journal_entry()
        elif choice == '2':
            get_journal_entry()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    main()
