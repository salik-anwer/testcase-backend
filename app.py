from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
CORS(app)

# Configure the PostgreSQL connection
conn = psycopg2.connect(
    host="localhost",
    database="testcasesdb",
    user="postgres", # Replace with custom username if set
    password="salik"  # Replace with your PostgreSQL password
)
cursor = conn.cursor(cursor_factory=RealDictCursor)

@app.route('/testcases', methods=['GET'])
def get_testcases():
    cursor.execute("SELECT * FROM testcases")
    testcases = cursor.fetchall()
    return jsonify(testcases)

@app.route('/testcases/<int:id>', methods=['PUT'])
def update_testcase(id):
    data = request.get_json()
    cursor.execute(
        "UPDATE testcases SET name=%s, estimate_time=%s, module=%s, priority=%s, status=%s WHERE id=%s RETURNING *",
        (data['name'], data['estimate_time'], data['module'], data['priority'], data['status'], id)
    )
    updated_testcase = cursor.fetchone()
    conn.commit()
    return jsonify(updated_testcase)

if __name__ == '__main__':
    app.run(debug=True)
