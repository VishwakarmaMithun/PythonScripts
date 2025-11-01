from snowflake.snowpark import Session
import snowflake.connector
import logging
import os
#logging.basicConfig(level=logging.DEBUG)
db_user = os.getenv("snowflake_password")


# Build connection parameters
connection_parameters = {
    "user": 'RAVINA',
    "password": db_user,
    "account":'oialxdd-xqb21073',
    "role": 'SYSADMIN',
    "warehouse":"COMPUTE_WH",
    "database":"HRMS",
    "schema":"HR"
}

ssession = Session.builder.configs(connection_parameters).create()

# Test query

sql ="SELECT * FROM HRMS.HR.TEST"
df = ssession.sql(sql)
df.show()