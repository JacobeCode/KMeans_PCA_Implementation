# This is the exemplary script for Google Colab (for eventual further use)
!pip install pyodbc --quiet

# Below script covers installation of ODBC17 for pyodbc in Google Colab (shell)
# %%sh
# apt-get install -y unixodbc-dev
# curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
# curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list
# sudo apt-get update
# sudo ACCEPT_EULA=Y apt-get -q -y install msodbcsql17

import pyodbc
import pandas

from google.colab import userdata

# IP or password can be stored in secure container and be extracted to connect to SQL Server (classic on port 1433 - trusted connection allows for Windows Auth)
SERVER=userdata.get('IP')
DATABASE=''
query=''

# By default there is no pyodbc drivers on Google Colab - simply install it with commands above
print(pyodbc.drivers())

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};PORT={1433};Network Library=DBMSSOCN;DATABASE={DATABASE};TRUSTED_CONNECTION=YES'

connection = pyodbc.connect(connectionString)
cursor = connection.cursor()

cursor.execute(query)

# Simple data fetch for testing functionality and connection
data=cursor.fetchall()
data=pandas.DataFrame(data)

print(data)

connection.close()