from sqlalchemy.orm import sessionmaker
from database import Base, Guard, Incident
from prettytable import PrettyTable
from sqlalchemy import create_engine
from datetime import datetime

class SecurityCompany:
    def __init__(self):
        try:
            self.engine = create_engine('sqlite:///security_company.db')
            Base.metadata.create_all(self.engine)
            Session = sessionmaker(bind=self.engine)
            self.session = Session()
        except Exception as e:
            print("Error initializing SecurityCompany:", e)
            
    def add_guard(self):
        try:
            department = input("Enter department (Operations/Management): ")
            name = input("Enter guard's name: ")
            start_date_str = input("Enter start date (YYYY-MM-DD): ")
            assignment = input("Enter assignment: ")
            shift = input("Enter shift (Day/Night): ")
            location = input("Enter location: ")

            # Convert start_date_str to a Python date object
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()

            guard = Guard(name=name, start_date=start_date, assignment=assignment, shift=shift, location=location)
            self.session.add(guard)
            self.session.commit()
            print(f"{department.capitalize()} guard added successfully.")
            
            # Debug prints
            print("Debug: Guards in database after adding:")
            guards = self.session.query(Guard).all()
            for guard in guards:
                print(guard.id, guard.name, guard.start_date, guard.assignment, guard.shift, guard.location)
                
        except Exception as e:
            print("Error adding guard:", e)
    
    def list_guards(self):
        try:
            department = input("Enter department (Operations/Management): ")
            department = department.capitalize()  # Capitalize the department name
            
            guards = self.session.query(Guard).filter(Guard.location == department).all()
            if guards:
                table = PrettyTable(['ID', 'Name', 'Start Date', 'Assignment', 'Shift', 'Location'])
                for guard in guards:
                    table.add_row([guard.id, guard.name, guard.start_date, guard.assignment, guard.shift, guard.location])
                print(f"{department} Department Guards:")
                print(table)
            else:
                print("No guards found.")
        except Exception as e:
            print("Error listing guards:", e)


    def add_incident(self):
        try:
            guard_id = int(input("Enter guard ID: "))
            guard = self.session.query(Guard).get(guard_id)
            if guard:
                date_str = input("Enter incident date (YYYY-MM-DD): ")
                description = input("Enter incident description: ")
                department = input("Enter department (Operations/Management): ")

                # Convert date_str to a Python date object
                incident_date = datetime.strptime(date_str, "%Y-%m-%d").date()

                incident = Incident(date=incident_date, description=description, department=department.capitalize(), guard=guard)
                self.session.add(incident)
                self.session.commit()
                print("Incident added successfully.")
            else:
                print("Guard not found.")
        except Exception as e:
            print("Error adding incident:", e)
            
    def list_incidents(self):
        try:
            incidents = self.session.query(Incident).all()
            if incidents:
                table = PrettyTable(['ID', 'Date', 'Description', 'Guard ID', 'Department'])
                for incident in incidents:
                    table.add_row([incident.id, incident.date, incident.description, incident.guard_id, incident.department])
                print("List of Incidents:")
                print(table)
            else:
                print("No incidents found.")
        except Exception as e:
            print("Error listing incidents:", e)

    def delete_guard(self):
        try:
            guard_id = int(input("Enter the ID of the guard to delete: "))
            guard = self.session.query(Guard).get(guard_id)
            if guard:
                self.session.delete(guard)
                self.session.commit()
                print("Guard deleted successfully.")
            else:
                print("Guard not found.")
        except Exception as e:
            print("Error deleting guard:", e)

if __name__ == "__main__":
    company = SecurityCompany()
    while True:
        print("\n1. Add Guard\n2. List Guards\n3. Add Incident\n4. List Incidents\n5. Delete Guard\n6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            company.add_guard()
        elif choice == "2":
            company.list_guards()
        elif choice == "3":
            company.add_incident()
        elif choice == "4":
            company.list_incidents()
        elif choice == "5":
            company.delete_guard()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 6.")
