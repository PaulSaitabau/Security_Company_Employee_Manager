# Security_Company_Employee_Manager

## Introduction
The Security Company Employee Manager is a command-line interface (CLI) application designed to streamline workforce management for security companies. It provides functionalities to add, list, update, and delete guard information, incidents, and more.

## Contributors
Name:Paul Saitabau
Email:paulsaitabau05@gmail.com

## Languages and Technologies Used
- Python
- SQLAlchemy
- SQLite
- PrettyTable
- argparse

## Installation
1. Clone the repository: `git clone [repository_url]`
2. Navigate to the project directory: `cd security_company_manager`
3. Install dependencies: `pip install -r requirements.txt`

## Usage
1. Run the main application file: `python app.py [command]`
2. Available commands:
    - `add_guard`: Add a new guard to the database.
    - `list_guards`: List guards based on department.
    - `add_incident`: Add an incident associated with a guard.
    - `list_incidents`: List all incidents.
    - `delete_guard`: Delete a guard from the database.

## Database Structure
- The database includes tables for guards, incidents, shifts, departments, and locations, with appropriate relationships defined between them.

## License
[License details]