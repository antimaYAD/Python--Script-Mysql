from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

# Load the environment variables from the .env file
mysql_host = os.getenv('MYSQL_HOST')
mysql_user = os.getenv('MYSQL_USER')
mysql_password = os.getenv('MYSQL_PASSWORD')

# Connect to the database
mydb = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database='School'
)

curr = mydb.cursor()

# curr.execute("CREATE USER 'Amit'@'localhost' IDENTIFIED BY 'Amit@1234';")
# Corrected GRANT statement
grant_query = "GRANT SELECT ON School.student TO 'Amit'@'localhost';"
curr.execute(grant_query)

# Show grants for the user
curr.execute("SHOW GRANTS FOR 'Amit'@'localhost';")

# Fetch and print the grants
grants = curr.fetchall()
print(grants)

revoke_query = "REVOKE SELECT ON SCHOOL.student from 'Amit'@'localhost';"
curr.execute(revoke_query)
# curr.execute("show revoke for 'Amit'@'localhost';")

# revoke = curr.fetchall()
# print(revoke)

curr.close()
mydb.close()
