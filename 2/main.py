from flask import Flask, render_template
import psycopg2
from psycopg2 import sql

app = Flask(__name__)

# Connect to the PostgreSQL database
db_host = 'your_db_host'  # replace with your PostgreSQL server's host
db_port = 5432  # replace with your PostgreSQL server's port
db_name = 'your_db_name'  # replace with your PostgreSQL database name
db_user = 'your_db_user'  # replace with your PostgreSQL database user
db_password = 'your_db_password'  # replace with your PostgreSQL database password

# Create a PostgreSQL connection
db_conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    database=db_name,
    user=db_user,
    password=db_password
)

# Create a cursor to execute SQL queries
db_cursor = db_conn.cursor()

# Define the table for the page counter in PostgreSQL
page_counter_table = 'page_counter'

@app.route('/')
def index():
    # Increment the page counter in PostgreSQL
    update_counter_query = sql.SQL("""
        INSERT INTO {} (count) VALUES (1)
        ON CONFLICT (id) DO UPDATE SET count = {} + 1
        RETURNING count;
    """).format(sql.Identifier(page_counter_table), sql.Identifier(page_counter_table, 'count'))

    db_cursor.execute(update_counter_query)
    page_count = db_cursor.fetchone()[0]

    # Commit the changes
    db_conn.commit()

    return render_template('index.html', page_count=page_count)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
