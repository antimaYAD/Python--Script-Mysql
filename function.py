#Function (AGG , STRING , DATATIME)

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
    database = 'world'
    )

    curr = mydb.cursor()
    
    #Aggregate Function
    
    #MAX()
    curr.execute("SELECT max(population) from city;")
    max_population = curr.fetchone()[0]
    print(max_population)
    
    #MIN()
    curr.execute("SELECT min(population) from city;")
    min_population = curr.fetchone()[0]
    print(min_population)
    
    #AVG()
    curr.execute("SELECT avg(population) from city")
    avg_population = curr.fetchone()[0]
    print(avg_population)
    
    #SUM()
    curr.execute("SELECT sum(population) as world_population from city;")
    world_population = curr.fetchone()[0]
    print(world_population)
    
    COUNT
    curr.execute("SELECT count(*) as total_cities from city;")
    total_cities = curr.fetchone()[0]
    print(total_cities)
    
    #ROUND
    curr.execute("SELECT ROUND(AVG(POPULATION)) FROM city;")
    avg_population = curr.fetchone()[0]
    print(avg_population)
    
    #POWER()
    curr.execute("SELECT POWER(2,3) FROM DUAL;")
    power_result = curr.fetchone()[0]
    print(power_result)
    
    #MOD()
    curr.execute("SELECT MOD(17,5) FROM DUAL;")
    mod_result = curr.fetchone()[0]
    print(mod_result)
    
    #SIGN
    curr.execute("SELECT SIGN(-5) FROM DUAL;")
    sign_result = curr.fetchone()[0]
    print(sign_result)
    
    #SQRT
    curr.execute("SELECT SQRT(16) FROM DUAL;")
    sqrt_result = curr.fetchone()[0]
    print(sqrt_result)
    
    
    # String Fcuntion
    
    #UPPER()/UCASE()
    curr.execute("SELECT UPPER(Name) from city limit 10;")
    upper_result = curr.fetchall()
    for name in upper_result:
        print(name[0])
        
    #LOWER()/LCASE()
    curr.execute("SELECT LOWER(Name) from city limit 10;")
    lower_result = curr.fetchall()
    for name in lower_result:
        print(name[0])
        
    #CONCAT
    curr.execute("SELECT CONCAT(name,' ',CountryCode) as name_contr_code FROM city limit 10;")
    concat_result = curr.fetchall()
    for name in concat_result:
        print(name[0])
        
    #LENGTH(())
    curr.execute("SELECT LENGTH(name) as name_length FROM city limit 10;")
    length_result = curr.fetchall()
    for name in length_result:
        print(name[0])
        
    #TRIM()
    curr.execute("SELECT TRIM(name) as name_trim FROM city limit 10;")
    trim_result = curr.fetchall()
    for name in trim_result:
        print(name[0])
    
    #SUBSTRING
    curr.execute("SELECT SUBSTR(name,1,5) as name_sub FROM city limit 14;")
    substr_result = curr.fetchall()
    for name in substr_result:
        print(name[0])
        
    # DATE TIME 
    #NOW()
    curr.execute("SELECT NOW() FROM DUAL;")
    now_result = curr.fetchone()[0]
    print(now_result)
    
    DATE()
    curr.execute("SELECT DATE('2020-01-01') FROM DUAL;")
    date_result = curr.fetchone()[0]
    print(date_result)
    
    TIME()
    curr.execute("SELECT TIME('2022-7-30 17:04:55') FROM DUAL;")
    time_result = curr.fetchone()
    print(time_result)
    
    #YEAR()
    curr.execute("SELECT YEAR('2022-7-30 17:04:55') FROM DUAL")
    year_result = curr.fetchone()[0]
    print(year_result)
    
   # MONTH()
    curr.execute("SELECT MONTH('2022-7-30 17:04:55') FROM DUAL")
    month_result = curr.fetchone()[0]
    print(month_result)
    
    
        
    curr.close()
    mydb.close()
    
    
except mysql.connector.Error as err:
    print(f"Error: {err}")