import pandas as pd
from sqlalchemy import create_engine

# Database connection
engine = create_engine('mysql+mysqlconnector://root:Antima@310@localhost:port/covid_db1')

# Load CSV data
df = pd.read_csv('C:\Users\Admin\Downloads\Covid Problem\covid_vaccine_statewise.csv')

# Import data to MySQL
df.to_sql('vaccine_state_wise', con=engine, if_exists='append', index=False)
