# Security_Company_Employee_Manager

## Introduction
The Security Company Employee Manager is a command-line interface (CLI) application designed to streamline workforce management for security companies. It offers a comprehensive set of features to efficiently manage guards, incidents, shifts, and departments.

## Contributors
- **Name:** Paul Saitabau
- **Email:** paulsaitabau05@gmail.com

## Languages and Technologies Used
The application is built using the following languages and technologies:
- **Python:** Used as the primary programming language for development.
- **SQLAlchemy:** Provides an Object-Relational Mapping (ORM) framework for working with databases.
- **SQLite:** A lightweight, serverless SQL database engine used for data storage.
- **PrettyTable:** A Python library used for generating ASCII tables, enhancing the presentation of data.
- **argparse:** Python's built-in module for parsing command-line arguments.

## Installation
To run the application locally, follow these steps:
1. **Clone the repository:** `git clone [repository_url]`
2. **Navigate to the project directory:** `cd security_company_manager`
3. **Install dependencies:** `pip install -r requirements.txt`

## Usage
1. **Run the main application file:** `python app.py [command]`
2. **Available commands:**
    - `add_guard`: Add a new guard to the database, providing details such as name, start date, assignment, shift, and location.
    - `list_guards`: List guards based on department. You can specify whether to list guards from the Operations or Management department.
    - `add_incident`: Record an incident associated with a guard, specifying the incident date, description, and department.
    - `list_incidents`: Display a list of all recorded incidents, including details such as date, description, guard ID, and department.
    - `delete_guard`: Remove a guard from the database by specifying the guard's ID.

## Database Structure
The application's database consists of the following tables:
- **guards:** Stores information about guards, including their name, start date, assignment, shift, location, and associated incidents.
- **incidents:** Records details of incidents, such as the date, description, department, and the guard involved.
- **shifts:** Defines the shifts available, such as Day or Night shifts.
- **departments:** Represents the departments within the security company, such as Operations or Management.
- **locations:** Specifies the locations where guards are assigned, enhancing the management of guard deployments.

## License
[License details]