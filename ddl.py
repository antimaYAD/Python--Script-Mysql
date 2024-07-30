#DDL - DATA DEFINation LANGUAGE  (create,alter,drop)

from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()
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
    #CREATE A TABLE
    curr.execute("CREATE TABLE IF NOT EXISTS teacher (tr_id int primary key , tr_name VARCHAR(45) NOT NULL,tr_sub VARCHAR(45) NOT NULL)")
    
    
    #INSERT INTO QUERY
    insert_query = """
    INSERT INTO teacher (tr_id, tr_name, tr_sub)
    VALUES (%s, %s, %s)
    """
    values = [
        (1, 'John Doe', 'Mathematics'),
        (2, 'Jane Smith', 'Physics'),
        (3, 'Emily Davis', 'Chemistry'),
        (4,'Samantha Vist','Biology')
        
    ]
    

    curr.executemany(insert_query, values)
    
    #ALTER THE TABLE
    query = """ ALTER TABLE teacher ADD home_tr VARCHAR(45) """
    curr.execute(query)
    
    section = """ALTER TABLE teacher ADD section VARCHAR(45)"""
    curr.execute(section)
    
    #ALTER THE CLOUMNS CONSTRAIN
    
    
    curr.execute(" ALTER TABLE teacher MODIFY COLUMN tr_id INT AUTO_INCREMENT ")
    
    
    #DROP column
    curr.execute(" ALTER TABLE teacher DROP column section")
    
    #INSERT VALES MORE
    insert_quer = """ INSERT INTO teacher (tr_name,tr_sub) VALUES(%s,%s)"""
    
    val = [
        ('Vikram Singh','Hindi'),
        ('Rahul Kumar','English'),
        ('Antika Lahore','Marathi'),
        ('Surabh Rai','PT')
    ]
    curr.executemany(insert_quer,val)
    
    
    mydb.commit()  # Commit the transaction



    # Close the cursor and connection
    curr.close()
    mydb.close()
    
except mysql.connector.Error as err:
    print(f"Error: {err}")