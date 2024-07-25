# testcase-backend

To run in your system(WINDOWS):
- Clone the repo
- Make sure postgresql is installed on your system
- Open CMD
- Run the following:
        - psql -U postgres
        - CREATE DATABASE testcasesdb;
- This creates the database on your system
- Navigate to the repo directory 
- Run the following command to set up the database and create table: python setup_db.py
- Run the following commands to create virtual environment for the app: python -m venv venv
- Activate virtual environment: source venv/Scripts/activate
- Install dependencies: pip install -r requirements.txt
- Run the app: python app.py


