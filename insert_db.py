# insert records from csv file into sqlite db
# can be found on kaggle: https://www.kaggle.com/datasets/moaboalwafa/salaries-data/data
import sqlite3
import pandas as pd


conn = sqlite3.connect('data/sqlite/salaries.db')
cursor = conn.cursor()

salaries_df = pd.read_csv("data/csv/Salaries.csv", dtype={
    'BasePay': str,
    'OvertimePay': str,
    'OtherPay': str,
    'Benefits': str,
    'Status': str
}
)

# Insert the data into the Salaries table
salaries_df.to_sql('SALARIES', conn, if_exists='append', index=False)

# Commit the changes and close the connection
conn.commit()
conn.close()