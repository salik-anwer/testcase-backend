import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_and_populate_table():
    # Database connection parameters
    conn = psycopg2.connect(
        host="localhost",
        database="testcasesdb",
        user="postgres",
        password="salik"  # Replace with your PostgreSQL password
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    # Check if table exists
    cursor.execute("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_name = 'testcases'
        );
    """)
    exists = cursor.fetchone()[0]

    if not exists:
        # Create table
        cursor.execute("""
            CREATE TABLE testcases (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                estimate_time VARCHAR(255),
                module VARCHAR(255),
                priority VARCHAR(50),
                status VARCHAR(50)
            );
        """)
        # Insert initial data
        cursor.execute("""
            INSERT INTO testcases (name, estimate_time, module, priority, status)
            VALUES 
                ('Test Case 1', '5 mins', 'Module 1', 'High', 'PASS'),
                ('Test Case 2', '10 mins', 'Module 2', 'Medium', 'FAIL');
        """)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_and_populate_table()
