# import mysql.connector

# db_config = {
#     "host": "your_host",
#     "user": "username",
#     "password": "password",
#     "database": "webscraper_db"
# }

# conn = mysql.connector.connect(**db_config)

import mysql.connector

# Database configuration
host = 'localhost'
user = 'your_username'
password = 'your_password'
database = 'your_database_name'

# Establish the connection
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor
cursor = conn.cursor()

# Execute a query
query = 'SELECT * FROM your_table'
cursor.execute(query)

# Fetch and print results
rows = cursor.fetchall()
for row in rows:
    print(row)

# Commit changes and close resources
conn.commit()
cursor.close()
conn.close()
