import time;
import snowflake
import snowflake.snowpark.functions 
from snowflake.snowpark.functions import col
from snowflake.snowpark import Session
import os

snowflake_password = os.getenv("snowflake_password")
snowflake_user = os.getenv("snowflake_user")
snowflake_account= os.getenv("snowflake_account")
snowflake_role = os.getenv("snowflake_role")
snowflake_warehouse= os.getenv("snowflake_warehouse")
snowflake_database= os.getenv("snowflake_database")
snowflake_schema= os.getenv("snowflake_schema")

connection_parameters = {
    "user": snowflake_user,
    "password": snowflake_password,
    "account":'oialxdd-xqb21073',
    "role": snowflake_role,
    "warehouse":snowflake_warehouse,
    "database":snowflake_database,
    "schema":snowflake_schema
}

session = Session.builder.configs(connection_parameters).create()
session.sql("USE WAREHOUSE COMPUTE_WH").collect()

#create a dataframe using list
test = session.create_dataframe([[1,2,3,4],[3,4,5,5]],schema=["q","e","r","t"])
test.show()

test = session.create_dataframe([[1,2,3,"2025-10-01"],[3,4,5,"2045-01-01"]],schema=["q","e","r","t"])
test.show()

test1 =test.cache_result();
test1.show()

begin =  time.time();
test1.show()
end  = time.time();
print(end-begin);
