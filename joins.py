from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

# Load the environment variables from the .env file
mysql_host = os.getenv("MYSQL_HOST")
mysql_user = os.getenv("MYSQL_USER")
mysql_password = os.getenv("MYSQL_PASSWORD")


try:
    mydb = mysql.connector.connect(
        host=mysql_host, user=mysql_user, password=mysql_password, database="world"
    )

    curr = mydb.cursor()

    # DIFFERENT TYPE OF JOINS

    # INNER JOINS
    # INNER JOIN is used to combine rows from two or more tables where the combination of records from
    curr.execute("SELECT c.name , c.district , cl.language, c.population from city as c join countrylanguage as cl on c.countrycode = cl.countrycode limit 15")
    inner_join_result = curr.fetchall()
    print(inner_join_result)
    
    inner_query = """ SELECT
                city.name AS city_name, country.name AS country_name,
                countrylanguage.language as Language, 
                countrylanguage.percentage as percentage
                FROM country
                INNER JOIN city ON country.capital = city.id
                INNER JOIN countrylanguage ON country.code = countrylanguage.countrycode
                WHERE
                country.continent = 'North America' and
                countrylanguage.isofficial = 'T'  
                ORDER BY
                city_name ASC,
                country_name,
                language,
                percentage ASC
                LIMIT 12;"""

    curr.execute(inner_query)
    inner_join_result = curr.fetchall()
    print(inner_join_result)
    
    
    # LEFT JOIN
    left_query = """ SELECT ct.name, cl.language 
                    FROM city ct 
                    LEFT JOIN countrylanguage cl ON ct.countrycode = cl.countrycode 
                    WHERE cl.isofficial = 'T' 
                    GROUP BY ct.name, cl.language 
                    HAVING COUNT(cl.isofficial) = 1 
                    ORDER BY ct.name ASC 
                    LIMIT 10;
                    """
    curr.execute(left_query)
    left_join_result = curr.fetchall()
    for res in left_join_result:
        print(res)
    
    
    ##Right JOIN
    rigth_query = """ SELECT cd.name , cd.continent,cd.region,ct.name,cd.population from city ct right join country cd on cd.capital = ct.id where cd.population >= (SELECT AVG(population)from country) order by cd.population  limit 10;"""
    curr.execute(rigth_query)
    right_join_result = curr.fetchall()
    dict_df = {}
    for res in right_join_result:
        dict_df[res[0]] = {'continent': res[1], 'region': res[2],'Capital_name':res[3],'Population':res[4]}
        print(dict_df)
    
   # # Full outer join
    full_query = "SELECT * FROM CITY ct LEFT JOIN COUNTRYLANGUAGE cl  ON ct.countrycode = cl.countrycode  union SELECT * FROM CITY ct Right JOIN COUNTRYLANGUAGE cl  ON ct.countrycode = cl.countrycode  limit 12;"    
    curr.execute(full_query)
    full_join_result = curr.fetchall()
    for res in full_join_result:
        print(res)
    
    
    
    




    


   

except mysql.connector.Error as error:
    print(f"Failed to connect to database: {error}")
