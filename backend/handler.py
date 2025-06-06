import json
import os
import psycopg2

# Example AWS Lambda handler
# Connects to a Postgres database (RDS) containing grade statistics
# Returns the top 10 courses with the highest average grade

def lambda_handler(event, context):
    conn = psycopg2.connect(os.environ['DB_CONN'])
    cur = conn.cursor()
    cur.execute(
        """
        SELECT subject_area, catalog_number, average_grade
        FROM ge_course_grades
        ORDER BY average_grade DESC
        LIMIT 10
        """
    )
    rows = cur.fetchall()
    result = [
        {
            "subject": row[0],
            "catalog": row[1],
            "average_grade": float(row[2]),
        }
        for row in rows
    ]
    return {"statusCode": 200, "body": json.dumps(result)}
