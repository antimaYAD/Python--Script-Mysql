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
    query = """INSERT INTO student (name,address,standar,result) values(%s,%s,%s,%s)"""
    value = [
        ('John', 'New York', 8, 'Pass'),
        ('Jane', 'London', 7, 'Pass'),
        ('Alice', 'Paris', 9, 'Pass'),
        ('Bob', 'Tokyo', 6, 'Fail'),
        ('Charlie', 'Sydney', 5, 'Fail')
    ]
    
    curr.executemany(query, value)
    
    
    #UPBATE THE DATA
    curr.execute("UPDATE  teacher set home_tr = '12A' WHERE tr_sub in ('Mathematics','Physics','Chemistry','Biology')")
    curr.execute("UPDATE teacher set home_tr = '11C' WHERE tr_sub in ('Hindi','English','Marathi')")
    
    #Delete the ROW 
    
    curr.execute("DELETE FROM teacher where tr_sub = 'PT'")
    
    mydb.commit()
    
    
    curr.close()
    mydb.close()
    
    
except mysql.connector.Error as err:
    print(f"Error: {err}")