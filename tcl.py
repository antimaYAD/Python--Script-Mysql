#TCL- Transaction Control Language

# DML - Data Manipulation Language or DML is a subset of operations used to insert, delete, and update data in a database. 
# A DML is often a sublanguage of a more extensive language like SQL; DML comprises some of the operators in the language.

from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

# Load the environment variables from the .env file
mysql_host = os.getenv('MYSQL_HOST')
mysql_user = os.getenv('MYSQL_USER')
mysql_password = os.getenv('MYSQL_PASSWORD')


try:
    mydb = mysql.connector.connect(
    host = mysql_host,
    user = mysql_user,
    password = mysql_password,
    database = 'School'
    )

    curr = mydb.cursor()
    # curr.execute("CREATE TABLE IF NOT EXISTS student (id INT AUTO_INCREMENT  PRIMARY KEY,name VARCHAR(45), address VARCHAR(225))")
    
    
    # Inserting data into the table
    curr.execute("INSERT INTO student (name, address,result) VALUES ('John Doe', 'Mumbai 123','Pass');")
    
    curr.execute("SAVEPOINT sp1;")
    
    
    curr.execute("INSERT INTO student (name, address,result) VALUES ('Antima Yadav', 'Mumbai 123','Pass');")
    
    curr.execute("ROLLBACK TO sp1;")
    
    mydb.commit()
    curr.close()
    mydb.close()
    
    
except mysql.connector.Error as err:
    print(f"Error: {err}")