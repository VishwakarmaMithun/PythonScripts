import os
import snowflake.connector
from dotenv import load_dotenv
load_dotenv()

# Load environment variables from .env file
snowflake_password = os.getenv("snowflake_password")
snowflake_user = os.getenv("snowflake_user")
snowflake_account= os.getenv("snowflake_account")
snowflake_role = os.getenv("snowflake_role")
snowflake_warehouse= os.getenv("snowflake_warehouse")
snowflake_database= os.getenv("snowflake_database")
snowflake_schema= os.getenv("snowflake_schema")
 
# Create connection
conn = snowflake.connector.connect(
    user=snowflake_user,
    password= snowflake_password ,
    account= snowflake_account,
    warehouse=snowflake_warehouse,
    database= snowflake_database,
    schema=snowflake_schema,
    role= snowflake_role,
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
