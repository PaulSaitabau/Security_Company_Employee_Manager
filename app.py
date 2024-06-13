from models import SecurityCompany

if __name__ == "__main__":
    company = SecurityCompany()

    while True:
        print("\n1. Add Guard")
        print("2. List Guards")
        print("3. Add Incident")
        print("4. List Incidents")
        print("5. Delete Guard")
        print("6. Exit")
        choice = input("Enter your choice: ")


        if choice == '1':
            company.add_guard()
        elif choice == '2':
            company.list_guards()
        elif choice == '3':
            company.add_incident()
        elif choice == '4':
            company.list_incidents()
        elif choice == '5':
            company.delete_guard()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
