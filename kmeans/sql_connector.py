# import mysql.connector
# from mysql.connector import Error
# import pandas as pd

# def establish_connection(host_name, user_name, password):
#     connection = None 
#     try:
#         connection = mysql.connector.connect(
#             host = host_name,
#             user = user_name,
#             passwd = password
#         )
#         print("Connection established")
#     except Error as err:
#         print(f"Error: '{err}'")
#     return connection

# connection = establish_connection("localhost", "root", pw)

import pyodbc
import pandas

print(pyodbc.drivers())

SERVER=r'EXPERIMENT_DATA'
print(SERVER)
DATABASE='clustering'

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};TRUSTED_CONNECTION=YES'
query = "SELECT * FROM dbo.clustering;"

connection = pyodbc.connect(connectionString)
cursor = connection.cursor()

cursor.execute(query)
data=cursor.fetchall()

data=pandas.DataFrame(data)

connection.close()