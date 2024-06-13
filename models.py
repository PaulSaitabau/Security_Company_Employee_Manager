from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, Guard, Incident
from prettytable import PrettyTable

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
        department = input("Enter department (Operations/Management): ")
        name = input("Enter guard's name: ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        assignment = input("Enter assignment: ")
        shift = input("Enter shift (Day/Night): ")
        location = input("Enter location: ")

        guard = Guard(name=name, start_date=start_date, assignment=assignment, shift=shift, location=location)
        self.session.add(guard)
        self.session.commit()
        print(f"{department.capitalize()} guard added successfully.")

    def list_guards(self):
        department = input("Enter department (Operations/Management): ")
        guards = self.session.query(Guard).filter(Guard.location == department.capitalize()).all()
        if guards:
            table = PrettyTable(['ID', 'Name', 'Start Date', 'Assignment', 'Shift', 'Location'])
            for guard in guards:
                table.add_row([guard.id, guard.name, guard.start_date, guard.assignment, guard.shift, guard.location])
            print(f"{department.capitalize()} Department Guards:")
            print(table)
        else:
            print("No guards found.")

    def add_incident(self):
        guard_id = int(input("Enter guard ID: "))
        guard = self.session.query(Guard).get(guard_id)
        if guard:
            date = input("Enter incident date (YYYY-MM-DD): ")
            description = input("Enter incident description: ")
            department = input("Enter department (Operations/Management): ")
            incident = Incident(date=date, description=description, department=department.capitalize(), guard=guard)
            self.session.add(incident)
            self.session.commit()
            print("Incident added successfully.")
        else:
            print("Guard not found.")

    def list_incidents(self):
        incidents = self.session.query(Incident).all()
        if incidents:
            table = PrettyTable(['ID', 'Date', 'Description', 'Guard ID', 'Department'])
            for incident in incidents:
                table.add_row([incident.id, incident.date, incident.description, incident.guard_id, incident.department])
            print("List of Incidents:")
            print(table)
        else:
            print("No incidents found.")

    def delete_guard(self):
        guard_id = int(input("Enter the ID of the guard to delete: "))
        guard = self.session.query(Guard).get(guard_id)
        if guard:
            self.session.delete(guard)
            self.session.commit()
            print("Guard deleted successfully.")
        else:
            print("Guard not found.")
