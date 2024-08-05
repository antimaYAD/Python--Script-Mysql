from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine

# Load environment variables from .env file
load_dotenv()

# Read database credentials and paths from .env file
mysql_user = os.getenv('MYSQL_USER')
mysql_host = os.getenv('MYSQL_HOST')
mysql_password = os.getenv('MYSQL_PASSWORD')
mysql_db1 = os.getenv('MYSQL_DB_1')
mysql_db2 = os.getenv('MYSQL_DB_2')

def create_database_from_folder(folder_path, database_name, user, host, password):
    # Create a connection to the MySQL database
    engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database_name}')

    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            table_name = os.path.splitext(filename)[0]

            # Read the CSV file into a DataFrame
            df = pd.read_csv(file_path)

            # Import the DataFrame into the MySQL database
            df.to_sql(table_name, engine, index=False, if_exists='replace')
            print(f"Imported {filename} into table {table_name}")

# Paths to your folders
folder_path1 = r'C:\Users\Admin\Downloads\covid-kaggle-dataset'
folder_path2 = r'C:\Users\Admin\Downloads\Covid Problem'

# Create databases from folders
create_database_from_folder(folder_path1, mysql_db1, mysql_user, mysql_host, mysql_password)
create_database_from_folder(folder_path2, mysql_db2, mysql_user, mysql_host, mysql_password)

print("All files have been imported successfully.")
