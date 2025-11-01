import os
import snowflake.connector

# Load environment variables from .env file
db_user = os.getenv("snowflake_password")
# Create connection
conn = snowflake.connector.connect(
    user='RAVINA',
    password= db_user,
    account= 'oialxdd-xqb21073',
    warehouse="COMPUTE_WH",
    database= "HRMS",
    schema="HR",
    role= 'ACCOUNTADMIN',
)


# "account":'oialxdd-xqb21073',
 
# Create a cursor and execute a query
cur = conn.cursor()
cur.execute("SELECT * FROM HRMS.HR.TEST")

# Fetch and print results
for row in cur:
    print(row)

# Close connection
cur.close()
conn.close()
