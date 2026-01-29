import os
from datetime import datetime
FileName="journal.txt"
print("Welcome to Personal Journal Manager!")
def menu():
    while True:
        print("Please select an option:")
        print("\n1. Add New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")
        choice=int(input("Enter user input: "))
        
        match choice:

            case 1:
                entry=input("Enter your journal entry: ")
                timestamp= datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

                with open(FileName,"a") as file:
                    file.write(timestamp + "\n" + entry + "\n\n")
                    print("Entry added successfully.")
                
            case 2:
                try:
                    with open(FileName,"r") as file:
                        content=file.read()
                        if content.strip():
                            print("Your journal entries:\n------------------------------------------------")
                            print(content) 
                        else:
                         print("No journal entries found")
                except Exception as e:
                    print("Error reading file: ", e)
            
            case 3:
                keyword=input("Enter keyword or date: ")
                try:
                    with open(FileName, "r") as file:
                        entries = file.readlines()
                    print("Matching Entries:\n--------------------------------------")
                    for line in entries:
                        if keyword.lower() in line.lower():
                            print(line.strip())
                            found = True
                    if not found:
                        print(f"No entries were found for the keyword: {keyword}")
                except Exception as e:
                    print("Error searching file:", e)

            case 4:
                confirm = input("Are you sure you want to delete all entries? (yes/no): ")
                if confirm.lower() == "yes":
                    try:
                        os.remove(FileName)
                        print("All journal entries have been deleted.")
                    except Exception as e:
                        print("Error deleting file:", e)
                else:
                    print("Deletion cancelled.")
            
            case 5:
                print("Thank you for using Personal Journal Manager. Goodbye!")
                break

            case _:
                print("Invalid option. Please select a valid option from the menu.")

if __name__ == "__main__":
    menu()

