from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()
mysql_host = os.getenv('MYSQL_HOST')
mysql_user = os.getenv('MYSQL_USER')
mysql_password = os.getenv('MYSQL_PASSWORD')


mydb = mysql.connector.connect(
  host = mysql_host,
  user = mysql_user,
  password = mysql_password
)

curr = mydb.cursor()


#create database
curr.execute("CREATE DATABASE School")

#Show the database which are exists
curr.execute("SHOW DATABASES")
for x in curr:
    print(x)


#CREATE TABLE
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Antima@310",
 database = "School"
)

curr = mydb.cursor()
#CREATE TABLE
curr.execute("CREATE TABLE student (id INT AUTO_INCREMENT  PRIMARY KEY,name VARCHAR(45), address VARCHAR(225))")

#INSET INTO
sql = "INSERT INTO student(name,address) values(%s,%s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

curr.executemany(sql,val)
#ALTER THE TABLE CLOUMNS
curr.execute("ALTER TABLE student ADD  standar INT DEFAULT 10")
curr.execute("ALTER TABLE student ADD result VARCHAR(20) DEFAULT 'Pass'")

#UPDATE THE COLUNMS VALUE
curr.execute("UPDATE student SET result = 'Fail' WHERE id % 2 = 0")

#Delete the row
curr.execute("DELETE FROM student WHERE name = 'Michael'")



mydb.commit()

