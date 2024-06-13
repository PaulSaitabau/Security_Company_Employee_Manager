import argparse
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from prettytable import PrettyTable
from database import OperationsGuard, ManagementGuard, Incident

Base = declarative_base()

class SecurityCompany:
    def __init__(self):
        self.engine = create_engine('sqlite:///security_company.db')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add_guard(self):
        department = input("Enter department (Operations/Management): ")
        name = input("Enter guard's name: ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        assignment = input("Enter assignment: ")
        shift = input("Enter shift (Day/Night): ")
        location = input("Enter location: ")

        if department.lower() == 'operations':
            guard = OperationsGuard(name=name, start_date=start_date, assignment=assignment, shift=shift, location=location)
        elif department.lower() == 'management':
            guard = ManagementGuard(name=name, start_date=start_date, assignment=assignment, shift=shift, location=location)
        else:
            print("Invalid department.")
            return

        self.session.add(guard)
        self.session.commit()
        print(f"{department.capitalize()} guard added successfully.")

    def list_guards(self):
        department = input("Enter department (Operations/Management): ")
        if department.lower() == 'operations':
            guards = self.session.query(OperationsGuard).all()
        elif department.lower() == 'management':
            guards = self.session.query(ManagementGuard).all()
        else:
            print("Invalid department.")
            return

        table = PrettyTable(['ID', 'Name', 'Start Date', 'Assignment', 'Shift', 'Location'])
        for guard in guards:
            table.add_row([guard.id, guard.name, guard.start_date, guard.assignment, guard.shift, guard.location])

        print(f"{department.capitalize()} Department Guards:")
        print(table)

    def add_incident(self):
        guard_id = int(input("Enter guard ID: "))
        guard = self.session.query(OperationsGuard).get(guard_id)
        if guard:
            date = input("Enter incident date (YYYY-MM-DD): ")
            description = input("Enter incident description: ")
            department = input("Enter department (Operations/Management): ")
            incident = Incident(date=date, description=description, department=department, guard=guard)
            self.session.add(incident)
            self.session.commit()
            print("Incident added successfully.")
        else:
            print("Guard not found.")

    def list_incidents(self):
        incidents = self.session.query(Incident).all()
        table = PrettyTable(['ID', 'Date', 'Description', 'Guard ID', 'Department'])
        for incident in incidents:
            table.add_row([incident.id, incident.date, incident.description, incident.guard_id, incident.department])
        print(table)
