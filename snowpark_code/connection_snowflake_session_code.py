from snowflake.snowpark import Session
import snowflake.connector
import logging
import os
#logging.basicConfig(level=logging.DEBUG)
snowflake_password = os.getenv("snowflake_password")
snowflake_user = os.getenv("snowflake_user")
snowflake_account= os.getenv("snowflake_account")
snowflake_role = os.getenv("snowflake_role")
snowflake_warehouse= os.getenv("snowflake_warehouse")
snowflake_database= os.getenv("snowflake_database")
snowflake_schema= os.getenv("snowflake_schema")

# Build connection parameters
connection_parameters = {
    "user": snowflake_user,
    "password": snowflake_password,
    "account":'oialxdd-xqb21073',
    "role": snowflake_role,
    "warehouse":snowflake_warehouse,
    "database":snowflake_database,
    "schema":snowflake_schema
}

ssession = Session.builder.configs(connection_parameters).create()



# Test query

sql ="SELECT * FROM HRMS.HR.TEST"
df = ssession.sql(sql)
df.show()